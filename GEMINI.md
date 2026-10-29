# Gemini Agent Directives — hsnlabs Official Website

Operational directives for Gemini models maintaining, extending, or refactoring this repository. Follow `AGENTS.md` as the single source of truth.

---

## 1. Core Architectural Invariants

* **Brand Casing:** Always write `hsnlabs` in lowercase as a single word.
* **Founder Title:** Always refer to Hugo Nascimento as `Founder & CPTO` or `CPTO`. Never use "Arquiteto", "Principal Architect", or "Forward Deployed Engineer" / "FDE".
* **Dual-Track Routing (PT-BR at Root, EN under `/en/`):**
  * Root routes (`/`, `/bootcamp/`, `/advisory/`, `/mcp/`, `/langchain/`, `/snowflake/`, `/databricks/`, `/braintrust/`, `/canvas/`) serve Brazilian Portuguese (`pt-BR`).
  * `/en/` routes serve English (`en`).
  * Never run the deprecated `scripts/build_pt_site.py` generator. Edit PT and EN HTML files directly, then run `python3 scripts/setup_apollo_and_m2m.py` and `python3 scripts/test_site_i18n_spec.py`.
* **Strict Language & Orthography Rules:**
  * Zero parentheses `(` or `)` in any visible Portuguese text, title, or meta description (Gate S2).
  * Zero em-dashes (`—`) or en-dashes (`–`) across all surfaces in both PT and EN.
  * Mandatory standard Brazilian Portuguese diacritics across all PT routes (Gate S8).
  * Express project or bootcamp cycles strictly in **months** (`"2 meses"` / `"2 months"`); never use weeks or days.
* **Hero Origami Notes & Example 01 Blue (`#0284c7`) Arrow System (Gate S12):**
  * `h1.display-hero` and `.hero-origami-pair` (`Headless Agents` on left, `Surface Agents` on right, titles in `var(--cyan-text)`) live inside `.hero-headline-stage` so `<h1>` remains pure for SEO and M2M `.md` generation.
  * All directional arrows across the site (`curved-arrow-left`, `curved-arrow-right`, `bp-arrow-header`, `bp-arrow-cta`, `bp-bridge-12`, `bp-bridge-23`, `bp-bento-12`, `bp-bento-23`, `bp-bento-34`) and `architecture.html` use the **Example 01 Cadenced Dashed** pattern in unified blue `#0284c7` (`stroke-dasharray="5 4"`, open chevron tip, zero start ticks).
  * `.bp-bento-34` is anchored inside `.card-bento-wide` (`top: -26px; left: calc(50% + 40px); width: calc(33.333% - 40px);`) with `preserveAspectRatio="none"` and `vector-effect="non-scaling-stroke"` so it adapts dynamically to any Row 1 card height on window resize.
* **Human Presence & Responsive Founder Callout:**
  * `.hero-founder-callout` (`max-width: 860px !important`) lives at the top of `#contact`, with its left identity column locked to `width: 278px; flex-shrink: 0;` on desktop (`> 920px`) so the 10s rotation (`assets/js/founder-rotation.js`, up to 30 uppercase chars `'PRECISA DE AJUDA PARA COMEÇAR?'`) never shifts layout or clips `Iniciar Conversa`.
  * Field documentary photos in `/assets/images/field/` (`opcao_19`, `opcao_08`, `opcao_01`) remain in original color and are connected underneath by belly-down Example 01 blue dashed bridges (`.bp-bridge-12`, `.bp-bridge-23`).
* **Validation Harness:** Run `python3 scripts/test_site_i18n_spec.py` before every commit to verify all 12 gates pass.
