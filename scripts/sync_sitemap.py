import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")
ROUTES_FILE = SITE_DIR / "i18n" / "routes-map.json"
SITEMAP_FILE = SITE_DIR / "sitemap.xml"

if not ROUTES_FILE.exists():
    print("ERRO: routes-map.json nao encontrado em site_hsn_labs")
    exit(1)

with open(ROUTES_FILE, "r", encoding="utf-8") as f:
    routes = json.load(f)

today = datetime.now().strftime("%Y-%m-%d")

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"',
    '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
    '                            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
]

def add_url_block(en_url, pt_url, priority="0.8", changefreq="monthly", image_info=None):
    # English block
    lines.append('  <url>')
    lines.append(f'    <loc>{en_url}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append(f'    <changefreq>{changefreq}</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}" />')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_url}" />')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="pt-BR" href="{pt_url}" />')
    if image_info:
        lines.append('    <image:image>')
        lines.append(f'      <image:loc>{image_info["loc"]}</image:loc>')
        lines.append(f'      <image:title>{image_info["title"]}</image:title>')
        lines.append(f'      <image:caption>{image_info["caption"]}</image:caption>')
        lines.append('    </image:image>')
    lines.append('  </url>')

    # Portuguese block
    lines.append('  <url>')
    lines.append(f'    <loc>{pt_url}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append(f'    <changefreq>{changefreq}</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}" />')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_url}" />')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="pt-BR" href="{pt_url}" />')
    lines.append('  </url>')

# Site pages
for page in routes.get("site_pages", []):
    en_url = f"https://hsnlabs.ai{page['en_path']}"
    pt_url = f"https://hsnlabs.ai{page['pt_path']}"
    prio = "1.0" if page["en_path"] == "/" else "0.9"
    freq = "weekly" if page["en_path"] == "/" else "monthly"
    img = None
    if page["en_path"] == "/":
        img = {
            "loc": "https://hsnlabs.ai/assets/brand/og-image.png",
            "title": "HSN Labs | Enterprise AI Architectures",
            "caption": "HSN Labs — Hybrid engineering, business ontologies, and deterministic agents."
        }
    add_url_block(en_url, pt_url, priority=prio, changefreq=freq, image_info=img)

# Blog posts (pilot translated + mapped)
for post in routes.get("blog_posts", []):
    en_url = f"https://hsnlabs.ai/blog/post/{post['slug_en']}/"
    pt_url = f"https://hsnlabs.ai/blog/pt/post/{post['slug_pt']}/"
    add_url_block(en_url, pt_url, priority="0.8", changefreq="monthly")

lines.append('</urlset>')

xml_content = "\n".join(lines)

# Verify valid XML
ET.fromstring(xml_content)

# Verify zero parentheses
assert "(" not in xml_content and ")" not in xml_content, "ERRO: Parenteses encontrados no sitemap.xml!"

SITEMAP_FILE.write_text(xml_content, encoding="utf-8")
print(f"Sitemap atualizado com sucesso em {SITEMAP_FILE}. Total URLs sincronizadas.")
