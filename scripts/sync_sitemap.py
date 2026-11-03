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

# Ensure all 5 product pages and protocol subpages are present in site_pages
existing_ids = {p["id"] for p in routes.get("site_pages", [])}
extra_product_pages = [
    {
        "id": "site_products_agents_swarm_protocol",
        "en_path": "/en/products/agents-swarm/protocol/",
        "pt_path": "/produtos/agents-swarm/protocolo/",
        "title_en": "Agents Swarm Protocol · hsnlabs",
        "title_pt": "Protocolo Agents Swarm · hsnlabs",
        "description_en": "Technical protocol specification for Agents Swarm external observability and state machine reconstruction.",
        "description_pt": "Especificação técnica do protocolo Agents Swarm para observabilidade externa e reconstrução de máquinas de estado."
    },
    {
        "id": "site_products_honeycomb_protocol",
        "en_path": "/en/products/honeycomb-protocol/",
        "pt_path": "/produtos/honeycomb-protocol/",
        "title_en": "Honeycomb Protocol · hsnlabs",
        "title_pt": "Honeycomb Protocol · hsnlabs",
        "description_en": "Deterministic coordination protocol for autonomous multi-agent swarms.",
        "description_pt": "Protocolo de coordenação determinística para enxames de múltiplos agentes autônomos."
    },
    {
        "id": "site_products_stigmergy_mesh",
        "en_path": "/en/products/stigmergy-mesh/",
        "pt_path": "/produtos/stigmergy-mesh/",
        "title_en": "Stigmergy Mesh · hsnlabs",
        "title_pt": "Stigmergy Mesh · hsnlabs",
        "description_en": "Decentralized stigmergic state coordination mesh for enterprise agent swarms.",
        "description_pt": "Malha de coordenação estigmérgica descentralizada para enxames de agentes corporativos."
    },
    {
        "id": "site_products_agent_analyzer",
        "en_path": "/en/products/agent-analyzer/",
        "pt_path": "/produtos/agent-analyzer/",
        "title_en": "Agent Analyzer · hsnlabs",
        "title_pt": "Agent Analyzer · hsnlabs",
        "description_en": "Static and dynamic diagnostic analyzer for enterprise AI agent architectures.",
        "description_pt": "Analisador de diagnóstico estático e dinâmico para arquiteturas de agentes de IA corporativos."
    }
]
for ep in extra_product_pages:
    if ep["id"] not in existing_ids:
        routes["site_pages"].append(ep)

with open(ROUTES_FILE, "w", encoding="utf-8") as f:
    json.dump(routes, f, ensure_ascii=False, indent=2)

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

def add_url_block(en_url, pt_url, priority="0.8", changefreq="monthly", image_info=None, pt_image_info=None):
    # English block
    lines.append('  <url>')
    lines.append(f'    <loc>{en_url}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append(f'    <changefreq>{changefreq}</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{pt_url}" />')
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
    lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{pt_url}" />')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_url}" />')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="pt-BR" href="{pt_url}" />')
    if pt_image_info or image_info:
        info = pt_image_info or image_info
        lines.append('    <image:image>')
        lines.append(f'      <image:loc>{info["loc"]}</image:loc>')
        lines.append(f'      <image:title>{info["title"]}</image:title>')
        lines.append(f'      <image:caption>{info["caption"]}</image:caption>')
        lines.append('    </image:image>')
    lines.append('  </url>')

# Institutional & Product pages only (Blog posts live in https://hsnlabs.ai/blog/sitemap.xml)
for page in routes.get("site_pages", []):
    if page["id"] == "blog_home":
        continue
    en_url = f"https://hsnlabs.ai{page['en_path']}"
    pt_url = f"https://hsnlabs.ai{page['pt_path']}"
    is_root = page["pt_path"] == "/"
    prio = "1.0" if is_root else "0.9"
    freq = "weekly" if is_root else "monthly"
    img = None
    pt_img = None
    if is_root:
        img = {
            "loc": "https://hsnlabs.ai/assets/brand/og-image.png",
            "title": "hsnlabs | Enterprise AI Architectures",
            "caption": "hsnlabs — Hybrid engineering, business ontologies, and deterministic agents."
        }
        pt_img = {
            "loc": "https://hsnlabs.ai/assets/brand/og-image-pt.png",
            "title": "hsnlabs | Adoção de Engenharia Agentica",
            "caption": "hsnlabs — Engenharia híbrida, ontologias de negócio e agentes determinísticos em produção."
        }
    add_url_block(en_url, pt_url, priority=prio, changefreq=freq, image_info=img, pt_image_info=pt_img)

# Standalone EN whitepaper
lines.append('  <url>')
lines.append('    <loc>https://hsnlabs.ai/en/products/honeycomb-protocol/whitepaper/</loc>')
lines.append(f'    <lastmod>{today}</lastmod>')
lines.append('    <changefreq>monthly</changefreq>')
lines.append('    <priority>0.8</priority>')
lines.append('  </url>')

lines.append('</urlset>')

xml_content = "\n".join(lines)

# Verify valid XML
ET.fromstring(xml_content)

# Verify zero parentheses
assert "(" not in xml_content and ")" not in xml_content, "ERRO: Parenteses encontrados no sitemap.xml!"

SITEMAP_FILE.write_text(xml_content, encoding="utf-8")
print(f"Sitemap atualizado com sucesso em {SITEMAP_FILE}. Total URLs institucionais e produtos sincronizadas.")
