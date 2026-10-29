# hsnlabs — Official Website Repository

Official production repository for the **hsnlabs** (`https://hsnlabs.ai`) corporate website.

**hsnlabs** is an enterprise agentic engineering boutique driving **Agentic Engineering Adoption** (`Adoção de Engenharia Agentica`) across the complete Agentic Development Life Cycle (ADLC): executable business ontologies, zero-trust infrastructure, stateful orchestration, and continuous evaluation for both **Headless Agents** (backoffice, data, and internal process automation) and **Surface Agents** (frontoffice real-time voice and text interfaces).

---

## 1. System & Routing Architecture

The website is engineered as a zero-dependency, 100/100 Lighthouse bilingual static application hosted on GitHub Pages with machine-readable Markdown twins (`.md`) and `llms.txt` for AI crawlers and agents.

### Dual-Track Bilingual Routing
* **Primary Portuguese (`pt-BR`) at Root:** `/`, `/bootcamp/`, `/advisory/`, `/mcp/`, `/langchain/`, `/snowflake/`, `/databricks/`, `/braintrust/`, `/canvas/`, `/privacy-policy/`, `/modern-slavery-statement/`.
* **English Mirror (`en`) under `/en/`:** `/en/`, `/en/bootcamp/`, `/en/advisory/`, `/en/mcp/`, `/en/langchain/`, `/en/snowflake/`, `/en/databricks/`, `/en/braintrust/`, `/en/canvas/`, `/en/privacy-policy/`, `/en/modern-slavery-statement/`.
* **Blog Reverse-Proxy (`/blog/` & `/blog/pt/`):** Hosted in the dedicated `hsnlabs-ai/blog` repository (`/Users/hugosoares/blog_hsn_labs`).

### Home Page Architecture
1. **Header (`.header-nav`):** Sticky translucent navbar with horizontal lockup, navigation links (`Advisory`, `Blog`), GitHub link, `EN · PT` interpunct language switcher, Example 01 blue arrow (`.bp-arrow-header`), and primary CTA (`Conhecer o Agentic Bootcamp™` / `Explore Agentic Bootcamp™`).
2. **Hero Section (`.hero-section`):** Interactive 90-degree cyan water emblem with origami carp, `Adoção de Engenharia Agentica.` display headline flanked by tactile origami paper notes (`Headless Agents` and `Surface Agents`) connected via symmetrical Example 01 blue dashed curved arrows, two-sentence tagline with US$ 5,000 ecosystem credits callout, dual CTAs (`Agentic Bootcamp™` with `.bp-arrow-cta` and `Agentic Canvas™`), and 9-logo Client Portfolio Strip.
3. **Market Reality & Field Documentary Strip (`#market-reality`):** S&P Global (`46%`) and Lucidworks (`83%`) empirical benchmark callout paired with a 3-column original-color documentary strip (`01 · Alinhamento Arquitetural`, `02 · Imersão em Bancada`, `03 · Code to Spec`) connected underneath by belly-down Example 01 blue dashed bridges (`.bp-bridge-12`, `.bp-bridge-23`).
4. **Services Section (`#services` — "Por que agentes falham"):** 4-card Bento grid with cyan `.post-it-badge` numbers `1` to `4` connected via responsive Example 01 blue dashed arches (`.bp-bento-12`, `.bp-bento-23`, and `.bp-bento-34` anchored inside `.card-bento-wide`), interactive 12-component Enterprise Agentic Architecture blueprint viewport, and localized `.sr-only` accessibility specification.
5. **Editorial Insights Section (`#editorial` — "Para ler antes de decidir."):** 3 canonical Spoke essay cards (`Falhas Reais`, `Engenharia Agentica`, `Futuro do Trabalho`).
6. **Contact Section (`#contact`) & Founder Callout:** `.hero-founder-callout` (`max-width: 860px`, fixed `278px` identity column for 10s rotating photo/prompt, `LangChain`, `Snowflake`, and `Databricks` credentials, and `.bp-arrow-header` + `Iniciar Conversa`) positioned directly above the qualification scoping form (`#contactForm` with `.bp-arrow-cta` + `Enviar Mensagem`).
7. **Canonical Footer (`.site-footer`):** 5-column layout with corporate email capture and `[Agentes] x [a Gente]` LinkedIn newsletter module, managed via `components/footer_pt.html` and `components/footer_en.html`.

---

## 2. Automation & Verification Scripts

* `python3 scripts/test_site_i18n_spec.py` — Runs the **12 bilingual specification gates** (structural integrity, zero-parentheses, hreflang/canonical reciprocity, language isolation, asset resolution, form localization, Open Graph/Twitter tri-sync, mandatory PT diacritics, verbatim footer parity, language leak detection, section parity, and Hero Origami + Example 01 Blue Arrow System invariants).
* `python3 scripts/sync_footer.py` — Synchronizes canonical PT and EN footers across all 24 HTML pages.
* `python3 scripts/render_architecture_png.py` — Exports the vector blueprint from `architecture.html` to `assets/diagrams/hsn_labs_agentic_architecture.png` and `.webp` (`2880x1620`).
* `python3 scripts/sync_sitemap.py` — Generates `sitemap.xml` from `i18n/routes-map.json`.
* `python3 scripts/setup_apollo_and_m2m.py` — Synchronizes deferred Apollo tracking and generates `.md` M2M twin files for all 26 routes.
* `python3 scripts/update_og.py` — Regenerates `assets/brand/og-image.png` and `assets/brand/og-image-pt.png`.
