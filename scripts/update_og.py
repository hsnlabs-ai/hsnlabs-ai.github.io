#!/usr/bin/env python3
"""
Dynamic Open Graph Image Generator for hsnlabs (hsnlabs.ai)
Generates clean, minimal editorial 1200x630 Open Graph cards in English (og-image.png) and Portuguese (og-image-pt.png),
using only the official emblem and single-line Cormorant Garamond 300 headline without header or CTA bloat.
"""

import base64
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT_DIR.parent / "blog_hsn_labs"
INDEX_PT = ROOT_DIR / "index.html"
INDEX_EN = ROOT_DIR / "en" / "index.html"
OG_EN_OUTPUT = ROOT_DIR / "assets" / "brand" / "og-image.png"
OG_PT_OUTPUT = ROOT_DIR / "assets" / "brand" / "og-image-pt.png"
TEMP_DIR = Path("/Users/hugosoares/.hermes/cache/scratch")
TEMP_DIR.mkdir(parents=True, exist_ok=True)


def get_embedded_font_css() -> Path:
    css_path = TEMP_DIR / "embedded_fonts.css"
    if css_path.exists() and css_path.stat().st_size > 10000:
        return css_path

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
    }
    css_url = (
        "https://fonts.googleapis.com/css2?"
        "family=Cormorant+Garamond:wght@300;400;500&family=Inter:wght@300;400;500;600&display=swap"
    )
    req = urllib.request.Request(css_url, headers=headers)
    css_text = urllib.request.urlopen(req).read().decode("utf-8")

    def inline_url(match):
        url = match.group(1).strip("'\"")
        font_bytes = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
        b64 = base64.b64encode(font_bytes).decode("utf-8")
        return f"url('data:font/woff2;base64,{b64}')"

    embedded = re.sub(r"url\((https://[^)]+)\)", inline_url, css_text)
    css_path.write_text(embedded, encoding="utf-8")
    return css_path


def extract_hero_data(html_path: Path, lang: str):
    content = html_path.read_text(encoding="utf-8")
    m_h1 = re.search(r'<h1 class="display-hero">\s*(.*?)\s*</h1>', content, re.DOTALL)
    if m_h1:
        raw_h1 = m_h1.group(1).strip()
        m_span = re.search(r'^(.*?)<span[^>]*>(.*?)</span>(.*)$', raw_h1, re.DOTALL)
        if m_span:
            lead = " ".join(m_span.group(1).split())
            accent = " ".join(m_span.group(2).split())
        else:
            lead = " ".join(re.sub(r'<[^>]+>', '', raw_h1).split())
            accent = ""
    else:
        if lang == "pt":
            lead, accent = "Adoção de", "Engenharia Agentica."
        else:
            lead, accent = "Agentic Engineering", "Adoption."

    return {
        "lang": "pt-BR" if lang == "pt" else "en",
        "lead": lead,
        "accent": accent,
    }


def build_og_template(data: dict) -> str:
    carp_path = f"file://{ROOT_DIR}/assets/brand/elements/origami-carp-clean.png"
    font_css_path = get_embedded_font_css()

    html = f"""<!DOCTYPE html>
<html lang="{data['lang']}">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="file://{font_css_path}">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }}

  body {{
    width: 1200px;
    height: 630px;
    background-color: #f5f5f5;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }}

  .atmosphere-bg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  }}

  .orb {{
    position: absolute;
    border-radius: 50%;
    filter: blur(90px);
  }}

  .orb-cyan {{
    width: 580px;
    height: 580px;
    background: rgba(82, 180, 253, 0.30);
    top: -120px;
    left: 8%;
  }}

  .orb-peach {{
    width: 480px;
    height: 480px;
    background: rgba(244, 197, 168, 0.22);
    top: -40px;
    right: -60px;
  }}

  .orb-emerald {{
    width: 460px;
    height: 460px;
    background: rgba(167, 229, 211, 0.25);
    bottom: -140px;
    left: -40px;
  }}

  .orb-lavender {{
    width: 440px;
    height: 440px;
    background: rgba(200, 184, 224, 0.18);
    bottom: -80px;
    right: 12%;
  }}

  .hero-center {{
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 72px;
  }}

  .brand-symbol-box {{
    width: 108px;
    height: 108px;
    border-radius: 0;
    margin: 0 auto 38px auto;
    background: #52B4FD;
    box-shadow: 0 14px 36px rgba(82, 180, 253, 0.32), 0 2px 8px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden;
  }}

  .symbol-carp {{
    position: absolute;
    width: 60px;
    height: 60px;
    top: 7px;
    right: 7px;
    object-fit: contain;
    z-index: 2;
  }}

  .display-hero {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 82px;
    font-weight: 300;
    letter-spacing: -0.025em;
    line-height: 1.06;
    color: #07090e;
    white-space: nowrap;
  }}

  .display-hero .accent {{
    color: #0284c7;
    font-weight: 300;
  }}
</style>
</head>
<body>
  <div class="atmosphere-bg">
    <div class="orb orb-cyan"></div>
    <div class="orb orb-peach"></div>
    <div class="orb orb-emerald"></div>
    <div class="orb orb-lavender"></div>
  </div>

  <div class="hero-center">
    <div class="brand-symbol-box">
      <img src="{carp_path}" alt="hsnlabs" class="symbol-carp">
    </div>

    <h1 class="display-hero">
      {data['lead']} <span class="accent">{data['accent']}</span>
    </h1>
  </div>
</body>
</html>
"""
    return html


def render_card(html_source: Path, lang: str, output_path: Path):
    data = extract_hero_data(html_source, lang)
    master_path = ROOT_DIR / "assets" / "brand" / f"og-master-{lang}.png"
    default_lead = "Adoção de" if lang == "pt" else "Agentic Engineering"
    default_accent = "Engenharia Agentica." if lang == "pt" else "Adoption."
    if master_path.exists() and data["lead"] == default_lead and data["accent"] == default_accent:
        from PIL import Image
        img = Image.open(master_path)
        if img.size != (1200, 630):
            img = img.resize((1200, 630), Image.Resampling.LANCZOS)
        img.save(output_path, format="PNG", optimize=True)
        print(f"Successfully synced master {output_path} ({output_path.stat().st_size} bytes)")
        return

    html = build_og_template(data)
    temp_html = TEMP_DIR / f"hsn_og_{lang}.html"
    temp_html.write_text(html, encoding="utf-8")

    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={output_path}",
        "--window-size=1200,630",
        "--default-background-color=f5f5f5",
        "--hide-scrollbars",
        f"file://{temp_html}",
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Successfully generated {output_path} ({output_path.stat().st_size} bytes)")


def main():
    render_card(INDEX_EN, "en", OG_EN_OUTPUT)
    if INDEX_PT.exists():
        render_card(INDEX_PT, "pt", OG_PT_OUTPUT)

    blog_brand_dir = BLOG_DIR / "docs" / "assets" / "brand"
    if blog_brand_dir.exists():
        shutil.copy2(OG_EN_OUTPUT, blog_brand_dir / "og-image.png")
        if OG_PT_OUTPUT.exists():
            shutil.copy2(OG_PT_OUTPUT, blog_brand_dir / "og-image-pt.png")
        print(f"Synchronized OG images to {blog_brand_dir}")


if __name__ == "__main__":
    main()
