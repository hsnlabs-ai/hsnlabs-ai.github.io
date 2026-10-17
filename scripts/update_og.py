#!/usr/bin/env python3
"""
Dynamic Open Graph Image Generator for hsnlabs (hsnlabs.ai)
Generates editorial 1200x630 Open Graph cards in English (og-image.png) and Portuguese (og-image-pt.png),
matching the exact visual structure of the live website navbar and hero without text bloat.
"""

import re
import shutil
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT_DIR.parent / "blog_hsn_labs"
INDEX_PT = ROOT_DIR / "index.html"
INDEX_EN = ROOT_DIR / "en" / "index.html"
OG_EN_OUTPUT = ROOT_DIR / "assets" / "brand" / "og-image.png"
OG_PT_OUTPUT = ROOT_DIR / "assets" / "brand" / "og-image-pt.png"
TEMP_DIR = Path("/Users/hugosoares/.hermes/cache/scratch")
TEMP_DIR.mkdir(parents=True, exist_ok=True)


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
            lead, accent = "Adoção de", "Engenharia Agêntica."
        else:
            lead, accent = "Agentic Engineering", "Adoption."

    m_ctas = re.search(r'<div class="hero-ctas">(.*?)</div>', content, re.DOTALL)
    cta_block = m_ctas.group(1) if m_ctas else content
    m_cta1 = re.search(r'<a[^>]*class="btn btn-primary"[^>]*>(.*?)</a>', cta_block)
    m_cta2 = re.search(r'<a[^>]*class="btn btn-outline"[^>]*>(.*?)</a>', cta_block)

    if lang == "pt":
        cta1 = m_cta1.group(1).strip() if m_cta1 else "Conhecer o Agentic Bootcamp"
        cta2 = m_cta2.group(1).strip() if m_cta2 else "Fale Conosco"
        return {
            "lang": "pt-BR",
            "lead": lead,
            "accent": accent,
            "cta1": cta1,
            "cta2": cta2,
            "lang_switch_html": '<span>EN ·</span> PT',
        }

    cta1 = m_cta1.group(1).strip() if m_cta1 else "Explore Agentic Bootcamp"
    cta2 = m_cta2.group(1).strip() if m_cta2 else "Contact Us"
    return {
        "lang": "en",
        "lead": lead,
        "accent": accent,
        "cta1": cta1,
        "cta2": cta2,
        "lang_switch_html": 'EN <span>· PT</span>',
    }


def build_og_template(data: dict) -> str:
    paper_path = f"file://{ROOT_DIR}/assets/textures/paper_crumpled_clean.jpg"
    lockup_path = f"file://{ROOT_DIR}/assets/brand/lockups/hsnlabs-lockup-horizontal-light.png"
    carp_path = f"file://{ROOT_DIR}/assets/brand/elements/origami-carp-clean.png"

    html = f"""<!DOCTYPE html>
<html lang="{data['lang']}">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400&family=Inter:wght@300;400;500;600&display=swap');

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
    color: #475569;
    display: flex;
    flex-direction: column;
  }}

  /* Atmospheric blooms identical to index.html */
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

  /* Header identical to site navbar */
  .header-nav {{
    position: relative;
    z-index: 2;
    height: 76px;
    background: rgba(245, 245, 245, 0.85);
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 56px;
  }}

  .brand-logo-img {{
    height: 44px;
    width: auto;
    display: block;
  }}

  .header-right {{
    display: flex;
    align-items: center;
    gap: 24px;
  }}

  .nav-item {{
    font-size: 14px;
    color: #64748b;
    font-weight: 400;
  }}

  .lang-switch {{
    font-size: 13px;
    font-weight: 600;
    color: #07090e;
    letter-spacing: 0.04em;
  }}

  .lang-switch span {{
    color: #94a3b8;
    font-weight: 400;
  }}

  /* Hero Center identical to site hero */
  .hero-center {{
    position: relative;
    z-index: 2;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 64px 16px 64px;
  }}

  .brand-symbol-box {{
    width: 92px;
    height: 92px;
    border-radius: 0;
    margin: 0 auto 34px auto;
    background: #52B4FD;
    box-shadow: 0 12px 32px rgba(82, 180, 253, 0.28), 0 2px 8px rgba(0, 0, 0, 0.04);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }}

  .symbol-carp {{
    width: 60px;
    height: 60px;
    object-fit: contain;
    position: relative;
    z-index: 2;
  }}

  .display-hero {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 74px;
    font-weight: 300;
    letter-spacing: -0.025em;
    line-height: 1.1;
    color: #07090e;
    margin: 0 auto 38px auto;
  }}

  .display-hero .accent {{
    color: #0284c7;
    font-weight: 300;
  }}

  .hero-ctas {{
    display: flex;
    justify-content: center;
    gap: 14px;
  }}

  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14.5px;
    font-weight: 500;
    border-radius: 0;
    padding: 13px 28px;
    line-height: 1;
    position: relative;
    overflow: hidden;
    isolation: isolate;
  }}

  .btn::before {{
    content: "";
    position: absolute;
    inset: 0;
    background-image: url('{paper_path}');
    background-size: 360px auto;
    background-position: center;
    mix-blend-mode: multiply;
    opacity: 0.55;
    pointer-events: none;
    z-index: -1;
  }}

  .btn-primary {{
    background: #52B4FD;
    color: #ffffff;
    border: 1px solid #3fa5f3;
    box-shadow: 0 2px 8px rgba(82, 180, 253, 0.30);
  }}

  .btn-outline {{
    background: #ffffff;
    color: #07090e;
    border: 1px solid #cbd5e1;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
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

  <header class="header-nav">
    <img src="{lockup_path}" alt="hsnlabs" class="brand-logo-img">
    <div class="header-right">
      <span class="nav-item">Advisory</span>
      <span class="nav-item">Blog</span>
      <span class="lang-switch">{data['lang_switch_html']}</span>
      <span class="btn btn-primary" style="padding: 10px 20px; font-size: 13.5px;">{data['cta1']}</span>
    </div>
  </header>

  <div class="hero-center">
    <div class="brand-symbol-box">
      <img src="{carp_path}" alt="hsnlabs" class="symbol-carp">
    </div>

    <h1 class="display-hero">
      {data['lead']} <span class="accent">{data['accent']}</span>
    </h1>

    <div class="hero-ctas">
      <span class="btn btn-primary">{data['cta1']}</span>
      <span class="btn btn-outline">{data['cta2']}</span>
    </div>
  </div>
</body>
</html>
"""
    return html


def render_card(html_source: Path, lang: str, output_path: Path):
    data = extract_hero_data(html_source, lang)
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
