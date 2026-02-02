# Patrick E. McKnight, Ph.D. — Academic CV

[![Build CV](https://github.com/pem725/cv/actions/workflows/build-cv.yml/badge.svg)](https://github.com/pem725/cv/actions/workflows/build-cv.yml)

Professional academic CV with interactive visualizations (HTML) and clean PDF output, powered by Quarto, Python, and Typst.

## Live Site

**[View Interactive CV](https://pem725.github.io/cv)**

## Downloads

| Document | Description |
|----------|-------------|
| [CV (PDF)](https://pem725.github.io/cv/McKnight_CV.pdf) | Full curriculum vitae (10 pages) |
| [NIH Biosketch (PDF)](https://pem725.github.io/cv/McKnight_NIH_Biosketch.pdf) | NIH format, well-being focus |

## Features

- **Complete publication record** — 89 journal articles, 6 book chapters, 2 books (1995–2025)
- **Interactive visualizations** — Citation metrics, publication trends, funding charts (HTML only)
- **Professional PDF output** — Clean Typst-generated PDF with Linux Libertine font
- **NIH Biosketch** — Matching format, tailored for well-being grant proposals
- **Automatic updates** — Rebuilt weekly via GitHub Actions
- **Single source of truth** — All data in `publications.yaml`

## Current Metrics

| Metric | Value |
|--------|-------|
| Total Citations | 17,454 |
| h-index | 62 |
| i10-index | 108 |
| Publications | 97 (89 articles + 6 chapters + 2 books) |

*Via [Google Scholar](https://scholar.google.com/citations?user=sH44LC4AAAAJ)*

## Technology Stack

- **[Quarto](https://quarto.org/)** — Scientific publishing system
- **[Typst](https://typst.app/)** — Modern PDF typesetting (replaces LaTeX)
- **[Python](https://python.org/)** — Data processing (pandas, pyyaml)
- **[Plotly](https://plotly.com/)** — Interactive visualizations (HTML only)
- **[GitHub Actions](https://github.com/features/actions)** — Automated builds
- **[GitHub Pages](https://pages.github.com/)** — Web hosting

## Building Locally

### Prerequisites

- Python 3.11+
- [Quarto](https://quarto.org/docs/get-started/) ≥1.4
- Typst (installed automatically by Quarto, or via `curl -fsSL https://typst.community/typst-install/install.sh | sh`)

### Build Commands

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build HTML (with interactive charts)
quarto render cv.qmd --to html

# Build PDF (clean text output via Typst)
quarto render cv.qmd --to typst

# Build NIH Biosketch
quarto render nih-biosketch.qmd --to typst
```

## Repository Structure

```
├── cv.qmd                     # Main CV source (Quarto + Python)
├── nih-biosketch.qmd          # NIH Biosketch source
├── publications.yaml          # Single source of truth for all data
├── requirements.txt           # Python dependencies
├── index.html                 # Generated HTML CV
├── McKnight_CV.pdf            # Generated PDF CV
├── McKnight_NIH_Biosketch.pdf # Generated NIH Biosketch
├── CLAUDE.md                  # Claude Code project context
└── .github/workflows/
    └── build-cv.yml           # GitHub Actions workflow
```

## Updating Content

All CV content is stored in `publications.yaml`. To update:

1. Edit `publications.yaml` with new publications, grants, positions, etc.
2. Push to `main` branch
3. GitHub Actions will automatically rebuild all outputs

### Adding a Publication

```yaml
publications:
  articles:
    - authors: "McKnight, P.E., et al."
      year: 2026
      title: "New Finding Title"
      journal: "Journal Name"
      volume: "10"
      pages: "1-15"
      citations: 0
      category: "methodology"  # or: purpose, curiosity, wellbeing, anxiety, health, etc.
```

### Categories for Publications

Used for grouping in the Scholarly Impact visualizations:
- `methodology` — Quantitative methods, missing data, measurement
- `purpose` — Purpose in life research
- `curiosity` — Curiosity and exploration
- `wellbeing` — Well-being and positive psychology
- `anxiety` — Anxiety and emotional disorders
- `health` — Health psychology and outcomes
- `cognition` — Cognitive psychology
- `education` — Educational research

## CV Structure

**Standard Academic Order:**
1. Contact Information
2. Education
3. Academic Positions
4. Books
5. Book Chapters
6. Journal Articles (complete list)
7. Research Funding
8. Teaching
9. Doctoral Students
10. Professional Affiliations
11. Technical Skills
12. Scholarly Impact (metrics + interactive charts in HTML)
13. Beyond Academia

## Contact

**Patrick E. McKnight, Ph.D.**
Associate Professor of Psychology
George Mason University

- [pmcknigh@gmu.edu](mailto:pmcknigh@gmu.edu)
- [GMU Profile](https://psychology.gmu.edu/people/pmcknigh)
- [Google Scholar](https://scholar.google.com/citations?user=sH44LC4AAAAJ)
- [ORCID](https://orcid.org/0000-0002-9067-9066)

## License

Content © Patrick E. McKnight. Code available under MIT license.
