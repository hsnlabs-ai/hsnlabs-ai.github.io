#!/usr/bin/env python3
"""
Render hsnlabs Architecture Diagram PNG (2880x1620)
Exports the vector blueprint from architecture.html directly to
assets/diagrams/hsn_labs_agentic_architecture.png in pixel-perfect retina fidelity.
"""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "architecture.html"
OUT_PNG = ROOT / "assets" / "diagrams" / "hsn_labs_agentic_architecture.png"

def render():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 2880, "height": 1620}, device_scale_factor=1)
        page.goto(f"file://{HTML_PATH}")
        page.wait_for_selector(".blueprint-svg")
        page.evaluate("document.fonts.ready")
        
        # Hide topbar to isolate the blueprint diagram
        page.evaluate("const topbar = document.querySelector('.arch-topbar'); if (topbar) topbar.style.display = 'none';")
        
        svg = page.locator(".blueprint-svg")
        svg.screenshot(path=str(OUT_PNG), omit_background=True)
        browser.close()
        print(f"✓ PNG sincronizado com sucesso: {OUT_PNG} (2880x1620)")

if __name__ == "__main__":
    render()
