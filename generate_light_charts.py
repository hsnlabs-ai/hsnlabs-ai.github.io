import os
from PIL import Image, ImageDraw, ImageFont

FONT_SERIF = "/System/Library/Fonts/NewYork.ttf"
FONT_SANS = "/System/Library/Fonts/HelveticaNeue.ttc"
SYMBOL_PATH = "/Users/hugosoares/site_hsn_labs/assets/brand/symbol/symbol-square-clean.png"

def get_fonts():
    return {
        "tag": ImageFont.truetype(FONT_SANS, 12, index=0),
        "title": ImageFont.truetype(FONT_SERIF, 24),
        "subtitle": ImageFont.truetype(FONT_SANS, 14, index=0),
        "card_num": ImageFont.truetype(FONT_SANS, 12, index=1),
        "card_title": ImageFont.truetype(FONT_SERIF, 16),
        "card_body": ImageFont.truetype(FONT_SANS, 13, index=0),
        "footer": ImageFont.truetype(FONT_SANS, 11, index=0),
        "col_header": ImageFont.truetype(FONT_SERIF, 18),
        "item_title": ImageFont.truetype(FONT_SANS, 14, index=1),
        "item_desc": ImageFont.truetype(FONT_SANS, 13, index=0),
    }

def draw_base_canvas(draw, img, title_text, subtitle_text, tag_text="[Agentes] x [a Gente]"):
    width, height = 1200, 675
    fonts = get_fonts()

    draw.rectangle([(0, 0), (width, height)], fill="#FAFAFA")

    if os.path.exists(SYMBOL_PATH):
        sym = Image.open(SYMBOL_PATH).convert("RGBA")
        sym = sym.resize((36, 36), Image.Resampling.LANCZOS)
        img.paste(sym, (width - 70 - 36, 46), sym)

    draw.text((70, 48), tag_text.upper(), font=fonts["tag"], fill="#0284C7")
    draw.text((70, 72), title_text, font=fonts["title"], fill="#111827")
    draw.text((70, 108), subtitle_text, font=fonts["subtitle"], fill="#6B7280")

    draw.line([(70, 615), (width - 70, 615)], fill="#E5E7EB", width=1)
    draw.text((70, 628), "hsnlabs • Reflexões sobre trabalho e tecnologia", font=fonts["footer"], fill="#9CA3AF")
    draw.text((width - 240, 628), "hsnlabs.ai", font=fonts["footer"], fill="#9CA3AF")


def render_cover_domino():
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), "#FAFAFA")
    draw = ImageDraw.Draw(img)

    draw_base_canvas(
        draw, img,
        "A evolução do trabalho com o High IC",
        "Como a produtividade pessoal muda a estrutura das equipes e valoriza o especialista"
    )
    fonts = get_fonts()

    steps = [
        ("Passo 1", "Trabalho com IA", "Tarefas repetitivas e rotinas manuais passam a ser resolvidas com muito mais rapidez."),
        ("Passo 2", "Menos tarefas básicas", "Demandas de apoio e organização são absorvidas diretamente por software."),
        ("Passo 3", "Menos intermediação", "Equipes pequenas e autônomas não precisam de camadas para repassar recados."),
        ("Passo 4", "Mais autonomia", "A comunicação acontece sem burocracia entre quem decide e quem coloca a mão na massa."),
        ("Passo 5", "Valorização técnica", "O especialista ganha liberdade de atuação e remuneração comparável à de diretoria.")
    ]

    card_y = 155
    card_w = 196
    card_h = 420
    start_x = 70
    gap = 20

    for i, (num, title, desc) in enumerate(steps):
        cx = start_x + i * (card_w + gap)
        is_last = (i == 4)

        bg_card = "#FFFFFF"
        border_col = "#0284C7" if is_last else "#E5E7EB"
        
        draw.rounded_rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], radius=8, fill=bg_card, outline=border_col, width=1 if not is_last else 2)

        tag_color = "#0284C7" if is_last else "#9CA3AF"
        draw.text((cx + 18, card_y + 24), num, font=fonts["card_num"], fill=tag_color)
        draw.text((cx + 18, card_y + 52), title, font=fonts["card_title"], fill="#111827")
        draw.line([(cx + 18, card_y + 82), (cx + card_w - 18, card_y + 82)], fill="#F3F4F6", width=1)

        words = desc.split()
        lines = []
        cur_line = []
        for w in words:
            cur_line.append(w)
            if len(" ".join(cur_line)) > 20:
                lines.append(" ".join(cur_line[:-1]))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))

        dy = card_y + 104
        for l in lines:
            draw.text((cx + 18, dy), l, font=fonts["card_body"], fill="#4B5563")
            dy += 22

        if not is_last:
            conn_x = cx + card_w + 10
            conn_y = card_y + card_h // 2
            draw.line([(conn_x - 3, conn_y - 4), (conn_x + 3, conn_y)], fill="#CBD5E1", width=1)
            draw.line([(conn_x + 3, conn_y), (conn_x - 3, conn_y + 4)], fill="#CBD5E1", width=1)

    out_path = "/Users/hugosoares/site_hsn_labs/capa_high_ic_domino.png"
    img.save(out_path, "PNG")
    print(f"Rendered: {out_path}")


def render_economic_matrix():
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), "#FAFAFA")
    draw = ImageDraw.Draw(img)

    draw_base_canvas(
        draw, img,
        "Comparativo de modelo de trabalho",
        "Diferenças entre uma equipe tradicional e um especialista apoiado por agentes"
    )
    fonts = get_fonts()

    col_y = 155
    col_w = 515
    col_h = 420

    c1_x = 70
    draw.rounded_rectangle([(c1_x, col_y), (c1_x + col_w, col_y + col_h)], radius=8, fill="#FFFFFF", outline="#E5E7EB", width=1)
    draw.text((c1_x + 28, col_y + 24), "Equipe tradicional com muitas funções", font=fonts["col_header"], fill="#374151")
    draw.line([(c1_x + 28, col_y + 58), (c1_x + col_w - 28, col_y + 58)], fill="#F3F4F6", width=1)

    items_c1 = [
        ("Tamanho do time", "De oito a doze pessoas divididas em papéis específicos"),
        ("Ritmo de alinhamento", "Muitas reuniões semanais para organizar tarefas e repassar demandas"),
        ("Tempo até a entrega", "Várias semanas entre planejamento, aprovações e testes"),
        ("Pontos de atrito", "Perda de contexto nas passagens de bastão e excesso de alinhamentos"),
        ("Foco principal", "Coordenação entre departamentos e gestão de processos")
    ]

    cur_y = col_y + 75
    for title, desc in items_c1:
        draw.text((c1_x + 28, cur_y), title, font=fonts["item_title"], fill="#111827")
        draw.text((c1_x + 28, cur_y + 22), desc, font=fonts["item_desc"], fill="#6B7280")
        cur_y += 66

    c2_x = 615
    draw.rounded_rectangle([(c2_x, col_y), (c2_x + col_w, col_y + col_h)], radius=8, fill="#FFFFFF", outline="#0284C7", width=1)
    draw.text((c2_x + 28, col_y + 24), "Especialista sênior com agentes", font=fonts["col_header"], fill="#0284C7")
    draw.line([(c2_x + 28, col_y + 58), (c2_x + col_w - 28, col_y + 58)], fill="#F3F4F6", width=1)

    items_c2 = [
        ("Tamanho do time", "Um operador experiente resolvendo o problema de ponta a ponta"),
        ("Ritmo de alinhamento", "Comunicação direta com quem toma decisões, sem intermediários"),
        ("Tempo até a entrega", "Soluções práticas colocadas para rodar em poucos dias"),
        ("Pontos de atrito", "Praticamente zero ruído, com contexto preservado do início ao fim"),
        ("Foco principal", "Construção direta, testes rápidos e impacto real no negócio")
    ]

    cur_y = col_y + 75
    for title, desc in items_c2:
        draw.text((c2_x + 28, cur_y), title, font=fonts["item_title"], fill="#0284C7")
        draw.text((c2_x + 28, cur_y + 22), desc, font=fonts["item_desc"], fill="#4B5563")
        cur_y += 66

    out_path = "/Users/hugosoares/site_hsn_labs/matriz_economica_high_ic.png"
    img.save(out_path, "PNG")
    print(f"Rendered: {out_path}")


def render_org_flattening():
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), "#FAFAFA")
    draw = ImageDraw.Draw(img)

    draw_base_canvas(
        draw, img,
        "Transição da estrutura das equipes",
        "Como a proximidade entre liderança e especialistas reduz camadas burocráticas"
    )
    fonts = get_fonts()

    col_y = 155
    col_w = 515
    col_h = 420

    c1_x = 70
    draw.rounded_rectangle([(c1_x, col_y), (c1_x + col_w, col_y + col_h)], radius=8, fill="#FFFFFF", outline="#E5E7EB", width=1)
    draw.text((c1_x + 28, col_y + 24), "Estrutura tradicional com muitas camadas", font=fonts["col_header"], fill="#374151")
    draw.line([(c1_x + 28, col_y + 58), (c1_x + col_w - 28, col_y + 58)], fill="#F3F4F6", width=1)

    layers_p = [
        ("Diretoria e vice-presidência", "Definição de metas gerais e orçamento"),
        ("Gerência executiva", "Desdobramento de projetos em planos menores"),
        ("Gerência intermediária", "Acompanhamento diário e relatórios de status"),
        ("Coordenação técnica", "Distribuição de tarefas entre equipes"),
        ("Profissionais executores", "Entrega pontual de partes isoladas do trabalho")
    ]

    cur_y = col_y + 75
    for title, desc in layers_p:
        draw.text((c1_x + 28, cur_y), title, font=fonts["item_title"], fill="#111827")
        draw.text((c1_x + 28, cur_y + 22), desc, font=fonts["item_desc"], fill="#6B7280")
        cur_y += 66

    c2_x = 615
    draw.rounded_rectangle([(c2_x, col_y), (c2_x + col_w, col_y + col_h)], radius=8, fill="#FFFFFF", outline="#0284C7", width=1)
    draw.text((c2_x + 28, col_y + 24), "Estrutura enxuta e colaborativa", font=fonts["col_header"], fill="#0284C7")
    draw.line([(c2_x + 28, col_y + 58), (c2_x + col_w - 28, col_y + 58)], fill="#F3F4F6", width=1)

    layers_h = [
        ("Liderança estratégica", "Alinhamento de prioridades e desafios reais do negócio"),
        ("Especialistas autônomos", "Operadores seniores com visão completa e liberdade técnica"),
        ("Automações e tecnologia", "Rotinas e sistemas que cuidam do trabalho repetitivo")
    ]

    cur_y = col_y + 85
    for title, desc in layers_h:
        is_specialist = ("Especialistas" in title)
        title_col = "#0284C7" if is_specialist else "#111827"
        draw.text((c2_x + 28, cur_y), title, font=fonts["item_title"], fill=title_col)
        draw.text((c2_x + 28, cur_y + 24), desc, font=fonts["item_desc"], fill="#4B5563")
        cur_y += 82

    draw.line([(c2_x + 28, col_y + 340), (c2_x + col_w - 28, col_y + 340)], fill="#F3F4F6", width=1)
    draw.text((c2_x + 28, col_y + 360), "Fluxo de decisões direto e sem barreiras de comunicação", font=fonts["item_desc"], fill="#0284C7")

    out_path = "/Users/hugosoares/site_hsn_labs/achatamento_organizacional_high_ic.png"
    img.save(out_path, "PNG")
    print(f"Rendered: {out_path}")

render_cover_domino()
render_economic_matrix()
render_org_flattening()
