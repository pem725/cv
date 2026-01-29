# Patrick E. McKnight, Ph.D. — Curriculum Vitae

[![Build CV](https://github.com/pem725/cv/actions/workflows/build-cv.yml/badge.svg)](https://github.com/pem725/cv/actions/workflows/build-cv.yml)

This repository contains my academic CV and NIH Biosketch, automatically built and updated using Quarto and GitHub Actions.

## 📄 Quick Links

- **[Download CV (PDF)](McKnight_CV.pdf)** — Full curriculum vitae
- **[Download NIH Biosketch (PDF)](McKnight_NIH_Biosketch.pdf)** — Standard NIH format

## 🔄 Automatic Updates

This CV is automatically rebuilt:
- On every push to `main`
- Weekly (Mondays at 6am UTC) to refresh Google Scholar metrics
- On demand via manual workflow trigger

Each PDF includes a generation date stamp in the footer.

## 📊 Current Metrics

| Metric | Value |
|--------|-------|
| Total Citations | 17,400+ |
| h-index | 60+ |
| i10-index | 100+ |

*Metrics pulled from [Google Scholar](https://scholar.google.com/citations?user=sH44LC4AAAAJ)*

## 🏗️ Building Locally

### Prerequisites
- [Quarto](https://quarto.org/) (≥1.3)
- R with packages: `scholar`, `dplyr`, `knitr`
- LaTeX (TinyTeX recommended)

### Build Commands

```bash
# Install R dependencies
Rscript -e 'install.packages(c("scholar", "dplyr", "knitr"))'

# Build CV
quarto render cv.qmd --to pdf

# Build NIH Biosketch
quarto render nih-biosketch.qmd --to pdf
```

## 📁 Repository Structure

```
├── cv.qmd                    # Full CV source (Quarto markdown)
├── nih-biosketch.qmd         # NIH Biosketch source
├── McKnight_CV.pdf           # Generated CV (always current)
├── McKnight_NIH_Biosketch.pdf # Generated biosketch (always current)
├── .github/
│   └── workflows/
│       └── build-cv.yml      # GitHub Actions workflow
└── README.md
```

## 📬 Contact

**Patrick E. McKnight, Ph.D.**
Associate Professor of Psychology
George Mason University
Fairfax, VA 22030

- Email: [pmcknigh@gmu.edu](mailto:pmcknigh@gmu.edu)
- GMU Profile: [psychology.gmu.edu/people/pmcknigh](https://psychology.gmu.edu/people/pmcknigh)
- Google Scholar: [scholar.google.com/citations?user=sH44LC4AAAAJ](https://scholar.google.com/citations?user=sH44LC4AAAAJ)

## 📜 License

Content © Patrick E. McKnight. Template and build system available under MIT license.
