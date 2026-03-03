"""
Build the SEC women's basketball fallback dataset.

Sources:
  School stats:   https://www.sports-reference.com/cbb/seasons/women/{SEASON}-advanced-school-stats.html
  Opponent stats: https://www.sports-reference.com/cbb/seasons/women/{SEASON}-advanced-opponent-stats.html

Columns pulled:
  School, G, W, L, W-L%, SRS, SOS, Pace, ORtg, DRtg, FTr, 3PAr, TS%, eFG%, TOV%, ORB%, FT/FGA

DRtg (Defensive Rating) comes from the opponent stats page as
('Opponent Advanced', 'ORtg') — the efficiency the team allows per 100
opponent possessions. The two tables are joined on School name.

Run:
    python scripts/build_data.py

Output:
    data/sec_teams.csv
"""

import io
import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment

SEASON = "2026"
SCHOOL_URL = f"https://www.sports-reference.com/cbb/seasons/women/{SEASON}-advanced-school-stats.html"
OPP_URL    = f"https://www.sports-reference.com/cbb/seasons/women/{SEASON}-advanced-opponent-stats.html"
OUTPUT = "data/sec_teams.csv"

# Team names as they appear on Sports Reference (not common nicknames)
SEC_TEAMS = {
    "Alabama", "Arkansas", "Auburn", "Florida", "Georgia",
    "Kentucky", "Louisiana State", "Mississippi State", "Missouri", "Oklahoma",
    "Mississippi", "South Carolina", "Tennessee", "Texas", "Texas A&M",
    "Vanderbilt",
}

# Friendly names for the output CSV (maps SR name → display name)
TEAM_RENAME = {
    "Louisiana State": "LSU",
    "Mississippi": "Ole Miss",
}

# Maps multi-level column tuples → output column name.
# The table uses a two-row header; we select by exact tuple to avoid
# duplicate column names (W and L appear under Overall, Conf, Home, Away).
COL_MAP = {
    ("Unnamed: 1_level_0", "School"): "School",
    ("Overall", "G"):    "G",
    ("Overall", "W"):    "W",
    ("Overall", "L"):    "L",
    ("Overall", "W-L%"): "W-L%",
    ("Overall", "SRS"):  "SRS",
    ("Overall", "SOS"):  "SOS",
    ("Conf.", "W"):      "Conf_W",
    ("Conf.", "L"):      "Conf_L",
    ("School Advanced", "Pace"):   "Pace",
    ("School Advanced", "ORtg"):   "ORtg",
    # DRtg is pulled separately from the opponent stats page
    ("School Advanced", "FTr"):    "FTr",
    ("School Advanced", "3PAr"):   "3PAr",
    ("School Advanced", "TS%"):    "TS%",
    ("School Advanced", "eFG%"):   "eFG%",
    ("School Advanced", "TOV%"):   "TOV%",
    ("School Advanced", "ORB%"):   "ORB%",
    ("School Advanced", "FT/FGA"): "FT/FGA",
}

# Columns to pull from the opponent stats page
OPP_COL_MAP = {
    ("Unnamed: 1_level_0", "School"):    "School",
    ("Opponent Advanced", "ORtg"):       "DRtg",  # opponent ORtg = team DRtg
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_table(url: str, table_id: str) -> pd.DataFrame:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    # Try direct table first
    table = soup.find("table", {"id": table_id})
    if table:
        return pd.read_html(io.StringIO(str(table)), header=[0, 1])[0]

    # Sports Reference sometimes hides tables inside HTML comments
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        if table_id in comment:
            inner = BeautifulSoup(comment, "lxml")
            table = inner.find("table", {"id": table_id})
            if table:
                return pd.read_html(io.StringIO(str(table)), header=[0, 1])[0]

    raise ValueError(f"Table '{table_id}' not found on {url}")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Select and rename columns by exact tuple key
    available = {k: v for k, v in COL_MAP.items() if k in df.columns}
    df = df[list(available.keys())].copy()
    df.columns = list(available.values())

    # Drop separator rows (Sports Reference inserts repeated header rows mid-table)
    df = df[df["School"].notna()]
    df = df[df["School"] != "School"]

    # Strip trailing asterisk/rank suffix (e.g. "Alabama *" or "Alabama (1)")
    df["School"] = df["School"].str.replace(r"\s*[\*\(].*$", "", regex=True).str.strip()

    # Filter to SEC
    df = df[df["School"].isin(SEC_TEAMS)].copy()

    # Apply friendly display names
    df["School"] = df["School"].replace(TEAM_RENAME)

    # Convert numerics
    for col in df.columns:
        if col != "School":
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values("School").reset_index(drop=True)
    return df


def fetch_drtg(url: str) -> pd.DataFrame:
    """Fetch DRtg from the opponent advanced stats page."""
    raw = fetch_table(url, "adv_opp_stats")
    available = {k: v for k, v in OPP_COL_MAP.items() if k in raw.columns}
    df = raw[list(available.keys())].copy()
    df.columns = list(available.values())
    df = df[df["School"].notna()]
    df = df[df["School"] != "School"]
    df["School"] = df["School"].str.replace(r"\s*[\*\(].*$", "", regex=True).str.strip()
    df = df[df["School"].isin(SEC_TEAMS)].copy()
    df["School"] = df["School"].replace(TEAM_RENAME)
    df["DRtg"] = pd.to_numeric(df["DRtg"], errors="coerce")
    return df.reset_index(drop=True)


def main():
    print(f"Fetching school stats: {SCHOOL_URL}")
    df = clean(fetch_table(SCHOOL_URL, "adv_school_stats"))

    print(f"Fetching opponent stats (DRtg): {OPP_URL}")
    drtg = fetch_drtg(OPP_URL)

    # Join DRtg and insert it after ORtg
    df = df.merge(drtg[["School", "DRtg"]], on="School", how="left")
    ortg_idx = df.columns.get_loc("ORtg")
    cols = list(df.columns)
    cols.insert(ortg_idx + 1, cols.pop(cols.index("DRtg")))
    df = df[cols]

    if df.empty:
        raise RuntimeError("No SEC teams found — check team names or URL.")

    print(f"Found {len(df)} SEC teams:\n{df['School'].tolist()}")
    df.to_csv(OUTPUT, index=False)
    print(f"\nSaved to {OUTPUT}")


if __name__ == "__main__":
    main()
