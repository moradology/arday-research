# Public document capture

- Capture date: 2026-08-05
- Acquisition method: `curl -L --fail` from the canonical public URLs
- Purpose: research-preservation copies; redistribution rights remain subject to each source’s terms and licence

| Local file | Canonical source | Type/pages | SHA-256 | Acquisition state |
|---|---|---:|---|---|
| `assets/documents/ucl-keynote.pdf` | [UCL keynote PDF](https://www.ucl.ac.uk/teaching-learning/sites/teaching-learning/files/bme_conference_2018_the_persistence_of_racism_in_higher_education_understanding_the_bme_attainment_gap.pdf) | PDF / 16 pages | `d0e289b8271edd1529e0a0e1c2d0e4ca8487b8eec29d39ff0a248621ba3082c8` | captured |
| `assets/documents/cambridge-correction.pdf` | [Cambridge repository correction](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17576301-dca8-4e33-b837-34db54d1a21d/content) | PDF / 2 pages | `fe97d838e760b5d585a1a2934bdfeb8a57f26ce446a1eac14e9406d7e6097745` | captured |
| `assets/documents/black-curriculum-2021.pdf` | [The Black Curriculum report](https://theblackcurriculum.com/s/The-Black-Curriculum-Black-British-History-in-The-National-Curriculum-2021-1.pdf) | PDF / 13 pages | `e6c4bf7a16191b74ec34deb0ea9262fe2c4d8d0dfd3edfda163dcc33dbb71fa6` | captured |
| `assets/documents/ljmu-thesis.pdf` | [LJMU thesis](https://researchonline.ljmu.ac.uk/4552/1/158222_Jason%20Arday_%20Final%20PhD%20Thesis%20Vesrion%20Final%20Draft%20Oct%202015.pdf) | PDF / 401 pages | `e5772e9855a7ee190adaafba9743b8d00b0a6b739da38e997e835630bb983f1a` | captured |
| `assets/documents/whigham-arday-response.pdf` | [Oxford Brookes RADAR manuscript](https://radar.brookes.ac.uk/radar/file/5a92b883-321b-4c34-8a61-9757b1c27c1c/1/Educational%20outcomes%20for%20Black%20students%20-%20Sociological%20persective%20-%202021%20-%20Whigham%20Arday.pdf) | PDF / 11 pages | `dd25622e296d4cc5500893deadfed532438aa4ea4e2ad7e7c42f23ff54a958bc` | captured |

## Failed acquisition retained

- BBC Lent Talk transcript PDF: `https://static1.squarespace.com/static/5c65dd81af46834afd07e40a/t/6056605ac3c8c96e0595153f/1616273501339/lives%2Bretold%2Barday%2Bjason.pdf`
- Result: `curl` failed with DNS error `Could not resolve host: static1.squarespace.com` on 2026-08-05.
- The public transcript URL and its source record remain authoritative leads; no local transcript file is claimed.
- PeDOCS article PDF was also attempted and failed with DNS resolution; the open article record remains a link-only source.
- 2024 *Elite schools and slavery in the UK* accepted manuscript: `https://durham-repository.worktribe.com/OutputFile/2160477` returned HTTP 403 on 2026-08-05; the Durham metadata and DOI remain preserved.
