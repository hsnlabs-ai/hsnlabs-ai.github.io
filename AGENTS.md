# Agent Guidelines — hsnlabs Official Website

Operational directives for AI coding agents maintaining, extending, or refactoring this repository.

---

## 1. Mission and Core Positioning

hsnlabs is an enterprise agentic engineering boutique building custom, resilient multi-agent architectures on executable business ontologies for mission-critical enterprise operations.

* **Core Positioning:** `Adoção de Engenharia Agentica` (`Agentic Engineering Adoption` in EN). We structure and execute enterprise agentic roadmaps across both **Headless Agents** (backoffice, data, BPO replacement, and internal workflows) and **Surface Agents** (frontoffice real-time voice and text interfaces with end customers) over legacy systems.
* **Language Architecture (Root PT-BR Default & `/en/` Secondary):**
  * Primary Brazilian Portuguese (`pt-BR`) lives at root routes: `/`, `/bootcamp/`, `/advisory/`, `/playbooks/`, `/mcp/`, `/langchain/`, `/snowflake/`, `/databricks/`, `/braintrust/`, `/canvas/`, `/privacy-policy/`, `/modern-slavery-statement/`.
  * Secondary English (`en`) mirror lives under `/en/`: `/en/`, `/en/bootcamp/`, `/en/advisory/`, `/en/playbooks/`, `/en/mcp/`, `/en/langchain/`, `/en/snowflake/`, `/en/databricks/`, `/en/braintrust/`, `/en/canvas/`, `/en/privacy-policy/`, `/en/modern-slavery-statement/`.
  * Legacy `/pt/<route>/` paths contain instant redirect shims to root routes.
  * Reciprocal `canonical` and `hreflang` (`pt-BR`, `en`, and `x-default` pointing to root PT-BR) tags on all pages.
  * **Strict Zero-Parentheses Invariant (Gate S2):** Zero visible parentheses `(` or `)` on all Portuguese text nodes, titles, and meta descriptions.
  * **Strict Zero-Travessões Invariant:** Zero em-dashes (`—`) or en-dashes (`–`) as clause separators across all surfaces in both PT and EN.
  * **Strict Portuguese Accentuation Invariant (Gate S8):** All visible Portuguese text, headings, buttons, and metadata must use formal Brazilian Portuguese orthography with proper diacritics (ã, õ, á, é, í, ó, ú, â, ê, ô, ç, à).
* **Target Audience:** Founders, C-levels (CTO, CIO, CFO, CPTO), and engineering directors in mid-to-large enterprises with high data volume, legacy ERPs, complex compliance, and margin exposure.
* **Aesthetic Standard:** ElevenLabs and Stripe Press editorial print-inspired aesthetic on an off-white canvas (`#f5f5f5`) with tactile crumpled paper materiality (`/assets/textures/paper_crumpled_clean.jpg`), origami geometry, and unified Accessible Cyan (`#0284c7`) directional annotations. Rejects all AI slop: no rounded pills (`border-radius: 9999px`), no thick neon side borders, no monospace uppercase badges, and no synthetic marketing steppers.

---

## 2. Structural Architecture of the Home Page

The home page (`index.html` and `en/index.html`) follows a 6-part editorial architecture:

1. **Header (`.header-nav`):**
   * Sticky blurred translucent navbar (`height: 80px` desktop, `64px` mobile) on off-white canvas.
   * Left: Official `hsnlabs` horizontal lockup (`/assets/brand/lockups/hsnlabs-lockup-horizontal-light.png`).
   * Navigation links (`.nav-menu`): `Advisory`, `Blog`.
   * Actions block (`.header-actions`) strict sequential order:
     1. GitHub repository link (`.header-github-link`) with SVG icon and `hsnlabs`.
     2. Editorial interpunct language switcher (`.lang-switch`, `EN · PT`).
     3. Example 01 straightish blue arrow (`.bp-arrow-header`) pointing to the primary CTA.
     4. Primary CTA button: `Conhecer o Agentic Bootcamp™` in PT (`/bootcamp/`) and `Explore Agentic Bootcamp™` in EN (`/en/bootcamp/`).
   * Mobile responsive invariant: Below `768px`, `.nav-menu`, `.header-github-link`, and `.bp-arrow-header` hide (`display: none !important;`). Below `380px`, `.brand-logo-img` scales to `21px` height and CTA button padding compacts so `.lang-switch` and the CTA button fit with `18px+` breathing room down to `320px` width.

2. **Hero Section (`.hero-section`):**
   * **Brand Emblem (`.brand-symbol-box`):** Centered `96x96px` cyan square (`#52B4FD`, strict `border-radius: 0`) with interactive WebGL/2D water ripple canvas (`#waterEmblemCanvas`) and white origami carp (`/assets/brand/elements/origami-carp-clean.png`).
   * **Single-DOM Headline & Origami Paper Notes Stage (`.hero-stage-flank` > `.hero-headline-stage`):**
     * Display Headline (`h1.display-hero`): `Adoção de <span style="color: var(--cyan-text);">Engenharia Agentica.</span>` (`Agentic Engineering <span style="color: var(--cyan-text);">Adoption.</span>` in EN). Never nest `<div>` or `<p>` inside `<h1>` so M2M Markdown extraction (`scripts/setup_apollo_and_m2m.py`) preserves the `#` heading.
     * Unified Origami Paper Pair (`.hero-origami-pair`): Single set of DOM nodes for `.flank-note-left` (**`Headless Agents`** — *"Agentes de backoffice, dados e automação interna."*) and `.flank-note-right` (**`Surface Agents`** — *"Agentes de frontoffice em voz e texto com o cliente."*). Each `.origami-note` features the multiplied crumpled paper texture, a 45-degree folded top-right corner (`::after`), zero top pin-lines, and strictly two typographic levels: `.note-heading` in `Cormorant Garamond` colored `var(--cyan-text)` (`#0284c7`) and `.note-text` in smaller `Inter` with `<span class="sr-only">` label prefixes.
     * Symmetrical Blue Curved Arrows: On desktop (`> 1120px`), `.curved-arrow-left` and `.curved-arrow-right` (`stroke="#0284c7"`, `stroke-dasharray="5 4"`) arc out from the left and right edges of `.hero-headline-stage` down into the flanking origami notes. On tablet/mobile (`<= 1120px`), `.hero-origami-pair` transitions via CSS to a centered 2-column grid (`max-width: 460px`) beneath `.mobile-arrows-bar`.
   * **Hero Tagline (`.hero-tagline`):** Two concise sentences introducing the `Agentic Bootcamp™` inline link (`class="inline-bootcamp-link"`) and US$ 5,000 ecosystem credits package.
   * **Dual Hero CTAs (`.hero-ctas`):** Symmetrical asset pair `Agentic Bootcamp™` (`.btn-primary`, wrapped in `.cta-arrow-anchor` with an absolutely positioned `.bp-arrow-cta` on its left so the button pair remains 100% centered) and `Agentic Canvas™` (`.btn-outline`).
   * **Client Portfolio Strip (`.portfolio-strip`):** Titled `Nosso Portfólio` / `Our Portfolio` in `color: var(--muted)` (`#526071`, 5.7:1 WCAG AA contrast), displaying 9 enterprise client marks (Deloitte, Santander, Insi, Softplan, Unipar, LWSA, Turbi, Caju, Cast Group).

3. **Market Reality & Field Documentary Strip (`#market-reality`):**
   * Two-column paper banner (`.reality-banner`): Left column presents *"Como escapar do cemitério de PoCs."* and lead copy; right column (`.reality-stat-box`) presents the stacked double-metric grid (`46%` S&P Global PoC abandonment and `83%` Lucidworks leadership stagnation), each with its own scoped source link.
   * **Field Documentary Strip (`.field-proof-grid`):** Three original-color documentary cards (`01 · Alinhamento Arquitetural`, `02 · Imersão em Bancada`, `03 · Code to Spec`). On desktop (`> 920px`), connected along the bottom edge (`bottom: -30px`) by two belly-down Example 01 blue dashed bridges (`.bp-bridge-12` and `.bp-bridge-23`) curving left-to-right from under one card up into the bottom of the next.

4. **Services Section (`#services` — "Por que agentes falham"):**
   * Asymmetric 4-card Bento grid (`.services-bento`) with `.post-it-badge` numbers `1` to `4`:
     * Card 1: `Preparação dos Dados` / `Data Preparation` (opens with the canonical production axiom).
     * Card 2: `Ontologia e Logs de Execução` / `Ontology & Execution Logs`.
     * Card 3: `Governança e Cibersegurança` / `Governance & Cybersecurity`.
     * Top Post-it Bridges (`.bp-bento-12`, `.bp-bento-23`): Responsive arches (`left: calc(16.666% + 44px)` and `left: calc(50% + 44px)`, `width: calc(33.333% - 88px)`, `preserveAspectRatio="none"`, `vector-effect="non-scaling-stroke"`) connecting Post-its `1 → 2 → 3`.
     * Card 4 (`.card-bento-wide` — `ADLC Complexo` / `Complex ADLC`): Full-width spanning card (`grid-column: 1 / -1 !important; overflow: visible !important;`). Contains `.bp-bento-34` (`top: -26px; left: calc(50% + 40px); width: calc(33.333% - 40px); height: 102px;`) anchored inside `.card-bento-wide` so the sweeping blue dashed return arrow from the bottom of Card 3 always lands on the right center of Post-it `4` regardless of dynamic text wrapping in Cards 1–3.
     * Interactive Architecture Blueprint Viewport (`.blueprint-viewport` on desktop, `.blueprint-mobile-card` on `<= 768px`, plus `.sr-only` 12-component semantic ordered list).

5. **Editorial Insights Section (`#editorial` — "Para ler antes de decidir."):**
   * Three Spoke essay cards (`Falhas Reais` / `Why Agents Fail`, `Engenharia Agentica` / `Agentic Engineering`, `Futuro do Trabalho` / `Future of Work`) linking to `/blog/pt/post/...` and `/blog/post/...`.

6. **Contact Section (`#contact`) & Founder Callout:**
   * **Founder Callout (`.hero-founder-callout`):** Positioned at the top of `#contact` (`max-width: 860px !important`). Left identity column is locked to `width: 278px; flex-shrink: 0;` on desktop (`> 920px`) so the 10-second synchronized rotation (`assets/js/founder-rotation.js`, up to 30 uppercase chars `'PRECISA DE AJUDA PARA COMEÇAR?'`) never causes horizontal layout jumps or clips the CTA button. Center column (`.founder-cred-group`) displays localized `LangChain` (`Certificado ↗`), `Snowflake` (`Parceiro ↗`), and `Databricks` (`Parceiro ↗`) badges. Right column (`.founder-cta-wrap`) pairs `.bp-arrow-header` with `Iniciar Conversa` / `Start a Conversation` (`23px` right inner padding).
   * **Technical Scoping Card (`.scoping-card`):** Qualification intake form (`#contactForm`) with centered `Enviar Mensagem` / `Send Message` button wrapped in `.cta-arrow-anchor` alongside `.bp-arrow-cta`.

7. **Canonical Footer (`.site-footer`):**
   * Single source of truth in `components/footer_pt.html` and `components/footer_en.html`, propagated across all 24 HTML files via `python3 scripts/sync_footer.py`. All footer `<img>` tags carry explicit `width` and `height` attributes (`142x46` and `36x36`) for zero CLS.

---

## 3. Standardized Example 01 Blue (`#0284c7`) Arrow System

All visual connectors and CTA callout arrows across the site and `architecture.html` follow the **Example 01 (Tracejado Cadenciado)** specification:
* **Color:** Unified Accessible Cyan `#0284c7` (`var(--cyan-text)`). Zero gray (`#526071` / `#64748b`) arrows.
* **Stroke & Dash:** Single smooth Bézier curve, `stroke-dasharray="5 4"`, `stroke-linecap="round"`, open 38-degree chevron tip (`stroke-linejoin="round"`), zero perpendicular start ticks, and zero S-wave distortion.
* **Directional Variations:**
  1. *Straightish Horizontal (`.bp-arrow-header`):* Shallow 3px inflection for single-row bars (Header CTA, Founder Callout CTA, and short Blueprint connectors).
  2. *Downward Left/Right Arcs (`.curved-arrow-left`, `.curved-arrow-right`, `.mobile-arrows-bar`):* Smooth 90-degree arcs connecting the Hero headline to `Headless Agents` and `Surface Agents`.
  3. *Bottom Belly-Down Card Bridges (`.bp-bridge-12`, `.bp-bridge-23`):* Under `.field-proof-grid` cards (`01 → 02 → 03`) with downward belly in open canvas.
  4. *Top Post-it Arches & Sweeping 3-to-4 Return (`.bp-bento-12`, `.bp-bento-23`, `.bp-bento-34`):* Connecting Post-its `1 → 2 → 3` and sweeping from the bottom of Card 3 to the right face of Post-it `4`.
  5. *Centered CTA Scoop (`.bp-arrow-cta` inside `.cta-arrow-anchor`):* Absolutely positioned (`right: calc(100% + 10px)`) to the left of centered primary buttons (`Agentic Bootcamp™` and `Enviar Mensagem`) so buttons stay 100% centered.

---

## 4. Automation, M2M & 12-Gate Verification Pipeline

* `python3 scripts/test_site_i18n_spec.py` — Runs the **12 mandatory verification gates** (enforced by `.git/hooks/pre-commit`):
  * **Gate S1:** Structural integrity across all 11 PT and 11 EN route pairs.
  * **Gate S2:** Strict Zero-Parentheses Invariant on all visible PT text and metadata.
  * **Gate S3:** Reciprocal `canonical` and `hreflang` links.
  * **Gate S4:** Language isolation on navigation and header selectors.
  * **Gate S5:** Disk resolution of all referenced `/assets/...` paths.
  * **Gate S6:** Complete PT localization of form labels, options, placeholders, and buttons.
  * **Gate S7:** Tri-sync and localization of `meta description`, `og:description`, and `twitter:description`.
  * **Gate S8:** Mandatory Brazilian Portuguese diacritics across all PT routes.
  * **Gate S9:** Strict verbatim footer parity across all 12 EN and 11 PT routes against `components/footer_*.html`.
  * **Gate S10:** Language leak detection in PT routes.
  * **Gate S11:** Structural `<section id="...">` ordering parity between `index.html` and `en/index.html`.
  * **Gate S12:** Origami Minimalist Hero Notes (`Headless Agents` / `Surface Agents` in `var(--cyan-text)`) and Example 01 Unified Blue (`#0284c7`, `stroke-dasharray="5 4"`) Arrow System parity across PT and EN.
* `python3 scripts/sync_footer.py` — Propagates `components/footer_pt.html` and `components/footer_en.html` across all pages.
* `python3 scripts/setup_apollo_and_m2m.py` — Generates the 26 machine-readable `.md` twin files from HTML.
* `python3 scripts/render_architecture_png.py` — Recompiles `architecture.html` (hiding `.arch-topbar`) into `assets/diagrams/hsn_labs_agentic_architecture.png` and `.webp` (`2880x1620`).
* `python3 scripts/update_og.py` — Regenerates `assets/brand/og-image.png` and `assets/brand/og-image-pt.png` (`1200x630`) and mirrors them to `~/blog_hsn_labs/docs/assets/brand/`.
