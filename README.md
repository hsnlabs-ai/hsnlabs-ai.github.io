# HSN Labs — Official Website

Repositório oficial do site da **HSN Labs**, boutique de Forward Deployed Engineering especializada em sistemas agênticos determinísticos e ontologias de negócios.

Hospedado no GitHub Pages: [hsnlabs.ai](https://hsnlabs.ai) / [hugonotnice.github.io/hsn-labs-site](https://hugonotnice.github.io/hsn-labs-site)

---

## Estrutura do Repositório

```text
├── assets/
│   └── brand/               # Kit completo de identidade visual
│       ├── elements/        # Carpa origami isolada em PNG transparente 1x e 4x
│       ├── favicons/        # Pacote completo de ícones de navegação
│       ├── lockups/         # Aplicações horizontal e vertical em PNG e WebP
│       ├── motion/          # Animações em MP4, WebM, GIF e código HTML
│       ├── symbol/          # Símbolo quadrado ciano oficial em 2000px
│       └── wordmark/        # Tipografia vetorial SVG e PNG nas cores da marca
├── AGENTS.md                # Diretrizes operacionais para agentes de código
├── BRAND.md                 # Manual de identidade visual e regras de aplicação
├── DESIGN.md                # Especificação oficial Google design-md com tokens
├── GEMINI.md                # Diretrizes técnicas compatíveis com Gemini
├── tailwind.theme.json      # Tokens prontos para Tailwind CSS
├── tokens.json              # Tokens em formato W3C DTCG
├── index.html               # Entrada estática para GitHub Pages
└── README.md                # Este documento
```

---

## Como rodar localmente

```bash
# Servir estaticamente via Python
python3 -m http.server 8000

# Abrir no navegador
open http://localhost:8000
```
