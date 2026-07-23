#!/usr/bin/env python3
"""Build a clean, chart-free Markdown CV from publications.yaml.

This is the text-only companion to cv.qmd (which produces the interactive HTML and
the Typst PDF). It exists so the Google Drive copy of the CV can be regenerated from
the same single source of truth without the Plotly visualizations, and then handed to
pandoc to produce an editable Word document.

Usage:
    python3 tools/build_markdown_cv.py [--date YYYY-MM-DD] [-o output.md]

With no output path it writes to stdout.
"""
import argparse
import datetime as _dt
import sys

import yaml


def esc(text):
    return str(text)


def emit(data, as_of):
    out = []
    w = out.append

    c = data.get("contact", {})
    m = data.get("metrics", {})

    # Header ------------------------------------------------------------------
    w(f"# Patrick E. McKnight, Ph.D.\n")
    w(f"*Curriculum Vitae — as of {as_of}*\n")

    contact_bits = []
    if c.get("office"):
        contact_bits.append(c["office"])
    if c.get("email"):
        contact_bits.append(f"{c['email']}")
    if c.get("phone"):
        contact_bits.append(c["phone"])
    if contact_bits:
        w(" · ".join(contact_bits) + "\n")

    ids = []
    if data.get("orcid"):
        ids.append(f"ORCID: {data['orcid']}")
    if data.get("scholar_id"):
        ids.append(
            f"Google Scholar: https://scholar.google.com/citations?user={data['scholar_id']}"
        )
    if data.get("era_commons"):
        ids.append(f"eRA Commons: {data['era_commons']}")
    if data.get("erdos_number"):
        ids.append(f"Erdős number: {data['erdos_number']}")
    if ids:
        w(" · ".join(ids) + "\n")

    if m:
        pieces = []
        if m.get("total_citations"):
            pieces.append(f"{m['total_citations']:,} citations")
        if m.get("h_index"):
            pieces.append(f"h-index {m['h_index']}")
        if m.get("i10_index"):
            pieces.append(f"i10-index {m['i10_index']}")
        line = "**Scholarly impact:** " + ", ".join(pieces)
        if m.get("citations_since_2021"):
            line += f" (since 2021: {m['citations_since_2021']:,} citations"
            if m.get("h_index_since_2021"):
                line += f", h-index {m['h_index_since_2021']}"
            if m.get("i10_index_since_2021"):
                line += f", i10-index {m['i10_index_since_2021']}"
            line += ")"
        if m.get("last_updated"):
            line += f" — as of {m['last_updated']}"
        w(line + "\n")

    # Education ---------------------------------------------------------------
    w("\n## Education\n")
    for e in data.get("education", []):
        line = f"- **{e['degree']}**, {e['institution']}"
        if e.get("field"):
            line += f" — {e['field']}"
        line += f" ({e['year']})"
        w(line)
        if e.get("details"):
            w(f"  \n  {e['details']}")
    w("")

    # Positions ---------------------------------------------------------------
    w("\n## Academic & Professional Appointments\n")
    positions = data.get("positions", {})
    for label, key in (("Current", "current"), ("Previous", "previous")):
        rows = positions.get(key, [])
        if not rows:
            continue
        w(f"### {label}\n")
        for p in rows:
            end = "present" if p.get("current") else p.get("end", "")
            dept = f", {p['department']}" if p.get("department") else ""
            w(f"- **{p['title']}**, {p['institution']}{dept} ({p['start']}–{end})")
        w("")

    # Honors ------------------------------------------------------------------
    honors = sorted(data.get("honors", []), key=lambda x: x.get("year", 0), reverse=True)
    if honors:
        w("\n## Honors & Awards\n")
        for h in honors:
            org = f" — {h['org']}" if h.get("org") else ""
            w(f"- **{h['year']}.** {h['title']}{org}")
        w("")

    pubs = data.get("publications", {})

    # Books -------------------------------------------------------------------
    if pubs.get("books"):
        w("\n## Books\n")
        for b in pubs["books"]:
            cites = f" [{b['citations']:,} citations]" if b.get("citations") else ""
            w(
                f"- {b['authors']} ({b['year']}). *{b['title']}*. "
                f"{b.get('location','')}: {b['publisher']}.{cites}"
            )
        w("")

    # Book chapters -----------------------------------------------------------
    if pubs.get("book_chapters"):
        w("\n## Book Chapters\n")
        for ch in sorted(pubs["book_chapters"], key=lambda x: x["year"], reverse=True):
            editors = ch.get("editors", ch.get("editor", ""))
            line = (
                f"- {ch['authors']} ({ch['year']}). {ch['title']}. "
                f"In {editors} (Eds.), *{ch['book']}*. {ch['publisher']}."
            )
            if ch.get("status"):
                line = line.rstrip(".") + f" ({ch['status']})."
            w(line)
        w("")

    # Journal articles --------------------------------------------------------
    if pubs.get("articles"):
        articles = sorted(pubs["articles"], key=lambda x: x["year"], reverse=True)
        w(f"\n## Journal Articles\n")
        w(f"*{len(articles)} peer-reviewed articles*\n")
        current_year = None
        for a in articles:
            if a["year"] != current_year:
                current_year = a["year"]
                w(f"### {current_year}\n")
            cite = f"{a['authors']} ({a['year']}). {a['title']}. "
            if a.get("journal"):
                cite += f"*{a['journal']}*"
                if a.get("volume"):
                    cite += f", {a['volume']}"
                    if a.get("issue"):
                        cite += f"({a['issue']})"
                if a.get("pages"):
                    cite += f", {a['pages']}"
                cite += "."
            if a.get("status"):
                cite = cite.rstrip(".") + f" ({a['status']})."
            if a.get("doi"):
                cite += f" https://doi.org/{a['doi']}"
            w(f"- {cite}")
        w("")

    # Conference proceedings --------------------------------------------------
    if pubs.get("conference_proceedings"):
        w("\n## Conference Proceedings\n")
        for p in sorted(pubs["conference_proceedings"], key=lambda x: x["year"], reverse=True):
            w(f"- {p['authors']} ({p['year']}). {p['title']}. *{p['venue']}*.")
        w("")

    # Under review ------------------------------------------------------------
    if pubs.get("under_review"):
        w("\n## Manuscripts Under Review\n")
        for mnu in pubs["under_review"]:
            auth = mnu["authors"].rstrip()
            yr = f" ({mnu['year']})" if mnu.get("year") else ""
            venue = mnu.get("venue", "")
            at = f" *{venue}*." if venue and venue.lower() != "under review" else " *Under review*."
            note = f" [{mnu['note']}]" if mnu.get("note") else ""
            w(f"- {auth}{yr}. {mnu['title']}.{at}{note}")
        w("")

    # Preprints ---------------------------------------------------------------
    if pubs.get("preprints"):
        w("\n## Preprints & Working Papers\n")
        for p in sorted(pubs["preprints"], key=lambda x: x.get("year", 0), reverse=True):
            auth = p["authors"].rstrip()
            venue = f" *{p['venue']}*." if p.get("venue") else ""
            link = f" https://doi.org/{p['doi']}" if p.get("doi") else ""
            w(f"- {auth} ({p['year']}). {p['title']}.{venue}{link}")
        w("")

    # Software ----------------------------------------------------------------
    if pubs.get("software"):
        w("\n## Software\n")
        for s in pubs["software"]:
            url = f" <{s['url']}>" if s.get("url") else ""
            w(f"- **{s['name']}** — {s['desc']}.{url}")
        w("")

    # Funding -----------------------------------------------------------------
    grants = data.get("grants", {}).get("funded", [])
    if grants:
        total = sum(g.get("amount", 0) for g in grants)
        w("\n## Research Funding\n")
        w(f"**Total funding:** ${total:,.0f}\n")
        active = [g for g in grants if g.get("status") == "active"]
        past = [g for g in grants if g.get("status") != "active"]
        for label, rows in (("Active", active), ("Completed", past)):
            if not rows:
                continue
            w(f"### {label}\n")
            for g in rows:
                amt = f" — ${g['amount']:,}" if g.get("amount") else ""
                pi = (
                    f" (PI: {g['pi']})"
                    if g.get("pi") and g.get("role") != "Principal Investigator"
                    else ""
                )
                w(f"- **{g['title']}**{pi}  \n  {g['funder']} | {g['role']}{amt} | {g['start']}–{g['end']}")
            w("")

    # Teaching ----------------------------------------------------------------
    courses = data.get("courses", {})
    if courses:
        w("\n## Teaching\n")
        for label, key in (("Graduate Courses", "graduate"), ("Undergraduate Courses", "undergraduate")):
            rows = courses.get(key, [])
            if not rows:
                continue
            w(f"### {label}\n")
            for co in rows:
                yrs = f" ({co['years']})" if co.get("years") else ""
                w(f"- **{co['code']}** — {co['title']}{yrs}")
            w("")

    # Doctoral students -------------------------------------------------------
    grads = data.get("students_graduated", [])
    if grads:
        w("\n## Doctoral Students Graduated\n")
        for s in sorted(grads, key=lambda x: x.get("year", 0), reverse=True):
            inst = f", {s['institution']}" if s.get("institution") else ""
            w(f"- {s['name']}{inst} ({s.get('year','')})")
        w("")

    current_students = data.get("students_current", [])
    if current_students:
        w("\n## Current Students & Mentees (MRES Lab)\n")
        for s in current_students:
            w(f"- {s['name']}")
        w("")

    # Affiliations ------------------------------------------------------------
    affils = data.get("affiliations", [])
    if affils:
        w("\n## Professional Affiliations\n")
        for a in affils:
            role = f" — {a['role']}" if a.get("role") else ""
            start = f" (since {a['start']})" if a.get("start") else ""
            w(f"- {a['name']}{role}{start}")
        w("")

    # Skills ------------------------------------------------------------------
    skills = data.get("skills", {})
    if skills:
        w("\n## Technical Skills\n")
        labels = {
            "statistical": "Statistical software",
            "sem": "Structural equation modeling",
            "irt": "Item response theory",
            "programming": "Programming",
            "web": "Web",
        }
        for key, items in skills.items():
            w(f"- **{labels.get(key, key.title())}:** {', '.join(items)}")
        w("")

    # Beyond academia ---------------------------------------------------------
    personal = data.get("personal", {})
    ath = personal.get("athletics", {})
    if ath:
        w("\n## Beyond Academia\n")
        for group, entries in ath.items():
            pretty = group.replace("_", " ").title()
            lines = []
            for item in entries:
                if item.get("event"):
                    d = f" ({item['date']})" if item.get("date") else ""
                    lines.append(f"{item['event']}{d}")
                elif item.get("achievement"):
                    lines.append(item["achievement"])
            if lines:
                w(f"- **{pretty}:** " + "; ".join(lines))
        w("")

    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yaml", default="publications.yaml")
    ap.add_argument("--date", default=None, help="As-of date (YYYY-MM-DD); defaults to today")
    ap.add_argument("-o", "--output", default=None)
    args = ap.parse_args()

    as_of = args.date or _dt.date.today().isoformat()
    with open(args.yaml) as fh:
        data = yaml.safe_load(fh)

    md = emit(data, as_of)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(md)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
