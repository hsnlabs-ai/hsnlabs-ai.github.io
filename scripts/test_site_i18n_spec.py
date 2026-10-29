#!/usr/bin/env python3
import sys
import re
from pathlib import Path

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")

PAGES = [
    {"id": "home", "pt": SITE_DIR / "index.html", "en": SITE_DIR / "en" / "index.html", "path_pt": "/", "path_en": "/en/"},
    {"id": "bootcamp", "pt": SITE_DIR / "bootcamp" / "index.html", "en": SITE_DIR / "en" / "bootcamp" / "index.html", "path_pt": "/bootcamp/", "path_en": "/en/bootcamp/"},
    {"id": "advisory", "pt": SITE_DIR / "advisory" / "index.html", "en": SITE_DIR / "en" / "advisory" / "index.html", "path_pt": "/advisory/", "path_en": "/en/advisory/"},
    {"id": "mcp", "pt": SITE_DIR / "mcp" / "index.html", "en": SITE_DIR / "en" / "mcp" / "index.html", "path_pt": "/mcp/", "path_en": "/en/mcp/"},
    {"id": "langchain", "pt": SITE_DIR / "langchain" / "index.html", "en": SITE_DIR / "en" / "langchain" / "index.html", "path_pt": "/langchain/", "path_en": "/en/langchain/"},
    {"id": "snowflake", "pt": SITE_DIR / "snowflake" / "index.html", "en": SITE_DIR / "en" / "snowflake" / "index.html", "path_pt": "/snowflake/", "path_en": "/en/snowflake/"},
    {"id": "databricks", "pt": SITE_DIR / "databricks" / "index.html", "en": SITE_DIR / "en" / "databricks" / "index.html", "path_pt": "/databricks/", "path_en": "/en/databricks/"},
    {"id": "braintrust", "pt": SITE_DIR / "braintrust" / "index.html", "en": SITE_DIR / "en" / "braintrust" / "index.html", "path_pt": "/braintrust/", "path_en": "/en/braintrust/"},
    {"id": "canvas", "pt": SITE_DIR / "canvas" / "index.html", "en": SITE_DIR / "en" / "canvas" / "index.html", "path_pt": "/canvas/", "path_en": "/en/canvas/"},
    {"id": "privacy", "pt": SITE_DIR / "privacy-policy" / "index.html", "en": SITE_DIR / "en" / "privacy-policy" / "index.html", "path_pt": "/privacy-policy/", "path_en": "/en/privacy-policy/"},
    {"id": "compliance", "pt": SITE_DIR / "modern-slavery-statement" / "index.html", "en": SITE_DIR / "en" / "modern-slavery-statement" / "index.html", "path_pt": "/modern-slavery-statement/", "path_en": "/en/modern-slavery-statement/"},
]

def test_gate_s1_structural_integrity():
    print("--- Gate S1: Integridade Estrutural ---")
    for item in PAGES:
        assert item["en"].exists(), f"ERRO: Pagina EN ausente: {item['en']}"
        assert item["pt"].exists(), f"ERRO: Pagina PT ausente: {item['pt']}"
        pt_content = item["pt"].read_text(encoding="utf-8")
        assert len(pt_content) > 500, f"ERRO: Pagina PT truncada: {item['pt']}"
        assert '<html lang="pt-BR">' in pt_content, f"ERRO: Atributo lang incorreto em {item['pt']}"
    print(f"PASS: Gate S1 Integridade Estrutural validada nas {len(PAGES)} rotas PT")

def test_gate_s2_zero_parentheses():
    print("--- Gate S2: Politica Zero Parenteses ---")
    for item in PAGES:
        pt_file = item["pt"]
        content = pt_file.read_text(encoding="utf-8")
        body_no_script = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'<style.*?</style>', '', body_no_script, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'style="[^"]*"', '', body_clean)
        
        text_nodes = re.findall(r'>([^<]+)<', body_clean)
        for t in text_nodes:
            stripped = t.strip()
            if not stripped:
                continue
            assert '(' not in stripped and ')' not in stripped, f"ERRO: Parentese encontrado em texto visivel de {pt_file}: {stripped}"
            
        titles = re.findall(r'<title>(.*?)</title>', body_clean)
        for title in titles:
            assert '(' not in title and ')' not in title, f"ERRO: Parentese encontrado em <title> de {pt_file}: {title}"
        descs = re.findall(r'<meta\s+name="description"\s+content="([^"]*)"', body_clean)
        for desc in descs:
            assert '(' not in desc and ')' not in desc, f"ERRO: Parentese encontrado em meta description de {pt_file}: {desc}"
    print("PASS: Gate S2 Invariante Zero Parenteses validado em todas as paginas PT")

def test_gate_s3_reciprocity():
    print("--- Gate S3: Reciprocidade de Hreflang e Canonicals ---")
    for item in PAGES:
        en_content = item["en"].read_text(encoding="utf-8")
        pt_content = item["pt"].read_text(encoding="utf-8")
        
        expected_can_en = f'https://hsnlabs.ai{item["path_en"]}'
        assert f'rel="canonical" href="{expected_can_en}"' in en_content or f'rel="canonical" href="{expected_can_en[:-1]}"' in en_content, f"Canonical EN invalido em {item['en']}"
        
        expected_can_pt = f'https://hsnlabs.ai{item["path_pt"]}'
        assert f'rel="canonical" href="{expected_can_pt}"' in pt_content or f'rel="canonical" href="{expected_can_pt[:-1]}"' in pt_content, f"Canonical PT invalido em {item['pt']}"
        
        assert f'hreflang="en" href="{expected_can_en}"' in pt_content, f"Hreflang en ausente em {item['pt']}"
        assert f'hreflang="pt-BR" href="{expected_can_pt}"' in pt_content, f"Hreflang pt-BR ausente em {item['pt']}"
        assert f'hreflang="x-default" href="{expected_can_pt}"' in pt_content, f"Hreflang x-default ausente em {item['pt']}"
    print(f"PASS: Gate S3 Reciprocidade Hreflang e Canonical validada nos {len(PAGES)} pares")

def test_gate_s4_language_isolation():
    print("--- Gate S4: Isolamento de Idioma ---")
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        nav_match = re.search(r'<div class="nav-menu"[^>]*>(.*?)</div>', pt_content, re.DOTALL)
        if nav_match:
            nav_html = nav_match.group(1)
            if 'Advisory' in nav_html:
                assert '/advisory' in nav_html and '/en/advisory' not in nav_html, f"Link de Advisory em {item['pt']} nao usa rota PT"
            if 'Playbooks' in nav_html:
                assert '/playbooks' in nav_html and '/en/playbooks' not in nav_html, f"Link de Playbooks em {item['pt']} nao usa rota PT"
            if 'Blog' in nav_html:
                assert '/blog/pt/' in nav_html, f"Link de Blog em {item['pt']} nao usa rota PT"
        header_match = re.search(r'<header[^>]*>(.*?)</header>', pt_content, re.DOTALL)
        header_html = header_match.group(1) if header_match else pt_content
        assert f'href="{item["path_en"]}"' in header_html or f'href="{item["path_en"][:-1]}"' in header_html or 'href="/"' in header_html, f"Seletor EN ausente em {item['pt']}"
    print("PASS: Gate S4 Isolamento de Idioma validado")

def test_gate_s5_asset_resolution():
    print("--- Gate S5: Resolucao de Assets ---")
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        assets = re.findall(r'(?:src|href)="/(assets/[^"\'\s>]+)"', pt_content)
        for asset_rel in assets:
            disk_path = SITE_DIR / asset_rel
            assert disk_path.exists(), f"ERRO: Asset inexistente referenciado em {item['pt']}: {disk_path}"
    print("PASS: Gate S5 Resolucao de Assets confirmada")

def test_gate_s6_forms_and_buttons():
    print("--- Gate S6: Localizacao de Formularios e Botoes PT ---")
    forbidden_en_strings = [
        'Select your role', 'Select annual revenue', 'Select primary system',
        '>Request Call<', '>Request Consultation<', '>Send Message<', '>Request Technical Scoping<',
        'placeholder="Your Name"', 'placeholder="Company Inc"'
    ]
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        for bad in forbidden_en_strings:
            assert bad not in pt_content, f"ERRO: String em ingles remanescente em {item['pt']}: {bad}"
    print("PASS: Gate S6 Localizacao de Formularios e Botoes validada")

def test_gate_s7_metadata_localization():
    print("--- Gate S7: Localizacao e Sincronia de Metadados Open Graph e Twitter ---")
    forbidden_en_meta = [
        "AI Agents That Don't Fail",
        "Boutique building resilient",
        "We build private, secure Model Context Protocol",
        "Discover how leading enterprises build",
        "Privacy Policy for hsnlabs",
        "Modern Slavery Statement for hsnlabs",
    ]
    for item in PAGES:
        for lang_key, path_key in [("en", "path_en"), ("pt", "path_pt")]:
            file_path = item[lang_key]
            content = file_path.read_text(encoding="utf-8")
            desc = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content)
            og_desc = re.search(r'<meta\s+property="og:description"\s+content="([^"]*)"', content)
            tw_desc = re.search(r'<meta\s+name="twitter:description"\s+content="([^"]*)"', content)
            og_url = re.search(r'<meta\s+property="og:url"\s+content="([^"]*)"', content)
            tw_url = re.search(r'<meta\s+name="twitter:url"\s+content="([^"]*)"', content)
            og_img = re.search(r'<meta\s+property="og:image"\s+content="([^"]*)"', content)
            tw_img = re.search(r'<meta\s+name="twitter:image"\s+content="([^"]*)"', content)

            assert desc and og_desc and tw_desc, f"ERRO: Meta description/OG/Twitter ausente em {file_path}"
            assert desc.group(1) == og_desc.group(1) == tw_desc.group(1), (
                f"ERRO: Divergencia entre meta description e og/twitter description em {file_path}:\n"
                f"  desc: {desc.group(1)}\n  og:desc: {og_desc.group(1)}"
            )
            expected_url = f"https://hsnlabs.ai{item[path_key]}"
            assert og_url and og_url.group(1) == expected_url, f"ERRO: og:url incorreto em {file_path}: {og_url.group(1) if og_url else None} != {expected_url}"
            assert tw_url and tw_url.group(1) == expected_url, f"ERRO: twitter:url incorreto em {file_path}: {tw_url.group(1) if tw_url else None} != {expected_url}"
            assert og_img and tw_img and og_img.group(1) == tw_img.group(1), f"ERRO: og:image != twitter:image em {file_path}"

            if lang_key == "pt":
                assert og_img.group(1).endswith("og-image-pt.png"), f"ERRO: Pagina PT {file_path} nao aponta para og-image-pt.png"
                for bad in forbidden_en_meta:
                    assert bad not in desc.group(1), f"ERRO: Meta description em ingles em {file_path}: {desc.group(1)}"
    print("PASS: Gate S7 Metadados Open Graph, Twitter e Meta Description 100% sincronizados e localizados")

def test_gate_s8_portuguese_accentuation():
    print("--- Gate S8: Acentuacao Grafica Obrigatoria em Portugues ---")
    unaccented_forbidden = [
        r'\badocao\b', r'\bestrategia\b', r'\boperacao\b', r'\boperacoes\b',
        r'\breducao\b', r'\bresponsavel\b', r'\banalisara\b', r'\brespondera\b',
        r'\bpolitica\b', r'\bdeclaracao\b', r'\blaboratorio\b', r'\bnavegacao\b',
        r'\bproducao\b', r'\bimplantacao\b',
        r'\bintegracao\b', r'\bvalidacao\b', r'\bgovernanca\b', r'\bperimetro\b',
        r'\bcriticos\b', r'\bautonomos\b', r'\bnegocio\b', r'\betica\b',
        r'\bsenior\b', r'\bqualificacao\b', r'\bcriterios\b',
        r'\bmetodo\b', r'\bprototipo\b', r'\bhomologacao\b', r'\breplicas\b',
        r'\bcodigo\b', r'\bconexoes\b', r'\bseguranca\b', r'\bextracao\b',
        r'\bmetricas\b', r'\btecnica\b', r'\btecnico\b', r'\bminima\b',
        r'\bmilhoes\b', r'\borcamento\b', r'\bcirurgicas\b', r'\binformacao\b',
        r'\binscricao\b', r'\bvoce\b', r'\bate\b', r'\bvisao\b', r'\batualizacao\b',
        r'\bsolicitacao\b', r'\brevisara\b', r'\balucinacao\b', r'\balucinacoes\b',
        r'\bexposicao\b', r'\bexecucao\b', r'\bfuncao\b', r'\bpermissao\b',
        r'\balcadas\b', r'\baprovacao\b', r'\bsupervisao\b', r'\bgenericos\b',
        r'\bacao\b', r'\bacoes\b', r'\bconstruimos\b', r'\bdeterministicos\b',
        r'\bdeterministicas\b', r'\bmaquinas\b', r'\bavaliacao\b', r'\bcontinuas\b',
        r'\bmultiplos\b', r'\bhibridos\b', r'\bproprietarias\b', r'\bnivel\b'
    ]
    pattern = re.compile('|'.join(unaccented_forbidden), re.IGNORECASE)
    
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        clean = re.sub(r'<script.*?</script>', '', pt_content, flags=re.DOTALL | re.IGNORECASE)
        clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL | re.IGNORECASE)
        clean = re.sub(r'<svg.*?</svg>', '', clean, flags=re.DOTALL | re.IGNORECASE)
        
        text_nodes = re.findall(r'>([^<]+)<', clean)
        titles = re.findall(r'<title>(.*?)</title>', clean)
        meta_descs = re.findall(r'<meta\s+name="description"\s+content="([^"]*)"', clean)
        og_titles = re.findall(r'property="og:title"\s+content="([^"]*)"', clean)
        og_descs = re.findall(r'property="og:description"\s+content="([^"]*)"', clean)
        
        all_strings = text_nodes + titles + meta_descs + og_titles + og_descs
        for s in all_strings:
            s_clean = s.strip()
            if not s_clean or 'clamp(' in s_clean:
                continue
            m = pattern.search(s_clean)
            assert not m, f"ERRO: Palavra sem acentuacao encontrada em {item['pt']}: '{m.group(0)}' no trecho '{s_clean}'"
    print("PASS: Gate S8 Acentuacao Grafica Obrigatoria validada em todas as 9 rotas PT")

def test_gate_s9_footer_consistency():
    print("--- Gate S9: Paridade Estrita de Rodape (Footer Invariant) ---")
    footer_en_file = SITE_DIR / "components" / "footer_en.html"
    footer_pt_file = SITE_DIR / "components" / "footer_pt.html"
    assert footer_en_file.exists(), f"ERRO: Componente de rodape EN ausente: {footer_en_file}"
    assert footer_pt_file.exists(), f"ERRO: Componente de rodape PT ausente: {footer_pt_file}"
    
    canonical_en = re.sub(r'\s+', ' ', footer_en_file.read_text(encoding="utf-8").strip())
    canonical_pt = re.sub(r'\s+', ' ', footer_pt_file.read_text(encoding="utf-8").strip())
    
    en_pages = [
        SITE_DIR / "en" / "index.html",
        SITE_DIR / "en" / "bootcamp" / "index.html",
        SITE_DIR / "en" / "advisory" / "index.html",
        SITE_DIR / "en" / "mcp" / "index.html",
        SITE_DIR / "en" / "langchain" / "index.html",
        SITE_DIR / "en" / "snowflake" / "index.html",
        SITE_DIR / "en" / "databricks" / "index.html",
        SITE_DIR / "en" / "braintrust" / "index.html",
        SITE_DIR / "en" / "canvas" / "index.html",
        SITE_DIR / "en" / "privacy-policy" / "index.html",
        SITE_DIR / "en" / "modern-slavery-statement" / "index.html",
        SITE_DIR / "404.html",
    ]
    
    pt_pages = [
        SITE_DIR / "index.html",
        SITE_DIR / "bootcamp" / "index.html",
        SITE_DIR / "advisory" / "index.html",
        SITE_DIR / "mcp" / "index.html",
        SITE_DIR / "langchain" / "index.html",
        SITE_DIR / "snowflake" / "index.html",
        SITE_DIR / "databricks" / "index.html",
        SITE_DIR / "braintrust" / "index.html",
        SITE_DIR / "canvas" / "index.html",
        SITE_DIR / "privacy-policy" / "index.html",
        SITE_DIR / "modern-slavery-statement" / "index.html",
    ]
    
    for page in en_pages:
        assert page.exists(), f"ERRO: Pagina EN inexistente: {page}"
        content = page.read_text(encoding="utf-8")
        m = re.search(r'<footer class="site-footer">.*?</footer>', content, re.DOTALL)
        assert m, f"ERRO: Tag de rodape ausente em {page}"
        page_footer = re.sub(r'\s+', ' ', m.group(0).strip())
        assert page_footer == canonical_en, f"ERRO: Inconsistencia de rodape EN em {page.name}"
        assert "[Agentes] x [a Gente]" in m.group(0), f"ERRO: Newsletter ausente em {page}"
        assert "1,600+" in m.group(0) and "subscribers" in m.group(0), f"ERRO: Contagem de inscritos ausente em {page}"
        assert len(re.findall(r'footer-social-icon', m.group(0))) == 8, f"ERRO: Icones sociais incompletos em {page}"
        
    for page in pt_pages:
        assert page.exists(), f"ERRO: Pagina PT inexistente: {page}"
        content = page.read_text(encoding="utf-8")
        m = re.search(r'<footer class="site-footer">.*?</footer>', content, re.DOTALL)
        assert m, f"ERRO: Tag de rodape ausente em {page}"
        page_footer = re.sub(r'\s+', ' ', m.group(0).strip())
        assert page_footer == canonical_pt, f"ERRO: Inconsistencia de rodape PT em {page.name}"
        assert "[Agentes] x [a Gente]" in m.group(0), f"ERRO: Newsletter ausente em {page}"
        assert "1.600+" in m.group(0) and "assinantes" in m.group(0), f"ERRO: Contagem de inscritos ausente em {page}"
        assert len(re.findall(r'footer-social-icon', m.group(0))) == 8, f"ERRO: Icones sociais incompletos em {page}"
        assert "Escritório" in m.group(0) and "Navegação" in m.group(0), f"ERRO: Titulos Escritorio/Navegacao sem acentuacao em {page}"
        assert "Parceiros" in m.group(0) and "Siga em Contato" in m.group(0), f"ERRO: Colunas Parceiros/Siga em Contato ausentes em {page}"
        assert "Laboratório" in m.group(0), f"ERRO: Laboratorio sem acentuacao em {page}"
        assert "Política de Privacidade" in m.group(0), f"ERRO: Politica sem acentuacao em {page}"
        assert "Declaração de Conformidade" in m.group(0), f"ERRO: Declaracao sem acentuacao em {page}"
        
    print(f"PASS: Gate S9 Paridade Estrita de Rodape validada nas {len(en_pages)} rotas EN e {len(pt_pages)} rotas PT")

def test_gate_s10_language_leak_detection():
    print("--- Gate S10: Detector de Vazamento de Idioma (Language Leak) ---")
    en_leaks_forbidden = [
        "Agentic Engineering Adoption",
        "Operational transition to enterprise agents without disrupting legacy systems",
        "Why Agents Fail",
        "Most enterprise AI agents break when exposed to messy company data",
        "Regulated Enterprise Verticals",
        "Talk to our architecture team to see if your systems are ready",
    ]
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        for leak in en_leaks_forbidden:
            assert leak not in pt_content, f"ERRO: Vazamento de ingles detectado em {item['pt']}: '{leak}'"
    print("PASS: Gate S10 Nenhum vazamento de idioma detectado em rotas PT")

def test_gate_s11_section_parity():
    print("--- Gate S11: Paridade Estrutural de Secoes (Section Parity) ---")
    pt_content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
    en_content = (SITE_DIR / "en" / "index.html").read_text(encoding="utf-8")
    
    en_sections = re.findall(r'<section[^>]*\sid="([^"]+)"', en_content)
    pt_sections = re.findall(r'<section[^>]*\sid="([^"]+)"', pt_content)
    
    assert en_sections == pt_sections, f"ERRO: Descompasso de secoes entre EN e PT!\nEN: {en_sections}\nPT: {pt_sections}"
    print(f"PASS: Gate S11 Paridade de secoes validada com sucesso: {en_sections}")

def test_gate_s12_origami_hero_notes():
    print("--- Gate S12: Invariante de Notas Origami Minimalistas na Hero ---")
    pt_content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
    en_content = (SITE_DIR / "en" / "index.html").read_text(encoding="utf-8")

    for label, content, exp_left, exp_right in [
        ("PT", pt_content, "Agentes de backoffice, dados e automação interna.", "Agentes de frontoffice em voz e texto com o cliente."),
        ("EN", en_content, "Back-office agents for data and internal automation.", "Front-office voice and text agents for end customers."),
    ]:
        assert "hero-stage-flank" in content, f"ERRO [{label}]: hero-stage-flank ausente"
        assert "hero-headline-stage" in content, f"ERRO [{label}]: hero-headline-stage ausente"
        assert "hero-origami-pair" in content, f"ERRO [{label}]: hero-origami-pair ausente"
        assert "curved-arrow-left" in content and "curved-arrow-right" in content, f"ERRO [{label}]: setas curvas ausentes"
        assert "flank-note-left" in content and "flank-note-right" in content, f"ERRO [{label}]: notas laterais ausentes"
        assert "mobile-arrows-bar" in content, f"ERRO [{label}]: setas mobile ausentes"
        assert "note-pin-line" not in content, f"ERRO [{label}]: traco azul proibido presente"
        assert "note-eyebrow" not in content, f"ERRO [{label}]: terceira variacao de fonte proibida presente"
        assert content.count('<div class="note-heading">Headless Agents</div>') == 1, f"ERRO [{label}]: esperado 1 titulo Headless Agents unificado no DOM"
        assert content.count('<div class="note-heading">Surface Agents</div>') == 1, f"ERRO [{label}]: esperado 1 titulo Surface Agents unificado no DOM"
        assert exp_left in content, f"ERRO [{label}]: descricao esquerda incorreta"
        assert exp_right in content, f"ERRO [{label}]: descricao direita incorreta"
    print("PASS: Gate S12 Notas Origami Minimalistas validadas em PT e EN")

if __name__ == "__main__":
    print("=== INICIANDO EXECUCAO DA SUITE SITE I18N ===")
    test_gate_s1_structural_integrity()
    test_gate_s2_zero_parentheses()
    test_gate_s3_reciprocity()
    test_gate_s4_language_isolation()
    test_gate_s5_asset_resolution()
    test_gate_s6_forms_and_buttons()
    test_gate_s7_metadata_localization()
    test_gate_s8_portuguese_accentuation()
    test_gate_s9_footer_consistency()
    test_gate_s10_language_leak_detection()
    test_gate_s11_section_parity()
    test_gate_s12_origami_hero_notes()
    print("=== TODAS AS 12 ASSERCOES DO SITE I18N PASSARAM COM SUCESSO ===")
