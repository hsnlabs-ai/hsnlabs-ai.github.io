# Swarm Self-Healing (SSH) — Homeostase Autônoma e Failover em < 5s para Enxames

> Runtime Python puro para resiliência operacional, governança térmica e proteção de recursos em enxames distribuídos de agentes de IA (SSH-SPEC-0001 · v0.1.0 · Licença MIT).

- **URL Canônica:** https://hsnlabs.ai/produtos/swarm-self-healing/
- **Repositório:** https://github.com/hsnlabs-ai/swarm-self-healing
- **Especificação Técnica:** https://github.com/hsnlabs-ai/swarm-self-healing/blob/main/docs/SPECIFICATION.md
- **Versão:** 0.1.0
- **Licença:** MIT
- **Runtime:** Python 3.11+ (Pydantic v2, AsyncIO, Arquitetura Hexagonal)

## Pilares Arquiteturais

1. **Promoção Hot Standby em < 5s (`HomeostasisController`):** Monitora o pool ativo em relação a `target_active_count`, promovendo imediatamente um agente aquecido em `STANDBY_READY` em `< 5s` quando um worker ativo transita para `BANNED` ou `COOLING_DOWN`.
2. **Governança Térmica com Histerese (`HeatPolicy`):** Escore térmico limitado em `[0.0, 1.0]` contabilizando fricção discreta (`normal_turn +0.06`, `TurnTimeout +0.18`, `CaptchaOrBlock +0.35`, `BanDetected -> 1.0`) e resfriamento passivo (`-0.08/min`), com banda morta de histerese `0.35..0.78`.
3. **Guarda de Afinidade de Rede em 3 Níveis (`NetworkAffinityGuard`):** Impõe vínculo estrito 1:1 entre identidade e proxy tolerando renovações legítimas de DHCP no mesmo ASN e sub-rede `/24` IPv4 (ou `/48` IPv6), lançando `ProxyAffinityViolationError` em desvios anômalos.
4. **Circuit Breaker de Recursos (`ResourceCircuitBreaker`):** Disjuntor de janela deslizante (5 falhas em 600s) que abre (`OPEN`) e bloqueia gastos descontrolados da incubadora até inspeção e `unlock()` explícito.
