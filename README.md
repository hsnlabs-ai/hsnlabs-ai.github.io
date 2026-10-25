# hsnlabs — Official Website Repository

Official production repository for the **hsnlabs** (`https://hsnlabs.ai`) corporate website.

**hsnlabs** is a Forward Deployed Engineering boutique solving why enterprise AI agents fail in production across the complete Agentic Development Life Cycle (ADLC): executable business ontologies, zero-trust infrastructure, stateful orchestration, and continuous evaluation.

---

## 1. System & Routing Architecture

The website is engineered as a zero-dependency, high-performance bilingual static application hosted on GitHub Pages with machine-readable Markdown twins (`.md`) for AI crawlers and agents.

### Dual-Track Bilingual Routing
* **Blog Reverse-Proxy (`/blog/` & `/blog/pt/`):** Hosted in the dedicated `hsnlabs-ai/blog` repository (`/Users/hugosoares/blog_hsn_labs`).

### Home Page Architecture
1. **Header (`.header-nav`):** Sticky translucent navbar with horizontal lockup, navigation links (`Advisory`, `Cases`, `Blog`), GitHub link, `EN · PT` language switcher, and primary CTA (`Conhecer o Agentic Bootcamp™`).
3. **Market Reality & Field Documentary Strip (`#market-reality`):** S&P Global 46% PoC abandonment callout paired with a 3-column original-color documentary strip (`01 · Alinhamento Arquitetural`, `02 · Imersão em Bancada`, `03 · Code to Spec`).
4. **Services Section (`#services` — "Por Que Agentes Falham"):** 4-card Bento grid with interactive 12-component Enterprise Agentic Architecture blueprint viewport and localized `.sr-only` accessibility specification.
5. **Editorial & Newsletter Section (`#editorial` — "Para ler antes de decidir."):** 3 Spoke essay cards with author bylines (`Por Hugo Nascimento · CPTO`) and the `[Agentes] x [a Gente]` newsletter conversion strip with FormSubmit Ajax integration.
6. **Contact Section (`#contact`) & Founder Callout:** `.hero-founder-callout` (10s rotating photo/prompt + `LangChain Certified`, `Snowflake Partner`, `Databricks Partner` credentials) positioned directly above the qualification scoping form.
7. **Canonical Footer (`.site-footer`):** Managed via `components/footer_pt.html` and `components/footer_en.html`.

---

## 2. Automation & Verification Scripts

* `python3 scripts/test_site_i18n_spec.py` — Runs the 11 bilingual specification, orthography, zero-parentheses, asset resolution, and footer parity gates.
* `python3 scripts/sync_footer.py` — Synchronizes canonical PT and EN footers across all 23 HTML pages.
* `python3 scripts/sync_sitemap.py` — Generates `sitemap.xml` from `i18n/routes-map.json`.
* `python3 scripts/setup_apollo_and_m2m.py` — Synchronizes Apollo tracking and generates `.md` M2M twin files for all routes.
* `python3 scripts/update_og.py` — Regenerates `assets/brand/og-image.png` and `assets/brand/og-image-pt.png`.
