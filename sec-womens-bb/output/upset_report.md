# SEC Women's Basketball Tournament — Upset Report
## Sub-Agent 4: Upset Detector

**Analysis Date:** 2026-02-27
**Season:** 2025-26
**Data Source:** Local CSV fallback — `/data/sec_teams.csv`, `/data/bracket.json`
**Note:** Seedings are preliminary; bracket.json flags re-run after March 1 as authoritative.

---

## Methodology

Each upset candidate was identified by comparing a team's tournament seed against its underlying efficiency metrics. The primary signal is **Net Efficiency** (ORtg − DRtg), supplemented by **SRS**, **SOS** (to flag inflated or deflated metrics), **DRtg**, **TS%**, and **TOV%**. Teams are flagged in two directions:

- **Upset candidate (overperformer):** A lower-seeded team whose metrics are meaningfully better than the team it faces.
- **Upset vulnerable (underperformer):** A higher-seeded team whose metrics are meaningfully worse than its seed implies.

The two flags naturally pair: every credible upset requires one of each.

---

## Master Metric Reference

| Seed | School | Net Eff | SRS | SOS | ORtg | DRtg | TS% | TOV% |
|------|--------|---------|-----|-----|------|------|-----|------|
| 1 | South Carolina | +42.5 | 48.26 | 16.66 | 118.6 | 76.1 | .587 | 14.7 |
| 2 | Texas | +40.6 | 46.35 | 16.39 | 116.3 | 75.7 | .559 | 13.5 |
| 3 | Vanderbilt | +28.0 | 34.60 | 14.09 | 115.6 | 87.6 | .575 | 15.0 |
| 4 | LSU | +45.8 | 46.93 | 11.11 | 121.8 | 76.0 | .579 | 15.1 |
| 5 | Oklahoma | +25.7 | 35.91 | 14.94 | 107.1 | 81.4 | .534 | 16.5 |
| 6 | Kentucky | +24.2 | 30.89 | 14.00 | 109.0 | 84.8 | .540 | 15.1 |
| 7 | Tennessee | +11.7 | 28.70 | 19.77 | 101.5 | 89.8 | .507 | 16.9 |
| 8 | Ole Miss | +21.1 | 28.61 | 13.44 | 105.4 | 84.3 | .516 | 16.0 |
| 9 | Alabama | +14.1 | 24.63 | 14.83 | 102.0 | 87.9 | .542 | 18.4 |
| 10 | Georgia | +18.0 | 23.89 | 10.89 | 102.5 | 84.5 | .538 | 17.3 |
| 11 | Texas A&M | -3.6 | 15.48 | 18.14 | 89.5 | 93.1 | .474 | 19.9 |
| 12 | Mississippi State | +12.5 | 20.37 | 11.19 | 102.8 | 90.3 | .528 | 17.9 |
| 13 | Florida | +10.3 | 19.56 | 12.02 | 100.0 | 89.7 | .531 | 19.6 |
| 14 | Missouri | -5.0 | 10.77 | 14.44 | 98.7 | 103.7 | .557 | 20.0 |
| 15 | Auburn | -3.5 | 12.19 | 14.60 | 86.5 | 90.0 | .470 | 20.1 |
| 16 | Arkansas | -7.6 | 6.91 | 12.81 | 91.6 | 99.2 | .482 | 18.6 |

---

## Upset Candidates — Ranked Most to Least Likely

---

### 1. Georgia (10) over Tennessee (7) — SECOND ROUND
**Probability: HIGH**

This is the clearest seed/metric misalignment in the bracket. Tennessee holds a two-seed advantage but its metrics rank it well below Georgia on almost every dimension.

| Metric | Tennessee (7) | Georgia (10) | Edge |
|--------|--------------|--------------|------|
| Net Efficiency | +11.7 | +18.0 | Georgia +6.3 |
| SRS | 28.70 | 23.89 | Tennessee +4.8 |
| ORtg | 101.5 | 102.5 | Georgia +1.0 |
| DRtg | 89.8 | 84.5 | Georgia −5.3 (better) |
| TS% | .507 | .538 | Georgia +.031 |
| TOV% | 16.9 | 17.3 | Tennessee −0.4 |
| SOS | 19.77 | 10.89 | Tennessee harder |

**Why the seed is misleading:** Tennessee's 8-7 conference record (tied with Kentucky and Ole Miss) was achieved against the toughest schedule in the field (SOS 19.77 — highest of all 16 teams). The seeding algorithm uses SRS as the tiebreaker among tied-record teams, which partially credits schedule difficulty — but Tennessee's underlying efficiency metrics do not hold up. Its Net Efficiency (+11.7) is the lowest among all teams seeded 1-8, and Georgia's +18.0 would rank 7th in the field if seed-re-sorted. Georgia's DRtg (84.5) is 5.3 points better per 100 possessions than Tennessee's (89.8) — a substantial margin. Georgia's TS% (.538) eclipses Tennessee's (.507) by 31 points.

**Path note:** Georgia must first beat Auburn (seed 15) in the First Round. Auburn has a negative Net Efficiency (−3.5), and Georgia is heavily favored in that opener. A Georgia upset of Tennessee in the Second Round would then set up a Quarterfinal collision with 2-seed Texas.

---

### 2. Alabama (9) over Ole Miss (8) — SECOND ROUND
**Probability: MEDIUM-HIGH**

Alabama and Ole Miss are separated by a single seed, but the metrics gap is meaningful and runs in Alabama's direction on defensive efficiency.

| Metric | Ole Miss (8) | Alabama (9) | Edge |
|--------|-------------|-------------|------|
| Net Efficiency | +21.1 | +14.1 | Ole Miss +7.0 |
| SRS | 28.61 | 24.63 | Ole Miss +3.98 |
| ORtg | 105.4 | 102.0 | Ole Miss +3.4 |
| DRtg | 84.3 | 87.9 | Ole Miss −3.6 (better) |
| TS% | .516 | .542 | Alabama +.026 |
| TOV% | 16.0 | 18.4 | Ole Miss +2.4 |
| SOS | 13.44 | 14.83 | Alabama slightly harder |
| ORB% | 40.4 | 31.3 | Ole Miss +9.1 |

**Why this is close:** Ole Miss holds a clear Net Efficiency advantage (+7.0) and a dominant offensive rebounding rate (40.4% vs. Alabama's 31.3%). However, Alabama plays with more efficient shooting (TS% .542 vs. .516) and faced a harder schedule. The seed gap is minimal (one position), and tournament single-elimination variance closes that further. Ole Miss is the favorite by metrics, but Alabama's shooting efficiency makes this a live upset game.

**Why the seed is somewhat misleading for Alabama:** Alabama's 7-8 conference record places it behind three 8-7 teams (Kentucky, Tennessee, Ole Miss) in seeding — but Alabama's SOS (14.83) is higher than Ole Miss's (13.44), suggesting Alabama's losses came in a slightly harder environment. The gap is not extreme, but in a one-game format it matters.

---

### 3. Mississippi State (12) over Florida (13) — FIRST ROUND, then Mississippi State (12) over Oklahoma (5) — SECOND ROUND
**Probability: MEDIUM (First Round near-certain; Second Round is the genuine upset)**

**First Round:** Mississippi State vs. Florida is a near-coin-flip seeded matchup. Mississippi State holds the edge on Net Efficiency (+12.5 vs. +10.3) and DRtg (90.3 vs. 89.7 — essentially equal). Florida's TOV% (19.6) is among the worst in the field. Mississippi State is a modest favorite in R1.

**The real upset — Second Round vs. Oklahoma (5):**

| Metric | Oklahoma (5) | Mississippi State (12) | Edge |
|--------|-------------|----------------------|------|
| Net Efficiency | +25.7 | +12.5 | Oklahoma +13.2 |
| SRS | 35.91 | 20.37 | Oklahoma +15.54 |
| ORtg | 107.1 | 102.8 | Oklahoma +4.3 |
| DRtg | 81.4 | 90.3 | Oklahoma −8.9 (better) |
| TS% | .534 | .528 | Oklahoma +.006 |
| TOV% | 16.5 | 17.9 | Oklahoma +1.4 |
| Pace | 80.7 | 73.4 | Oklahoma +7.3 |
| SOS | 14.94 | 11.19 | Oklahoma harder |

**Why Mississippi State is a live underdog:** Oklahoma plays at the fastest pace in the field (80.7 possessions/40 min vs. Mississippi State's 73.4). In tournament single-elimination, pace mismatches create variance — a slower team can drag a faster team into a half-court grind and reduce possessions. Mississippi State's ORtg (102.8) is respectable; if the game slows down, they have the offense to compete for 30-35 possessions rather than 40+. Oklahoma is the clear metric favorite, but the style mismatch is real.

---

### 4. LSU (4) Deep Run / Quarterfinal Win — STRUCTURAL UPSET RISK
**Probability: HIGH (that LSU outperforms seed expectations)**

This is not a single-game upset pick but a structural seeding anomaly: **LSU has the highest Net Efficiency in the field (+45.8) but is the 4-seed**, positioned to face higher seeds in the Semifinals and Championship if those favorites hold.

| Metric | LSU (4) | South Carolina (1) | Texas (2) | Vanderbilt (3) |
|--------|---------|-------------------|-----------|----------------|
| Net Efficiency | **+45.8** | +42.5 | +40.6 | +28.0 |
| SRS | **46.93** | 48.26 | 46.35 | 34.60 |
| ORtg | **121.8** | 118.6 | 116.3 | 115.6 |
| DRtg | 76.0 | 76.1 | **75.7** | 87.6 |
| TS% | .579 | **.587** | .559 | .575 |
| SOS | 11.11 | **16.66** | 16.39 | 14.09 |

**Why the seed is misleading:** LSU's seeding is an artifact of the conference win % algorithm (11-4 conference record vs. 12-3 for both Texas and Vanderbilt). But by every efficiency metric — ORtg, Net Efficiency, and SRS — LSU is the second-best team in the field, essentially tied with South Carolina. The primary caveat is SOS: LSU's schedule difficulty (11.11) is the second-lowest in the bracket, behind only Georgia (10.89). If that SOS caveat overstates LSU's weakness, a Semifinal win over Texas (2-seed) or Vanderbilt (3-seed) would be a bracket-busting moment. If the SOS caveat is real (LSU ran up numbers against weaker opponents), then the seed is approximately correct.

**LSU's bracket path:** First Round bye → Quarterfinal vs. Oklahoma/Mississippi State/Florida winner (a manageable draw) → Semifinal likely vs. Texas (2) — that game is the crux. By raw metrics, it is essentially a coin flip.

---

### 5. Florida (13) over Mississippi State (12) — FIRST ROUND
**Probability: MEDIUM**

The 12-13 matchup is the flattest seed differential in the bracket. Florida's metrics trail Mississippi State's on efficiency but the gap is narrow enough that this is a genuine toss-up.

| Metric | Mississippi State (12) | Florida (13) | Edge |
|--------|----------------------|-------------|------|
| Net Efficiency | +12.5 | +10.3 | MSU +2.2 |
| SRS | 20.37 | 19.56 | MSU +0.81 |
| ORtg | 102.8 | 100.0 | MSU +2.8 |
| DRtg | 90.3 | 89.7 | Florida −0.6 (better) |
| TS% | .528 | .531 | Florida +.003 |
| TOV% | 17.9 | 19.6 | MSU +1.7 |
| ORB% | 37.7 | 34.9 | MSU +2.8 |

**Conclusion:** Mississippi State holds a small but consistent statistical edge. However, Florida's DRtg (89.7) is fractionally better, and this is the type of game where a hot shooting night or a single late-game possession decides the outcome. Florida wins this often enough to model as a legitimate upset.

---

### 6. Texas A&M (11) over Missouri (14) — FIRST ROUND (Expected outcome, not an upset)
**Probability: HIGH — but flagged as a data concern**

This matchup is technically "Texas A&M over Missouri," but the framing requires clarification. Missouri (seed 14) has the worst metrics in the bracket — the only team with a DRtg above 100 (103.7) and a negative Net Efficiency (−5.0). Texas A&M (seed 11) also posts a negative Net Efficiency (−3.6) — making this the worst quality game in the tournament by metrics.

| Metric | Texas A&M (11) | Missouri (14) | Edge |
|--------|---------------|--------------|------|
| Net Efficiency | -3.6 | **-5.0** | Texas A&M +1.4 |
| SRS | 15.48 | 10.77 | Texas A&M +4.71 |
| ORtg | 89.5 | 98.7 | Missouri +9.2 |
| DRtg | 93.1 | **103.7** | Texas A&M −10.6 (better) |
| TS% | .474 | .557 | Missouri +.083 |
| TOV% | 19.9 | 20.0 | Essentially tied |
| SOS | **18.14** | 14.44 | Texas A&M tougher schedule |

**Important flags:**
- Texas A&M played only 24 games (the fewest in the field; all others played 27-30). Small sample size adds uncertainty — their metrics, both positive (tougher SOS) and negative (worst TS% in the field at .474), carry wider confidence intervals.
- Missouri's ORtg (98.7) is legitimately respectable, but their DRtg (103.7) — opponents scoring over a point per possession — is catastrophically bad. They cannot stop anyone.
- Texas A&M's TS% (.474) is the lowest in the field and their ORtg (89.5) is second-lowest (above only Auburn's 86.5). They can't score either.
- This is a true bottom-of-bracket game between two statistically negative teams. Texas A&M is a modest favorite via defensive advantage; Missouri's offense adds uncertainty.

**Upset flag — Missouri over Texas A&M:** Given Missouri's ORtg advantage (+9.2) and strong TS% (.557), an offensive explosion could carry Missouri to a First Round win. Rate this at **Low-Medium** probability given the defensive disparity.

---

## Summary Upset Probability Table

| Rank | Matchup | Round | Probability |
|------|---------|-------|-------------|
| 1 | **Georgia (10) over Tennessee (7)** | Second Round | HIGH |
| 2 | Alabama (9) over Ole Miss (8) | Second Round | MEDIUM-HIGH |
| 3 | Mississippi State (12) over Oklahoma (5) | Second Round | MEDIUM |
| 4 | LSU (4) over Texas (2) | Semifinals | MEDIUM (structural) |
| 5 | Florida (13) over Mississippi State (12) | First Round | MEDIUM |
| 6 | Missouri (14) over Texas A&M (11) | First Round | LOW-MEDIUM |

---

## BOLD PICK: Georgia (10) Makes the Semifinals

**The pick:** 10-seed Georgia defeats 15-seed Auburn in the First Round, then defeats 7-seed Tennessee in the Second Round, then pushes 2-seed Texas in the Quarterfinals.

**The case:** Georgia's seed (10) is one of the larger metric distortions in the bracket. Their Net Efficiency (+18.0) and DRtg (84.5) rank ahead of both teams they would face in Rounds 1 and 2 by a meaningful margin. Tennessee's Net Efficiency (+11.7) is the lowest among all seeds 1-8 — a team that survives on schedule reputation, not underlying quality. Georgia winning two games to reach the Quarterfinals would be labeled a double-digit seed upset by the bracket, but the numbers suggest it is closer to a chalk result.

---

## Upset Vulnerability Rankings — Seeds Most at Risk

Teams whose metrics most underperform their seed:

| Seed | School | Net Eff Rank | Net Eff | Seed/Rank Gap | Risk Level |
|------|--------|--------------|---------|---------------|------------|
| 7 | Tennessee | 11th | +11.7 | −4 (seeded 4 spots above metric rank) | HIGH |
| 11 | Texas A&M | 13th | −3.6 | −2 | MEDIUM-HIGH |
| 14 | Missouri | 15th | −5.0 | −1 | MEDIUM |
| 8 | Ole Miss | 7th | +21.1 | +1 (seeded one spot below metric rank) | LOW |

Tennessee's seed/metric gap is the largest in the field. Seeded 7th, they rank 11th by Net Efficiency — a four-position gap driven by their tough schedule earning SRS credit. In a single-elimination setting, schedule credit evaporates; only performance on the day matters.

---

## Key Statistical Flags Carried Forward to Sub-Agent 5

1. **LSU's SOS caveat is the most important unresolved question in the bracket.** If their +45.8 Net Efficiency is real (i.e., would hold against better competition), they are the best team in the field. If SOS (11.11) substantially inflated their numbers, they are appropriately a 4-seed. Sub-Agent 5 should surface this uncertainty explicitly rather than resolving it.

2. **Tennessee is the most statistically overseeded team in the bracket.** Any preview that treats them as a reliable 7-seed is not accounting for their metrics.

3. **Three teams post negative Net Efficiency** (Texas A&M, Auburn, Missouri). All three are expected to lose in the First Round, but the Texas A&M/Missouri matchup between two negative-efficiency teams introduces genuine uncertainty.

4. **Texas A&M's 24-game sample** is the smallest in the field. Their metrics — both positive (SOS 18.14) and negative (TS% .474) — carry wider uncertainty bounds than any other team.
