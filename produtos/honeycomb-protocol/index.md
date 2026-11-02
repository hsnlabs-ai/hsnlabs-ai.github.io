# Protocolo Honeycomb · Coordenação Estigmérgica e Idempotência Atômica · hsnlabs

**HACP-RFC-0001 · v1.0.0 · Plataforma Aberta · Licença MIT**

O **Protocolo Honeycomb** atua na camada semântica de coordenação descentralizada, substituindo trocas ruidosas de mensagens ponto a ponto em linguagem natural por marcas duráveis em grafo e bloqueio atômico de idempotência pré-inferência sobre SQLite WAL.

- **Repositório GitHub**: https://github.com/hsnlabs-ai/honeycomb-protocol
- **Especificação Formal**: https://github.com/hsnlabs-ai/honeycomb-protocol/blob/main/docs/SPECIFICATION.md
- **Whitepaper Técnico**: https://hsnlabs.ai/en/products/honeycomb-protocol/whitepaper/

## Os Quatro Pilares Arquiteturais

1. **P1 · Aperto de Mão Dinâmico**: Anúncio de capacidades ativas via `HONEYCOMB_SESSION_INIT` e concessão de escopo delimitado via `HONEYCOMB_HANDSHAKE_ACK`.
2. **P2 · Envelope Estrito com Primitivas Abertas**: Contrato Pydantic v2 `HoneycombEnvelope` e `HoneycombPayload` com nós, arestas, confiança e dicionário `properties`.
3. **P3 · Governança e Idempotência Atômica**: Bloqueio atômico por `target_scope_hash` na tabela `honeycomb_idempotency_keys` em SQLite WAL e validação em dois tempos via `HONEYCOMB_DOUBLE_ACK`.
4. **P4 · Ciclo de Vida e Encerramento Formal**: Tokens assinados `hcrt1` para retomada após pausas de múltiplos dias e encerramento explícito via `HONEYCOMB_SESSION_TEARDOWN`.
