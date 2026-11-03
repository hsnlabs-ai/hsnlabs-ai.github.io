---
title: "Agent Analyzer · Mapeador Topológico e Engenharia Reversa LangGraph · hsnlabs"
description: "Mapeador topológico em caixa-preta via sonda única para reconstrução de máquinas de estado LangGraph StateGraph no WhatsApp pela hsnlabs."
url: "https://hsnlabs.ai/produtos/agent-analyzer/"
locale: "pt-BR"
updatedAt: "2026-11-03T21:11:40Z"
---

# Agent Analyzer · Mapeador Topológico e Engenharia Reversa LangGraph · hsnlabs

> Mapeador topológico em caixa-preta via sonda única para reconstrução de máquinas de estado LangGraph StateGraph no WhatsApp pela hsnlabs.

# Agent Analyzer Mapeador topológico em caixa-preta via sonda única para WhatsApp e LangGraph.

Engenharia reversa de máquinas de estado LangGraph StateGraph a partir da superfície usando apenas uma sessão de WhatsApp. O sistema extrai guardrails estáticos, roteadores condicionais, paralelismo subaditivo e persistência de checkpointer sem acesso ao código-fonte.

## Protocolo Sequencial de Seis Ondas

Mapeamento de superfície progressivo e não-destrutivo desde a calibração inicial até a auditoria de persistência de memória.

### W0 · Linha de Base Caixa-Preta

Estabelece a topologia inicial com um único nó opaco de início ao fim. O sistema executa testes prévios de ping no canal WebSocket para calibrar a oscilação da conexão antes de iniciar a inferência.

### W1 · Guardrails de Borda e Roteamento

Mede a latência líquida de inferência abaixo de 600 milissegundos para isolar bloqueios estáticos de palavras-chave. Tempos entre 600 e 1800 milissegundos identificam pivôs semânticos de roteadores de entrada.

### W2 · Descoberta de Ferramentas de Leitura

Dispara sondas somente leitura em catálogo de produtos, faixas de preços, saldo de estoque e verificação de agenda. Permite identificar integrações externas de API sem causar alterações no banco do alvo.

### W3 · Dry-Run de Escrita e Portão Humano

Sonda intenções mutativas como criação de reservas e estornos financeiros. O analisador valida se o assistente possui travas de confirmação obrigatória e transbordo prévio para operadores humanos.

### W4 · Paralelismo Subaditivo Concorrente

Avalia turnos com múltiplas intenções simultâneas. Quando a razão de latência entre a consulta combinada e a soma das consultas individuais fica abaixo de 0.72, o sistema comprova execução concorrente em LangGraph.

### W5 · Memória de Checkpointer Canário

Injeta identificadores canários exclusivos seguidos de desvios bruscos de assunto. O teste avalia a retenção exata do contexto para determinar a presença de armazenamento durável em SQLite ou PostgreSQL.

## Decomposição de Latência e Validação

Fundamentação matemática para separar atrasos de transporte, regras estáticas e raciocínio de modelos.

### Cálculo da Latência Líquida

A latência bruta observada no canal inclui a ida e volta das mensagens pelo WhatsApp. O analisador subtrai duas vezes o tempo de ping aferido no servidor de mensagens para isolar com exatidão o tempo de processamento do agente alvo.

- • Filtros Estáticos: Inferência líquida abaixo de 600 milissegundos caracterizando checagens de regex na borda.

- • Roteadores Semânticos: Inferência entre 600 e 1800 milissegundos identificando modelos rápidos de classificação.

- • Ferramentas Externas: Inferência entre 1800 e 3200 milissegundos revelando chamadas de banco e APIs.

- • Raciocínio Profundo: Inferência acima de 3200 milissegundos apontando síntese avançada de respostas.

### Replay Sequencial em Dois Passes

Para eliminar falsos positivos sem depender de enxames complexos com múltiplos números, o analisador adota um protocolo em duas etapas com uma única sessão de mensagens.

- • Passo Um: Execução exploratória inicial de sondas mapeando nós e atribuindo selo provisório de hipótese.

- • Quebra de Contexto: Envio de comando de reinicialização de sessão para garantir ponto de partida limpo.

- • Passo Dois: Reexecução controlada das mesmas trilhas para confirmar a determinística de cada transição.

- • Certificação: Elevação do nó ao nível verificado apenas quando a confirmação em dois passos é atingida.

## Arquitetura de Sonda e Persistência

Armazenamento relacional em SQLite WAL e controle biométrico de envio para proteção operacional total.

Opera com apenas um número de telefone conectado ao container WAHA na porta 3001, dispensando a gestão onerosa de frotas de chips e mitigando riscos de bloqueio.

Aplica pausas de leitura e digitação com distribuição log-normal, mantendo um piso mínimo de dois segundos entre turnos para simular o comportamento de um usuário real.

Armazena todo o histórico em banco SQLite no modo WAL, dividindo registros entre sessões de varredura, turnos cronológicos, nós mapeados, arestas direcionadas e parâmetros de conexão.

Inclui um assistente simulado em memória que permite testar as seis ondas e gerar artefatos em segundos, sem necessidade de credenciais de nuvem ou aparelhos físicos.

Converte o grafo inferido em esqueleto Python para LangGraph, diagrama Mermaid para documentação, esquema JSON para pipelines e relatório técnico em Markdown.

## Casos de Uso em Produção

Desenvolvido para engenharia reversa e conformidade arquitetural em sistemas conversacionais corporativos.

Mapeamento da topologia conversacional de concorrentes no WhatsApp para identificar ferramentas integradas, estratégias de roteamento, tiers de modelo e limites de latência.

Verificação prática em operações críticas como concessão de limites, alterações cadastrais e estornos, garantindo que o assistente respeite travas antes de persistir dados.

Extração estruturada de assistentes legados sem documentação técnica com exportação direta para código Python StateGraph moderno e tipado em LangGraph.

## Código Aberto e Especificação Técnica

Todo o código, incluindo o servidor em FastAPI, banco SQLite WAL em cinco tabelas, executor do protocolo de seis ondas, estúdio em React 19 e os quatro exportadores determinísticos, está disponível sob a licença MIT no GitHub.

Laboratório de engenharia com mais de cinco anos implementando produtos de IA e arquiteturas agenticas resilientes em produção.

Rua Pais Leme, 215 Conjunto 1713 Pinheiros, São Paulo

- Agentic Bootcamp™

- Produtos

- Advisory

- Enterprise MCP

- The Agentic Canvas™

- Blog

- Fale Conosco

- LangChain & LangGraph

- Snowflake AI Data Cloud

- Databricks Lakehouse

Notas de campo de arquitetura e playbooks no seu e-mail corporativo.

Utilizamos telemetria para avaliar o desempenho do sistema sob normas da LGPD. Consulte nossa Política de Privacidade.
