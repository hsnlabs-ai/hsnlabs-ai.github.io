---
title: "Honeycomb Protocol (HACP v1.0.0) · Stigmergic Agent Coordination · hsnlabs"
description: "Open stigmergic coordination protocol for long-horizon autonomous AI swarms: dynamic capability handshake, typed graph envelopes, and SQLite WAL pre-inference atomic idempotency."
url: "https://hsnlabs.ai/en/products/honeycomb-protocol/"
locale: "en"
updatedAt: "2026-11-02T16:40:00Z"
---

# Honeycomb Agent Coordination Protocol (HACP v1.0.0)

> Open stigmergic coordination protocol for long-horizon autonomous AI swarms by **hsnlabs**.

- **Official Page (EN):** https://hsnlabs.ai/en/products/honeycomb-protocol/
- **Official Page (PT-BR):** https://hsnlabs.ai/produtos/honeycomb-protocol/
- **Technical Whitepaper:** https://hsnlabs.ai/en/products/honeycomb-protocol/whitepaper/
- **GitHub Repository (MIT):** https://github.com/hsnlabs-ai/honeycomb-protocol
- **RFC Specification (`HACP-RFC-0001`):** https://github.com/hsnlabs-ai/honeycomb-protocol/blob/main/docs/SPECIFICATION.md

## The Four Architectural Pillars

1. **Dynamic Capability Handshake (`HoneycombHandshake`):** Mutual verification flow (`HONEYCOMB_SESSION_INIT` / `HONEYCOMB_HANDSHAKE_ACK`) issuing scoped capability grants (`hcgrant1.<digest>`).
2. **Strict Envelope with Open Graph Primitives (`HoneycombEnvelope`):** Pydantic v2 header metadata paired with universal graph primitives (`node_id`, `edges`, `confidence_score`) and an open `properties` dictionary.
3. **Pre-Inference Atomic Idempotency & Double-ACK (`HoneycombIdempotencyGuard`):** Deterministic SHA-256 `target_scope_hash` locks persisted in SQLite WAL (`honeycomb_idempotency_keys`) plus two-phase `HONEYCOMB_DOUBLE_ACK` verification.
4. **Stateful Resume Tokens & Formal Session Teardown:** Signed `hcrt1` tokens for multi-day mission pauses and mandatory `HONEYCOMB_SESSION_TEARDOWN` queue deallocation.
