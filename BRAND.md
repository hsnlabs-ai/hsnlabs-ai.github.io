# hsnlabs — Brand Identity Guidelines

Operational standards for applying the hsnlabs brand across digital products, engineering documentation, investor decks, and public communications.

---

## 1. Brand Concept and Metaphor

* **Core Positioning:** Enterprise agentic engineering boutique driving `Adoção de Engenharia Agentica` (`Agentic Engineering Adoption`), building resilient multi-agent architectures on executable business ontologies across both **Headless Agents** (backoffice, data, BPO replacement, and internal automation) and **Surface Agents** (frontoffice real-time voice and text customer interfaces).
* **Approved Descriptors:** `Adoção de Engenharia Agentica`, `Enterprise Agentic Architecture`, `Sistemas em Produção`.
* **Symbol:** Pure geometric cyan square containing a white paper origami koi carp leaping toward the upper right corner.
* **Origami & Tactile Paper Metaphor:**
  * Precise paper folds represent structural rigor and artisanal engineering versus stochastic drift.
  * Ascending direction signals progress, technical velocity, and operational mastery.
  * Cyan square represents the dynamic liquid medium where intelligent agents operate.

---

## 2. Strict Geometric & Tactile Invariants

* **Corner Radius Rule:**
  * The cyan square symbol, buttons, cards, and inputs must ALWAYS maintain sharp 90-degree corners with `border-radius: 0`.
  * Never apply rounded corners, pill badges (`border-radius: 9999px`), squircles, or circular masks.
* **Tactile Origami Paper Notes (`.origami-note`):**
  * Used in the Hero section to frame `Headless Agents` and `Surface Agents`.
  * Constructed with pure white surface (`#ffffff`), multiplied crumpled paper texture (`/assets/textures/paper_crumpled_clean.jpg`, opacity `0.55`), a 45-degree folded top-right origami corner crease (`::after`), subtle organic tilt (`-1.1deg` left, `+1.1deg` right), zero top pin-lines, and strictly two typographic levels: heading in `Cormorant Garamond` colored `var(--cyan-text)` (`#0284c7`) and concise description in smaller `Inter`.
* **Standardized Example 01 Blue (`#0284c7`) Cadenced Dashed Arrow System:**
  * All visual connectors, card bridges, and CTA callouts across the website and architecture blueprint use a single unified family: smooth single-arc Bézier curves in Accessible Cyan (`#0284c7`), `stroke-dasharray="5 4"`, `stroke-linecap="round"`, and an open 38-degree chevron tip, with curvature calibrated to each spatial context (straightish horizontal for narrow bars, 90-degree downward arcs for Hero origami notes, bottom belly-down bridges for Field Documentary cards `01 → 02 → 03`, top arches plus a responsive bottom-of-Card-3-to-Post-it-4 sweep for Services Bento `1 → 2 → 3 → 4`, and lateral scoop arrows for centered CTAs).
* **Angle and Orientation:**
  * Never rotate, mirror, or slant the origami carp outside its original ascending trajectory.
* **Exclusion Zone:**
  * Maintain minimum clear space equal to half the width of the cyan square around all sides of the mark.

---

## 3. Official Color Palette

* **Obsidian Black (`#07090E`):** Primary ink for typography and high-contrast elements.
* **Brand Sky Blue (`#52B4FD`):** Primary corporate identifier, `.btn-primary` fill, `.post-it-badge` fill, and background of the origami carp basin.
* **Accessible Cyan (`#0284c7`):** High-contrast accent text (`Engenharia Agentica.`, `Headless Agents`, `Surface Agents`) and unified color for all Example 01 dashed arrows on light surfaces (meeting WCAG AA requirements).
* **Muted Slate (`#526071`):** Calibrated secondary and label text color guaranteeing 5.7:1 WCAG AA contrast on `#f5f5f5` and `#fafafa`.
* **Canvas Floor (`#F5F5F5`):** Clean off-white surface for editorial print presentation.
* **Card Surface (`#FFFFFF`):** Pure white elevated surface for cards, post-it notes, and interactive modules.
* **Hairline Border (`#E2E8F0` / `#CBD5E1`):** Subtle 1px structural dividing lines.
* **Operational Emerald (`#10B981`):** Verified invariant passes, audit checks, and SLA metrics.

---

## 4. Typography System

* **Wordmark:** Pure lowercase geometric sans `hsnlabs` with uniform tracking.
* **Display Headings:** `Cormorant Garamond` at weight 300–500 with tight line height.
* **Running Body and Interface:** `Inter` regular, medium, and semibold with slight positive tracking for airy reading.

---

## 5. Asset Library Directory

All canonical files reside in `assets/brand/`:
* `elements/`: Clean isolated transparent origami carp in 1x and 4x scales.
* `symbol/`: Cyan square mark with carp in standard and 4x resolution.
* `wordmark/`: Vector SVG wordmarks in black, white, and cyan.
* `lockups/`: Horizontal and vertical lockups for light and dark backgrounds.
* `motion/`: Physical liquid simulation renders in MP4, WebM, and GIF formats.
* `favicons/`: Complete multi-resolution browser favicon bundle.

---

## 6. Prohibited Practices

* Do not apply generic AI visual tropes such as neon gradients, purple ribbons, thick colored left borders, or floating spheres.
* Do not alter the lowercase casing of the wordmark `hsnlabs`.
* Do not combine the mark with third-party logos without maintaining the standard exclusion margin.
* Never use `Forward Deployed Engineering` or `FDE` as a brand descriptor, headline, tagline, banner eyebrow, or public positioning. FDE is an internal delivery capability within specific technical sandbox sprints, never the public company category or executive bio descriptor.
