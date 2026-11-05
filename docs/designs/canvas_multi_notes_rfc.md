# The Agentic Canvas · Multi-Note Ergonomics & Persistent Creation

* **Autor:** Hugo S. Nascimento
* **Data:** 2026-11-04
* **Status:** RFC / Proposta de Refatoração

## Overview

O The Agentic Canvas™ é uma ferramenta visual corporativa para desenho de sistemas agênticos em dez blocos estratégicos. Em dinâmicas de workshop e planejamento executivo, cada bloco precisa receber múltiplas notas adesivas correspondentes às subperguntas de cada área.

Atualmente, ao inserir a primeira nota em um bloco, o botão principal de criação é removido da área visual de trabalho, restringindo a percepção de continuidade e impedindo a adição fluida de múltiplos post-its na zona de interação.

Este RFC estabelece a refatoração do ciclo de vida das notas e da interface de interação dos blocos, garantindo persistência do gatilho de adição, geometria quadrada estrita e autonomia total de preenchimento por bloco.

## Análise do Problema

1. **Desaparecimento do Gatilho Principal:** quando o array de notas de um bloco passa de zero para um elemento, a interface substitui o container de criação direta por apenas a lista estática de post-its, ocultando o elemento interativo de ação primária.
2. **Dependência de Controle Secundário:** o único botão remanescente de adição ficava restrito ao cabeçalho do bloco em tamanho reduzido, distante da área de colagem das notas e visualmente desconectado do fluxo de trabalho.
3. **Escalabilidade Visual do Bloco:** a área de notas precisa acomodar de uma a seis notas quadradas com quebra de linha suave, mantendo sempre ao final da fila um slot de adição permanente.

## Metas e Não-Metas

* **Metas em Escopo:**
  * Manter um card interativo de adição permanente dentro de cada bloco, permitindo cliques repetidos para adicionar quantas notas forem necessárias.
  * Garantir proporção quadrada estrita em todas as notas e no próprio card de adição em todos os dez blocos.
  * Posicionar o foco automaticamente na nova nota criada para digitação imediata.
  * Isolar o rótulo numérico da nota contra exclusão acidental por backspace.
  * Preservar o isolamento de estado por bloco, sem que a ação em um card interfira nos outros nove.
  * Suportar exclusão individual e edição inline em tempo real.
  * Ocultar todos os gatilhos e cards de adição na exportação em PDF e impressão.

* **Não-Metas Fora de Escopo:**
  * Implementação de sincronização colaborativa em tempo real com WebSockets no navegador nesta etapa.
  * Criação de exportação para arquivos binários proprietários além do suporte nativo a PDF e impressão.

## Alternativas Avaliadas

1. **Apenas Botão no Cabeçalho:**
   * *Decisão:* Rejeitada. Força o usuário a desviar o olhar da área de colagem para o título do bloco, criando atrito cognitivo em telas amplas e dispositivos móveis.
2. **Modal Flutuante de Inserção:**
   * *Decisão:* Rejeitada. Adicionar uma etapa intermediária em popover quebra a velocidade de ideação direta na superfície do quadro.
3. **Slot Permanente na Fila de Post-its:**
   * *Decisão:* Aprovada. Adicionar um card interativo quadrado com borda tracejada e ícone de soma permanente logo após a última nota garante descoberta imediata e adição ilimitada com um clique.

## Decisões Arquiteturais e Plano de Execução

1. **Arquivos Afetados:**
   * `canvas/especialista.html`
   * `canvas/processos.html`

2. **Estrutura de Renderização do Bloco:**
   * Se o bloco estiver vazio: exibe o botão de adição em destaque ocupando a área útil.
   * Se o bloco tiver uma ou mais notas: exibe as notas quadradas renderizadas seguidas imediatamente por um card quadrado permanente de adição (`.add-note-tile`), pronto para o próximo clique.
   * Proteção de Rótulo: `<strong class="note-lead" contenteditable="false">${p.tag}:</strong> <span class="note-text-val" contenteditable="true" data-placeholder="Escreva aqui...">${p.text}</span>`.
   * Geração de Prefixo: cálculo do sufixo com base no maior número existente mais um, prevenindo colisões de tag após exclusões pontuais.

3. **Modelo de Dados e Persistência:**
   * Array mutável de objetos `{ tag, text, color, rot }` indexado por bloco em memória.
   * Persistência de continuidade no `localStorage` sob a chave `hsnlabs_canvas_notes_<variant>`, sincronizando em tempo real no `oninput` e no `onblur`.

## Riscos, Limites e Mitigações

1. **Risco de Vazamento em PDF/Impressão:**
   * *Mitigação:* inclusão estrita de `.add-note-tile` e `.empty-state-clickable` na diretiva `@media print` com `display: none !important`.
2. **Risco de Acúmulo Excessivo de Notas (Overflow Vertical):**
   * *Mitigação:* área de notas com rolagem suave automática e layout responsivo flex-wrap sem quebra do grid global.
3. **Risco de Perda de Foco em Dispositivos Touch:**
   * *Mitigação:* chamada explícita de foco no elemento editável após `requestAnimationFrame`, com botão de exclusão acessível no foco da nota.
