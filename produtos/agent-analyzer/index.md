---
title: "Agent Analyzer · Mapeador Topológico e Engenharia Reversa LangGraph · hsnlabs"
description: "Mapeador topológico em caixa-preta via sonda única (W0–W5) para reconstrução de StateGraph em LangGraph no WhatsApp pela hsnlabs."
url: "https://hsnlabs.ai/produtos/agent-analyzer/"
locale: "pt-BR"
updatedAt: "2026-11-01T19:40:00Z"
---

# Agent Analyzer · Mapeador Topológico e Engenharia Reversa LangGraph · hsnlabs

> Mapeador topológico em caixa-preta via sonda única (W0–W5) para reconstrução de StateGraph em LangGraph no WhatsApp pela hsnlabs.

# Agent Analyzer Mapeador topológico em caixa-preta via sonda única para WhatsApp e LangGraph.

Engenharia reversa de máquinas de estado LangGraph StateGraph a partir da superfície usando apenas 1 sessão de WhatsApp. Mapeia guardrails estáticos, roteadores condicionais, paralelismo subaditivo e persistência de checkpointer sem acesso ao código-fonte.

## Protocolo Sequencial de Seis Ondas (W0 a W5)

Mapeamento de superfície progressivo e não-destrutivo desde o estado inicial até a auditoria de persistência de checkpointer.

### W0 · Linha de Base Caixa-Preta
Inicializa o grafo de referência com um único nó opaco (__start__ -> unknown_blackbox_node -> __end__) e calibra a latência base do canal.

### W1 · Guardrails de Borda e Roteamento
Isola latência líquida abaixo de 600ms para filtros estáticos de regex/palavras-chave e diferencia pivôs de roteadores semânticos entre 600ms e 1800ms.

### W2 · Descoberta de Ferramentas de Leitura
Executa sondas somente leitura em catálogo, consulta de preços, verificação de estoque e checagem de horários sem efeitos colaterais.

### W3 · Dry-Run de Escrita e Portão Humano (HITL)
Sonda ações mutativas (criação de pedidos, estornos) validando limites de interrupção interrupt_before e transbordo obrigatório para operador humano.

### W4 · Paralelismo Subaditivo (E)
Prova matemática de subaditividade (Razão = T_composto / (T_A + T_B) <= 0.72) comprovando execução concorrente via Send() versus rotas condicionais OU.

### W5 · Memória de Checkpointer e Tokens Canários
Injeta tokens canários após interrupções de assunto para auditar retenção de contexto de sessão em SqliteSaver ou PostgresSaver.

## Blueprint Studio e Exportadores Determinísticos

Espaço de trabalho interativo em React 19 com scrubber de time-travel e geração de código LangGraph em funções puras.

### Topologia Visual LangGraph StateGraph
Visualização em tela cheia dos nós descobertos, telemetria de latência líquida, estimativa de modelo e selos de validação em dois passes (1/2 hipótese -> 2/2 verificado).

### Código Compilável e Relatórios Forenses
Geração determinística instantânea de esqueleto Python compilável em LangGraph, fluxogramas Mermaid, esquema JSON de topologia e dossiê forense completo em Markdown.

## Arquitetura Técnica de Sonda Única (N=1)

Elimina complexidade de múltiplos bots através de persistência assimétrica em SQLite WAL de 5 tabelas e transporte calibrado no WAHA.

- **Protocolo de Replay em Dois Passes (N=1):** Sondagem sequencial com 1 único número (Pass 1), reset de fronteira de contexto (/reset) e replay de verificação (Pass 2).
- **Decomposição de Latência Líquida:** Subtrai a calibração de ping WebSocket (L_net = max(0, RTT - 2 * WS_Ping)).
- **Persistência SQLite WAL (5 Tabelas):** Armazenamento transacional em data/analyzer.sqlite3.
- **Conexão Não-Destrutiva ao WAHA (:3001):** Conexões persistentes via httpx.AsyncClient com piso de jitter anti-ban (>= 2.0s).
- **Quatro Exportadores Pós-W5:** langgraph_skeleton.py, topology.mmd, topology.json e diagnostic_report.md.

## Casos de Uso em Ambientes de Produção

Desenvolvido para times de segurança, arquitetos de IA e equipes de red-team auditando agentes externos sem acesso ao repositório de código.

1. **Inteligência Competitiva e Benchmarking:** Mapeamento da arquitetura conversacional de concorrentes no WhatsApp para descobrir ferramentas internas, estratégias de roteamento, tiers de modelo e limites de latência.
2. **Auditorias de Segurança e Fronteiras HITL:** Verificação de operações de alto risco garantindo que interrupções humanas aconteçam antes da mutação de dados.
3. **Modernização de Chatbots Legados para LangGraph:** Extração de fluxos conversacionais legados não documentados com exportação direta para código Python StateGraph compilável.

## Código Aberto e Especificação Técnica

Todo o código, incluindo o servidor FastAPI, armazenamento transacional em SQLite WAL de 5 tabelas, executor do protocolo de 6 ondas, Blueprint Studio em React 19 e os 4 exportadores determinísticos, está disponível sob a licença MIT no GitHub:
https://github.com/hsnlabs-ai/agent-analyzer
