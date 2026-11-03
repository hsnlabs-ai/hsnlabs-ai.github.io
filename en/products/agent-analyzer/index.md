---
title: "Agent Analyzer · Topological Mapper & LangGraph Reverse Engineering · hsnlabs"
description: "Single-probe black-box conversational agent topology mapper for WhatsApp and LangGraph StateGraph reconstruction by hsnlabs."
url: "https://hsnlabs.ai/en/products/agent-analyzer/"
locale: "en"
updatedAt: "2026-11-03T21:11:40Z"
---

# Agent Analyzer · Topological Mapper & LangGraph Reverse Engineering · hsnlabs

> Single-probe black-box conversational agent topology mapper for WhatsApp and LangGraph StateGraph reconstruction by hsnlabs.

# Agent Analyzer Single-probe black-box conversational agent topology mapper for WhatsApp & LangGraph.

Reverse-engineers hidden LangGraph StateGraph state machines from the surface using a single WhatsApp session. The system extracts static guardrails, conditional routers, subadditive parallel fan-outs, and checkpointer persistence without source-code access.

## The Six-Wave Sequential Probing Protocol

Progressive, non-destructive surface mapping from baseline calibration to memory checkpointer persistence auditing.

### W0 · Initial Black-Box Baseline

Initializes graph baseline topology with a single unobserved black-box node (__start__ → unknown_blackbox_node → __end__). Conducts WebSocket ping calibration to establish channel transport latency.

### W1 · Surface Guardrails & Routing

Measures net inference latency below 600ms to isolate static regex or keyword blocks. Latencies between 600ms and 1800ms pinpoint semantic classification pivots executed by LLM entry routers.

### W2 · Read-Only Tools Discovery

Executes read-only probes across product catalogs, pricing tiers, inventory counts, and scheduling slots without side effects, mapping external tool integrations.

### W3 · Write Dry-Run & HITL Gate

Probes mutating intents such as booking creations and refund reversals, verifying whether the target enforces confirmation boundaries and human handoffs before committing state.

### W4 · Subadditive Parallel Fan-Out

Mathematical subadditivity proof (Ratio = T_compound / (T_A + T_B) ≤ 0.72) to decisively confirm parallel execution via LangGraph Send() fan-out versus serial conditional routing.

### W5 · Canary Checkpointer Memory

Injects unique canary tokens followed by abrupt topic pivots to audit context retention across thread interrupts, verifying SqliteSaver or PostgresSaver state persistence.

## Latency Decomposition & Verification

Empirical formulation separating carrier transport overhead from model inference and external tools.

### Net Inference Latency Formula

Raw observed round-trip times include messaging hop delays. The analyzer subtracts calibrated WebSocket round-trip times (L_net = max(0, RTT - 2 * WS_Ping)) to classify node tiers accurately:

- • Static Guardrails: Net latency < 600ms representing edge regex and token filters.

- • Semantic Routers: Net latency 600ms to 1800ms representing lightweight routing models.

- • Database & APIs: Net latency 1800ms to 3200ms indicating external synchronous tool calls.

- • Core Reasoning: Net latency > 3200ms denoting deep multi-step synthesis.

### Two-Pass Sequential Replay Protocol

Eliminating multi-bot consensus overhead, the analyzer uses a deterministic two-pass verification protocol through a single channel:

- • Pass 1 Discovery: Initial probe sequence discovering potential transition paths and nodes.

- • Boundary Reset: Issues a session reset command (/reset) to clear volatile conversation buffer.

- • Pass 2 Verification: Re-executes exact probe paths to measure deterministic edge repeatability.

- • Node Certification: Promotes node confidence from single-pass hypothesis to replay verified (2/2).

## Single-Probe Architecture & Persistence

Transactional SQLite WAL store, biometric jitter pacing, and zero-risk local simulation.

Attaches non-destructively to a single WAHA Multi-Device session on port 3001, eliminating multi-SIM carrier overhead and reducing ban surfaces.

Enforces log-normal reading delays and simulated typing presence with an inviolable ≥ 2.0s turn gap floor to mirror natural human cadence.

Transactional persistence in data/analyzer.sqlite3 tracking target scans, chronological turns, topology nodes, directed edges, and settings.

Includes an in-memory deterministic target simulator allowing immediate execution of all 6 waves and artifact generation without external API keys.

Compiles verified SQLite topology in <15ms into executable LangGraph Python code, Mermaid documentation diagrams, JSON schemas, and Markdown reports.

## Production Reverse-Engineering Use Cases

Designed for security auditors, AI architects, and red-team engineers validating conversational surface systems.

Mapping competitor conversational architecture on WhatsApp to uncover internal tools, routing strategies, model tiers, and latency boundaries.

Verifying whether high-stakes operations (refunds, order updates, PII sharing) enforce human-in-the-loop interrupts before committing mutations.

Extracting undocumented legacy chatbot flows and automatically exporting clean, compilable LangGraph StateGraph Python skeletons for modernization.

## Open Source & Technical Specification

Full source code, including the FastAPI backend, 5-table SQLite WAL store, 6-wave protocol runner, React 19 Blueprint Studio, and 4 deterministic exporters, is available on GitHub under the MIT License.

An engineering lab with over five years of shipping AI products and resilient agent architectures in production.

Rua Pais Leme, 215 Conjunto 1713 Pinheiros, São Paulo

- Agentic Bootcamp™

- Products

- Advisory

- Enterprise MCP

- The Agentic Canvas™

- Blog

- Contact Us

- LangChain & LangGraph

- Snowflake AI Data Cloud

- Databricks Lakehouse

Architecture field notes & playbooks sent to your corporate inbox.

Utilizamos telemetria para avaliar o desempenho do sistema sob normas da LGPD. Consulte nossa Política de Privacidade.
