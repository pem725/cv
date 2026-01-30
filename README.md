# Patrick E. McKnight, Ph.D. — Academic CV

[![Build CV](https://github.com/pem725/cv/actions/workflows/build-cv.yml/badge.svg)](https://github.com/pem725/cv/actions/workflows/build-cv.yml)
[![Netlify Status](https://api.netlify.com/api/v1/badges/placeholder/deploy-status)](https://pem-cv.netlify.app)

Interactive academic CV with visualizations, powered by Python, Quarto, and Plotly.

## 🌐 Live Site

**[View Interactive CV →](https://pem725.github.io/cv)**

## 📄 Quick Downloads

| Document | Description |
|----------|-------------|
| [**CV (PDF)**](McKnight_CV.pdf) | Full curriculum vitae |
| [**NIH Biosketch (PDF)**](McKnight_NIH_Biosketch.pdf) | Standard NIH format |

## ✨ Features

- **Interactive visualizations** — Citation metrics, publication timelines, funding charts
- **Responsive design** — Works on desktop and mobile
- **Automatic updates** — Rebuilt weekly via GitHub Actions
- **Date-stamped PDFs** — Always know when documents were generated
- **Single source of truth** — All data in `publications.yaml`

## 📊 Current Metrics

| Metric | Value |
|--------|-------|
| Total Citations | 17,400+ |
| h-index | 62 |
| i10-index | 108 |
| Publications | 130+ |

*Via [Google Scholar](https://scholar.google.com/citations?user=sH44LC4AAAAJ)*

## 🔧 Technology Stack

- **[Quarto](https://quarto.org/)** — Scientific publishing system
- **[Python](https://python.org/)** — Data processing (pandas, plotly)
- **[Plotly](https://plotly.com/)** — Interactive visualizations
- **[GitHub Actions](https://github.com/features/actions)** — Automated builds
- **[Netlify](https://netlify.com/)** — Web hosting (optional)

## 🏗️ Building Locally

### Prerequisites

- Python 3.11+
- [Quarto](https://quarto.org/docs/get-started/) ≥1.3
- LaTeX (TinyTeX via `quarto install tinytex`)

### Build Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Build interactive HTML
quarto render cv.qmd --to html

# Build PDF
quarto render cv.qmd --to pdf

# Build NIH Biosketch
quarto render nih-biosketch.qmd --to pdf
```

## 📁 Repository Structure

```
├── cv.qmd                    # Main CV source (Quarto + Python)
├── nih-biosketch.qmd         # NIH Biosketch source
├── publications.yaml         # Single source of truth for all data
├── custom.scss               # Custom styling
├── requirements.txt          # Python dependencies
├── McKnight_CV.pdf           # Generated CV
├── McKnight_NIH_Biosketch.pdf
├── netlify.toml              # Netlify deployment config
└── .github/workflows/
    └── build-cv.yml          # GitHub Actions workflow
```

## 📝 Updating Content

All CV content is stored in `publications.yaml`. To update:

1. Edit `publications.yaml` with new publications, grants, etc.
2. Push to `main` branch
3. GitHub Actions will automatically rebuild all outputs

### Adding a Publication

```yaml
publications:
  articles:
    - authors: "McKnight, P.E., et al."
      year: 2026
      title: "New Amazing Finding"
      journal: "Nature"
      volume: "999"
      pages: "1-10"
      citations: 0
      category: "measurement"
```

## 📬 Contact

**Patrick E. McKnight, Ph.D.**
Associate Professor of Psychology
George Mason University

- 📧 [pmcknigh@gmu.edu](mailto:pmcknigh@gmu.edu)
- 🏛️ [GMU Profile](https://psychology.gmu.edu/people/pmcknigh)
- 📚 [Google Scholar](https://scholar.google.com/citations?user=sH44LC4AAAAJ)
- 🔗 [ORCID](https://orcid.org/0000-0002-9067-9066)

## 📜 License

Content © Patrick E. McKnight. Code available under MIT license.
