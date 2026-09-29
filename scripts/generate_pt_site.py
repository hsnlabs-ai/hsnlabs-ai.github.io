import re
from pathlib import Path

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")
SRC_INDEX = SITE_DIR / "index.html"
PT_DIR = SITE_DIR / "pt"
PT_INDEX = PT_DIR / "index.html"

PT_DIR.mkdir(parents=True, exist_ok=True)

html = SRC_INDEX.read_text(encoding="utf-8")

# 1. Update lang attribute
html = html.replace('<html lang="en">', '<html lang="pt-BR">')

# 2. Update head meta tags
html = html.replace(
    '<title>Boutique | Agentic AI - hsn labs</title>',
    '<title>Boutique | Arquitetura de Agentes de IA - HSN Labs</title>'
)
html = html.replace(
    '<meta property="og:url" content="https://hsnlabs.ai/">',
    '<meta property="og:url" content="https://hsnlabs.ai/pt/">'
)
html = html.replace(
    '<meta property="og:title" content="HSN Labs — AI Agents That Don\'t Fail in Production">',
    '<meta property="og:title" content="HSN Labs — Agentes de IA que Nao Falham em Producao">'
)
html = html.replace(
    '<meta property="og:description" content="Boutique building resilient multi-agent architectures on business ontologies.">',
    '<meta property="og:description" content="Boutique construindo arquiteturas multiagente resilientes sobre ontologias de negocios.">'
)
html = html.replace(
    '<meta name="twitter:url" content="https://hsnlabs.ai/">',
    '<meta name="twitter:url" content="https://hsnlabs.ai/pt/">'
)
html = html.replace(
    '<meta name="twitter:title" content="HSN Labs — AI Agents That Don\'t Fail in Production">',
    '<meta name="twitter:title" content="HSN Labs — Agentes de IA que Nao Falham em Producao">'
)
html = html.replace(
    '<meta name="twitter:description" content="Boutique building resilient multi-agent architectures on business ontologies.">',
    '<meta name="twitter:description" content="Boutique construindo arquiteturas multiagente resilientes sobre ontologias de negocios.">'
)
html = html.replace(
    '<link rel="canonical" href="https://hsnlabs.ai/">',
    '<link rel="canonical" href="https://hsnlabs.ai/pt/">'
)
html = html.replace(
    '<meta name="description" content="AI agents fail on unstructured data. We build the ontologies required for production.">',
    '<meta name="description" content="Agentes de IA falham em dados nao estruturados. Construimos as ontologias necessarias para producao.">'
)

# 3. Update Nav
html = html.replace(
    '<a href="/advisory" class="nav-link">Advisory</a>',
    '<a href="/pt/advisory" class="nav-link">Advisory</a>'
)
html = html.replace(
    '<a href="/blog/" class="nav-link">Blog</a>',
    '<a href="/blog/pt/" class="nav-link">Blog</a>'
)
html = html.replace(
    '<a href="/bootcamp" class="btn btn-primary">Apply for Bootcamp</a>',
    '<a href="/pt/bootcamp" class="btn btn-primary">Aplicar para o Bootcamp</a>'
)

# Add language toggle in header nav
en_nav_marker = '<div class="nav-menu" style="margin-left: auto; margin-right: 32px;">'
pt_nav_replacement = '<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">\n        <a href="/pt/advisory" class="nav-link">Advisory</a>\n        <a href="/blog/pt/" class="nav-link">Blog</a>\n        <a href="/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>\n      </div>'
html = re.sub(
    r'<div class="nav-menu"[^>]*>[\s\S]*?</div>',
    pt_nav_replacement,
    html,
    count=1
)

# 4. Hero section copy
html = html.replace(
    '<span class="hero-title-lead">Enterprise AI Agents</span>',
    '<span class="hero-title-lead">Agentes de IA Enterprise</span>'
)
html = html.replace(
    '<span class="hero-title-sub">that don\'t fail in production</span>',
    '<span class="hero-title-sub">que nao falham em producao</span>'
)
html = html.replace(
    'AI agents fail on unstructured data. We build the ontologies required for production.',
    'Agentes de IA falham em dados corporativos sujos. Construimos as ontologias necessarias para producao real.'
)
html = html.replace(
    '<a href="/bootcamp" class="btn btn-primary">Apply for Bootcamp</a>',
    '<a href="/pt/bootcamp" class="btn btn-primary">Aplicar para o Bootcamp</a>'
)
html = html.replace(
    '<a href="#contact" class="btn btn-outline">Contact Us</a>',
    '<a href="#contact" class="btn btn-outline">Fale Conosco</a>'
)
html = html.replace(
    '<div class="portfolio-label">Our Portfolio</div>',
    '<div class="portfolio-label">Nosso Portfolio</div>'
)

# 5. Services / Bento section
html = html.replace(
    '<h2 class="display-section">Why Agents Fail</h2>',
    '<h2 class="display-section">Por Que Agentes Falham</h2>'
)
html = html.replace(
    'Most enterprise AI agents break when exposed to messy company data, complex compliance, and strict business rules.',
    'A maioria dos agentes corporativos quebra ao lidar com dados legados sujos, regras estritas de conformidade e integridade relacional.'
)
html = html.replace(
    '<h3 class="card-title">SaaS Billing Reduction</h3>',
    '<h3 class="card-title">Reducao de Custos com SaaS</h3>'
)
html = html.replace(
    '<h3 class="card-title">Failed Pilots</h3>',
    '<h3 class="card-title">Pilotos que Falham</h3>'
)
html = html.replace(
    '<h3 class="card-title">Operational Errors</h3>',
    '<h3 class="card-title">Erros Operacionais</h3>'
)
html = html.replace(
    '<h3 class="card-title">Agent Development Life Cycle Stack</h3>',
    '<h3 class="card-title">Stack do Ciclo de Vida de Desenvolvimento de Agentes</h3>'
)

# 6. Regulated Enterprise Verticals
html = html.replace(
    '<h2 class="display-section">Regulated Enterprise Verticals</h2>',
    '<h2 class="display-section">Setores Corporativos Regulados</h2>'
)
html = html.replace(
    '<h2 class="display-section" style="margin-bottom: 12px;">Contact Us</h2>',
    '<h2 class="display-section" style="margin-bottom: 12px;">Fale Conosco</h2>'
)

# Check zero parentheses in any newly introduced Portuguese texts
# Write file
PT_INDEX.write_text(html, encoding="utf-8")
print(f"Salvo {PT_INDEX} com sucesso.")
