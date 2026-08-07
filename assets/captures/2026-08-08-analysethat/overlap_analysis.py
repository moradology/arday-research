#!/usr/bin/env python3
"""
Text overlap analysis: Arday (2015) vs Zwozdiak-Myers (2009), with controls.

Reproduces every figure in the accompanying article from scratch.
Downloads all four theses from their institutional repositories.

    pip install sentence-transformers scipy numpy
    sudo apt-get install poppler-utils      # provides pdftotext
    python overlap_analysis.py

CPU runtime ~20 min. No GPU required.
"""

import json, os, re, subprocess, unicodedata
import numpy as np
from scipy.stats import poisson, chi2

# --------------------------------------------------------------------------
# 0. Sources
# --------------------------------------------------------------------------
DOCS = {
    'arday': ('https://researchonline.ljmu.ac.uk/id/eprint/4552/1/'
              '158222_Jason%20Arday_%20Final%20PhD%20Thesis%20Vesrion%20Final%20Draft%20Oct%202015.pdf',
              'Arday 2015, PhD, Liverpool John Moores'),
    'zwoz':  ('https://bura.brunel.ac.uk/bitstream/2438/4316/1/FulltextThesis.pdf',
              'Zwozdiak-Myers 2009, PhD, Brunel'),
    'ctrl1': ('https://etheses.whiterose.ac.uk/id/eprint/31670/1/'
              'Kushkiev%2C%20Plamen%2C%20EdD%20Thesis.pdf',
              'Kushkiev 2022, EdD, Sheffield (near control)'),
    'ctrl2': ('https://etheses.whiterose.ac.uk/id/eprint/38362/7/Alhumaidan.Thesis.pdf',
              'Alhumaidan 2025, PhD, York (far control)'),
}
FOCAL = ('arday', 'zwoz')
UA = 'Mozilla/5.0 (X11; Linux x86_64) Chrome/120'

STOP = set('''a an the and or but if of to in on at by for with from as is are was were be been
being it its this that these those which who whom whose what when where how why not no nor so
than then there here their they them he she his her you your we our us i me my can could will
would shall should may might must do does did done have has had having also more most such some
any all each other into within between during through about over under further'''.split())

ABBREV = {'e.g','i.e','cf','et al','etc','vs','pp','ed','eds','vol','no','fig',
          'dr','prof','mr','mrs','ms','st','ch','p','al','ibid','viz','esp'}


# --------------------------------------------------------------------------
# 1. Acquire and extract
# --------------------------------------------------------------------------
def fetch(key):
    url, label = DOCS[key]
    pdf, txt = f'{key}.pdf', f'{key}.txt'
    if not os.path.exists(txt):
        if not os.path.exists(pdf):
            print(f'  downloading {label}')
            subprocess.run(['curl', '-sL', '-A', UA, '-o', pdf, url], check=True)
        subprocess.run(['pdftotext', pdf, txt], check=True)
    return open(txt, encoding='utf-8', errors='ignore').read()


def clean(t):
    """Strip TOC, bibliography, page furniture; de-hyphenate; reflow."""
    t = unicodedata.normalize('NFKD', t).replace('\x0c', '\n')
    t = re.sub(r'[\u2018\u2019]', "'", t)
    t = re.sub(r'[\u201c\u201d]', '"', t)
    t = re.sub(r'[\u2013\u2014]', '-', t)
    t = '\n'.join(l for l in t.split('\n') if not re.search(r'\.{4,}', l))  # TOC
    cut = None
    for m in re.finditer(r'\n\s*(References|Bibliography|REFERENCES|BIBLIOGRAPHY)\s*\n', t):
        if m.start() > len(t) * 0.55:
            cut = m.start(); break
    if cut: t = t[:cut]
    keep = [l.strip() for l in t.split('\n')
            if not re.fullmatch(r'[\divxlcIVXLC\s\-\.]{0,8}', l.strip())]
    t = '\n'.join(keep)
    t = re.sub(r'(\w)-\n(\w)', r'\1\2', t)      # de-hyphenate line breaks
    t = re.sub(r'\n(?=[a-z,;])', ' ', t)        # continuation lines
    return re.sub(r'[ \t]+', ' ', t)


def sentences(t):
    t = re.sub(r'\n+', ' ', t)
    out, buf = [], []
    for tok in re.split(r'(?<=[.!?])\s+', t):
        buf.append(tok)
        last = tok.rstrip().split()
        w = re.sub(r'[^A-Za-z\.]', '', last[-1]).lower().rstrip('.') if last else ''
        if w in ABBREV or re.fullmatch(r'[A-Z]', w or ''):
            continue
        out.append(' '.join(buf).strip()); buf = []
    if buf: out.append(' '.join(buf).strip())
    return out


def prepare(key):
    raw = fetch(key)
    sents = sentences(clean(raw))
    keep, seen = [], set()
    for s in sents:
        wc = len(s.split())
        if wc < 10 or wc > 120: continue
        if sum(c.isalpha() or c.isspace() for c in s) / max(len(s), 1) < 0.80: continue
        k = re.sub(r'\W+', '', s.lower())
        if k in seen: continue
        seen.add(k); keep.append(s)
    print(f'  {DOCS[key][1]}: {len(raw.split()):,} words -> {len(keep):,} sentences')
    return keep


# --------------------------------------------------------------------------
# 2. Similarity primitives
# --------------------------------------------------------------------------
def words(s):   return re.findall(r"[a-z']+", s.lower().replace('\u201f', "'"))
def content(s): return set(w for w in re.findall(r'[a-z]+', s.lower())
                           if w not in STOP and len(w) > 2)


def longest_run(a, b):
    """Longest run of identical consecutive words. Topic-immune; the key statistic."""
    A_, B_ = words(a), words(b)
    best, prev = 0, [0] * (len(B_) + 1)
    for i in range(1, len(A_) + 1):
        cur, ai = [0] * (len(B_) + 1), A_[i - 1]
        for j in range(1, len(B_) + 1):
            if ai == B_[j - 1]:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best


def pair_stats(S, D1, D2, thr=0.90, cap=500, seed=0):
    flat = S.ravel(); n = S.size
    out = {'n_pairs': n, 'mean': float(flat.mean()), 'max': float(flat.max())}
    for t in (0.95, 0.98, 0.999):
        out[f'per1M>={t}'] = float((flat >= t).sum()) / n * 1e6
    ii, jj = np.where(S >= thr)
    idx = list(zip(ii, jj)); out['hi_n'] = len(idx)
    if idx:
        rng = np.random.default_rng(seed)
        if len(idx) > cap:
            idx = [idx[k] for k in rng.choice(len(idx), cap, replace=False)]
        runs = np.array([longest_run(D1[int(i)], D2[int(j)]) for i, j in idx])
        jacs = np.array([len(content(D1[int(i)]) & content(D2[int(j)])) /
                         max(1, len(content(D1[int(i)]) | content(D2[int(j)])))
                         for i, j in idx])
        out.update(run_med=float(np.median(runs)), run_max=int(runs.max()),
                   jac_med=float(np.median(jacs)),
                   run12_per1M=float((runs >= 12).mean()) * out['hi_n'] / n * 1e6)
    else:
        out.update(run_med=0.0, run_max=0, jac_med=0.0, run12_per1M=0.0)
    return out


def within_baseline(e, gap=200):
    """Sentences from the SAME document, far apart: ceiling for independent prose."""
    S = e @ e.T
    i, j = np.triu_indices(S.shape[0], k=gap)
    v = S[i, j]
    return {'mean': float(v.mean()), 'max': float(v.max()),
            'p99.99': float(np.percentile(v, 99.99)),
            'n>=0.999': int((v >= 0.999).sum()), 'n_pairs': int(v.size)}


# --------------------------------------------------------------------------
# 3. Main
# --------------------------------------------------------------------------
def main():
    from sentence_transformers import SentenceTransformer

    print('\n[1] Acquiring and segmenting')
    S_ = {k: prepare(k) for k in DOCS}

    print('\n[2] Embedding (all-MiniLM-L6-v2)')
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    E_ = {k: model.encode(v, batch_size=64, normalize_embeddings=True,
                          show_progress_bar=False).astype('float32')
          for k, v in S_.items()}

    print('\n[3] Within-document baselines')
    for k in FOCAL:
        b = within_baseline(E_[k])
        print(f"  {k:6} mean={b['mean']:.3f} max={b['max']:.3f} "
              f"near-identical={b['n>=0.999']} in {b['n_pairs']/1e6:.1f}M")

    print('\n[4] Pairwise comparison')
    keys = list(DOCS)
    pairs = [(x, y) for i, x in enumerate(keys) for y in keys[i + 1:]]
    hdr = (f"{'pair':16}{'mean':>7}{'max':>7}{'>=.95':>8}{'>=.98':>8}"
           f"{'>=.999':>9}{'jac|hi':>8}{'runmed':>8}{'runmax':>8}{'run>=12':>9}")
    print(hdr); print('-' * len(hdr))
    res = {}
    for x, y in pairs:
        r = pair_stats(E_[x] @ E_[y].T, S_[x], S_[y]); res[(x, y)] = r
        tag = '*' if (x, y) == FOCAL or (y, x) == FOCAL else ' '
        print(f"{tag}{x[:6]}x{y[:6]:9}{r['mean']:7.3f}{r['max']:7.3f}"
              f"{r['per1M>=0.95']:8.2f}{r['per1M>=0.98']:8.2f}{r['per1M>=0.999']:9.3f}"
              f"{r['jac_med']:8.3f}{r['run_med']:8.1f}{r['run_max']:8d}"
              f"{r['run12_per1M']:9.2f}")
    print('  (* = focal pair; rates per million sentence pairs)')

    print('\n[5] Poisson test against pooled control null')
    S_focal = E_[FOCAL[0]] @ E_[FOCAL[1]].T
    foc_n = int((S_focal >= 0.999).sum()); foc_N = S_focal.size
    null_n = sum(int((E_[x] @ E_[y].T >= 0.999).sum())
                 for x, y in pairs if (x, y) != FOCAL)
    null_N = sum(E_[x].shape[0] * E_[y].shape[0]
                 for x, y in pairs if (x, y) != FOCAL)
    lam = null_n / null_N * foc_N
    lam_hi = chi2.ppf(0.975, 2 * (null_n + 1)) / 2 / null_N * foc_N
    print(f'  focal: {foc_n} near-identical in {foc_N/1e6:.2f}M pairs')
    print(f'  null : {null_n} in {null_N/1e6:.2f}M pairs')
    print(f'  expected {lam:.3f} (conservative upper {lam_hi:.3f}); observed {foc_n}')
    print(f'  P(X>={foc_n} | point)        = {poisson.sf(foc_n-1, lam):.3e}')
    print(f'  P(X>={foc_n} | conservative) = {poisson.sf(foc_n-1, lam_hi):.3e}')

    # block correction: collapse spatially adjacent matches into single events
    ii, jj = np.where(S_focal >= 0.999)
    blocks = []
    for i, j in sorted(zip(ii.tolist(), jj.tolist())):
        if not any(any(abs(i-x) <= 3 and abs(j-y) <= 3 for x, y in b) for b in blocks):
            blocks.append([(i, j)])
        else:
            next(b for b in blocks
                 if any(abs(i-x) <= 3 and abs(j-y) <= 3 for x, y in b)).append((i, j))
    print(f'  {foc_n} matches -> {len(blocks)} independent blocks; '
          f'P(X>={len(blocks)} | conservative) = {poisson.sf(len(blocks)-1, lam_hi):.3e}')

    print('\n[6] Extent (excess over control baseline)')
    rng = np.random.default_rng(0)
    def best(q, r, nsub=1800, reps=5):
        return np.mean([(E_[q] @ E_[r][rng.choice(E_[r].shape[0],
                        min(nsub, E_[r].shape[0]), replace=False)].T).max(axis=1)
                        for _ in range(reps)], axis=0)
    bZ, bK, bH = best('arday','zwoz'), best('arday','ctrl1'), best('arday','ctrl2')
    w = np.array([len(s.split()) for s in S_['arday']]); tot = w.sum()
    print(f'  Arday cleaned body text: {tot:,} words')
    print(f"  {'thr':>6}{'vs Zwoz':>9}{'baseline':>10}{'excess':>8}{'words':>8}{'%':>8}")
    for t in (0.75, 0.80, 0.85, 0.90, 0.95, 0.99):
        nZ = int((bZ >= t).sum()); base = (int((bK >= t).sum()) + int((bH >= t).sum())) / 2
        exc = max(0.0, nZ - base)
        sel = w[bZ >= t]
        wx = exc * (sel.mean() if len(sel) else 0)
        print(f'  {t:>6.2f}{nZ:>9d}{base:>10.1f}{exc:>8.1f}{wx:>8.0f}{100*wx/tot:>7.2f}%')

    print('\n  by section (threshold 0.80):')
    pos = np.arange(len(S_['arday'])) / len(S_['arday'])
    for nm, m in [('intro + lit review (deciles 1-2)', pos < 0.2),
                  ('discussion + conclusion (9-10)', pos >= 0.8),
                  ('methods, data, findings (3-8)', (pos >= 0.2) & (pos < 0.8))]:
        c = int(((bZ >= 0.80) & m).sum())
        print(f'    {nm:34} {c:4d}/{int(m.sum()):4d} ({100*c/m.sum():5.1f}%)  '
              f'{int(w[(bZ >= 0.80) & m].sum()):6d} words')

    json.dump({f'{x}x{y}': v for (x, y), v in res.items()},
              open('results.json', 'w'), indent=1)
    print('\nWritten: results.json')


if __name__ == '__main__':
    main()
