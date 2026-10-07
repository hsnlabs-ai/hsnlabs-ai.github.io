#!/usr/bin/env python3
"""
scripts/sync_footer.py — HSN Labs Official Footer Synchronization Engine.

Maintains strict parity across all 15 website routes by treating
components/footer_en.html and components/footer_pt.html as the single source of truth.
"""

import re
from pathlib import Path

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")
FOOTER_EN = (SITE_DIR / "components" / "footer_en.html").read_text(encoding="utf-8").strip()
FOOTER_PT = (SITE_DIR / "components" / "footer_pt.html").read_text(encoding="utf-8").strip()

EN_PAGES = [
    SITE_DIR / "index.html",
    SITE_DIR / "bootcamp" / "index.html",
    SITE_DIR / "advisory" / "index.html",
    SITE_DIR / "mcp" / "index.html",
    SITE_DIR / "privacy-policy" / "index.html",
    SITE_DIR / "modern-slavery-statement" / "index.html",
    SITE_DIR / "404.html",
]

PT_PAGES = [
    SITE_DIR / "pt" / "index.html",
    SITE_DIR / "pt" / "bootcamp" / "index.html",
    SITE_DIR / "pt" / "advisory" / "index.html",
    SITE_DIR / "pt" / "mcp" / "index.html",
    SITE_DIR / "pt" / "privacy-policy" / "index.html",
    SITE_DIR / "pt" / "modern-slavery-statement" / "index.html",
]

MCP_STANDARD_FOOTER_CSS = '''    /* FOOTER */
    .site-footer {
      background: var(--canvas);
      border-top: 1px solid var(--hairline);
      padding: 72px 0 44px 0;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1.2fr 1fr 1.6fr;
      gap: 48px;
      margin-bottom: 56px;
      align-items: start;
    }

    .footer-col-title {
      font-size: 0.78rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--ink);
      margin-bottom: 16px;
    }

    .footer-nav {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 0;
      margin: 0;
    }

    .footer-nav a {
      color: var(--muted);
      text-decoration: none;
      font-size: 0.88rem;
      transition: color 0.2s ease;
    }

    .footer-nav a:hover {
      color: var(--ink);
    }

    .footer-bottom {
      border-top: 1px solid var(--hairline);
      padding-top: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      font-size: 0.82rem;
      color: var(--muted);
      font-family: var(--font-sans);
    }

    .footer-bottom-links {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .footer-bottom-links a {
      color: var(--muted);
      text-decoration: none;
      font-size: 0.82rem;
      font-family: var(--font-sans);
      transition: color 0.2s ease;
    }

    .footer-bottom-links a:hover {
      color: var(--ink);
    }

    .footer-social-row {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .footer-social-icon {
      color: var(--muted);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      border-radius: 8px;
      transition: color 0.2s ease, background 0.2s ease, transform 0.2s ease;
    }

    .footer-social-icon:hover {
      color: var(--ink);
      background: var(--surface-card);
      transform: translateY(-1px);
    }'''

def sync_page_footer(file_path: Path, canonical_footer: str) -> bool:
    if not file_path.exists():
        print(f"WARN: Arquivo nao encontrado: {file_path}")
        return False
    
    content = file_path.read_text(encoding="utf-8")
    
    # 1. Replace <footer class="site-footer">...</footer>
    new_content, count = re.subn(
        r'<footer class="site-footer">.*?</footer>',
        canonical_footer,
        content,
        flags=re.DOTALL
    )
    if count == 0:
        print(f"ERRO: Nenhuma tag <footer class=\"site-footer\"> encontrada em {file_path}")
        return False
        
    # 2. Fix legacy MCP footer CSS if needed
    if "mcp" in str(file_path):
        if ".footer-bottom-links" not in new_content:
            mcp_footer_css_pattern = r'/\*\s*FOOTER\s*\*/[\s\S]*?\.footer-bottom\s*\{[^}]*\}'
            if re.search(mcp_footer_css_pattern, new_content):
                new_content = re.sub(mcp_footer_css_pattern, MCP_STANDARD_FOOTER_CSS, new_content)
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"OK: Atualizado {file_path.relative_to(SITE_DIR)}")
        return True
    else:
        print(f"SKIP (ja atualizado): {file_path.relative_to(SITE_DIR)}")
        return False

def main():
    print("=== SINCRONIZANDO RODAPES HSN LABS ===")
    print("\n--- Paginas em Ingles (EN) ---")
    en_updated = sum(sync_page_footer(p, FOOTER_EN) for p in EN_PAGES)
    
    print("\n--- Paginas em Portugues (PT) ---")
    pt_updated = sum(sync_page_footer(p, FOOTER_PT) for p in PT_PAGES)
    
    print(f"\nConcluido! {en_updated} paginas EN e {pt_updated} paginas PT modificadas.")

if __name__ == "__main__":
    main()
