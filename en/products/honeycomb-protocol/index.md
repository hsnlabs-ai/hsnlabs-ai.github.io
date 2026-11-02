# Honeycomb Protocol · Stigmergic Agent Coordination & Atomic Idempotency · hsnlabs

**HACP-RFC-0001 · v1.0.0 · Open Platform · MIT License**

The **Honeycomb Agent Coordination Protocol (HACP)** operates at the semantic decentralized coordination layer—replacing noisy, quadratic point-to-point natural language agent chatter with durable, strongly-typed graph traces and pre-inference atomic idempotency locks on SQLite WAL.

- **GitHub Repository**: https://github.com/hsnlabs-ai/honeycomb-protocol
- **Formal Specification (HACP-RFC-0001)**: https://github.com/hsnlabs-ai/honeycomb-protocol/blob/main/docs/SPECIFICATION.md
- **Launch Whitepaper**: https://hsnlabs.ai/en/products/honeycomb-protocol/whitepaper/

## The Four Architectural Pillars

1. **P1 · Dynamic Capability Handshake**: Mutual verification via `HONEYCOMB_SESSION_INIT` and scoped `hcgrant1` authorization tokens via `HONEYCOMB_HANDSHAKE_ACK`.
2. **P2 · Strict Envelope with Open Graph Primitives**: Pydantic v2 `HoneycombEnvelope` and `HoneycombPayload` separating causal routing metadata from universal graph primitives and an open `properties` dictionary.
3. **P3 · Pre-Inference Atomic Idempotency & Double-ACK**: Deterministic SHA-256 `target_scope_hash` locking in SQLite WAL (`honeycomb_idempotency_keys`) and two-phase `HONEYCOMB_DOUBLE_ACK` verification.
4. **P4 · Multi-Day Resume & Formal Teardown**: Integrity-signed `hcrt1` continuation tokens and mandatory `HONEYCOMB_SESSION_TEARDOWN` queue deallocation.
