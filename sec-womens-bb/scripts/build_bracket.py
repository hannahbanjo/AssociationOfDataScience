"""
Generate data/bracket.json by deriving tournament seedings from the
SEC conference standings in data/sec_teams.csv.

Seeding is determined by conference win percentage (Conf_W / (Conf_W + Conf_L)).
Ties are broken by overall SRS (Simple Rating System) as a proxy for head-to-head
and other SEC tiebreaker criteria. This is an approximation — the official SEC
tiebreaker procedure involves H2H records, which are not captured in the CSV.

The tournament bracket structure (matchup format, dates, times, networks) is
fixed and embedded in this script. Only the seed-to-team mapping is derived.

Run:
    python scripts/build_bracket.py

Output:
    data/bracket.json  (overwrites existing file)

Note:
    Re-run after the final regular season games (March 1) to lock in official seedings.
"""

import json
import csv
from datetime import date

DATA_FILE   = "data/sec_teams.csv"
BRACKET_FILE = "data/bracket.json"

BRACKET_TEMPLATE = [
    {
        "round": 1,
        "name": "First Round",
        "date": "2026-03-04",
        "games": [
            {"game_id": "G1",  "time": "11:00 AM EST", "network": "SEC Network", "higher_seed": 9,  "lower_seed": 16},
            {"game_id": "G2",  "time": "1:30 PM EST",  "network": "SEC Network", "higher_seed": 12, "lower_seed": 13},
            {"game_id": "G3",  "time": "6:00 PM EST",  "network": "SEC Network", "higher_seed": 10, "lower_seed": 15},
            {"game_id": "G4",  "time": "8:30 PM EST",  "network": "SEC Network", "higher_seed": 11, "lower_seed": 14},
        ],
    },
    {
        "round": 2,
        "name": "Second Round",
        "date": "2026-03-05",
        "games": [
            {"game_id": "G5", "time": "11:00 AM EST", "network": "SEC Network", "higher_seed": 8, "lower_seed": None, "fed_by": ["G1"]},
            {"game_id": "G6", "time": "1:30 PM EST",  "network": "SEC Network", "higher_seed": 5, "lower_seed": None, "fed_by": ["G2"]},
            {"game_id": "G7", "time": "6:00 PM EST",  "network": "SEC Network", "higher_seed": 7, "lower_seed": None, "fed_by": ["G3"]},
            {"game_id": "G8", "time": "8:30 PM EST",  "network": "SEC Network", "higher_seed": 6, "lower_seed": None, "fed_by": ["G4"]},
        ],
    },
    {
        "round": 3,
        "name": "Quarterfinals",
        "date": "2026-03-06",
        "games": [
            {"game_id": "G9",  "time": "12:00 PM EST", "network": "ESPN",        "higher_seed": 1, "lower_seed": None, "fed_by": ["G5"]},
            {"game_id": "G10", "time": "2:30 PM EST",  "network": "ESPN",        "higher_seed": 4, "lower_seed": None, "fed_by": ["G6"]},
            {"game_id": "G11", "time": "6:00 PM EST",  "network": "SEC Network", "higher_seed": 2, "lower_seed": None, "fed_by": ["G7"]},
            {"game_id": "G12", "time": "8:30 PM EST",  "network": "SEC Network", "higher_seed": 3, "lower_seed": None, "fed_by": ["G8"]},
        ],
    },
    {
        "round": 4,
        "name": "Semifinals",
        "date": "2026-03-07",
        "games": [
            {"game_id": "G13", "time": "4:30 PM EST", "network": "ESPN2", "fed_by": ["G9",  "G10"]},
            {"game_id": "G14", "time": "7:00 PM EST", "network": "ESPN2", "fed_by": ["G11", "G12"]},
        ],
    },
    {
        "round": 5,
        "name": "Championship",
        "date": "2026-03-08",
        "games": [
            {"game_id": "G15", "time": "3:00 PM EDT", "network": "ESPN", "fed_by": ["G13", "G14"]},
        ],
    },
]


def derive_seeds(csv_path: str) -> dict:
    """
    Read sec_teams.csv and return a {seed_int: team_name} dict.
    Primary sort: conference win % (desc). Tiebreaker: SRS (desc).
    """
    teams = []
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            conf_w = float(row.get("Conf_W", 0) or 0)
            conf_l = float(row.get("Conf_L", 0) or 0)
            conf_pct = conf_w / (conf_w + conf_l) if (conf_w + conf_l) > 0 else 0
            srs = float(row.get("SRS", 0) or 0)
            teams.append({"name": row["School"], "conf_pct": conf_pct, "srs": srs})

    teams.sort(key=lambda t: (t["conf_pct"], t["srs"]), reverse=True)
    return {i + 1: t["name"] for i, t in enumerate(teams)}


def main():
    seeds = derive_seeds(DATA_FILE)

    bracket = {
        "season": "2025-26",
        "tournament": "SEC Women's Basketball Tournament",
        "seedings_as_of": str(date.today()),
        "note": (
            "Seeds derived from conference win % in data/sec_teams.csv. "
            "Tiebreaker: SRS (approximates SEC H2H criteria). "
            "Re-run after March 1 regular season games to finalize."
        ),
        "seeds": {str(k): v for k, v in seeds.items()},
        "rounds": BRACKET_TEMPLATE,
    }

    with open(BRACKET_FILE, "w") as f:
        json.dump(bracket, f, indent=2)

    print(f"Seedings derived from {DATA_FILE}:")
    for seed, team in seeds.items():
        print(f"  {seed:2d}. {team}")
    print(f"\nSaved to {BRACKET_FILE}")


if __name__ == "__main__":
    main()
