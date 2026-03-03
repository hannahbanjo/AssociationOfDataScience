"""
Generate presentation/tournament-preview.pdf from presentation/tournament-preview.html.
Run from the project root: python scripts/generate_pdf.py
"""
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("playwright not found — run: pip install playwright && playwright install chromium")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
HTML = ROOT / "presentation" / "tournament-preview.html"
PDF  = ROOT / "presentation" / "tournament-preview.pdf"

if not HTML.exists():
    print(f"ERROR: {HTML} not found")
    sys.exit(1)

html_content = HTML.read_text(encoding="utf-8")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content, wait_until="networkidle")
    page.pdf(
        path=str(PDF),
        format="Letter",
        margin={"top": "0.5in", "bottom": "0.5in", "left": "0.5in", "right": "0.5in"},
        print_background=True,
    )
    browser.close()

print(f"PDF written: {PDF} ({PDF.stat().st_size // 1024}K)")
