---
version: alpha
name: hsn-labs
description: Forward Deployed Engineering boutique for deterministic AI systems.
colors:
  primary: "#07090E"
  secondary: "#52B4FD"
  tertiary: "#10B981"
  neutral: "#FFFFFF"
  surface: "#0E1017"
  surface-hover: "#161924"
  border: "#222736"
  text-secondary: "#94A3B8"
  text-muted: "#718096"
  cyan-deep: "#135BA1"
typography:
  display:
    fontFamily: "Satoshi, Inter, sans-serif"
    fontSize: "3rem"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  h1:
    fontFamily: "Satoshi, Inter, sans-serif"
    fontSize: "2.25rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  h2:
    fontFamily: "Inter, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.4
  mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.8125rem"
    fontWeight: 500
    lineHeight: 1.5
rounded:
  sm: "4px"
  md: "8px"
  lg: "16px"
  full: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
components:
  card-base:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  card-bordered:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-secondary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  button-primary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
  button-primary-hover:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
  badge-cyan:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.secondary}"
    typography: "{typography.mono}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  telemetry-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.mono}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  water-basin:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    size: "140px"
  divider-line:
    backgroundColor: "{colors.border}"
    textColor: "{colors.neutral}"
    height: "1px"
  wave-trough:
    backgroundColor: "{colors.cyan-deep}"
    textColor: "{colors.neutral}"
    height: "2px"
  caption-muted:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-muted}"
    typography: "{typography.caption}"
---

## Overview

HSN Labs visual identity reflects a Forward Deployed Engineering boutique building deterministic multi-agent architectures on executable business ontologies.

The aesthetic rejects visual AI slop such as neon gradients, glowing purple ribbons, and generic templates. The brand enforces strict engineering discipline: deep obsidian canvas, pure Sky Blue water accents, crisp tactile white origami paper, and high-density technical typography.

The central mark is a 3D folded white paper origami koi carp poised inside a Sky Blue water square. The carp symbolizes ascent, agile propulsion, and precision engineering. The origami folds emphasize deterministic, handcrafted structure over stochastic hallucination.

## Colors

- Primary #07090E: Deep obsidian black canvas. Provides high-contrast negative space for technical content and diagram flows.
- Secondary #52B4FD: Brand Sky Blue. Represents the liquid medium of the koi carp water square and acts as the singular interactive focus signal across the UI.
- Tertiary #10B981: Functional emerald green for operational validation, verified tests, and deterministic invariant assertions.
- Neutral #FFFFFF: Stark white for primary display typography, logo wordmark, and clean origami paper highlights.
- Surface #0E1017: Deep charcoal for structural cards, interactive nodes, and code containers.
- Surface-Hover #161924: Elevated card background on cursor interaction.
- Border #222736: Structural boundary lines, grid lines, and technical card borders.
- Text-Secondary #94A3B8: Light slate for descriptive narrative copy and subheadings.
- Text-Muted #64748B: Neutral gray for metadata, schema keys, and telemetry timestamps.
- Cyan-Deep #1A7BC7: Wave troughs and liquid depth shading in the water motion engine.

## Typography

- Display: Satoshi 900 bold for hero titles and high-impact statements.
- H1 and H2: Satoshi and Inter semi-bold with tight letter spacing for technical headers.
- Body: Inter regular 400 for long-form narrative, client case studies, and bootcamp curriculum.
- Caption: Inter medium 500 for buttons, navigation links, and compact interface controls.
- Mono: JetBrains Mono for telemetry metrics, JSON schema definitions, API endpoints, and FDE squad operational badges.

## Layout

- Grid: 12-column responsive technical grid with 24px gutters on desktop and 16px on mobile.
- Max Width: 1200px container for editorial content; full-viewport dynamic flex canvas for interactive architecture graphs.
- Spacing Scale: Strict multiples of 4px and 8px: xs 4px, sm 8px, md 16px, lg 24px, xl 32px, xxl 48px.
- Density: High information density with clean white space separating distinct logical modules.

## Elevation & Depth

- Base Layer: Pure flat obsidian canvas #07090E.
- Card Layer: #0E1017 with 1px border #222736 and ambient shadow 0 10px 30px rgba 0, 0, 0, 0.6.
- Interactive Layer: Elevated with border-color #52B4FD and subtle glow box-shadow 0 0 20px rgba 82, 180, 253, 0.2.
- No Fake 3D Ribbons: Shadows must be physical contact shadows, not floating neon vaporware.

## Shapes

- Water Square: Perfect 1:1 aspect ratio with 4px to 8px corner radius. Represents the liquid pond.
- Cards: 8px to 12px corner radius for technical enclosures.
- Pills: Full 9999px border radius for telemetry status tags.
- Buttons: Sharp 4px corner radius conveying engineering precision.

## Components

- `card-base`: Fundamental enclosure for architectural nodes, case studies, and vertical breakdowns.
- `button-primary`: Main call-to-action button for Bootcamp application and technical demos.
- `button-primary-hover`: High-contrast state flipping to pure white with black text.
- `badge-cyan`: Telemetry indicator for operational statuses and FDE squad identifiers.

## Do's and Don'ts

- Do keep the origami carp static and crisp when animating the water motion.
- Do use pure #52B4FD Sky Blue for the water foundation and primary interactive affordances.
- Do pair Satoshi display titles with JetBrains Mono metadata for authentic engineering contrast.
- Do provide isolated transparent assets for slide decks and Keynote presentations.
- Don't use purple gradients, magenta glows, or multi-colored AI vaporware lines.
- Don't deform or stretch the origami carp geometry into arbitrary curves.
- Don't enclose brand marks inside generic rounded squircle app-store tiles.
- Don't use hand-coded low-poly SVG approximations where the photorealistic folded paper texture belongs.
