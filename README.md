# HSN Labs — Official Website Repository

Official production repository for the **HSN Labs** corporate website.

HSN Labs is an AI architecture consulting boutique solving why AI agents fail in production through hybrid engineering, enterprise ontologies, and custom deep agents for mission-critical operations.

---

## 1. System Architecture

The website is engineered as a zero-dependency, high-performance static application hosted on GitHub Pages.

### Page Structure
* **Header:** Sticky blurred translucent navbar with official horizontal wordmark and direct navigation.
* **Hero Section:**
  * Interactive liquid basin emblem with 3-stage wave physics engine.
  * Editorial display headline and value proposition.
  * Primary action linking to the 5-Day Bootcamp and secondary action to Contact Us.
  * Client Portfolio strip featuring nine normalized monochrome enterprise marks.
* **Services Section:**
  * Balanced two-by-two grid presenting four core delivery pillars:
    * Personalized Business Ontologies.
    * Deep Agent Infrastructure.
    * Deterministic Guardrails.
    * Enterprise ADLC Stack.
* **Verticals Section:**
  * Three-column layout covering high-stakes regulated domains:
    * BFSI Infrastructure.
    * Clinical Operations.
    * Industrial Operations.
* **Technical Scoping Section:**
  * Executive engagement card with four qualification gates and direct email dispatch.
* **Footer:**
  * Clean institutional signature with navigation, engineering specifications, and copyright.

---

## 2. Design System and Visual Tokens

Built on the ElevenLabs editorial print design system without artificial visual artifacts or generic AI aesthetics.

### Color Tokens
* **Canvas Floor:** `#f5f5f5`
* **Card Surface:** `#ffffff`
* **Soft Canvas:** `#fafafa`
* **Ink Text:** `#07090e`
* **Running Body:** `#475569`
* **Muted Labels:** `#64748b`
* **Hairline Dividers:** `#e2e8f0`
* **Brand Sky Blue:** `#52B4FD`
* **Operational Emerald:** `#10B981`

### Typography Hierarchy
* **Display Headings:** Cormorant Garamond at weight 300 with negative tracking.
* **Body and UI:** Inter with positive tracking for airy editorial reading.
* **Metrics and Code:** JetBrains Mono for telemetry and invariant verification.

---

## 3. Brand Identity and Logo Invariant

The HSN Labs brand mark represents determinism through paper geometry and dynamic water physics.

### Strict Geometry Rule
* The cyan square symbol must ALWAYS maintain sharp 90-degree corners with `border-radius: 0`.
* Never apply rounded corners, squircles, or border-radius to the cyan square mark.
* The white origami carp is positioned in the upper right quadrant at a fixed ascending angle.

---

## 4. Enterprise Portfolio Clients

The website displays nine verified enterprise client marks in normalized monochrome vector format:
* Deloitte
* PagoNext
* Insi
* Softplan
* Unipar Carbocloro
* LWSA
* Turbi
* Caju
* Cast Group

---

## 5. Repository File Tree

```text
├── assets/
│   ├── brand/                 # Complete brand asset library
│   │   ├── elements/          # Clean isolated origami carp assets
│   │   ├── favicons/          # Web browser favicon bundle 16px to 512px
│   │   ├── lockups/           # Horizontal and vertical lockups
│   │   ├── motion/            # Rendered video, webm, and gif motion files
│   │   ├── symbol/            # Official cyan square symbol in high resolution
│   │   └── wordmark/          # Vector SVG wordmarks in black, white, and cyan
│   └── portfolio/             # Client portfolio vector assets
│       ├── png/               # High-resolution raster client marks
│       └── svg/               # Normalized monochrome vector client marks
├── AGENTS.md                  # Operational directives for AI coding agents
├── BRAND.md                   # Brand guidelines and application rules
├── DESIGN.md                  # Google design-md token specification
├── GEMINI.md                  # Gemini model technical constraints
├── analytics.json             # Tag manager and measurement stream IDs
├── index.html                 # Production entrypoint
└── README.md                  # Repository documentation
```

---

## 6. Local Development

```bash
# Start local HTTP server
python3 -m http.server 8124

# Open in browser
open http://localhost:8124/index.html
```

---

## 7. Telemetry and Analytics

* **Google Tag Manager Container:** `GTM-KPL6PVKC`
* **Google Analytics 4 Measurement ID:** `G-GMK24ECXMF`
* **Stream ID:** `15812853732`
