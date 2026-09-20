# Diretrizes para Agentes de Desenvolvimento - HSN Labs Site

Orientações para qualquer agente de inteligência artificial que for manter, implementar ou expandir este repositório.

---

## 1. Missão do Repositório

Construir e manter o site oficial da **HSN Labs**, hospedado de forma estática no **GitHub Pages**.

---

## 2. Escopo Estrutural do Site

O site será implementado a partir de um template que será selecionado pelo Hugo Soares. A estrutura final deve conter obrigatoriamente:

1. **Header:** Barra de navegação limpa com o lockup horizontal oficial da marca.
2. **Hero Page:** Seção de impacto inicial com proposta de valor direta e aplicação autoral do logo com motion da água.
3. **Seção de Mercados Verticais:** Apresentação estruturada das verticais em que a boutique atua: BFSI, Saúde e Operações Industriais.
4. **Footer:** Assinatura institucional, links para contato e repositórios abertos como Proto-Ontologies.

---

## 3. Diretriz Central de Implementação - HITL Estrito

* **Não inventar a fundação do projeto antecipadamente:** Não crie layouts complexos, wireframes ou copys fictícios por conta própria.
* **Aguardar a escolha do template:** A estrutura visual e a biblioteca de componentes devem se basear estritamente no template que o Hugo Soares fornecer.
* **Aplicação autoral da marca:** O elemento central que torna o site único é o logo da HSN Labs e o comportamento tátil da água ciano com a carpa origami. O template deve ser customizado para valorizar essa identidade.
* **Zero AI Slop:** Proibido o uso de templates genéricos de web3, gradientes neon purples, ilustrações abstratas de cérebros brilhantes ou robôs. Manter estética técnica de engenharia de software de missão crítica.

---

## 4. Padrões Técnicos e Tokens

* Seguir rigorosamente as definições de tokens contidas em `DESIGN.md` e `tokens.json`.
* Utilizar `tailwind.theme.json` caso o template utilize Tailwind CSS.
* Garantir compatibilidade 100% estática para deploy no GitHub Pages:
  * Ponto de entrada: `index.html` na raiz do repositório.
  * Caminhos de assets sempre relativos: `./assets/brand/...`.
  * Nenhum servidor backend proprietário obrigatório no runtime.
* Testar sempre em viewports desktop 1440px e mobile 390px.
