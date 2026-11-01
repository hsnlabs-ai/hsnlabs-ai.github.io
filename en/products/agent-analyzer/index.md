---
title: "Agent Analyzer · Surface Topology Mapper & LangGraph Reconstructor · hsnlabs"
description: "Single-probe black-box conversational agent topology mapper (W0–W5) for WhatsApp & LangGraph StateGraph reconstruction by hsnlabs."
url: "https://hsnlabs.ai/en/products/agent-analyzer/"
locale: "en"
updatedAt: "2026-11-01T19:40:00Z"
---

# Agent Analyzer · Surface Topology Mapper & LangGraph Reconstructor · hsnlabs

> Single-probe black-box conversational agent topology mapper (W0–W5) for WhatsApp & LangGraph StateGraph reconstruction by hsnlabs.

# Agent Analyzer Single-probe black-box conversational agent topology mapper for WhatsApp & LangGraph.

Reverse-engineers hidden LangGraph StateGraph state machines from the surface using a single WhatsApp session. Maps static guardrails, conditional routers, subadditive parallel fan-outs, and checkpointer persistence without source-code access.

## The Six-Wave Sequential Probing Protocol

Progressive, non-destructive surface mapping from initial black-box unprobed state to canary checkpointer persistence verification.

### W0 · Initial Black-Box Baseline
Initializes graph baseline topology with single unobserved black-box node (__start__ -> unknown_blackbox_node -> __end__) and baseline ping calibration.

### W1 · Surface Guardrails & Routing
Measures net inference latency below 600ms to isolate static regex/keyword blocks from semantic router LLM pivots between 600ms and 1800ms.

### W2 · Read-Only Tools Discovery
Executes read-only probes across catalog queries, inventory lookups, discount policy rules, and scheduling slots without side effects.

### W3 · Write Dry-Run & HITL Gate
Probes mutable actions (booking creation, refund reversal) verifying human-in-the-loop interrupt_before boundaries and confirmation handoffs.

### W4 · Subadditive Parallel Fan-Out
Mathematical subadditivity proof (Ratio = T_compound / (T_A + T_B) <= 0.72) to decisively separate LangGraph Send() parallel branches from serial conditional routes.

### W5 · Canary Checkpointer Memory
Injects canary tokens across topic interrupts to audit thread memory retention and verify SqliteSaver/PostgresSaver state persistence.

## Blueprint Studio & Deterministic Exporters

Interactive React 19 workspace with Wave Time-Travel scrubber and pure-function LangGraph state machine generation.

### LangGraph StateGraph Visual Topology
Full-screen visual representation of discovered nodes, net latency telemetry, model tier estimation, and two-pass verification badges (1/2 hypothesis -> 2/2 verified).

### Compilable Code & Diagnostic Deliverables
Instant deterministic post-W5 generation of runnable LangGraph Python skeleton, Mermaid flowcharts, JSON topology schema, and Markdown forensic audit report.

## Single-Probe Technical Architecture

Decouples internal 5-table SQLite WAL storage from external WhatsApp probing, eliminating split-brain multi-bot coordination.

- **Two-Pass Sequential Protocol (N=1):** Discovery pass followed by session boundary reset (/reset) and verification replay.
- **Net Inference Decomposition:** Subtracts WebSocket ping calibration (L_net = max(0, RTT - 2 * WS_Ping)).
- **5-Table SQLite WAL Store:** Transactional persistence in data/analyzer.sqlite3.
- **Non-Destructive WAHA Bridge (:3001):** Persistent client connections with anti-ban jitter floor (>= 2.0s).
- **Four Pure-Function Exporters:** langgraph_skeleton.py, topology.mmd, topology.json, and diagnostic_report.md.

## Production Reverse-Engineering Use Cases

Built for security teams, AI architects, and red-team auditors verifying external agent surfaces without internal repository access.

1. **Competitive Intelligence & Benchmarking:** Mapping competitor conversational architecture on WhatsApp to uncover internal tools, routing strategies, model tiers, and latency boundaries.
2. **Security Audits & HITL Boundary Verification:** Verifying whether high-stakes operations enforce human-in-the-loop interrupts before committing mutations.
3. **Legacy Migration to LangGraph:** Extracting undocumented legacy chatbot flows and automatically exporting clean, compilable LangGraph StateGraph Python skeletons.

## Open Source & Technical Specification

Full source code, including the FastAPI backend, 5-table SQLite WAL store, 6-wave protocol runner, React 19 Blueprint Studio, and 4 deterministic exporters, is available on GitHub under the MIT License:
https://github.com/hsnlabs-ai/agent-analyzer
