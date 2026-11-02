# Swarm Self-Healing (SSH) — Autonomous Swarm Homeostasis & Sub-5s Hot Failover

> Pure-Python resilience, thermal governance, and resource protection runtime for distributed AI agent swarms (SSH-SPEC-0001 · v0.1.0 · MIT License).

- **Canonical URL:** https://hsnlabs.ai/en/products/swarm-self-healing/
- **Repository:** https://github.com/hsnlabs-ai/swarm-self-healing
- **Specification:** https://github.com/hsnlabs-ai/swarm-self-healing/blob/main/docs/SPECIFICATION.md
- **Version:** 0.1.0
- **License:** MIT
- **Runtime:** Python 3.11+ (Pydantic v2, AsyncIO, Hexagonal Architecture)

## Core Pillars

1. **Sub-5-Second Hot Standby Promotion (`HomeostasisController`):** Monitors active Scout pool against `target_active_count`, immediately promoting a warm `STANDBY_READY` agent in `< 5s` when an active worker transitions to `BANNED` or `COOLING_DOWN`.
2. **Thermal Governance with Hysteresis (`HeatPolicy`):** Bounded `[0.0, 1.0]` thermal score tracking discrete friction (`normal_turn +0.06`, `TurnTimeout +0.18`, `CaptchaOrBlock +0.35`, `BanDetected -> 1.0`) and passive cooling (`-0.08/min`), with a `0.35..0.78` hysteresis deadband.
3. **3-Tier Network Affinity Guard (`NetworkAffinityGuard`):** Enforces 1:1 identity-to-proxy binding while tolerating legitimate ISP DHCP renewals within the same ASN and `/24` IPv4 (or `/48` IPv6) subnet, raising `ProxyAffinityViolationError` on anomalous jumps.
4. **Resource Circuit Breaker (`ResourceCircuitBreaker`):** Sliding-window breaker (5 failures across 600s) that trips to `OPEN` and blocks runaway SIM/eSIM and proxy expenditure until explicit operator `unlock()`.
