# SPEC: Header Playbooks e Rotas Bilingues

## Objetivo
Adicionar item Playbooks no header do site e estruturar URLs bilingues `/playbooks/` e `/pt/playbooks/`.
Conteudo central da pagina:
1. Agentic Adoption Canvas
2. Ontology Mapping

---

## 1. Regras Arquiteturais Estritas

* Estrutura Dual-Track:
  * Rota EN: `/playbooks/` em `playbooks/index.html`
  * Rota PT: `/pt/playbooks/` em `pt/playbooks/index.html`
* Politica Zero Parenteses: proibido qualquer parentese em texto visivel, titles e metas da rota PT.
* Zero Componentes Novos: reaproveitar estritamente elementos de `advisory/index.html` e `pt/advisory/index.html`.
* Tokens Visuais:
  * Canvas: `#f5f5f5`
  * Card: `#ffffff`
  * Destaque: `#52B4FD`
  * Tipografia: Cormorant Garamond 300 para display, Inter para corpo. Zero monospace.
  * Geometria: bordas retas com 90 graus, `border-radius: 0`.
  * Textura: papel amassado `/assets/textures/paper_crumpled_clean.jpg` via `mix-blend-mode: multiply`.
* Telemetria Oficial:
  * GTM: GTM-KPL6PVKC
  * GA4: G-GMK24ECXMF

---

## 2. Atualizacao de Header em Todas as Paginas

### Header EN
Inserir link entre Advisory e Blog:
```html
<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
  <a href="/advisory" class="nav-link">Advisory</a>
  <a href="/playbooks" class="nav-link">Playbooks</a>
  <a href="/blog" class="nav-link">Blog</a>
  <a href="/pt/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">PT</a>
</div>
```
Arquivos EN afetados:
* `index.html`
* `bootcamp/index.html`
* `advisory/index.html`
* `mcp/index.html`
* `privacy-policy/index.html`
* `modern-slavery-statement/index.html`

### Header PT
Inserir link entre Advisory e Blog com isolamento de idioma:
```html
<div class="nav-menu" style="margin-left: auto; margin-right: 32px; display: flex; align-items: center; gap: 24px;">
  <a href="/pt/advisory" class="nav-link">Advisory</a>
  <a href="/pt/playbooks" class="nav-link">Playbooks</a>
  <a href="/blog/pt/" class="nav-link">Blog</a>
  <a href="/" class="nav-link" style="font-weight: 500; font-size: 0.85rem; letter-spacing: 0.05em; color: var(--muted); text-transform: uppercase;">EN</a>
</div>
```
Arquivos PT afetados:
* `pt/index.html`
* `pt/bootcamp/index.html`
* `pt/advisory/index.html`
* `pt/mcp/index.html`
* `pt/privacy-policy/index.html`
* `pt/modern-slavery-statement/index.html`

---

## 3. Criacao das Rotas /playbooks/ e /pt/playbooks/

### Estrutura de Diretorios
```text
site_hsn_labs/
├── playbooks/
│   └── index.html
└── pt/
    └── playbooks/
        └── index.html
```

### Metadados e Canonicals

#### Rota EN `playbooks/index.html`
* Canonical: `https://hsnlabs.ai/playbooks/`
* Hreflang en: `https://hsnlabs.ai/playbooks/`
* Hreflang pt-BR: `https://hsnlabs.ai/pt/playbooks/`
* Hreflang x-default: `https://hsnlabs.ai/playbooks/`
* Title: `Proprietary Playbooks | HSN Labs`
* Description: `Battle-tested enterprise frameworks: Agentic Adoption Canvas and Ontology Mapping.`

#### Rota PT `pt/playbooks/index.html`
* Canonical: `https://hsnlabs.ai/pt/playbooks/`
* Hreflang en: `https://hsnlabs.ai/playbooks/`
* Hreflang pt-BR: `https://hsnlabs.ai/pt/playbooks/`
* Hreflang x-default: `https://hsnlabs.ai/playbooks/`
* Title: `Playbooks Proprietarios | HSN Labs`
* Description: `Metodologias de engenharia e arquitetura: Agentic Adoption Canvas e Ontology Mapping.`
* Regra: zero parenteses no texto visivel.

---

## 4. Blocos de Conteudo da Pagina Playbooks

### Hero
* Headline Display:
  * EN: `Proprietary Frameworks that eliminate production failures`
  * PT: `Metodologias proprietarias para execucao sem falhas em producao`
* Subtitulo: Contexto direto de Forward Deployed Engineering.

### Secao 1: Agentic Adoption Canvas
* Badge `.post-it-badge`: `01`
* Titulo: `Agentic Adoption Canvas`
* Escopo: Mapeamento de prontidao operacional, limites de autonomia, matriz de risco e casos de uso enterprise.

### Secao 2: Ontology Mapping
* Badge `.post-it-badge`: `02`
* Titulo: `Ontology Mapping`
* Escopo: Modelagem de grafos de conhecimento, ontologias executaveis de negocio e contratos deterministicos para agentes.

### Secao de Conversao
* Card de contato com os 4 gates de qualificacao tecnicos identico ao advisory.

---

## 5. Integracao com Pipeline e Testes

1. Atualizar `i18n/routes-map.json` incluindo entrada para `site_playbooks`:
   * `en_path`: `/playbooks/`
   * `pt_path`: `/pt/playbooks/`
2. Atualizar `scripts/test_site_i18n_spec.py`:
   * Adicionar id `playbooks` na lista `PAGES`.
3. Executar sincronizacao de sitemap:
   * Comando: `python3 scripts/sync_sitemap.py`
4. Executar bateria de validacao:
   * Comando: `python3 scripts/test_site_i18n_spec.py`
   * Verificar aprovacao em todos os 5 gates.
