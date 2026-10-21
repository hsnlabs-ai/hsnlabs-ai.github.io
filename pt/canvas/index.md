---
title: "The Agentic Pilot Canvas v1.4 · hsnlabs"
description: "Framework aberto de arquitetura sob licença MIT para desenhar pilotos de IA agentica enterprise: ontologia de dados legados, determinismo, testes de harness e governança no CPF."
url: "https://hsnlabs.ai/pt/canvas/"
locale: "pt-BR"
updatedAt: "2026-10-17T12:40:41Z"
---

# The Agentic Pilot Canvas v1.4 · hsnlabs

> Framework aberto de arquitetura sob licença MIT para desenhar pilotos de IA agentica enterprise: ontologia de dados legados, determinismo, testes de harness e governança no CPF.

# The Agentic Pilot Canvas

## 1. Processo Alvo & Impacto

1.1 O Processo Manual: Qual trabalho manual repetitivo mais consome o tempo da equipe no fluxo atual e qual o resultado ideal quando concluído?

Exemplos comparando o fluxo atual AS-IS com o desejado TO-BE: triagem de 500 currículos, digitação de faturas no ERP, enriquecer leads no CRM.

1.2 Gargalo & Sintomas: Onde o fluxo trava e quais os sintomas visíveis dessa sobrecarga?

Ex: Horas extras recorrentes no fechamento, erros manuais de digitação, analistas agindo como digitadores.

## 2. Impacto não determinístico

2.1 Teste de Sanidade: Esse processo realmente exige a flexibilidade de um agente ou o risco não tolera margem de incerteza?

Exemplos para avaliar se precisa de IA: Cálculos fiscais e folha exigem código determinístico; interpretar e-mails caóticos e conciliar dados exige IA.

2.2 Raio de Destruição: Se o agente falhar, qual o estrago interno financeiro ou emocional e o prejuízo externo para clientes e mercado?

Exemplos de blast radius e impacto emocional: Ansiedade da equipe, sensação de desumanização, medo de queimar leads, multas e clientes VIP irritados.

## 3. Legados, conexão e dados

3.1 Onde os Dados Moram: Em quais sistemas, planilhas ou e-mails as informações desse processo estão guardadas hoje?

Exemplos: SAP S/4HANA no módulo MM, TOTVS, Salesforce, planilhas mestras no Drive ou contratos em PDF.

3.2 Dinâmica de Acesso: Como a equipe acessa esses dados no dia a dia e com que frequência eles são atualizados?

Ex: Consulta diária via tela, APIs, ou exportação de CSV; isolamento em réplica read-only no staging D1.

3.3 Engenharia Reversa como Oportunidade: Quais regras ocultas em planilhas ou sistemas antigos podemos auditar para virar documentação viva?

Ex: Mapear 30 stored procedures legadas ou macros antigas do Excel para transformá-las em código tipado.

## 4. Ontologia Operacional

4.1 Objetos do Mundo Real: Quais são os itens centrais desse trabalho que o agente precisa reconhecer para entender a operação?

Ex. RH: Colaborador, Vaga, Avaliação. Finanças: Fatura, PedidoCompra, Fornecedor. Vendas: Lead, Oportunidade.

4.2 Ações Tipadas & Invariantes: Quais as únicas ações que o agente pode executar e qual regra nunca pode ser violada?

Exemplos de ações tipadas: ClassificarDiscrepancia, NotificarGestor. Invariante: agente nunca roda SQL livre nem paga direto.

## 5. Human in the loop

5.1 Limiares de Bloqueio: Em quais situações de valor, risco ou incerteza o agente é proibido de agir sozinho e deve pedir aprovação?

Ex: Confiança do modelo < 95%; valores > R$ 500 em faturas; demissões/promoções em RH; clientes VIP com risco de cancelamento.

5.2 Responsabilidade no CPF: Quem é a pessoa responsável por avaliar e bater o martelo formal nas exceções que o agente sinalizar?

Ex: Card com 1 clique de aprovação no Teams/Slack. A máquina processa, mas o gestor assina a decisão no CPF.

## 6. Governança e Compliance

6.1 Sigilo & LGPD: Quais dados confidenciais ou sensíveis das pessoas e da empresa não podem vazar de forma alguma?

Ex: CPF, salários, dados médicos ou bancários mascarados antes da inferência, com retenção zero para treino.

6.2 Tracing Imutável: Como a empresa vai auditar e comprovar o histórico de cada ação e raciocínio que o agente realizou?

Ex: Trilha OpenTelemetry gravando hash, timestamp e prompt para reconstituir qualquer transação em auditorias.

## 7. Sabotadores

7.1 Medos & Perda Política: Quem na organização pode sentir receio de perder espaço, equipe, relevância ou controle?

Ex: Analistas com medo de demissão; gestores com receio de perder tamanho de time; TI com medo de Shadow IT.

7.2 Framing Anti-Sabotagem: Como reposicionar o projeto para transformar céticos em patrocinadores ativos da solução?

Ex: Vender o agente como estagiário digital de trabalho repetitivo e colocar a TI como guardiã da governança no comitê.

## 8. Harness

8.1 Runtime & Ferramentas: Quais ferramentas, telas e permissões o agente precisa ter para conseguir trabalhar?

Ex: OCR de PDFs especializado, conector seguro de banco de dados, sandbox Docker isolada e integração Slack/Teams.

8.2 Memória & Contexto: Onde e como o agente guardará a memória das conversas e o histórico das tarefas já feitas?

Ex: Gerenciamento de janela de contexto, histórico de transações e memória vetorial para consulta a manuais de regras.

8.3 Evals & Testes Contínuos: Quais testes práticos provarão que o agente está calibrado e sem regressões antes do deploy?

Ex: Bateria automatizada com 200 casos reais desafiadores rodada a cada atualização de prompt ou modelo.

## 9. Ancoragem de valor e ROI

9.1 Diagnóstico do Dual Bleed: Quanto a empresa queima hoje na soma de salários/horas extras com licenças de softwares?

Ex: 12 analistas x R$ 8.500/mês + R$ 15.000 em horas extras + R$ 14.000 em softwares satélites legados.

9.2 Economia Líquida na DRE: Quais custos reais serão cortados imediatamente após descontar os custos de IA?

Ex: Economia de R$ 98k/mês MENOS R$ 16k de infraestrutura = R$ 82k/mês líquido auditável pelo CFO.

9.3 Prazo de Payback do Piloto: Em quantos meses o valor investido no projeto precisa se pagar para ser um sucesso financeiro?

Ex: Investimento inicial de R$ 120k amortizado em apenas 45 a 60 dias de operação produtiva.

## 10. Do sucesso do piloto ao rollout

10.1 Meta de Sucesso no Sandbox: Qual meta clara de resolução e acurácia definirá que o piloto deu certo no D5?

Ex: 75% a 80% de resolução autônoma ponta a ponta com zero erro nas regras determinísticas.

10.2 Aval Executivo dos Co-Autores: Quem são os líderes que precisam dar o aval final para considerar o teste validado?

Ex: Parecer assinado conjuntamente pelo Head de Operações/RH, Arquiteto de TI e Controller.

10.3 Gatilho Contratual de Produção: Qual é o gatilho combinado para liberar a implantação definitiva para toda a empresa?

Exemplos: Atingida a acurácia combinada no sandbox, o orçamento de rollout de R$ 120k é destravado automaticamente.

Laboratório de engenharia com mais de cinco anos implementando produtos de IA e arquiteturas agenticas resilientes em produção.

Rua Pais Leme, 215 Conjunto 1713 Pinheiros, São Paulo

- Bootcamp de Agentes

- The Agentic Pilot Canvas

- Advisory

- Enterprise MCP

- LangChain & LangGraph

- Snowflake AI Data Cloud

- Braintrust Evals

- Blog

- Fale Conosco

Notas de campo de arquitetura e playbooks no seu e-mail corporativo.
