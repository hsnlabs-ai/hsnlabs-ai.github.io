# Gemini Agent Directives — hsnlabs Official Website

Operational directives for Gemini models maintaining, extending, or refactoring this repository. Follow `AGENTS.md` as the single source of truth.

---

## 1. Core Architectural Invariants

* **Brand Casing:** Always write `hsnlabs` in lowercase as a single word.
* **Founder Title:** Always refer to Hugo Nascimento as `Founder & CPTO` or `CPTO`. Never use "Arquiteto" or "Principal Architect".
* **Bilingual Routing:** Root routes (`/`, `/bootcamp/`, `/advisory/`, `/portfolio/`, `/canvas/`, `/mcp/`, `/langchain/`, `/snowflake/`, `/braintrust/`, `/privacy-policy/`, `/modern-slavery-statement/`) are in Brazilian Portuguese (`pt-BR`). English routes live under `/en/`.
* **Strict Portuguese Rules:**
  * Zero parentheses `(` or `)` in any visible Portuguese text, title, or meta description.
  * Mandatory standard Brazilian Portuguese diacritics across all PT routes.
  * Never use "semanas" / "weeks" or "dias" / "days" for project or bootcamp durations; always use **months** (`"2 meses"` / `"2 months"`).
* **Human Presence & Visual Rules:**
  * `.hero-founder-callout` lives at the top of the final Contact/Application section (`#contact` / `#apply`) near the footer, preserving the 10s rotation (`assets/js/founder-rotation.js`) and the 3 credential lockups (`LangChain Certified`, `Snowflake Partner`, `Braintrust Partner`).
  * Field documentary photos in `/assets/images/field/` (`opcao_19`, `opcao_08`, `opcao_01`) must remain in original color (never apply grayscale/B&W filters) and must never be inserted inside the `"Nosso Método"` (`#protocol`) cards of `/bootcamp/`.
  * Preserve `/advisory/` without `.hero-founder-callout` and preserve `/portfolio/` CSS as-is.
* **Validation Harness:** Run `python3 scripts/test_site_i18n_spec.py` before every commit to verify all 11 gates pass.
