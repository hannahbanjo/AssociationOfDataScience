# SEC Women's Tournament Analysis — Claude Code CLI Sub-Agent Approach

## Overview

This project uses Claude Code's native sub-agent capabilities to perform a multi-agent analysis of the SEC Women's Basketball Tournament. Rather than writing a custom orchestration script, Claude Code itself manages the decomposition, parallel execution, and sequential handoffs between specialized agents — all from the CLI.

The result is a data-driven tournament preview including team profiles, matchup assessments, upset picks, and a final narrative report.

---

## Why Claude Code Sub-Agents vs. a Scripted Approach

| Scripted Orchestration | Claude Code Sub-Agents |
|---|---|
| Requires Python orchestration code | No orchestration code needed |
| Agent logic lives in scripts | Agent logic lives in CLAUDE.md and prompts |
| Students learn the plumbing | Students learn the thinking |
| Harder to adapt to new problems | CLAUDE.md is portable to any similar project |
| More setup and debugging | Claude Code manages decomposition natively |

Claude Code natively supports spawning parallel sub-agents, managing handoffs, and synthesizing outputs. This is a built-in CLI capability — not something that needs to be engineered. It also makes for a more compelling live demo because students see agentic behavior happening in real time at the terminal.

---

## How It Works

You give Claude Code a high-level goal. Claude Code reads the project context from `CLAUDE.md`, decomposes the task into specialized sub-agents, runs parallel agents simultaneously, collects their outputs, and hands off sequentially to synthesis. All of this is visible in the terminal as it happens.

### Example Invocation

```bash
claude "Analyze the SEC women's basketball tournament using the agent architecture defined in CLAUDE.md. Use the data in /data or gather it live if needed. Produce a full tournament preview in /output/tournament_preview.md"
```

That single prompt triggers the entire pipeline.

---

## Execution Flow

```
Claude Code CLI receives high-level goal
              ↓
     Reads CLAUDE.md for context
              ↓
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

**Phase 1 — Sequential:** Data Gatherer runs alone first. Its clean output becomes the shared input for everything downstream.

**Phase 2 — Parallel:** Team Profiler, Matchup Analyst, and Upset Detector run simultaneously, each analyzing the data from a different angle.

**Phase 3 — Sequential:** Narrative & Reporting agent collects all three outputs and synthesizes the final tournament preview.

---

## The Five Sub-Agents

### Sub-Agent 1 — Data Gatherer & Cleaner
- **Goal:** Find, pull, and normalize SEC women's basketball team statistics
- **Inputs:** SEC tournament bracket and team list
- **Outputs:** Clean, structured dataset with consistent metrics — offensive/defensive efficiency, pace, shooting splits, turnover rates, strength of schedule, recent form
- **Data strategy:** Attempts live scraping first; falls back to `/data/sec_teams.csv` if needed
- **Teaching moment:** Data provenance — clean inputs determine the quality of everything downstream

### Sub-Agent 2 — Team Profiler *(parallel)*
- **Goal:** Build a statistical portrait of each SEC tournament team
- **Inputs:** Clean dataset from Sub-Agent 1
- **Outputs:** Structured profile per team — strengths, weaknesses, style of play, key players, tournament trajectory
- **Teaching moment:** Translating raw numbers into analytical meaning

### Sub-Agent 3 — Matchup Analyst *(parallel)*
- **Goal:** Head-to-head assessment of tournament matchups
- **Inputs:** Clean dataset from Sub-Agent 1, bracket structure
- **Outputs:** Per matchup — dimensional advantages, predicted game flow, winner with reasoning and confidence level
- **Teaching moment:** Structured reasoning and comparative analysis under uncertainty

### Sub-Agent 4 — Upset Detector *(parallel)*
- **Goal:** Identify mismatches between seeding and underlying metrics
- **Inputs:** Clean dataset from Sub-Agent 1, bracket seedings
- **Outputs:** Ranked upset candidates with supporting statistical evidence
- **Teaching moment:** The gap between perception (seeding) and reality (metrics)

### Sub-Agent 5 — Narrative & Reporting *(sequential, runs last)*
- **Goal:** Synthesize all outputs into a clean, publishable tournament preview
- **Inputs:** Profiles from Sub-Agent 2, matchup assessments from Sub-Agent 3, upset picks from Sub-Agent 4
- **Outputs:** `/output/tournament_preview.md` — bracket predictions, upset picks, Final Four projection, key storylines
- **Teaching moment:** AI as a communication tool, not just an analysis tool — closing the pipeline into something stakeholders can actually read

---

## Project Structure

```
sec_tournament_agents/
├── CLAUDE.md               # heart of the project — context and agent instructions
├── README.md               # how to run it
├── data/
│   └── sec_teams.csv       # fallback dataset if live scraping fails
└── output/
    └── tournament_preview.md   # generated by Sub-Agent 5
```

No orchestration scripts. No agent Python files. The `CLAUDE.md` file is the core artifact — it defines the entire project and is what students take away and adapt.

---

## The CLAUDE.md File — Why It Matters

`CLAUDE.md` is the persistent instruction set that Claude Code reads at the start of every session. It replaces what would otherwise be a Python orchestration script. It tells Claude Code:

- What this project is and what the goal is
- What each sub-agent is responsible for
- What data is available and where to find it
- What the expected outputs are and where to write them
- How to handle fallbacks and edge cases

Because the logic lives in a markdown file rather than code, students can pick it up, modify the agent roles, point it at a different dataset or tournament, and run the whole pipeline themselves with minimal friction. It teaches them how to *think* about structuring agent projects rather than how to read someone else's Python.

---

## What Students Need to Run This

1. **Claude Code CLI installed** — `npm install -g @anthropic-ai/claude-code`
2. **Anthropic API key** — set as environment variable `ANTHROPIC_API_KEY`
3. **Clone or download this project folder**
4. **Run the invocation command** from the project root

API costs for a full pipeline run are very small — typically a few cents. Students will need their own Anthropic account to get an API key.

---

## Live Demo Flow (Session Guide)

| Step | What happens | What to narrate |
|---|---|---|
| Show project folder | Open the folder, show CLAUDE.md | "This file is the entire brain of the project" |
| Run invocation | Execute the claude command in terminal | "One prompt, five agents" |
| Agent 1 runs | Watch data gathering in terminal | "Notice it's deciding what data it needs" |
| Agents 2-4 run | Parallel execution visible in terminal | "Three agents working simultaneously" |
| Agent 5 runs | Synthesis phase begins | "Now it's reading what the other agents found" |
| Open output | Show tournament_preview.md | "From raw data to publishable report" |
| Discuss | Where did it surprise you? Where would you push back? | Critical evaluation instincts |

---

## Student Exercise

After the demo, students receive the same project folder and a different prompt — for example a specific regional matchup or a question like *"which SEC team is most dangerous as a low seed?"* They use Claude Code to run their own analysis and share findings with the group.

The variation in outputs across groups — from the same data and same agent architecture — is itself a teaching moment about how prompt framing shapes analytical conclusions.

---

## Key Takeaways for Students

- Complex analytical problems can be decomposed into specialized agent roles without writing orchestration code
- Parallel and sequential execution patterns mirror how real analytics teams are structured
- The quality of your problem framing determines the quality of the agent's output
- AI-generated analysis must be critically evaluated — the agents can be wrong, biased by data quality, or overconfident
- The CLAUDE.md pattern is portable — this same architecture applies to any data science problem

