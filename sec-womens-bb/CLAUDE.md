# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This is a **multi-agent data science demonstration** for classroom use. Claude Code uses its native sub-agent capabilities to produce a professional-grade SEC Women's Basketball Tournament preview — no custom orchestration code required. This file replaces what would otherwise be a Python orchestration script.

## Invocation

**Use existing local data (recommended for demos — faster, no scraping):**
```bash
claude "Analyze the SEC women's basketball tournament using the agent architecture defined in CLAUDE.md. Use the existing data in /data as-is — do not attempt live scraping. Produce a full tournament preview in /output/tournament_preview.md"
```

**Allow live data refresh (use when stats may be stale):**
```bash
claude "Analyze the SEC women's basketball tournament using the agent architecture defined in CLAUDE.md. Use the data in /data or gather it live if needed. Produce a full tournament preview in /output/tournament_preview.md"
```

Either prompt triggers the full five-agent pipeline. The only difference is whether Sub-Agent 1 attempts web scraping.

## Project Structure

```
sec-womens-bb/
├── CLAUDE.md               # this file — project context and agent instructions
├── README.md               # student setup instructions
├── data/
│   ├── sec_teams.csv       # fallback dataset (team stats)
│   └── bracket.json        # tournament seedings and bracket structure
├── scripts/
│   ├── build_data.py       # scrapes and regenerates sec_teams.csv
│   ├── build_bracket.py    # derives seedings and regenerates bracket.json
│   └── generate_pdf.py     # renders presentation/tournament-preview.html → PDF
├── output/                 # all agent outputs written here
│   ├── team_profiles.md    # Sub-Agent 2
│   ├── matchup_analysis.md # Sub-Agent 3
│   ├── upset_report.md     # Sub-Agent 4
│   └── tournament_preview.md  # Sub-Agent 5 (final output)
└── presentation/           # Sub-Agent 5 also writes here
    ├── tournament-preview.html  # print-optimized HTML report
    ├── tournament-preview.pdf   # generated from HTML via Playwright
    └── analysis-deck.html       # 10-slide analysis slide deck
```

---

## Agent Architecture

### Execution Flow

```
[Sub-Agent 1: Data Gatherer & Cleaner]
              ↓ clean dataset
   ┌──────────┼──────────┐
   ↓          ↓          ↓
[Sub-Agent 2] [Sub-Agent 3] [Sub-Agent 4]
 Team          Matchup       Upset
 Profiler      Analyst       Detector
   └──────────┬──────────┘
              ↓ all outputs collected
  [Sub-Agent 5: Narrative & Reporting]
              ↓
    /output/tournament_preview.md
```

**Phase 1 — Sequential:** Sub-Agent 1 runs first and alone. Its clean output is the shared input for everything downstream.

**Phase 2 — Parallel:** Sub-Agents 2, 3, and 4 run simultaneously once Sub-Agent 1 completes. **Each must write its output to a file in `/output/`** before returning — this is how Sub-Agent 5 consumes their work without the orchestrator needing to stay alive.

**Phase 3 — Sequential:** Sub-Agent 5 reads the three output files and synthesizes the final report.

**Important orchestration note:** Launch Phase 2 agents with `run_in_background: false` (foreground). This ensures the orchestrator waits for each to complete before proceeding to Sub-Agent 5, rather than hitting a turn limit while polling background tasks.

---

### Sub-Agent 1 — Data Gatherer & Cleaner

**Goal:** Find, pull, and normalize SEC women's basketball team statistics.

**Inputs:** SEC tournament bracket and team list.

**Outputs:** Clean, structured dataset with consistent metrics across all teams:
- Offensive/defensive efficiency
- Pace
- Shooting splits
- Turnover rates
- Strength of schedule
- Recent form

**Data strategy:** Attempt live web scraping first. If scraping fails or produces inconsistent data, fall back to `/data/sec_teams.csv`. Document the data source in the output so downstream agents know its provenance.

---

### Sub-Agent 2 — Team Profiler *(parallel)*

**Goal:** Build a statistical portrait of each SEC tournament team.

**Inputs:** Clean dataset from Sub-Agent 1.

**Outputs:** Write to `output/team_profiles.md` — structured profile per team covering strengths, weaknesses, style of play, key players, and tournament trajectory.

---

### Sub-Agent 3 — Matchup Analyst *(parallel)*

**Goal:** Head-to-head assessment of tournament matchups.

**Inputs:** Clean dataset from Sub-Agent 1, bracket structure from `data/bracket.json`.

**Outputs:** Write to `output/matchup_analysis.md` — per matchup: dimensional advantages, predicted game flow, winner with reasoning and confidence level.

---

### Sub-Agent 4 — Upset Detector *(parallel)*

**Goal:** Identify mismatches between seeding and underlying metrics.

**Inputs:** Clean dataset from Sub-Agent 1, bracket seedings from `data/bracket.json`.

**Outputs:** Write to `output/upset_report.md` — ranked list of upset candidates with supporting statistical evidence.

---

### Sub-Agent 5 — Narrative & Reporting *(sequential, runs last)*

**Goal:** Synthesize all outputs into a publishable tournament preview and deliver three presentation artifacts.

**Inputs:** Read `output/team_profiles.md`, `output/matchup_analysis.md`, and `output/upset_report.md`.

**Outputs — produce all four of the following:**

1. **`output/tournament_preview.md`** — the full narrative report: bracket predictions, upset picks, Final Four projection, key storylines, stat leaders, data note.

2. **`presentation/tournament-preview.html`** — a self-contained, print-optimized HTML version of the same report. Light theme (white background, Georgia serif body font, `--gold: #c8860a` accent). Sections: header with title/date/tagline, executive summary, field-at-a-glance table (all 16 teams with seed/record/ORtg/DRtg/SRS), five key storylines, all 15 game picks (each game as a styled block with teams, prediction, confidence label, and one-sentence rationale), bracket summary, upset alerts, stat leaders table, data provenance note. Color-code confidence: High = green, Medium = blue, Low = amber.

3. **`presentation/tournament-preview.pdf`** — generated from the HTML above by running:
   ```bash
   python scripts/generate_pdf.py
   ```
   This script uses Playwright (installed in `.venv`). Run it as: `.venv/bin/python scripts/generate_pdf.py`

4. **`presentation/analysis-deck.html`** — a self-contained 10-slide HTML presentation (keyboard arrow navigation, slide counter). Dark theme (`#0b0e14` background, `#e8a020` gold accent, same design system as `presentation/intro-deck.html`). Slides:
   - Slide 1: Title — tournament name, year, "Powered by Claude Code" subtitle
   - Slide 2: The Field — 16-team tier grid (Contenders / Dangerous / Longshots)
   - Slide 3: Top storyline #1 (key team comparison or anomaly surfaced by the data)
   - Slide 4: Top storyline #2
   - Slide 5: First-round picks grid (all Round 1 matchups with predicted winners)
   - Slide 6: Upset picks (top 3 upset candidates with seed differential and key stat)
   - Slide 7: Final Four projections (4 teams, with brief reasoning)
   - Slide 8: Championship pick (matchup, key stats head-to-head, predicted winner)
   - Slide 9: Stat leaders (top 3 in ORtg, DRtg, SRS — displayed as columns)
   - Slide 10: About this report — data source, pipeline note, date generated

---

---

## Fallback Data

**Sources:**
- [Advanced School Stats](https://www.sports-reference.com/cbb/seasons/women/2026-advanced-school-stats.html) — ORtg, Pace, shooting, turnover, and rebound metrics
- [Advanced Opponent Stats](https://www.sports-reference.com/cbb/seasons/women/2026-advanced-opponent-stats.html) — DRtg (opponent ORtg = defensive efficiency allowed)

Both pages are scraped and joined on team name. No login required.

**To regenerate `data/sec_teams.csv`:**
```bash
python scripts/build_data.py
```

**To regenerate `data/bracket.json`** (re-run after March 1 regular season games to lock in final seedings):
```bash
python scripts/build_bracket.py
```

Seedings are derived from conference win % in `sec_teams.csv`, with SRS as the tiebreaker. The bracket structure (matchups, dates, times, networks) is fixed in `build_bracket.py` — only the seed-to-team mapping is recalculated.

The script scrapes the advanced stats table, filters to the 16 SEC teams, applies friendly team names (Sports Reference uses "Louisiana State" and "Mississippi" — the script renames these to "LSU" and "Ole Miss"), and writes `data/sec_teams.csv`.

**Column reference:**

| Column | Description |
|--------|-------------|
| G, W, L, W-L% | Record |
| SRS | Simple Rating System — average point differential adjusted for SOS |
| SOS | Strength of Schedule |
| Pace | Possessions per 40 minutes |
| ORtg | Offensive efficiency (points per 100 possessions) |
| DRtg | Defensive efficiency (points allowed per 100 opponent possessions) |
| FTr | Free throw rate (FTA/FGA) |
| 3PAr | Three-point attempt rate (3PA/FGA) |
| TS% | True shooting percentage |
| eFG% | Effective field goal percentage |
| TOV% | Turnover percentage |
| ORB% | Offensive rebound percentage |
| FT/FGA | Free throws made per field goal attempt |
| Conf_W / Conf_L | Conference wins and losses (used to derive tournament seedings) |

---

## Edge Cases

- If live data is unavailable, use `/data/sec_teams.csv` as fallback and note this in the report.
- If a matchup cannot be assessed due to missing data, note the gap explicitly rather than fabricating estimates.
- If agents produce conflicting conclusions, Sub-Agent 5 should surface the disagreement rather than silently resolve it.
