#!/usr/bin/env python3
import re
from pathlib import Path

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")

def clean_html_body_text_only(html: str) -> str:
    """
    Cleans parentheses ONLY from visible HTML text nodes, title, and meta tags.
    Leaves <style>, <script>, inline attributes (like onclick, href), and SVGs untouched.
    """
    styles = []
    def save_style(match):
        styles.append(match.group(0))
        return f"__STYLE_PLACEHOLDER_{len(styles)-1}__"
    html = re.sub(r'<style.*?</style>', save_style, html, flags=re.DOTALL | re.IGNORECASE)

    scripts = []
    def save_script(match):
        scripts.append(match.group(0))
        return f"__SCRIPT_PLACEHOLDER_{len(scripts)-1}__"
    html = re.sub(r'<script.*?</script>', save_script, html, flags=re.DOTALL | re.IGNORECASE)

    svgs = []
    def save_svg(match):
        svgs.append(match.group(0))
        return f"__SVG_PLACEHOLDER_{len(svgs)-1}__"
    html = re.sub(r'<svg.*?</svg>', save_svg, html, flags=re.DOTALL | re.IGNORECASE)

    def clean_text(match):
        txt = match.group(1)
        cleaned = re.sub(r'\(([^)]+)\)', r'— \1 —', txt)
        cleaned = cleaned.replace('(', '— ').replace(')', ' —')
        cleaned = re.sub(r'—\s*—+', '—', cleaned)
        return f">{cleaned}<"

    html = re.sub(r'>([^<]+)<', clean_text, html)

    def clean_meta_desc(match):
        desc = match.group(1)
        cleaned = re.sub(r'\(([^)]+)\)', r'— \1 —', desc)
        cleaned = cleaned.replace('(', '— ').replace(')', ' —')
        return f'<meta name="description" content="{cleaned}"'

    html = re.sub(r'<meta\s+name="description"\s+content="([^"]*)"', clean_meta_desc, html)

    for i, s in enumerate(styles):
        html = html.replace(f"__STYLE_PLACEHOLDER_{i}__", s)
    for i, s in enumerate(scripts):
        html = html.replace(f"__SCRIPT_PLACEHOLDER_{i}__", s)
    for i, s in enumerate(svgs):
        html = html.replace(f"__SVG_PLACEHOLDER_{i}__", s)

    return html

def localize_common_pt_components(html: str) -> str:
    # 1. Cookie consent banner
    old_cookie_pattern = r'<div class="cookie-banner" id="cookieBanner"[\s\S]*?</div>\s*</div>'
    new_cookie_banner = '''<div class="cookie-banner" id="cookieBanner" role="dialog" aria-label="Consentimento de privacidade e cookies">
    <div class="cookie-title">Consentimento de Privacidade e Cookies</div>
    <p class="cookie-text">
      Utilizamos telemetria para avaliar o desempenho do sistema sob normas da LGPD. Consulte nossa <a href="/pt/privacy-policy/">Política de Privacidade</a>.
    </p>
    <div class="cookie-actions">
      <button type="button" class="btn btn-primary cookie-btn-accept" onclick="acceptCookies()">Aceitar Todos</button>
      <button type="button" class="btn btn-outline cookie-btn-decline" onclick="declineCookies()">Recusar</button>
    </div>
  </div>'''
    html = re.sub(old_cookie_pattern, new_cookie_banner, html)

    # 2. Form success message
    html = html.replace(
        'Thank you. An engineering lead will review your submission and respond within 24 hours.',
        'Obrigado. Um engenheiro responsável analisará seus dados e responderá em até 24 horas.'
    )

    # 3. Footer brand tagline
    html = html.replace(
        'An engineering lab with over five years of shipping AI products and resilient agent architectures in production.',
        'Laboratório de engenharia com mais de cinco anos implementando produtos de IA e arquiteturas agênticas resilientes em produção.'
    )

    # 4. Footer navigation title and links
    html = html.replace('<div class="footer-col-title">Navigation</div>', '<div class="footer-col-title">Navegação</div>')
    html = html.replace('<li><a href="/bootcamp">Agentic Bootcamp</a></li>', '<li><a href="/pt/bootcamp/">Bootcamp de Agentes</a></li>')
    html = html.replace('<li><a href="/advisory">Advisory</a></li>', '<li><a href="/pt/advisory/">Advisory</a></li>')
    html = html.replace('<li><a href="/playbooks">Playbooks</a></li>', '<li><a href="/pt/playbooks/">Playbooks</a></li>')
    html = html.replace('<li><a href="/blog/">Blog</a></li>', '<li><a href="/blog/pt/">Blog</a></li>')
    html = html.replace('<li><a href="/blog/">Blog</a></li>', '<li><a href="/blog/pt/">Blog</a></li>')
    html = html.replace('<li><a href="/#contact">Contact Us</a></li>', '<li><a href="/pt/#contact">Fale Conosco</a></li>')

    # 5. Footer newsletter
    html = html.replace('placeholder="name@company.com"', 'placeholder="seu.email@empresa.com"')
    html = html.replace(">Send</button>", ">Assinar</button>")
    html = html.replace("b.innerText='Joining...';", "b.innerText='Enviando...';")
    html = html.replace("b.innerText='Subscribed';", "b.innerText='Inscrito';")
    html = html.replace("b.innerText='Send';", "b.innerText='Assinar';")

    # 6. Footer bottom bar
    html = html.replace('2026 HSN Labs. All rights reserved.', '2026 HSN Labs. Todos os direitos reservados.')
    html = html.replace('<a href="/privacy-policy">Privacy Policy</a>', '<a href="/pt/privacy-policy/">Política de Privacidade</a>')
    html = html.replace('<a href="/modern-slavery-statement">Modern Slavery Statement</a>', '<a href="/pt/modern-slavery-statement/">Declaração de Conformidade</a>')

    return html

def update_english_page_headers():
    en_pages = [
        SITE_DIR / "index.html",
        SITE_DIR / "bootcamp" / "index.html",
        SITE_DIR / "advisory" / "index.html",
        SITE_DIR / "mcp" / "index.html",
        SITE_DIR / "privacy-policy" / "index.html",
        SITE_DIR / "modern-slavery-statement" / "index.html",
        SITE_DIR / "playbooks" / "index.html",
    ]
    
    path_map = {
        "index.html": "/pt/",
        "bootcamp/index.html": "/pt/bootcamp/",
        "advisory/index.html": "/pt/advisory/",
        "mcp/index.html": "/pt/mcp/",
        "privacy-policy/index.html": "/pt/privacy-policy/",
        "modern-slavery-statement/index.html": "/pt/modern-slavery-statement/",
        "playbooks/index.html": "/pt/playbooks/",
    }
    
    for page in en_pages:
        if not page.exists():
            continue
        rel = page.relative_to(SITE_DIR).as_posix()
        pt_target = path_map.get(rel, "/pt/")
        content = page.read_text(encoding="utf-8")
        
        content = re.sub(r'<link rel="canonical" href="https://hsnlabs.ai/([^"/]+)">', r'<link rel="canonical" href="https://hsnlabs.ai/\1/">', content)
        
        en_target = pt_target.replace("/pt", "")
        if en_target == "": en_target = "/"
        
        hreflangs = f'''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai{en_target}">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai{pt_target}">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai{en_target}">'''
        
        content = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', content)
        content = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, content)
        
        old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
        new_nav = f'''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/advisory" class="nav-link">Advisory</a>
        <a href="/playbooks" class="nav-link">Playbooks</a>
        <a href="/blog/" class="nav-link">Blog</a>
        <a href="{pt_target}" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">PT</a>
      </div>'''
        
        content = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
        page.write_text(content, encoding="utf-8")
        print(f"Atualizada pagina EN: {page.name}")

def build_pt_home():
    src = SITE_DIR / "index.html"
    dest_dir = SITE_DIR / "pt"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "index.html"
    
    html = src.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="pt-BR">')
    html = html.replace(
        '<title>Boutique | Agentic AI - hsn labs</title>',
        '<title>Boutique | Arquitetura de Agentes de IA — HSN Labs</title>'
    )
    html = html.replace(
        '<meta property="og:url" content="https://hsnlabs.ai/">',
        '<meta property="og:url" content="https://hsnlabs.ai/pt/">'
    )
    html = html.replace(
        '<meta property="og:title" content="HSN Labs — Accelerate Enterprise AI Agent Adoption">',
        '<meta property="og:title" content="HSN Labs — Acelere a Adoção de Agentes de IA Enterprise">'
    )
    html = html.replace(
        '<meta property="og:description" content="Bridge the gap between AI strategy and live operations without disrupting legacy systems.">',
        '<meta property="og:description" content="Conecte a estratégia de IA à operação real sem travar os sistemas legados da companhia.">'
    )
    html = html.replace(
        '<meta name="twitter:title" content="HSN Labs — Accelerate Enterprise AI Agent Adoption">',
        '<meta name="twitter:title" content="HSN Labs — Acelere a Adoção de Agentes de IA Enterprise">'
    )
    html = html.replace(
        '<meta name="twitter:description" content="Bridge the gap between AI strategy and live operations without disrupting legacy systems.">',
        '<meta name="twitter:description" content="Conecte a estratégia de IA à operação real sem travar os sistemas legados da companhia.">'
    )
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/">', '<link rel="canonical" href="https://hsnlabs.ai/pt/">')
    html = html.replace(
        '<meta name="description" content="Bridge the gap between AI strategy and live operations without disrupting legacy systems.">',
        '<meta name="description" content="Conecte a estratégia de IA à operação real sem travar os sistemas legados da companhia.">'
    )
    
    hreflangs = '''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai/">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai/pt/">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai/">'''
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, html)
    
    old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
    new_nav = '''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/pt/advisory" class="nav-link">Advisory</a>
        <a href="/blog/pt/" class="nav-link">Blog</a>
        <a href="/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
      </div>'''
    html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)
    
    html = html.replace('<a href="/bootcamp" class="btn btn-primary">Apply for Bootcamp</a>', '<a href="/pt/bootcamp" class="btn btn-primary">Aplicar para o Bootcamp</a>')
    
    html = html.replace(
        '<span class="hero-title-lead">Accelerate Enterprise</span>',
        '<span class="hero-title-lead">Acelere a Adoção</span>'
    )
    html = html.replace(
        '<span class="hero-title-sub" style="color: var(--cyan-text);">Agentic AI adoption.</span>',
        '<span class="hero-title-sub" style="color: var(--cyan-text);">de IA agêntica enterprise.</span>'
    )
    html = html.replace(
        'Bridge the gap between AI strategy and live operations without disrupting legacy systems.',
        'Conecte a estratégia de IA à operação real sem travar os sistemas legados da companhia.'
    )
    html = html.replace('>Contact Us<', '>Fale Conosco<')
    html = html.replace('>Our Portfolio<', '>Nosso Portfólio<')
    
    html = html.replace('>Why Agents Fail<', '>Por Que Agentes Falham<')
    html = html.replace(
        'Most enterprise AI agents break when exposed to messy company data, complex compliance, and strict business rules.',
        'A maioria dos agentes corporativos quebra ao lidar com dados legados sujos, regras estritas de conformidade e integridade relacional.'
    )
    html = html.replace('>SaaS Billing Reduction<', '>Redução de Custos com SaaS<')
    html = html.replace('>Failed Pilots<', '>Pilotos que Falham<')
    html = html.replace('>Operational Errors<', '>Erros Operacionais<')
    html = html.replace('>Agent Development Life Cycle Stack<', '>Stack do Ciclo de Vida de Desenvolvimento de Agentes<')
    
    html = html.replace('>Regulated Enterprise Verticals<', '>Setores Corporativos Regulados<')
    
    html = html.replace('placeholder="Your Name"', 'placeholder="Seu Nome"')
    html = html.replace('placeholder="name@company.com"', 'placeholder="seu.email@empresa.com"')
    html = html.replace('placeholder="Acme Corp"', 'placeholder="Nome da Empresa"')
    html = html.replace('placeholder="What are you looking to build or automate?"', 'placeholder="O que voce precisa construir ou automatizar?"')
    html = html.replace('>Send Message<', '>Enviar Mensagem<')
    
    html = localize_common_pt_components(html)
    html = clean_html_body_text_only(html)
    
    dest.write_text(html, encoding="utf-8")
    print(f"Gerado {dest}")

def build_pt_bootcamp():
    src = SITE_DIR / "bootcamp" / "index.html"
    dest_dir = SITE_DIR / "pt" / "bootcamp"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "index.html"
    
    html = src.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="pt-BR">')
    html = html.replace('<title>Agentic Bootcamp — HSN Labs</title>', '<title>Bootcamp de Agentes — HSN Labs</title>')
    
    html = html.replace('content="https://hsnlabs.ai/bootcamp"', 'content="https://hsnlabs.ai/pt/bootcamp/"')
    html = html.replace('content="https://hsnlabs.ai/bootcamp/"', 'content="https://hsnlabs.ai/pt/bootcamp/"')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/bootcamp">', '<link rel="canonical" href="https://hsnlabs.ai/pt/bootcamp/">')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/bootcamp/">', '<link rel="canonical" href="https://hsnlabs.ai/pt/bootcamp/">')
    
    html = html.replace(
        'content="We embed senior Forward Deployed Engineers with your team to build AI agents that survive production. 100% credited toward production rollout for qualified accounts."',
        'content="Alocamos Engenheiros Forward Deployed seniores junto a sua equipe para construir agentes de IA que operam em producao. Cem por cento creditado para o contrato de implantacao em contas qualificadas."'
    )
    
    hreflangs = '''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai/bootcamp/">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai/pt/bootcamp/">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai/bootcamp/">'''
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, html)
    
    old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
    new_nav = '''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/pt/advisory" class="nav-link">Advisory</a>
        <a href="/blog/pt/" class="nav-link">Blog</a>
        <a href="/bootcamp/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
      </div>'''
    html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)
    
    html = html.replace('<a href="/bootcamp" class="btn btn-primary">Apply for Bootcamp</a>', '<a href="/pt/bootcamp" class="btn btn-primary">Inscrever no Bootcamp</a>')
    
    html = html.replace('← Return to Overview', '← Voltar para Visao Geral')
    html = html.replace('href="/" class="back-link"', 'href="/pt/" class="back-link"')
    html = html.replace('<h1 class="display-hero">Agentic Bootcamp</h1>', '<h1 class="display-hero">Bootcamp de Agentes</h1>')
    html = html.replace(
        'We embed a senior FDE inside your operation. 100% credited toward production rollout for qualified accounts.',
        'Alocamos um engenheiro senior FDE dentro da sua operacao. Cem por cento creditado para implantacao em contas qualificadas.'
    )
    html = html.replace('>Request Call<', '>Solicitar Chamada<')
    html = html.replace('>Review Criteria<', '>Revisar Criterios<')
    
    html = html.replace('<h2 class="display-section">Our Method</h2>', '<h2 class="display-section">Nosso Metodo</h2>')
    html = html.replace('01 • Environment Setup', '01 • Setup de Ambiente')
    html = html.replace(
        'Database read replicas, ERP connections, and security isolation before writing code.',
        'Replicas de leitura de banco de dados, conexoes ERP e isolamento de seguranca antes de escrever qualquer codigo.'
    )
    html = html.replace('02 • Ontology Mapping', '02 • Mapeamento Ontologico')
    html = html.replace(
        'Extracting business rules and mapping legacy ERP tables into executable business ontologies.',
        'Extracao de regras de negocio e mapeamento de tabelas de ERP legado em ontologias de negocio executaveis.'
    )
    html = html.replace('03 • Sandbox Prototype', '03 • Prototipo em Sandbox')
    html = html.replace(
        'Deploying deep agents in a secure, isolated test environment, testing edge cases.',
        'Implantacao de deep agents em ambiente de teste isolado e seguro, validando casos de borda.'
    )
    html = html.replace('04 • Business Case', '04 • Business Case')
    html = html.replace(
        'Delivery of technical feasibility, audited ROI metrics, and full rollout roadmap. Sprint fee is completely rebated against the production deployment contract.',
        'Entrega de viabilidade tecnica, metricas auditadas de ROI e roadmap de implantacao. Taxa do sprint totalmente reembolsada no contrato de producao.'
    )
    
    html = html.replace('<h2 class="display-section">Qualification Criteria</h2>', '<h2 class="display-section">Criterios de Qualificacao</h2>')
    html = html.replace(
        'The bootcamp is an intensive 12k USD production sprint. Qualified enterprises unlock our Performance Rebate: the fee is 100% credited toward your full production contract upon rollout.',
        'O bootcamp e um sprint intensivo de producao de 12 mil USD. Empresas qualificadas desbloqueiam nosso Reembolso por Desempenho: a taxa e cem por cento creditada para o contrato de producao.'
    )
    html = html.replace('01 • Executive Sponsor', '01 • Patrocinador Executivo')
    html = html.replace(
        'Direct involvement from a C-level executive, such as the CIO, CTO, or CEO.',
        'Envolvimento direto de um executivo C-level, como CIO, CTO ou CEO.'
    )
    html = html.replace('02 • Approved Budget', '02 • Orcamento Aprovado')
    html = html.replace(
        'Minimum annual revenue of 10M USD with pre-approved budget for the current fiscal year to develop and deploy the project upon verified validation.',
        'Receita anual minima de 10 milhoes de USD com orcamento pre-aprovado no ano fiscal vigente para desenvolver e implantar o projeto.'
    )
    html = html.replace('03 • Data Access', '03 • Acesso a Dados')
    html = html.replace(
        'Staging credentials or read replicas ready before day one.',
        'Credenciais de homologacao ou replicas de leitura liberadas antes do primeiro dia.'
    )
    
    html = html.replace('Bootcamp Application', 'Inscricao no Bootcamp')
    html = html.replace(
        'Submit your information to request a technical intake call. We review your systems and confirm qualification details within 24 hours.',
        'Envie seus dados para solicitar uma chamada tecnica. Analisamos seus sistemas e confirmamos os detalhes de qualificacao em ate 24 horas.'
    )
    html = html.replace('Full Name', 'Nome Completo')
    html = html.replace('Work Email', 'E-mail Corporativo')
    html = html.replace('Company Name', 'Nome da Empresa')
    html = html.replace('Company Website', 'Website da Empresa')
    html = html.replace('Executive Role', 'Cargo Executivo')
    html = html.replace('Select your role', 'Selecione seu cargo')
    html = html.replace('Annual Revenue', 'Receita Anual')
    html = html.replace('Select revenue tier', 'Selecione a faixa de receita')
    html = html.replace('Under 10M USD', 'Abaixo de 10M USD')
    html = html.replace('Above 500M USD', 'Acima de 500M USD')
    html = html.replace(
        'Apply for Performance Rebate Program — 100% fee credited toward production rollout.',
        'Candidatar-se ao Programa de Reembolso por Desempenho — taxa cem por cento creditada para o contrato de producao.'
    )
    
    html = localize_common_pt_components(html)
    html = clean_html_body_text_only(html)
    dest.write_text(html, encoding="utf-8")
    print(f"Gerado {dest}")

def build_pt_advisory():
    src = SITE_DIR / "advisory" / "index.html"
    dest_dir = SITE_DIR / "pt" / "advisory"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "index.html"
    
    html = src.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="pt-BR">')
    html = html.replace('<title>Architecture Advisory | Hugo S. Nascimento</title>', '<title>Advisory de Arquitetura | Hugo S. Nascimento</title>')
    html = html.replace('<title>Architecture Advisory — HSN Labs</title>', '<title>Advisory de Arquitetura — HSN Labs</title>')
    
    html = html.replace('content="https://hsnlabs.ai/advisory"', 'content="https://hsnlabs.ai/pt/advisory/"')
    html = html.replace('content="https://hsnlabs.ai/advisory/"', 'content="https://hsnlabs.ai/pt/advisory/"')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/advisory">', '<link rel="canonical" href="https://hsnlabs.ai/pt/advisory/">')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/advisory/">', '<link rel="canonical" href="https://hsnlabs.ai/pt/advisory/">')
    
    hreflangs = '''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai/advisory/">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai/pt/advisory/">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai/advisory/">'''
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, html)
    
    old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
    new_nav = '''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/pt/advisory" class="nav-link">Advisory</a>
        <a href="/blog/pt/" class="nav-link">Blog</a>
        <a href="/advisory/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
      </div>'''
    html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)
    
    html = html.replace('<a href="/bootcamp" class="btn btn-primary">Apply for Bootcamp</a>', '<a href="/pt/bootcamp" class="btn btn-primary">Aplicar para o Bootcamp</a>')
    
    html = html.replace('>Agentic AI Advisory<', '>Advisory de IA Agentica<')
    html = html.replace('>Beyond technical implementation.<', '>Alem da implementacao tecnica.<')
    html = html.replace(
        'Agentic automation rewrites unit economics and threatens traditional operating margins. We guide C-levels through the structural change required to protect market share, modernize core operations, and deploy autonomous workflows safely.',
        'A automacao agentica reescreve a economia unitaria e ameaca as margens operacionais tradicionais. Guiamos executivos C-level na mudanca estrutural necessaria para proteger market share, modernizar operacoes centrais e implantar fluxos autonomos com seguranca.'
    )
    html = html.replace('>Start the Conversation<', '>Iniciar Conversa<')
    
    html = html.replace('>The Disruption Gap<', '>O Abismo da Disrupcao<')
    html = html.replace(
        'Autonomous agents threaten traditional operating margins. We prepare your enterprise to defend market share and scale safely.',
        'Agentes autonomos ameacam as margens operacionais tradicionais. Preparamos sua empresa para defender mercado e escalar com seguranca.'
    )
    html = html.replace('<h3 class="card-title">Operating Models</h3>', '<h3 class="card-title">Modelos Operacionais</h3>')
    html = html.replace(
        'Software no longer just assists workers. It executes work. We help executive teams restructure core workflows, reallocate headcount to high-leverage supervision, and adapt operating rhythms for continuous autonomous execution.',
        'O software nao atua mais apenas como assistente. Ele executa trabalho. Ajudamos diretorias a reestruturar fluxos, realocar equipes para supervisao estrategica e adaptar ritmos para execucao autonoma continua.'
    )
    html = html.replace('<h3 class="card-title">Margin Defense</h3>', '<h3 class="card-title">Defesa de Margem</h3>')
    html = html.replace(
        'New competitors deploy digital workforces at a fraction of traditional BPO costs. We audit your cost structures, identify vulnerable high-friction operations, and build defense plans to maintain your operational edge.',
        'Novos concorrentes implantam forcas de trabalho digitais por uma fracao do custo de BPO tradicional. Auditamos suas estruturas de custo, identificamos operacoes vulneraveis e desenhamos planos de defesa.'
    )
    html = html.replace('<h3 class="card-title">Progressive Migration</h3>', '<h3 class="card-title">Migracao Progressiva</h3>')
    html = html.replace(
        'Replacing legacy operations all at once creates catastrophic risk. We engineer progressive routing paths that swap human and rule-based tasks for autonomous deep agents without disrupting live revenue lines.',
        'Substituir operacoes legadas de uma so vez gera risco desastroso. Desenhamos rotas progressivas que transferem tarefas manuais para deep agents sem interromper fluxos de receita ativos.'
    )
    html = html.replace('<h3 class="card-title">Executive Governance</h3>', '<h3 class="card-title">Governanca Executiva</h3>')
    html = html.replace(
        'Board-level visibility into autonomous agent reliability, regulatory compliance, and audit trails. We help C-suites establish operational boundaries that prevent runaway costs and protect corporate reputation.',
        'Visibilidade para conselhos sobre confiabilidade de agentes autonomos, conformidade regulatoria e trilhas de auditoria. Ajudamos a lideranca a estabelecer limites operacionais que evitam custos excessivos.'
    )
    
    html = localize_common_pt_components(html)
    html = clean_html_body_text_only(html)
    dest.write_text(html, encoding="utf-8")
    print(f"Gerado {dest}")

def build_pt_mcp():
    src = SITE_DIR / "mcp" / "index.html"
    dest_dir = SITE_DIR / "pt" / "mcp"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "index.html"
    
    html = src.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="pt-BR">')
    html = html.replace('<title>Enterprise MCP Servers — HSN Labs</title>', '<title>Servidores MCP Enterprise — HSN Labs</title>')
    
    html = html.replace('content="https://hsnlabs.ai/mcp"', 'content="https://hsnlabs.ai/pt/mcp/"')
    html = html.replace('content="https://hsnlabs.ai/mcp/"', 'content="https://hsnlabs.ai/pt/mcp/"')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/mcp">', '<link rel="canonical" href="https://hsnlabs.ai/pt/mcp/">')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/mcp/">', '<link rel="canonical" href="https://hsnlabs.ai/pt/mcp/">')
    
    hreflangs = '''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai/mcp/">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai/pt/mcp/">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai/mcp/">'''
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, html)
    
    old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
    new_nav = '''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/pt/advisory" class="nav-link">Advisory</a>
        <a href="/blog/pt/" class="nav-link">Blog</a>
        <a href="/mcp/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
      </div>'''
    html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)
    
    html = html.replace('<a href="/bootcamp" class="btn btn-primary">Apply for Bootcamp</a>', '<a href="/pt/bootcamp" class="btn btn-primary">Aplicar para o Bootcamp</a>')
    
    html = html.replace('Enterprise MCP Servers', 'Servidores MCP Enterprise')
    html = html.replace('Secure context pipelines for mission-critical core data.', 'Pipelines de contexto seguro para dados operacionais criticos.')
    html = html.replace(
        'Autonomous agents fail when disconnected from live business context or exposed to unvetted API tools. We build and harden private Model Context Protocol servers directly inside your cloud perimeter, connecting deep agents to SAP, TOTVS, and SQL databases under zero-trust governance.',
        'Agentes autonomos falham quando desconectados do contexto real do negocio ou expostos a ferramentas de API sem validacao. Construimos e blindamos servidores privados de Model Context Protocol dentro do seu perimetro de nuvem, conectando deep agents ao SAP, TOTVS e bancos relacionais sob governanca zero trust.'
    )
    html = html.replace('>Request Technical Scoping<', '>Solicitar Escopo Tecnico<')
    html = html.replace('>Review Architecture<', '>Revisar Arquitetura<')
    
    html = html.replace('>The Integration Hazard<', '>O Risco de Integracao<')
    html = html.replace(
        'Public SaaS connectors and brittle API scripts create catastrophic security holes and runtime hallucinations.',
        'Conectores SaaS publicos e scripts frageis de API abrem brechas criticas de seguranca e geram alucinacoes em producao.'
    )
    html = html.replace('Perimeter Exposure', 'Exposicao de Perimetro')
    html = html.replace(
        'Public SaaS connectors require routing sensitive database credentials and customer records through third-party multi-tenant clouds. CISOs and risk committees reject external data transit on regulatory grounds.',
        'Conectores SaaS publicos exigem trafegar credenciais de banco e registros confidenciais por nuvens de terceiros. CISOs e comites de risco vetam esse trafego por razoes regulatorias estritas.'
    )
    html = html.replace('Schema Hallucination', 'Alucinacao de Schema')
    html = html.replace(
        'Stochastic models guess unmapped columns, foreign keys, and status codes on complex ERPs. When an agent calls an unhardened tool, malformed payloads fail silently or trigger destructive database rollbacks.',
        'Modelos probabilisticos adivinham colunas, chaves estrangeiras e codigos de status em ERPs complexos. Sem contratos firmes, cargas corrompidas falham silenciosamente ou causam rollbacks destrutivos.'
    )
    html = html.replace('Blind Tool Execution', 'Execucao Cega')
    html = html.replace(
        'Without granular role-based bounds, an agent granted write access can mutate inventory tables, trigger duplicate vendor disbursements, or bypass enterprise authorization tiers without supervision.',
        'Sem limites granulares baseados em funcao, um agente com permissao de escrita pode alterar estoques, duplicar desembolsos ou contornar alcadas de aprovacao sem supervisao humana.'
    )
    html = html.replace('Zero Telemetry', 'Zero Telemetria')
    html = html.replace(
        'Generic REST webhooks provide no standard audit trail for AI actions. In the event of an operational anomaly, engineering teams cannot trace which prompt triggered which tool call or verify parameter provenance.',
        'Webhooks genericos nao oferecem trilha de auditoria padronizada para acoes de IA. Em incidentes operacionais, a engenharia nao consegue rastrear qual prompt disparou qual chamada.'
    )
    
    html = html.replace('>What We Engineer<', '>O Que Construimos<')
    html = html.replace('Sovereign MCP Runtime', 'Runtime MCP Soberano')
    html = html.replace('Deterministic Data Contracts', 'Contratos Deterministicos')
    html = html.replace('Enterprise Identity & RBAC', 'Identidade Enterprise e RBAC')
    html = html.replace('Runtime Audit Trail', 'Trilha de Auditoria em Execucao')
    
    html = localize_common_pt_components(html)
    html = clean_html_body_text_only(html)
    dest.write_text(html, encoding="utf-8")
    print(f"Gerado {dest}")

def build_pt_privacy_policy():
    src = SITE_DIR / "privacy-policy" / "index.html"
    dest_dir = SITE_DIR / "pt" / "privacy-policy"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "index.html"
    
    html = src.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="pt-BR">')
    html = html.replace('<title>Privacy Policy — HSN Labs</title>', '<title>Politica de Privacidade — HSN Labs</title>')
    
    html = html.replace('content="https://hsnlabs.ai/privacy-policy"', 'content="https://hsnlabs.ai/pt/privacy-policy/"')
    html = html.replace('content="https://hsnlabs.ai/privacy-policy/"', 'content="https://hsnlabs.ai/pt/privacy-policy/"')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/privacy-policy">', '<link rel="canonical" href="https://hsnlabs.ai/pt/privacy-policy/">')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/privacy-policy/">', '<link rel="canonical" href="https://hsnlabs.ai/pt/privacy-policy/">')
    
    hreflangs = '''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai/privacy-policy/">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai/pt/privacy-policy/">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai/privacy-policy/">'''
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, html)
    
    old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
    new_nav = '''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/pt/advisory" class="nav-link">Advisory</a>
        <a href="/blog/pt/" class="nav-link">Blog</a>
        <a href="/privacy-policy/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
      </div>'''
    html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)
    
    html = html.replace('← Return to Overview', '← Voltar para Visao Geral')
    html = html.replace('href="/" class="back-link"', 'href="/pt/" class="back-link"')
    html = html.replace('<h1 class="display-title">Privacy Policy</h1>', '<h1 class="display-title">Politica de Privacidade</h1>')
    html = html.replace('Last updated: February 2026', 'Ultima atualizacao: Fevereiro de 2026')
    
    html = localize_common_pt_components(html)
    html = clean_html_body_text_only(html)
    dest.write_text(html, encoding="utf-8")
    print(f"Gerado {dest}")

def build_pt_compliance():
    src = SITE_DIR / "modern-slavery-statement" / "index.html"
    dest_dir = SITE_DIR / "pt" / "modern-slavery-statement"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "index.html"
    
    html = src.read_text(encoding="utf-8")
    html = html.replace('<html lang="en">', '<html lang="pt-BR">')
    html = html.replace('<title>Modern Slavery Statement — HSN Labs</title>', '<title>Declaracao de Conformidade e Etica — HSN Labs</title>')
    
    html = html.replace('content="https://hsnlabs.ai/modern-slavery-statement"', 'content="https://hsnlabs.ai/pt/modern-slavery-statement/"')
    html = html.replace('content="https://hsnlabs.ai/modern-slavery-statement/"', 'content="https://hsnlabs.ai/pt/modern-slavery-statement/"')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/modern-slavery-statement">', '<link rel="canonical" href="https://hsnlabs.ai/pt/modern-slavery-statement/">')
    html = html.replace('<link rel="canonical" href="https://hsnlabs.ai/modern-slavery-statement/">', '<link rel="canonical" href="https://hsnlabs.ai/pt/modern-slavery-statement/">')
    
    hreflangs = '''  <link rel="alternate" hreflang="en" href="https://hsnlabs.ai/modern-slavery-statement/">
  <link rel="alternate" hreflang="pt-BR" href="https://hsnlabs.ai/pt/modern-slavery-statement/">
  <link rel="alternate" hreflang="x-default" href="https://hsnlabs.ai/modern-slavery-statement/">'''
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', r'\1\n' + hreflangs, html)
    
    old_nav_pattern = r'<div class="nav-menu" style="[^"]*">.*?</div>'
    new_nav = '''<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
        <a href="/pt/advisory" class="nav-link">Advisory</a>
        <a href="/blog/pt/" class="nav-link">Blog</a>
        <a href="/modern-slavery-statement/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
      </div>'''
    html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)
    
    html = html.replace('← Return to Overview', '← Voltar para Visao Geral')
    html = html.replace('href="/" class="back-link"', 'href="/pt/" class="back-link"')
    html = html.replace('<h1 class="display-title">Modern Slavery Statement</h1>', '<h1 class="display-title">Declaracao de Conformidade e Etica</h1>')
    html = html.replace('Financial Year 2026', 'Ano Fiscal de 2026')
    
    html = localize_common_pt_components(html)
    html = clean_html_body_text_only(html)
    dest.write_text(html, encoding="utf-8")
    print(f"Gerado {dest}")

if __name__ == "__main__":
    print("Atualizando cabeçalhos e metadados nas páginas em inglês...")
    update_english_page_headers()
    print("Gerando páginas em português...")
    build_pt_home()
    build_pt_bootcamp()
    build_pt_advisory()
    build_pt_mcp()
    build_pt_privacy_policy()
    build_pt_compliance()
    print("Concluído!")
