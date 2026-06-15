# CV maintenance tools

Stdlib-only Python helpers that operate on `../publications.yaml`. No client
secret needed — they use public APIs (ORCID Public, Crossref).

- **sync_orcid.py** — find works on the ORCID public record missing from
  publications.yaml. Dry-run by default; `--write` appends new journal articles
  (flagged `category: "TODO"`). Matches by DOI then fuzzy title; skips errata.
- **backfill_dois.py** — add DOIs to existing entries by matching titles against
  ORCID. Dry-run shows a diff; `--write` applies (backs up first).
- **crossref_year_audit.py** — verify each DOI'd article's year against Crossref
  (online-first vs print aware). Report only.

Run from anywhere: `python3 tools/sync_orcid.py`. After edits, the
`build-cv.yml` workflow re-renders and deploys on push to `main`.
