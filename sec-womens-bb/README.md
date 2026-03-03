# SEC Women's Basketball Tournament — Multi-Agent Analysis

A live demonstration of multi-agent AI analysis using Claude Code's native sub-agent capabilities. One prompt triggers a five-agent pipeline that produces a full SEC Women's Basketball Tournament preview — team profiles, matchup breakdowns, upset picks, and a final narrative report.

## Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — `npm install -g @anthropic-ai/claude-code`
- Anthropic API key set as `ANTHROPIC_API_KEY`

## Running the Pipeline

From the project root:

```bash
claude "Analyze the SEC women's basketball tournament using the agent architecture defined in CLAUDE.md. Use the data in /data or gather it live if needed. Produce a full tournament preview in /output/tournament_preview.md"
```

The full report will be written to `/output/tournament_preview.md` when the pipeline completes.

## How It Works

Five specialized sub-agents run in a structured pipeline:

1. **Data Gatherer & Cleaner** — collects and normalizes SEC team statistics (runs first)
2. **Team Profiler** — builds a statistical portrait of each team (runs in parallel)
3. **Matchup Analyst** — assesses head-to-head tournament matchups (runs in parallel)
4. **Upset Detector** — identifies seeding vs. metrics mismatches (runs in parallel)
5. **Narrative & Reporting** — synthesizes everything into a publishable preview (runs last)

The agent roles and instructions are defined in `CLAUDE.md`. That file is the core artifact — modify it to change agent behavior, point the pipeline at a different tournament, or adapt it to a different data science problem entirely.

## Student Exercise

After the demo, try running your own analysis with a different prompt:

```bash
claude "Using the agent architecture in CLAUDE.md, analyze which SEC team is most dangerous as a low seed and make the case for them as a dark horse Final Four pick."
```

The variation in outputs from the same architecture and data — based solely on how you frame the prompt — is itself part of the lesson.

## Data

The pipeline attempts live web scraping first. If that fails, it falls back to `/data/sec_teams.csv`. You can populate that file in advance as a guaranteed fallback for live demos.
