---
title: "Protocolo Honeycomb (HACP v1.0.0) · Coordenação Estigmérgica de Agentes · hsnlabs"
description: "Protocolo aberto de coordenação estigmérgica para enxames autônomos de IA: aperto de mão dinâmico, envelopes em grafo tipados e idempotência atômica pré-inferência em SQLite WAL."
url: "https://hsnlabs.ai/produtos/honeycomb-protocol/"
locale: "pt-BR"
updatedAt: "2026-11-02T16:40:00Z"
---

# Protocolo Honeycomb (HACP v1.0.0)

> Protocolo aberto de coordenação estigmérgica para enxames autônomos de longa duração pela **hsnlabs**.

- **Página Oficial (PT-BR):** https://hsnlabs.ai/produtos/honeycomb-protocol/
- **Página Oficial (EN):** https://hsnlabs.ai/en/products/honeycomb-protocol/
- **Whitepaper Técnico (EN):** https://hsnlabs.ai/en/products/honeycomb-protocol/whitepaper/
- **Repositório GitHub (MIT):** https://github.com/hsnlabs-ai/honeycomb-protocol
- **Especificação Formal (`HACP-RFC-0001`):** https://github.com/hsnlabs-ai/honeycomb-protocol/blob/main/docs/SPECIFICATION.md

## Os Quatro Pilares Arquiteturais

1. **Aperto de Mão Dinâmico (`HoneycombHandshake`):** Verificação mútua (`HONEYCOMB_SESSION_INIT` / `HONEYCOMB_HANDSHAKE_ACK`) com concessão de escopo delimitado (`hcgrant1.<digest>`).
2. **Envelope Estrito com Primitivas Abertas (`HoneycombEnvelope`):** Separação estrita entre metadados causais e carga útil em grafo (`node_id`, `edges`, `confidence_score`) com campo aberto `properties`.
3. **Governança e Idempotência Atômica (`HoneycombIdempotencyGuard`):** Bloqueio pré-inferência em SQLite WAL (`honeycomb_idempotency_keys`) por `target_scope_hash` e confirmação em dois tempos (`HONEYCOMB_DOUBLE_ACK`).
4. **Ciclo de Vida e Encerramento Formal:** Sessões assíncronas retomáveis por tokens assinados (`hcrt1`) e destruição automática de filas em `HONEYCOMB_SESSION_TEARDOWN`.
