#!/usr/bin/env python3
"""
Dynamic Open Graph Image Generator for HSN Labs (hsnlabs.ai)
Automatically syncs assets/brand/og-image.png with the Hero section of index.html.
"""

import os
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
INDEX_HTML = ROOT_DIR / "index.html"
OG_OUTPUT = ROOT_DIR / "assets" / "brand" / "og-image.png"
TEMP_HTML = Path("/tmp/hsn_og_dynamic.html")

def extract_hero_data():
    content = INDEX_HTML.read_text(encoding="utf-8")
    
    # Extract title lead
    m_lead = re.search(r'<span class="hero-title-lead">(.*?)</span>', content, re.DOTALL)
    title_lead = m_lead.group(1).strip() if m_lead else "Enterprise AI Agents"
    
    # Extract title sub
    m_sub = re.search(r'<span class="hero-title-sub">(.*?)</span>', content, re.DOTALL)
    title_sub = m_sub.group(1).strip() if m_sub else "that don't fail in production"
    
    # Extract hero sub paragraph
    m_p = re.search(r'<p class="hero-sub">(.*?)</p>', content, re.DOTALL)
    hero_p = m_p.group(1).strip() if m_p else "We use a business ontology tailored to your operations to build agentic systems, combining deterministic engineering with resilient deep agents."
    # Clean whitespace
    hero_p = " ".join(hero_p.split())
    
    # Extract CTAs
    m_cta1 = re.search(r'<a href="[^"]*" class="btn btn-primary">(.*?)</a>', content)
    cta1 = m_cta1.group(1).strip() if m_cta1 else "Apply for Bootcamp"
    
    m_cta2 = re.search(r'<a href="[^"]*" class="btn btn-outline">(.*?)</a>', content)
    cta2 = m_cta2.group(1).strip() if m_cta2 else "Contact Us"

    return {
        "title_lead": title_lead,
        "title_sub": title_sub,
        "hero_p": hero_p,
        "cta1": cta1,
        "cta2": cta2
    }

def build_og_template(data):
    paper_path = f"file://{ROOT_DIR}/assets/textures/paper_crumpled_clean.jpg"
    lockup_path = f"file://{ROOT_DIR}/assets/brand/lockups/hsn-labs-lockup-horizontal-light.png"
    carp_path = f"file://{ROOT_DIR}/assets/brand/elements/origami-carp-clean.png"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&display=swap');

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
    justify-content: space-between;
    padding: 36px 64px 44px 64px;
    border: 1px solid #e2e8f0;
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
    filter: blur(85px);
  }}

  .orb-cyan {{
    width: 580px;
    height: 580px;
    background: rgba(82, 180, 253, 0.38);
    top: -160px;
    left: 8%;
  }}

  .orb-peach {{
    width: 480px;
    height: 480px;
    background: rgba(244, 197, 168, 0.32);
    top: -40px;
    right: -60px;
  }}

  .orb-emerald {{
    width: 460px;
    height: 460px;
    background: rgba(167, 229, 211, 0.30);
    bottom: -120px;
    left: -40px;
  }}

  .orb-lavender {{
    width: 440px;
    height: 440px;
    background: rgba(200, 184, 224, 0.28);
    bottom: -80px;
    right: 12%;
  }}

  .paper-overlay {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    background-image: url('{paper_path}');
    background-size: cover;
    background-position: center;
    mix-blend-mode: multiply;
    opacity: 0.40;
    pointer-events: none;
    z-index: 1;
  }}

  .relative-content {{
    position: relative;
    z-index: 2;
    width: 100%;
  }}

  .header-nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    border-bottom: 1px solid rgba(226, 232, 240, 0.85);
    padding-bottom: 20px;
  }}

  .brand-logo-img {{
    height: 38px;
    width: auto;
    display: block;
  }}

  .header-badge {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #0284c7;
    background: rgba(255, 255, 255, 0.85);
    border: 1px solid #e2e8f0;
    padding: 6px 14px;
    border-radius: 0;
  }}

  .hero-center {{
    text-align: center;
    margin: auto 0;
    padding: 24px 0 10px 0;
  }}

  .brand-symbol-box {{
    width: 76px;
    height: 76px;
    border-radius: 0;
    margin: 0 auto 20px auto;
    background: #52B4FD;
    box-shadow: 0 10px 26px rgba(82, 180, 253, 0.32), 0 2px 8px rgba(0, 0, 0, 0.04);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }}

  .symbol-carp {{
    width: 48px;
    height: 48px;
    object-fit: contain;
    position: relative;
    z-index: 2;
  }}

  .display-hero {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    letter-spacing: -0.025em;
    margin-bottom: 14px;
  }}

  .hero-title-lead {{
    display: block;
    font-size: 64px;
    font-weight: 400;
    line-height: 1.05;
    color: #07090e;
  }}

  .hero-title-sub {{
    display: block;
    font-size: 52px;
    font-weight: 300;
    font-style: italic;
    line-height: 1.08;
    color: #475569;
    margin-top: 4px;
  }}

  .hero-sub {{
    font-size: 17px;
    line-height: 1.55;
    color: #64748b;
    max-width: 820px;
    margin: 0 auto 24px auto;
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
    font-size: 13px;
    font-weight: 500;
    border-radius: 0;
    padding: 10px 24px;
    text-decoration: none;
    line-height: 1;
    position: relative;
  }}

  .btn-primary {{
    background: #52B4FD;
    color: #ffffff;
    border: 1px solid #3fa5f3;
    box-shadow: 0 2px 8px rgba(82, 180, 253, 0.35);
  }}

  .btn-outline {{
    background: #ffffff;
    color: #07090e;
    border: 1px solid #cbd5e1;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  }}

  .footer-strip {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(226, 232, 240, 0.85);
    padding-top: 14px;
    font-size: 12px;
    color: #94a3b8;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }}

  .footer-strip .url {{
    font-weight: 600;
    color: #07090e;
    letter-spacing: 0.02em;
    text-transform: none;
    font-size: 13px;
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

  <div class="paper-overlay"></div>

  <div class="relative-content header-nav">
    <img src="{lockup_path}" alt="HSN Labs" class="brand-logo-img">
    <span class="header-badge">Forward Deployed Engineering</span>
  </div>

  <div class="relative-content hero-center">
    <div class="brand-symbol-box">
      <img src="{carp_path}" alt="HSN Labs" class="symbol-carp">
    </div>

    <h1 class="display-hero">
      <span class="hero-title-lead">{data['title_lead']}</span>
      <span class="hero-title-sub">{data['title_sub']}</span>
    </h1>

    <p class="hero-sub">
      {data['hero_p']}
    </p>

    <div class="hero-ctas">
      <span class="btn btn-primary">{data['cta1']}</span>
      <span class="btn btn-outline">{data['cta2']}</span>
    </div>
  </div>

  <div class="relative-content footer-strip">
    <span class="url">hsnlabs.ai</span>
    <span>High-Assurance AI • Business Ontologies • Private VPC</span>
  </div>
</body>
</html>
"""
    return html

def render_screenshot():
    data = extract_hero_data()
    html = build_og_template(data)
    TEMP_HTML.write_text(html, encoding="utf-8")
    
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={OG_OUTPUT}",
        "--window-size=1200,630",
        "--hide-scrollbars",
        f"file://{TEMP_HTML}"
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Successfully synchronized {OG_OUTPUT}")

if __name__ == "__main__":
    render_screenshot()
