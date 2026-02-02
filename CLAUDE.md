# Claude Code Project Context

This file provides context for Claude Code sessions working on this academic CV project.

## Project Overview

This is Patrick E. McKnight's academic CV system that generates:
1. **Interactive HTML CV** — With Plotly visualizations, hosted on GitHub Pages
2. **PDF CV** — Clean 10-page document via Typst
3. **NIH Biosketch** — 5-page NIH format, tailored for well-being grant proposals

## Key Files

| File | Purpose |
|------|---------|
| `publications.yaml` | **Single source of truth** — All CV data (publications, grants, positions, etc.) |
| `cv.qmd` | Main CV template (Quarto + Python) |
| `nih-biosketch.qmd` | NIH Biosketch template |
| `.github/workflows/build-cv.yml` | GitHub Actions workflow |

## Architecture Decisions

### Why Typst instead of LaTeX?
- No external dependencies (TinyTeX had 403 errors on GitHub Actions)
- Faster compilation
- Cleaner syntax
- Still produces professional PDF output

### Why conditional Plotly execution?
- Plotly generates HTML widgets that can't render in PDF
- `IS_HTML = os.environ.get('QUARTO_FIG_FORMAT', '') != 'svg'` detects output format
- Charts wrapped in `if IS_HTML:` blocks only execute for HTML output
- PDF gets clean text-only content

### CV Structure Philosophy
- **Standard academic order**: Education → Positions → Publications → Funding → Teaching
- **Scholarly Impact section at end** (not top) — metrics and visualizations grouped together
- **Complete publication list** in HTML/PDF, curated selection in NIH biosketch

## Common Tasks

### Update publications
Edit `publications.yaml`, push to main. GitHub Actions rebuilds automatically.

### Render locally
```bash
source .venv/bin/activate
quarto render cv.qmd --to html   # Interactive HTML
quarto render cv.qmd --to typst  # PDF via Typst
quarto render nih-biosketch.qmd --to typst  # NIH Biosketch
```

### Check for PDF errors
```bash
pdftotext cv.pdf - | grep -i "unable to display"
```
If this returns matches, Plotly code is executing in PDF context — wrap in `if IS_HTML:`.

## Data Structure in publications.yaml

```yaml
publications:
  books: [...]           # 2 books
  book_chapters: [...]   # 6 chapters
  articles: [...]        # 89 journal articles

grants:
  funded: [...]          # 11 grants

positions:
  current: [...]
  previous: [...]

education: [...]
courses:
  graduate: [...]
  undergraduate: [...]
students_graduated: [...]
students_current: [...]
affiliations: [...]
skills:
  statistical: [...]
  sem: [...]
  irt: [...]
  programming: [...]
personal:
  athletics: {...}       # Mountaineering, swimming, triathlon
metrics:                 # Google Scholar stats
  total_citations: 17454
  h_index: 62
  i10_index: 108
```

## Deployment

- **GitHub Pages**: Deploys from `gh-pages` branch automatically
- **URLs**:
  - HTML: https://pem725.github.io/cv/
  - PDF: https://pem725.github.io/cv/McKnight_CV.pdf
  - Biosketch: https://pem725.github.io/cv/McKnight_NIH_Biosketch.pdf

## Git Workflow Notes

GitHub Actions auto-commits generated files, which can cause merge conflicts when pushing local changes. Standard resolution:
```bash
git pull --rebase origin main
git checkout --ours *.pdf *.html
git add *.pdf *.html
git rebase --continue
git push origin main
```

## Style Guidelines

- **HTML theme**: cosmo (clean, conservative)
- **PDF font**: Linux Libertine, 11pt
- **Margins**: 1 inch
- **Color palette**: Conservative academic tones (#2c3e50, #34495e, #c0392b)
- **No emojis** in generated documents
