---
title: "The Agentic Pilot Canvas v1.4 · hsnlabs"
description: "Open MIT architecture framework for designing enterprise agentic AI pilots: legacy data ontologies, deterministic guards, eval harnesses, and governance."
url: "https://hsnlabs.ai/en/canvas/"
locale: "en"
updatedAt: "2026-10-19T13:02:11Z"
---

# The Agentic Pilot Canvas v1.4 · hsnlabs

> Open MIT architecture framework for designing enterprise agentic AI pilots: legacy data ontologies, deterministic guards, eval harnesses, and governance.

# The Agentic Pilot Canvas

## 1. Target Process & Impact

1.1 The Manual Process: Which repetitive manual workflow consumes the most team capacity today, and what is the ideal outcome when completed?

Examples comparing AS-IS vs. TO-BE: screening 500 resumes, keying invoices into the ERP, or enriching leads in the CRM.

1.2 Bottleneck & Symptoms: Where does the workflow stall, and what are the visible symptoms of this operational overload?

Examples: Recurring month-end overtime, manual data-entry errors, senior analysts acting as human routers.

## 2. Non-Deterministic Impact

2.1 Sanity Check: Does this workflow genuinely require agentic reasoning, or does the risk profile tolerate zero margin for uncertainty?

Examples: Tax and payroll calculations require deterministic code; parsing unstructured emails and reconciling messy documents require AI.

2.2 Blast Radius: If the agent fails, what is the internal financial or organizational damage and the external liability with customers?

Examples: Team anxiety, perceived dehumanization, burned enterprise leads, regulatory fines, or escalated VIP accounts.

## 3. Legacy Systems, Access & Data

3.1 Where Data Lives: Across which ERPs, spreadsheets, or inboxes is the ground-truth state of this workflow stored today?

Examples: SAP S/4HANA MM module, TOTVS, Salesforce, master spreadsheets in Drive, or PDF contracts.

3.2 Access Dynamics: How does the team query or mutate this data daily, and what is the synchronization cadence?

Examples: Daily UI lookups, REST APIs, or CSV exports; read-only replica isolation in Day-1 staging.

3.3 Reverse Engineering Opportunity: Which tacit rules buried in spreadsheets or legacy scripts can be audited into living specifications?

Examples: Auditing 30 legacy stored procedures or Excel macros and compiling them into typed Python schemas.

## 4. Operational Ontology

4.1 Domain Entities: What are the core business objects the agent must recognize to reason over the operation?

Examples — HR: Employee, Requisition, Review. Finance: Invoice, PurchaseOrder, Vendor. Sales: Lead, Opportunity.

4.2 Typed Actions & Invariants: What are the strictly typed tools the agent may invoke, and which invariant must never be violated?

Examples: FlagDiscrepancy, NotifyManager. Invariant: the agent never executes raw SQL or releases payments autonomously.

## 5. Human in the Loop

5.1 Escalation Thresholds: Under which financial, risk, or confidence thresholds is the agent blocked from acting without human sign-off?

Examples: Model confidence < 95%, invoice delta > $500, HR terminations/promotions, or VIP accounts at churn risk.

5.2 Named Human Sign-off: Which specific role reviews flagged exceptions and records the auditable decision?

Examples: 1-click approval card in Teams or Slack. The state machine prepares the case; the manager signs off.

## 6. Governance & Compliance

6.1 Privacy & Data Masking: Which PII, financial, or confidential records must be masked before model inference?

Examples: Tax IDs, compensation, medical or banking records masked via Presidio with zero data retention.

6.2 Immutable Tracing: How will the organization audit and reconstruct every tool call, prompt, and state transition?

Examples: OpenTelemetry and LangSmith traces recording immutable hashes, timestamps, and payloads for compliance audits.

## 7. Organizational Saboteurs

7.1 Political Friction & Fears: Which stakeholders might fear losing headcount, operational control, or institutional relevance?

Examples: Analysts fearing replacement, middle managers protecting team size, or IT concerned with Shadow AI.

7.2 Anti-Sabotage Framing: How do we position the deployment so internal skeptics become active sponsors?

Examples: Frame the agent as an operational triage copilot and position IT as the architecture governance owner.

## 8. Harness

8.1 Runtime & Tooling: Which connectors, sandboxes, and scoped permissions does the agent need to execute safely?

Examples: Specialized PDF OCR, read-only database MCP server, isolated Docker sandbox, and Slack/Teams bot.

8.2 Memory & State: How will the agent persist conversation state, episodic checkpoints, and domain rules?

Examples: LangGraph state checkpointing in PostgreSQL, bounded context windows, and hybrid vector retrieval.

8.3 Continuous Evals: Which golden datasets and regression gates will certify accuracy before every production release?

Examples: Automated Braintrust suite with 200 adversarial historical cases executed on every CI/CD pull request.

## 9. Value Anchoring & ROI

9.1 Dual Bleed Baseline: What is the current monthly burn across manual labor hours, overtime, and legacy SaaS seats?

Examples: 12 FTEs x $4,500/mo + $6,000 in overtime + $5,500 in redundant legacy ticketing licenses.

9.2 Net P&L Savings: What auditable cost reduction hits the P&L after deducting cloud and token run-rate?

Examples: $42k/mo gross operational savings minus $6k/mo inference & infra = $36k/mo net CFO-verified savings.

9.3 Pilot Payback Window: Within how many months must the initial engineering investment break even in production?

Examples: $30k pilot investment fully amortized within 45 to 60 days of production rollout.

## 10. From Pilot Success to Rollout

10.1 Sandbox Acceptance Gate: Which deterministic accuracy and resolution threshold certifies pilot success at Day 5?

Examples: 75% to 80% autonomous end-to-end resolution with zero violations on deterministic guardrails.

10.2 Executive Co-Author Sign-off: Which business, IT, and finance leaders jointly sign the production acceptance report?

Examples: Joint sign-off by the VP of Operations, Enterprise Architect, and Financial Controller.

10.3 Production Rollout Trigger: What pre-agreed milestone unlocks full-scale production deployment and rebate credit?

Examples: Upon hitting the Day-5 eval gate in sandbox, the production rollout contract unlocks with 100% pilot rebate.

An engineering lab with over five years of shipping AI products and resilient agent architectures in production.

Rua Pais Leme, 215 Conjunto 1713 Pinheiros, São Paulo

- Agentic Bootcamp

- Advisory

- Enterprise MCP

- The Agentic Pilot Canvas

- Blog

- Contact Us

- LangChain & LangGraph

- Snowflake AI Data Cloud

- Databricks Lakehouse

- Braintrust Evals

Architecture field notes & playbooks sent to your corporate inbox.
