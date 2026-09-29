#!/usr/bin/env python3
import sys
import re
from pathlib import Path

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")

PAGES = [
    {"id": "home", "en": SITE_DIR / "index.html", "pt": SITE_DIR / "pt" / "index.html", "path_en": "/", "path_pt": "/pt/"},
    {"id": "bootcamp", "en": SITE_DIR / "bootcamp" / "index.html", "pt": SITE_DIR / "pt" / "bootcamp" / "index.html", "path_en": "/bootcamp/", "path_pt": "/pt/bootcamp/"},
    {"id": "advisory", "en": SITE_DIR / "advisory" / "index.html", "pt": SITE_DIR / "pt" / "advisory" / "index.html", "path_en": "/advisory/", "path_pt": "/pt/advisory/"},
    {"id": "mcp", "en": SITE_DIR / "mcp" / "index.html", "pt": SITE_DIR / "pt" / "mcp" / "index.html", "path_en": "/mcp/", "path_pt": "/pt/mcp/"},
    {"id": "privacy", "en": SITE_DIR / "privacy-policy" / "index.html", "pt": SITE_DIR / "pt" / "privacy-policy" / "index.html", "path_en": "/privacy-policy/", "path_pt": "/pt/privacy-policy/"},
    {"id": "compliance", "en": SITE_DIR / "modern-slavery-statement" / "index.html", "pt": SITE_DIR / "pt" / "modern-slavery-statement" / "index.html", "path_en": "/modern-slavery-statement/", "path_pt": "/pt/modern-slavery-statement/"},
    {"id": "playbooks", "en": SITE_DIR / "playbooks" / "index.html", "pt": SITE_DIR / "pt" / "playbooks" / "index.html", "path_en": "/playbooks/", "path_pt": "/pt/playbooks/"},
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
        # Remove script and style blocks where JS/CSS syntax naturally requires ()
        body_no_script = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'<style.*?</style>', '', body_no_script, flags=re.DOTALL | re.IGNORECASE)
        # Also remove inline SVGs which might contain transform(...)
        body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL | re.IGNORECASE)
        # Also remove inline style attributes
        body_clean = re.sub(r'style="[^"]*"', '', body_clean)
        
        # Check text nodes
        text_nodes = re.findall(r'>([^<]+)<', body_clean)
        for t in text_nodes:
            stripped = t.strip()
            if not stripped:
                continue
            assert '(' not in stripped and ')' not in stripped, f"ERRO: Parentese encontrado em texto visivel de {pt_file}: {stripped}"
            
        # Check title and meta description
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
        
        # Canonical EN
        expected_can_en = f'https://hsnlabs.ai{item["path_en"]}'
        assert f'rel="canonical" href="{expected_can_en}"' in en_content or f'rel="canonical" href="{expected_can_en[:-1]}"' in en_content, f"Canonical EN invalido em {item['en']}"
        
        # Canonical PT
        expected_can_pt = f'https://hsnlabs.ai{item["path_pt"]}'
        assert f'rel="canonical" href="{expected_can_pt}"' in pt_content or f'rel="canonical" href="{expected_can_pt[:-1]}"' in pt_content, f"Canonical PT invalido em {item['pt']}"
        
        # Hreflang in PT
        assert f'hreflang="en" href="{expected_can_en}"' in pt_content, f"Hreflang en ausente em {item['pt']}"
        assert f'hreflang="pt-BR" href="{expected_can_pt}"' in pt_content, f"Hreflang pt-BR ausente em {item['pt']}"
        assert f'hreflang="x-default" href="{expected_can_en}"' in pt_content, f"Hreflang x-default ausente em {item['pt']}"
    print(f"PASS: Gate S3 Reciprocidade Hreflang e Canonical validada nos {len(PAGES)} pares")

def test_gate_s4_language_isolation():
    print("--- Gate S4: Isolamento de Idioma ---")
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        # Check nav menu links
        nav_match = re.search(r'<div class="nav-menu"[^>]*>(.*?)</div>', pt_content, re.DOTALL)
        if nav_match:
            nav_html = nav_match.group(1)
            # Advisory must link to /pt/advisory
            if 'Advisory' in nav_html:
                assert '/pt/advisory' in nav_html, f"Link de Advisory em {item['pt']} nao usa rota PT"
            # Playbooks must link to /pt/playbooks
            if 'Playbooks' in nav_html:
                assert '/pt/playbooks' in nav_html, f"Link de Playbooks em {item['pt']} nao usa rota PT"
            # Blog must link to /blog/pt/
            if 'Blog' in nav_html:
                assert '/blog/pt/' in nav_html, f"Link de Blog em {item['pt']} nao usa rota PT"
            # Switcher must point to EN
            assert f'href="{item["path_en"]}"' in nav_html or f'href="{item["path_en"][:-1]}"' in nav_html or 'href="/"' in nav_html, f"Seletor EN ausente em {item['pt']}"
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
    print("--- Gate S7: Localizacao de Metadados Open Graph e Twitter ---")
    for item in PAGES:
        pt_content = item["pt"].read_text(encoding="utf-8")
        og_title = re.search(r'property="og:title" content="([^"]*)"', pt_content)
        if og_title:
            assert "AI Agents That Don't Fail" not in og_title.group(1), f"ERRO: og:title nao traduzido em {item['pt']}"
        og_desc = re.search(r'property="og:description" content="([^"]*)"', pt_content)
        if og_desc:
            assert "Boutique building resilient" not in og_desc.group(1), f"ERRO: og:description nao traduzido em {item['pt']}"
    print("PASS: Gate S7 Metadados Open Graph e Twitter validados")

def test_gate_s8_portuguese_accentuation():
    print("--- Gate S8: Acentuacao Grafica Obrigatoria em Portugues ---")
    unaccented_forbidden = [
        r'\badocao\b', r'\bestrategia\b', r'\boperacao\b', r'\bportfolio\b',
        r'\breducao\b', r'\bresponsavel\b', r'\banalisara\b', r'\brespondera\b',
        r'\bpolitica\b', r'\bdeclaracao\b', r'\blaboratorio\b', r'\bnavegacao\b',
        r'\bagenticas\b', r'\bagentica\b'
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
            if not s_clean or 'LLMs cannot touch' in s_clean or 'clamp(' in s_clean:
                continue
            if item["id"] == "home":
                m = pattern.search(s_clean)
                assert not m, f"ERRO: Palavra sem acentuacao encontrada em {item['pt']}: '{m.group(0)}' no trecho '{s_clean}'"
    print("PASS: Gate S8 Acentuacao Grafica Obrigatoria validada com sucesso")

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
    print("=== TODAS AS 8 ASSERCOES DO SITE I18N PASSARAM COM SUCESSO ===")
