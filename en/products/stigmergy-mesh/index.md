---
title: "Stigmergy Mesh · Biomimetic Pheromone Routing & Collective Immune Memory · hsnlabs"
description: "Zero-daemon Python library by hsnlabs for multi-agent indirect coordination, continuous lazy exponential pheromone decay, ACO Boltzmann routing, K-Origin Anti-Sybil quorum circuit breaking, and structural antigen fingerprinting over SQLite WAL and Redis Lua."
url: "https://hsnlabs.ai/en/products/stigmergy-mesh/"
locale: "en"
updatedAt: "2026-11-03T21:11:40Z"
---

# Stigmergy Mesh · Biomimetic Pheromone Routing & Collective Immune Memory · hsnlabs

> Zero-daemon Python library by hsnlabs for multi-agent indirect coordination, continuous lazy exponential pheromone decay, ACO Boltzmann routing, K-Origin Anti-Sybil quorum circuit breaking, and structural antigen fingerprinting over SQLite WAL and Redis Lua.

# Stigmergy Mesh Biomimetic indirect coordination & collective immune memory for multi-agent systems.

A zero-daemon, zero-broker Python library (v0.1.0) that coordinates distributed agent workers through continuous lazy exponential pheromone decay, ACO Boltzmann softmax routing, K-Origin Anti-Sybil quorum circuit breaking, and structural antigen fingerprinting over SQLite WAL and Redis Lua.

## The Four Bio-Mathematical Pillars

Engineered to prevent cascading upstream outages, synchronized half-open thundering herds, single-worker Sybil false trips, and positive trail poisoning from hallucinated responses.

### P1 · Continuous Lazy Exponential Decay

Attractive (tau_pos) and repulsive alarm (tau_neg) pheromones evaporate continuously via exact closed-form exponential decay evaluated inline at read and write time. Zero background sweeper threads, zero cron jobs, and zero idle CPU overhead.

### P2 · ACO Boltzmann Softmax Routing

Candidate routes are sampled via numerically stable log-sum-exp Boltzmann softmax combining effective pheromone score and prior heuristics with an exploration floor (epsilon) that enables smooth, autonomous self-healing as alarm traces evaporate.

### P3 · K-Origin Anti-Sybil Quorum Gate

Protects shared routes with a three-state immune state machine (HEALTHY, SOFT_THROTTLE, HARD_QUARANTINE). Entering HARD_QUARANTINE requires both high repulsive pheromone and confirmation from at least K distinct worker origins within a sliding window.

### P4 · Structural Antigens & Validation Oracles

Extracts 64-bit PII-free structural payload fingerprints (antigen_hash) to isolate payload-specific failures from full endpoint outages, paired with synchronous ValidationOracle hooks and HMAC-SHA256 signed TrailReceipt tokens.

## Empirical Swarm Benchmarks & Differentiation

Validated across 1,000 multi-agent episodes with 8 concurrent workers under severe upstream outage, Sybil fault injection, and silent schema hallucination.

### 1,000-Episode Swarm Simulation Results

When a primary LLM or tool provider suffers a 95% outage mid-run, stateless routers continue sending traffic into the failing endpoint. Stigmergy Mesh immediately shifts swarm traffic via repulsive alarm pheromones and self-heals upon recovery.

- • 96.2% Overall Episode Success Rate: Outperforms stateless round-robin routing (67.1%) across normal, outage, Sybil, and recovery phases.

- • 89.2% Reduction in Wasted Failed Calls: Cuts wasted upstream failure calls during severe outages from 324 down to 35 across 8 workers.

- • 0.0% Sybil Hard-Quarantine False Trips: Single compromised worker flooding false errors never triggers HARD_QUARANTINE when K=3.

- • 21-Episode Post-Recovery Convergence: Automatically re-adopts the recovered primary provider without manual intervention or thundering herds.

### Why Not Standard Circuit Breakers?

Traditional binary circuit breakers (CLOSED / OPEN / HALF_OPEN) were designed for homogeneous microservices·not stochastic multi-agent fleets where failures depend on payload structure and semantic validity.

- • Versus Binary Circuit Breakers: Replaces rigid step-function thresholds with continuous Boltzmann probability shifts and gradual evaporation.

- • Payload-Aware Antigen Isolation: Quarantines only the specific failing payload schema (antigen_hash) while keeping the endpoint healthy for other tasks.

- • Anti-Poisoning Validation Oracles: Blocks fast-failing HTTP 200 hallucinations from reinforcing positive pheromone trails.

- • Dual Atomic Storage Parity: Identical mathematical semantics across local zero-dependency SQLite WAL and distributed Redis Lua scripts.

## Substrate & Diagnostic Engineering

Production-grade modules engineered for atomic concurrency, cryptographic receipt verification, and real-time terminal observability.

Zero-dependency local multi-process backend using BEGIN IMMEDIATE transactions, 2,000-origin circular buffers, and lazy LRU antigen compaction.

Single-roundtrip server-side Lua scripts using redis.call('TIME') and cjson for race-free multi-host pheromone decay and quorum updates.

Stateless signed receipts with single-use event_id deduplication for delayed asynchronous reward confirmation after downstream verification.

Sublinear per-origin deposit damping prevents any single runaway worker loop from saturating positive or negative pheromone concentrations.

Built-in stigmergy-mesh CLI with inspect, explain, and reset subcommands to audit live decayed scores and Boltzmann routing probabilities.

## Production Engineering Use Cases

Drop-in collective intelligence for engineering teams operating multi-provider LLM routers, tool-calling fleets, and autonomous research swarms.

Dynamically balance traffic across OpenAI, Anthropic, and Gemini endpoints based on live validated accuracy and rate-limit repulsion without central proxies.

Isolate toxic SQL dialects, malformed API payloads, or failing scraper targets via 64-bit antigen hashes while preserving normal traffic on the same tool.

Mint HMAC-SHA256 TrailReceipts during route selection and deposit positive or negative pheromones minutes later when unit tests or reviewers confirm the outcome.

## Open Source Python SDK & Formal Specification

The complete Stigmergy Mesh library·including the closed-form math engine, SQLite WAL and Redis Lua backends, ValidationOracle hooks, CLI diagnostics, and 1,000-episode benchmark suite·is available under the MIT License on GitHub.

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
