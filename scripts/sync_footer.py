#!/usr/bin/env python3
"""
scripts/sync_footer.py — hsnlabs Official Footer Synchronization Engine.

Maintains strict parity across all website routes by treating
components/footer_en.html and components/footer_pt.html as the single source of truth,
and synchronizing the 5-column editorial footer CSS across all pages.
"""

import re
from pathlib import Path

SITE_DIR = Path("/Users/hugosoares/site_hsn_labs")
FOOTER_EN = (SITE_DIR / "components" / "footer_en.html").read_text(encoding="utf-8").strip()
FOOTER_PT = (SITE_DIR / "components" / "footer_pt.html").read_text(encoding="utf-8").strip()

EN_PAGES = [
    SITE_DIR / "en" / "index.html",
    SITE_DIR / "en" / "bootcamp" / "index.html",
    SITE_DIR / "en" / "advisory" / "index.html",
    SITE_DIR / "en" / "mcp" / "index.html",
    SITE_DIR / "en" / "langchain" / "index.html",
    SITE_DIR / "en" / "snowflake" / "index.html",
    SITE_DIR / "en" / "braintrust" / "index.html",
    SITE_DIR / "en" / "portfolio" / "index.html",
    SITE_DIR / "en" / "privacy-policy" / "index.html",
    SITE_DIR / "en" / "modern-slavery-statement" / "index.html",
    SITE_DIR / "404.html",
]

PT_PAGES = [
    SITE_DIR / "index.html",
    SITE_DIR / "bootcamp" / "index.html",
    SITE_DIR / "advisory" / "index.html",
    SITE_DIR / "mcp" / "index.html",
    SITE_DIR / "langchain" / "index.html",
    SITE_DIR / "snowflake" / "index.html",
    SITE_DIR / "braintrust" / "index.html",
    SITE_DIR / "portfolio" / "index.html",
    SITE_DIR / "canvas" / "index.html",
    SITE_DIR / "en" / "canvas" / "index.html",
    SITE_DIR / "privacy-policy" / "index.html",
    SITE_DIR / "modern-slavery-statement" / "index.html",
    SITE_DIR / "agentic_pilot_canvas_v0.4.html",
]

CANONICAL_FOOTER_CSS = """    /* FOOTER */
    .site-footer {
      background: var(--canvas);
      border-top: 1px solid var(--hairline);
      padding: 64px 0 36px 0;
      position: relative;
      z-index: 2;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.45fr) minmax(0, 0.95fr) minmax(0, 1.18fr) minmax(0, 1.12fr) minmax(0, 1.95fr);
      gap: 32px;
      margin-bottom: 48px;
      align-items: start;
    }

    .footer-col-title {
      font-size: 0.74rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: var(--ink);
      margin-bottom: 16px;
      white-space: nowrap;
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
      font-size: 0.86rem;
      line-height: 1.35;
      transition: color 0.15s ease;
      display: inline-block;
      white-space: nowrap;
    }

    .footer-nav a:hover {
      color: var(--ink);
    }

    .footer-bottom {
      border-top: 1px solid var(--hairline);
      padding-top: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      font-size: 0.82rem;
      color: var(--muted);
      font-family: var(--font-sans);
    }

    .footer-bottom-left {
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    .footer-bottom-sep {
      width: 1px;
      height: 14px;
      background: var(--hairline-strong);
      flex-shrink: 0;
    }

    .footer-bottom-links {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .footer-bottom-links a {
      color: var(--muted);
      text-decoration: none;
      font-size: 0.82rem;
      font-family: var(--font-sans);
      transition: color 0.15s ease;
    }

    .footer-bottom-links a:hover {
      color: var(--ink);
    }

    .footer-social-row {
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: nowrap;
    }

    .footer-social-icon {
      color: var(--muted);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 34px;
      height: 34px;
      border-radius: 0;
      border: 1px solid transparent;
      transition: color 0.15s ease, background 0.15s ease, border-color 0.15s ease;
      flex-shrink: 0;
    }

    .footer-social-icon:hover {
      color: var(--ink);
      background: var(--surface-card);
      border-color: var(--hairline-strong);
    }

    @media (max-width: 980px) {
      .footer-grid {
        grid-template-columns: 1fr 1fr;
        gap: 32px;
      }
      .footer-col-brand,
      .footer-col-subscribe {
        grid-column: 1 / -1;
      }
      .footer-bottom {
        flex-direction: column;
        align-items: flex-start;
        gap: 18px;
      }
    }

    @media (max-width: 640px) {
      html, body {
        overflow-x: hidden !important;
        max-width: 100vw !important;
      }
      .header-github-link {
        display: none !important;
      }
      .site-footer {
        padding: 48px 0 32px 0;
      }
      .footer-grid {
        grid-template-columns: 1.08fr 0.92fr !important;
        gap: 26px 16px !important;
        margin-bottom: 32px;
      }
      .footer-col-brand,
      .footer-col-office,
      .footer-col-subscribe {
        grid-column: 1 / -1 !important;
      }
      .footer-nav a {
        white-space: normal;
        font-size: 0.82rem;
        line-height: 1.35;
      }
      .footer-newsletter-form input[type="email"] {
        font-size: 16px !important;
      }
      .footer-bottom-left {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
      }
      .footer-bottom-sep {
        display: none;
      }
      .footer-bottom-links {
        flex-wrap: wrap;
        gap: 14px;
      }
      .footer-social-row {
        flex-wrap: nowrap;
        gap: 3px;
      }
      .footer-social-icon {
        width: 34px;
        height: 34px;
      }
    }
    @media (max-width: 355px) {
      .footer-social-row {
        flex-wrap: wrap;
      }
    }
    /* END FOOTER */"""


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
        flags=re.DOTALL,
    )
    if count == 0:
        print(f'ERRO: Nenhuma tag <footer class="site-footer"> encontrada em {file_path}')
        return False

    # 2. Replace primary footer CSS block in <style> (including any previously injected media blocks)
    css_patterns = [
        r'[ \t]*/\*\s*FOOTER\s*\*/[\s\S]*?/\*\s*END FOOTER\s*\*/',
        r'[ \t]*/\*\s*(?:FOOTER|RODAPÉ|Site Footer Styles)\s*\*/[\s\S]*?(?:\s*@media\s*\(max-width:\s*980px\)[\s\S]*?\.footer-social-row\s*\{\s*flex-wrap:\s*wrap;\s*gap:\s*4px;\s*\}\s*\})+',
        r'[ \t]*/\*\s*(?:FOOTER|RODAPÉ|Site Footer Styles)\s*\*/[\s\S]*?\.footer-social-icon:hover\s*\{[^}]*\}',
        r'[ \t]*/\*\s*(?:FOOTER|RODAPÉ|Site Footer Styles)\s*\*/[\s\S]*?\.footer-bottom-links a:hover\s*\{[^}]*\}',
    ]
    replaced_css = False
    for pat in css_patterns:
        if re.search(pat, new_content):
            new_content = re.sub(pat, CANONICAL_FOOTER_CSS, new_content, count=1)
            replaced_css = True
            break

    if not replaced_css:
        print(f"WARN: Bloco CSS de footer nao localizado por padrao em {file_path}")

    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"OK: Atualizado {file_path.relative_to(SITE_DIR)}")
        return True
    else:
        print(f"SKIP (ja atualizado): {file_path.relative_to(SITE_DIR)}")
        return False


def main():
    print("=== SINCRONIZANDO RODAPES hsnlabs ===")
    print("\n--- Paginas em Ingles (EN) ---")
    en_updated = sum(sync_page_footer(p, FOOTER_EN) for p in EN_PAGES)

    print("\n--- Paginas em Portugues (PT) ---")
    pt_updated = sum(sync_page_footer(p, FOOTER_PT) for p in PT_PAGES)

    print(f"\nConcluido! {en_updated} paginas EN e {pt_updated} paginas PT modificadas.")


if __name__ == "__main__":
    main()
