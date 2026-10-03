# Agent Guidelines — HSN Labs Official Website

Operational directives for AI coding agents maintaining, extending, or refactoring this repository.

---

## 1. Mission and Core Positioning

HSN Labs is a Forward Deployed Engineering boutique building custom, resilient multi-agent architectures on executable business ontologies for mission-critical enterprise operations.

* Language Architecture: Bilingual dual-track. Primary English at root routes: /, /bootcamp/, /advisory/, /playbooks/, /mcp/, /privacy-policy/, /modern-slavery-statement/. Secondary Portuguese under /pt/: /pt/, /pt/bootcamp/, /pt/advisory/, /pt/playbooks/, /pt/mcp/, /pt/privacy-policy/, /pt/modern-slavery-statement/. Reciprocal canonical and hreflang tags on all pages. Strict Zero-Parentheses Invariant on all visible Portuguese text. Strict Portuguese Accentuation Invariant: All visible Portuguese text, headings, buttons, and metadata must strictly use standard Brazilian Portuguese orthography with proper diacritics (ã, õ, á, é, í, ó, ú, â, ê, ô, ç, à). ASCII unaccented variants (e.g., adocao, producao, estrategia, operacao, ate, voce, politica) are strictly prohibited.
* Target Audience: Founders, C-levels such as CTO, CIO, CFO, and engineering directors in mid-to-large enterprises with high data volume, complex compliance, and margin exposure.
* Aesthetic Standard: ElevenLabs editorial print-inspired aesthetic on an off-white canvas `#f5f5f5`. Rejects all AI slop: no pills with borders or glow dots, no loud slash headers, no generic neon purple gradients, no floating data ribbons, no abstract robotic illustrations.

---

## 2. Structural Architecture of the Website

The website follows a clean 4-section architecture:

1. Header:
   * Sticky blurred translucent navbar on off-white canvas.
   * Left: Official HSN Labs horizontal lockup.
   * Minimalist navbar: Contains brand lockup (left), secondary navigation dropdown "Services" (Bootcamp / Advisory), a GitHub repository link, and primary "Apply for Bootcamp" CTA (right). Dropdown uses paper texture overlay.
   * Primary action button linking to Bootcamp application.
2. Hero Page:
   * Brand mark centered above the primary headline: Official 3-stage water motion logo. Strict requirement: The cyan square mark must ALWAYS have sharp 90-degree corners with `border-radius: 0`. Never apply rounded corners to the mark.
   * Primary headline: Two-tier split-scale hierarchy with commanding anchor line `Enterprise AI Agents` and subordinate differentiator clause `that don't fail in production`.
   * Subtitle: Narrative explaining specialized architecture consulting versus theoretical management consulting slides, solving why AI agents fail in production.
   * Dual actions: Primary button linking to Bootcamp application and secondary button linking to Contact Us.
   * Client Portfolio Strip: Titled `Our Portfolio`, presenting nine normalized monochrome vector marks: Deloitte, Santander, Insi, Softplan, Unipar Carbocloro, LWSA, Turbi, Caju, Cast Group.
3. Services Section:
   * Services / Delivery Method section with balanced two-by-two grid presenting four pillars:
     1. Discovery Canvas (Scoping Tool).
     2. Legacy Reader (Reverse-engineering engine).
     3. Data Router (Surgical data extraction).
     4. Agent Development Life Cycle (Orchestration and enterprise-grade tools).
   * Numbered steps must use the `.post-it-badge` element, visually simulating a cyan square post-it floating above the card.
4. Verticals Section:
   * Three-column layout for regulated enterprise industries:
     1. Banking and Capital.
     2. Healthcare Operations.
     3. Legacy ERP and BPO.
5. Contact Section:
   * Direct technical scoping card with four qualification gates and direct email dispatch.
6. Footer:
   * Institutional signature with wordmark lockup, navigation links, and engineering specifications.
   * Copyright line: `2026 HSN Labs. All rights reserved.`
   * Prohibited in footer bottom: Do not add redundant location strings or repetitive descriptor suffixes.

---

## 3. Design Tokens and Styling Rules

* Color Palette:
  * Canvas: `#f5f5f5`
  * Card Surface: `#ffffff`
  * Soft Surface: `#fafafa`
  * Primary Ink: `#07090e`
  * Running Body: `#475569`
  * Muted Text: `#64748b`
  * Hairline: `#e2e8f0`
  * Brand Sky Blue: `#52B4FD`
  * Accessible Cyan: `#0284c7`
  * Operational Emerald: `#10B981`
* Typography:
  * Display: Cormorant Garamond weight 300 with negative tracking.
  * Body: Inter regular and medium with slight positive tracking.
  * Zero Monospace Rule: Monospace typefaces like JetBrains Mono are completely eliminated across all public surfaces to maintain an elegant editorial print aesthetic.
* Logo & Component Geometry (Strict 90-Degree Invariant):
  * Always keep `border-radius: 0` on the cyan square symbol, and on ALL interactive buttons, cards, boxes, badges, and form inputs.
  * All cards, containers, and banners (including cookie banners, alert boxes, and post-it badges) must use the clean crumpled paper texture overlay (`/assets/textures/paper_crumpled_clean.jpg`) via `mix-blend-mode: multiply`. Opacity: 0.50 for large cards, 0.65 for `.btn-primary` and `.post-it-badge`.
  * The `.post-it-badge` uses `width/height: 64px`, `background: var(--cyan)`, and edge lighting (`inset 0 1px 0 rgba(255, 255, 255, 0.4)`) combined with a dynamic float shadow (`0 4px 12px rgba(82, 180, 253, 0.45)`) and `transform: translateY(-2px)` to simulate physical depth.
  * For small elements like `.post-it-badge`, the crumpled paper texture must use a forced background-size (e.g., `background-size: 400px;`) rather than `cover` to ensure the fibers are visible.
    * CRITICAL: Use absolute paths (`/assets/...`) for the texture image to prevent 404s on subpages.
    * CRITICAL: Set `isolation: isolate` on the parent container, and apply the texture via a `::before` pseudo-element with `z-index: -1` to prevent the texture from covering pure text nodes.
  * Primary CTA buttons use Brand Sky Blue `#52B4FD` with clean crumpled paper texture overlay via `mix-blend-mode: multiply` at opacity 0.65.
  * Secondary CTA buttons use pure white paper with clean crumpled paper texture overlay via `mix-blend-mode: multiply` at opacity 0.50.
  * Never alter the origami carp proportions or angle.

---

## 4. Telemetry and Analytics

Maintain official Google tags on all public pages:
* Google Tag Manager: `GTM-KPL6PVKC`
* Google Analytics 4: `G-GMK24ECXMF` with Stream ID `15812853732`

---

## 5. Open Graph Synchronization Rule

The social preview card `assets/brand/og-image.png` must strictly mirror the live Hero section:
* Automated Script: `python3 scripts/update_og.py` extracts headlines, subtitles, and CTAs from `index.html` and renders a 1200x630 card with the official atmosphere orbs, symbol, and paper texture.
* Git Pre-Commit Hook: Configured in `.git/hooks/pre-commit` to automatically re-render and stage `og-image.png` whenever `index.html` is committed.

---

## 6. Multi-Repository Architecture Invariant: The Blog
* The blog does NOT live in this repository. It is a separate project and repository: hsnlabs-ai/blog, stored locally at /Users/hugosoares/blog_hsn_labs.
* In production, the /blog path is reverse-proxied and routed to the independent MkDocs blog deployment.
* In local development via python http server on site_hsn_labs, clicking /blog returns a 404 error because blog files do not exist here. This is expected local behavior.
* Never create a /blog directory or mock pages here. Never overwrite or duplicate blog files across repositories.

---

## 7. Internationalization and Consistency Gates
* Dual-track architecture: any modification to core copy, forms, or structural components on root English routes must be reflected in the reciprocal `/pt/` page.
* Validation harness: always execute `python3 scripts/test_site_i18n_spec.py` prior to committing.
* Verification gates:
  1. Structural integrity across all 6 route pairs.
  2. Strict Zero-Parentheses Invariant on all visible Portuguese text.
  3. Reciprocal canonical and hreflang links.
  4. Language isolation on navigation links.
  5. Asset resolution.
  6. Localization of form labels, options, placeholders, buttons, and feedback states.
  7. Localization of Open Graph and Twitter Card metadata.
  8. Strict Portuguese Accentuation Invariant (Gate S8) ensuring mandatory formal Brazilian Portuguese diacritics.
  9. Strict Footer Parity Invariant (Gate S9) enforcing that all 8 English routes and 7 Portuguese routes use canonical components from `components/footer_en.html` and `components/footer_pt.html` via `scripts/sync_footer.py`.

---

## 8. Footer Architecture and Synchronization Invariant
* Single Source of Truth: Canonical footers live in `components/footer_en.html` (English) and `components/footer_pt.html` (Portuguese).
* Never edit footer HTML fragments inside subpages directly.
* To update the footer across all 15 routes:
  1. Modify `components/footer_en.html` or `components/footer_pt.html`.
  2. Run `python3 scripts/sync_footer.py`.
  3. Validate with `python3 scripts/test_site_i18n_spec.py`.
* Automated Pre-Commit Hook: Validates that Gate S9 passes on any commit touching `.html` or component files.
