# Agent Guidelines — HSN Labs Official Website

Operational directives for AI coding agents maintaining, extending, or refactoring this repository.

---

## 1. Mission and Core Positioning

HSN Labs is a Forward Deployed Engineering boutique building custom, deterministic multi-agent architectures on executable business ontologies for mission-critical enterprise operations.

* Primary Language: The website must be 100% in English. All copy, labels, meta tags, and alt texts are strictly English.
* Target Audience: Founders, C-levels such as CTO, CIO, CFO, and engineering directors in mid-to-large enterprises with high data volume, complex compliance, and margin exposure.
* Aesthetic Standard: ElevenLabs editorial print-inspired aesthetic on an off-white canvas `#f5f5f5`. Rejects all AI slop: no pills with borders or glow dots, no loud slash headers, no generic neon purple gradients, no floating data ribbons, no abstract robotic illustrations.

---

## 2. Structural Architecture of the Website

The website follows a clean 4-section architecture:

1. Header:
   * Sticky blurred translucent navbar on off-white canvas.
   * Left: Official HSN Labs horizontal lockup.
   * Minimalist navbar: Intermediate navigation links strictly eliminated to maximize visual breathing room and conversion focus; navbar contains only the brand lockup on the left and primary Apply for Bootcamp button on the right.
   * Primary action button linking to Bootcamp application.
2. Hero Page:
   * Brand mark centered above the primary headline: Official 3-stage water motion logo. Strict requirement: The cyan square mark must ALWAYS have sharp 90-degree corners with `border-radius: 0`. Never apply rounded corners to the mark.
   * Primary headline: Two-tier split-scale hierarchy with commanding anchor line `Enterprise AI Agents` and subordinate differentiator clause `that don't fail in production`.
   * Subtitle: Narrative explaining specialized architecture consulting versus theoretical management consulting slides, solving why AI agents fail in production.
   * Dual actions: Primary button linking to Bootcamp application and secondary button linking to Contact Us.
   * Client Portfolio Strip: Titled `Our Portfolio`, presenting nine normalized monochrome vector marks: Deloitte, Santander, Insi, Softplan, Unipar Carbocloro, LWSA, Turbi, Caju, Cast Group.
3. Services Section:
   * Balanced two-by-two grid presenting four technical pillars:
     1. Personalized Business Ontologies.
     2. Deep Agent Infrastructure.
     3. Deterministic Guardrails.
     4. Agent Development Life Cycle Stack: 4-stage enterprise pipeline covering Ontology & Design, Infrastructure, Orchestration, and Deploy, Evaluation & Observability.
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
  * All cards and containers use the clean crumpled paper texture overlay (`assets/textures/paper_crumpled_clean.jpg`) via `mix-blend-mode: multiply` at opacity 0.50.
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
