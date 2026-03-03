# SEC Women's Tournament Multi-Agent Analysis System
## Project Outline

**Purpose:** A live demonstration for data science students showing how multiple specialized AI agents can collaborate to produce a professional-grade tournament preview, showcasing both parallel execution and sequential handoffs.

---

## The Five Agents

### Agent 1 — Data Gatherer & Cleaner
- **Role:** Find, pull, and normalize SEC women's basketball team statistics
- **Inputs:** List of SEC tournament teams, bracket seedings
- **Outputs:** A clean, structured dataset (dataframe or JSON) with consistent metrics across all teams — offensive/defensive efficiency, pace, shooting splits, turnover rates, strength of schedule, recent form
- **Runs:** First, independently, before anything else
- **Key teaching moment:** Data provenance and the importance of clean inputs for everything downstream

---

### Agent 2 — Team Profiler
- **Role:** Build a rich statistical portrait of each SEC team
- **Inputs:** Clean dataset from Agent 1
- **Outputs:** A structured profile for each team — strengths, weaknesses, style of play, key players, tournament trajectory
- **Runs:** In parallel with Agents 3 and 4 (once Agent 1 completes)
- **Key teaching moment:** Summarization and feature interpretation — translating raw numbers into meaning

---

### Agent 3 — Matchup Analyst
- **Role:** Head-to-head assessment of specific tournament matchups
- **Inputs:** Clean dataset from Agent 1, bracket structure
- **Outputs:** For each matchup — dimensional advantages, predicted game flow, winner with reasoning and confidence level
- **Runs:** In parallel with Agents 2 and 4
- **Key teaching moment:** Comparative analysis and structured reasoning under uncertainty

---

### Agent 4 — Upset Detector
- **Role:** Identify mismatches between seeding and underlying metrics
- **Inputs:** Clean dataset from Agent 1, bracket seedings
- **Outputs:** Ranked list of upset candidates with supporting statistical evidence
- **Runs:** In parallel with Agents 2 and 3
- **Key teaching moment:** The difference between perception (seeding) and reality (metrics)

---

### Agent 5 — Narrative & Reporting
- **Role:** Synthesize all outputs into a clean, publishable tournament preview
- **Inputs:** Profiles from Agent 2, matchup assessments from Agent 3, upset picks from Agent 4
- **Outputs:** A structured narrative report — bracket predictions, upset picks, Final Four projection, key storylines
- **Runs:** Last, sequentially, after Agents 2, 3, and 4 complete
- **Key teaching moment:** The full pipeline closing, and AI as a communication tool not just an analysis tool

---

## Execution Flow

```
[Agent 1: Data Gatherer & Cleaner]
              ↓
   ┌──────────┼──────────┐
   ↓          ↓          ↓
[Agent 2]  [Agent 3]  [Agent 4]
 Profiler   Matchup    Upset
            Analyst    Detector
   └──────────┬──────────┘
              ↓
   [Agent 5: Narrative & Reporting]
              ↓
      Final Tournament Preview
```

**Phase 1 — Sequential:** Agent 1 runs alone and produces the clean dataset that feeds everything downstream.

**Phase 2 — Parallel:** Agents 2, 3, and 4 run simultaneously, each consuming Agent 1's output from a different analytical angle.

**Phase 3 — Sequential:** Agent 5 collects all outputs and synthesizes a final report.

---

## Session Flow

| Segment | Duration | Description |
|---|---|---|
| Introduction | 10 min | Introduce the problem and multi-agent architecture. Walk through the execution diagram. Explain the decomposition rationale. |
| Live Demo | 20 min | Run the full pipeline live. Narrate what each agent is doing and why. Show handoffs explicitly. |
| Student Exercise | 20 min | Students modify or extend one agent — tweak upset detector criteria, add a matchup, or prompt the narrative agent for a different audience. |
| Discussion & Critique | 10 min | Where did agents agree or disagree? What would you change? Where could this go wrong? |

---

## Open Questions

1. **Data sources** — Live web scraping or pre-downloaded dataset as fallback?
2. **Execution environment** — Running locally on presenter machine during session?
3. **Agent 5 output format** — Markdown report, PDF, or printed summary?
4. **Student takeaway** — Should the orchestration script be packaged for students to run themselves?

---

## Key Learning Objectives for Students

- Understand how to decompose a complex analytical problem into specialized agent roles
- See the difference between parallel and sequential agent execution and when to use each
- Recognize that multi-agent systems mirror how real analytics teams are structured
- Develop critical instincts for evaluating and questioning AI-generated analysis
- Experience the full data science pipeline from raw data to published narrative
