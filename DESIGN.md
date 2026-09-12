# HSN Labs | Design System & Brand Identity Specification

> **Deterministic Control for Stochastic Systems**  
> Canonical Design Guide & Architectural Frontend Standard for all `HSN Labs` interfaces, portals, and products.

---

## 1. Brand Philosophy & Aesthetic Foundations

`HSN Labs` engineers mission-critical infrastructure for **Forward Deployed Engineering**, formal SMT invariant verification, and deterministic error containment in multi-agent networks. The brand identity reflects this mathematical rigor, sovereign resilience, and high-precision engineering through:

* **Brand Name & Wordmark Rule:** The brand is strictly named **`HSN Labs`** (all-lowercase). Never write `SFlabs`, `SF Labs`, or `SFLABS` in logo, navigation, or visual wordmark contexts.
* **Logo Typography:** Rendered in **Satoshi Semi-Bold Italic** (`font-style: italic`, `font-weight: 600`, `letter-spacing: -0.03em`, lowercase `HSN Labs`).
* **High-Precision Engineering Palette:** Clean white and light slate surfaces anchored by Midnight Navy (`#0F172A`), electric Primary Blue (`#2D74DE`), and Signal Green (`#10B981`) status validation chips.
* **Strict Geometric Intent:** Precise corner radii (8px for interactive controls, 12px for content cards), reserving full pill radii (`rounded-full`) exclusively for metadata badges and status chips.
* **Signature Stripe Band:** An 8px multi-stop gradient band (`.sunset-stripe-band`) anchoring the transition to the footer on every page.

---

## 2. Color System & Semantic Tokens

### A. Core Identity Palette

| Token Name | Tailwind Class | Hex Value | Usage / Semantic Role |
| :--- | :--- | :--- | :--- |
| **Primary Blue** | `bg-primary`, `text-primary`, `border-primary` | `#2D74DE` | Primary CTA, active states, key interactive accents, flow SVG paths |
| **Primary Deep** | `hover:bg-primary-deep` | `#1E58B0` | Primary CTA hover state, active focus rings, gradient start anchor |
| **Primary Light** | `bg-primary-light`, `bg-blue-50` | `#EFF6FF` | Soft blue background tint for active tabs and highlighted containers |
| **Midnight Navy** | `bg-navy`, `text-navy` | `#0F172A` | Primary display headings, central kernel node, modal headers, dark accents |
| **Charcoal Slate** | `bg-navy-card` | `#1E293B` | Deep card surfaces, dark containers, structural contrast |
| **Support Slate** | `border-slate-support`, `bg-slate-support` | `#E2E8F0` | Card borders, grid lines, dividers, subtle boundaries |
| **Signal Green** | `text-signal-green`, `bg-signal-green` | `#10B981` | Status badges for "PASS", "Validated", live pulse indicators |

### B. Slate Neutral Hierarchy

| Token Name | Tailwind Class | Hex Value | Usage / Semantic Role |
| :--- | :--- | :--- | :--- |
| **Slate Editorial** | `text-slate-editorial` | `#475569` | Subheadings, descriptive body prose, paragraph text |
| **Slate Steel** | `text-slate-steel` | `#64748B` | Secondary metadata labels, captions, inactive status text |
| **Slate Stone** | `text-slate-stone` | `#94A3B8` | Inactive tab dots, secondary hints, decorative dividers |
| **Slate Muted** | `text-slate-muted`, `border-slate-muted`| `#CBD5E1` | Input placeholders, scrollbar thumb, soft dividers |

### C. Surface Hierarchy

| Surface Token | Hex Value | Usage / Semantic Role |
| :--- | :--- | :--- |
| `surface.canvas` | `#FFFFFF` | Clean white page background and primary card background |
| `surface.cream` / `slate-50` | `#F8FAFC` | Subtle section backgrounds, partner cards background, footer background |
| `surface.dark` | `#0F172A` | Dark modal headers, central kernel node |
| `surface.card` | `#1E293B` | Dark card backgrounds |
| `surface.code` | `#0F172A` | Monospaced code blocks, invariant solver telemetry |

---

## 3. Legacy Replacement Mapping (MANDATORY)

The legacy orange/cream palette has been permanently deprecated. All future modifications must adhere to the following mapping:

| Deprecated Legacy Token | Deprecated Hex | Replacement Token | New Hex Value |
| :--- | :--- | :--- | :--- |
| `primary` (Orange) | `#fa520f` | `primary` (Primary Blue) | **`#2D74DE`** |
| `primary-deep` (Dark Orange) | `#cc3a05` | `primary-deep` (Deep Blue) | **`#1E58B0`** |
| `cream` / `cream-light` | `#fff8e0` / `#fffaeb` | Clean Canvas / Slate 50 | **`#FFFFFF` / `#F8FAFC`** |
| `beige-deep` (Beige Border) | `#e6d5a8` | `slate-support` (Support Slate) | **`#E2E8F0`** |
| `ink` (Dark Charcoal) | `#1f1f1f` | `navy` (Midnight Navy) | **`#0F172A`** |

---

## 4. Typography System

The `HSN Labs` typography uses a three-tier hierarchy combining modern geometry, legibility, and technical precision:

```html
<!-- Fontshare CDN for Satoshi -->
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900,301,401,501,701,901&display=swap" rel="stylesheet">

<!-- Google Fonts for Inter and JetBrains Mono -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

### Typographic Hierarchy

1. **Brand Wordmark (Header & Footer):**
   * **Family:** `Satoshi` (`font-display`)
   * **Styling:** Semi-Bold (`font-weight: 600`), Italic (`font-style: italic`), Letter Spacing `-0.03em`, Lowercase (`lowercase`).
   * **Markup:**
     ```html
     <a href="/" aria-label="HSN Labs home" class="inline-flex items-center">
       <span class="font-display text-[26px] font-semibold italic tracking-tight text-primary lowercase">
         HSN Labs
       </span>
     </a>
     ```

2. **Display & Section Headings:**
   * **Family:** `Satoshi`, `Inter`, `sans-serif` (`font-display`)
   * **Attributes:** Size 34px–80px, Line-Height `1.05`–`1.15`, Letter-Spacing `-1.5px` to `-0.5px`, Weights `400`–`600`.
   * **Usage:** Hero title, main section headers, metric counters.

3. **Interface, Subheadings & Prose:**
   * **Family:** `Inter`, `sans-serif` (`font-sans`)
   * **Attributes:** Size 13px–18px, Line-Height `1.5`–`1.6`, Weights `400`, `500`, `600`.
   * **Usage:** Navigation links, subheadings, descriptive paragraphs, buttons, form inputs.

4. **Telemetry, Code & Verification Invariants:**
   * **Family:** `JetBrains Mono`, `monospace` (`font-mono`)
   * **Attributes:** Size 9px–13px, Line-Height `1.4`, Letter-Spacing `+0.04em` to `+0.08em`, Weights `400`, `500`, `600`.
   * **Usage:** Section eyebrows ("INTEGRATIONS", "DEPLOYMENTS", "CAREERS"), status badges ("PASS", "VALIDATED"), telemetry chips, code blocks.

---

## 5. Geometric Rules & Component Radii

To prevent visual drift and preserve architectural clarity, geometry must strictly obey:

* **Buttons & Actions:** `rounded-md` (`8px`) — **Never `rounded-full` / pill for action buttons.**
* **Form Inputs & Selects:** `rounded-md` (`8px`), standard height `44px`.
* **Cards, Containers & Panels:** `rounded-lg` (`12px`) with `border: 1px solid #E2E8F0`.
* **Modal Dialogs:** `rounded-lg` (`12px`) native HTML `<dialog>` with `rgba(15, 23, 42, 0.65)` backdrop blur.
* **Badges & Status Chips:** `rounded-full` (`9999px`) — **Pill geometry is strictly reserved for metadata tags only.**

---

## 6. Signature Brand Elements

### 1. The Signature Stripe Band (`.sunset-stripe-band`)
A full-width 8px horizontal bar placed immediately above the footer on all web surfaces:
```css
.sunset-stripe-band {
  height: 8px;
  width: 100%;
  background: linear-gradient(90deg, #1E58B0 0%, #2D74DE 35%, #60A5FA 70%, #E2E8F0 100%);
}
```

### 2. Atmospheric Mesh Background (`.bg-brand-mesh`)
Placed on hero and high-impact sections:
```css
.bg-brand-mesh {
  background-image: 
    radial-gradient(1000px circle at 50% -10%, rgba(45, 116, 222, 0.08), transparent 70%),
    radial-gradient(800px circle at 95% 20%, rgba(45, 116, 222, 0.05), transparent 60%),
    radial-gradient(700px circle at 5% 50%, rgba(248, 250, 252, 0.9), transparent 70%);
}
```

### 3. Architectural Hairline Grid (`.bg-grid-hairline`)
Subtle background grid used inside cards and diagram containers:
```css
.bg-grid-hairline {
  background-size: 36px 36px;
  background-image: 
    linear-gradient(to right, rgba(226, 232, 240, 0.8) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(226, 232, 240, 0.8) 1px, transparent 1px);
}
```

### 4. Interactive 3x3 Client Logo Grid Visual Conventions
- **Layout:** Square 1:1 Aspect Ratio container (`aspect-square`) with hairline background grid and ambient radial pulse glow.
- **Header Bar:** Upper status indicator with Signal Green pulsing status dot (`Enterprise Deployments`) and deployment counter (`9 Selected`).
- **Logo Cards:** 9 distinct client logo cards (DHL, CMA CGM, Uber, job&talent, WERNER, Naturgy, Davante, Circle Logistics, infiniT) with subtle ambient floating motion (`animate-float-a`, `animate-float-b`, `animate-float-c`).
- **Hover Transitions:** Smooth transition on hover (`transition-all duration-300`) with scale effect (`hover:scale-[1.03]`), border highlight (`hover:border-primary`), background tint (`hover:bg-blue-50/40`), and logo contrast shift from muted grayscale (`opacity-65 grayscale`) to full clarity (`group-hover:opacity-100 group-hover:grayscale-0 group-hover:scale-105`).

---

## 7. Component Specifications

### Header Mega-Menus (Enterprise Navigation)
Mega-menus provide structured, high-density discovery for Platform capabilities and Mission Verticals without visual clutter.
* **Flyout Container:** `rounded-lg border border-slate-support bg-white shadow-modal p-6` with top invisible hover bridge (`pt-3`).
* **Column Headers:** `font-mono text-[10px] uppercase tracking-wider text-slate-steel font-semibold border-b border-slate-support pb-1.5`.
* **Nav Items:** `group/item block rounded-md p-2 -mx-2 hover:bg-slate-50 transition-colors`.
* **Item Titles:** `text-[13px] font-semibold text-navy group-hover/item:text-primary transition-colors`.
* **Descriptions:** `text-[11.5px] text-slate-editorial leading-relaxed mt-0.5`.
* **Featured Side Panel:** `rounded-md bg-slate-50 border border-slate-support p-4`.

### Buttons
* **Primary Button:**
  ```html
  <button class="inline-flex items-center justify-center gap-2 rounded-md bg-primary hover:bg-primary-deep px-5 py-2.5 text-[13px] font-sans font-medium text-white transition-colors shadow-xs">
    <span>Schedule Discovery</span>
    <span aria-hidden="true">→</span>
  </button>
  ```
* **Dark / Secondary Button:**
  ```html
  <button class="inline-flex items-center justify-center gap-2 rounded-md bg-navy hover:bg-primary px-5 py-2.5 text-[13px] font-sans font-medium text-white transition-colors shadow-xs">
    <span>Request Briefing</span>
    <span>→</span>
  </button>
  ```

### Cards
* **Standard Editorial Card:**
  ```html
  <div class="rounded-lg border border-slate-support bg-white p-6 shadow-editorial hover:border-primary transition-all duration-200">
    <!-- Card Content -->
  </div>
  ```
* **Featured / Active Card:**
  ```html
  <div class="rounded-lg border-2 border-primary bg-blue-50/40 p-6 shadow-editorial transition-all duration-200">
    <!-- Featured Content -->
  </div>
  ```

### Inputs & Forms
* **Text Input:**
  ```html
  <input 
    type="email" 
    class="w-full px-3.5 py-2.5 rounded-md border border-slate-muted bg-white text-[13.5px] text-navy placeholder:text-slate-stone focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary font-sans"
    placeholder="name@enterprise.com"
  />
  ```

---

## 8. Anti-Drift Quality Checklist (Mandatory for All Future Changes)

Before committing any modifications to `index.html`, `404.html`, or other interfaces:

- [ ] **Brand Name:** Is the brand name strictly `HSN Labs` (all-lowercase) in logo contexts?
- [ ] **Logo Font:** Is the logo rendered in Satoshi Semi-Bold Italic?
- [ ] **No Legacy Orange/Cream:** Are all occurrences of `#fa520f`, `#fff8e0`, `#fffaeb`, `#e6d5a8`, and `#1f1f1f` completely absent?
- [ ] **Color Tokens:** Are all buttons, active borders, and highlights using `#2D74DE` (Primary Blue) and `#1E58B0` (Primary Deep)?
- [ ] **Status Badges:** Are verification states using `#10B981` (Signal Green) with `rounded-full`?
- [ ] **Button Geometry:** Are all action buttons `rounded-md` (8px), avoiding `rounded-full`?
- [ ] **Card Geometry:** Are cards `rounded-lg` (12px) with `#E2E8F0` Support Slate borders?
- [ ] **Signature Stripe:** Is the 8px `.sunset-stripe-band` maintained above the footer?
- [ ] **Local Assets:** Are all images and integration logos in `assets/` preserved?

---

© 2026 HSN Labs. All rights reserved.
