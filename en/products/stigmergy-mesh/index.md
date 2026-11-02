# Stigmergy Mesh — Biomimetic Indirect Coordination & Collective Immune Memory

**Version:** `v0.1.0` · **License:** MIT · **Runtime:** Python `>=3.11`  
**Repository:** [https://github.com/hsnlabs-ai/stigmergy-mesh](https://github.com/hsnlabs-ai/stigmergy-mesh)

## Overview

**Stigmergy Mesh** is an open-source Python library by **hsnlabs** that provides zero-daemon, zero-broker indirect coordination and adaptive immune memory for multi-agent systems over **SQLite WAL** and **Redis Lua**.

## Key Capabilities

1. **Continuous Lazy Exponential Pheromone Decay** — Exact closed-form exponential evaporation (`math.exp`) evaluated inline on read/write with zero background threads.
2. **Probabilistic ACO Boltzmann Softmax Routing** — Balances positive reinforcement (`tau_pos`), alarm repulsion (`tau_neg`), heuristic priors, and an exploration floor (`epsilon`) for automatic post-outage self-healing.
3. **K-Origin Anti-Sybil Quorum Circuit Breaker** — Requires `K` distinct worker origins within a sliding time window before entering `HARD_QUARANTINE`, with `1/sqrt(n)` per-origin deposit damping.
4. **Structural Antigen Fingerprinting & Validation Oracles** — 64-bit structural payload fingerprints (`antigen_hash`) and HMAC-SHA256 signed `TrailReceipt` tokens prevent positive trail poisoning.
