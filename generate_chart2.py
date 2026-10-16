import os
from PIL import Image, ImageDraw, ImageFont

def create_economic_matrix():
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), "#080b0f")
    draw = ImageDraw.Draw(img)

    # Grid background
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill="#111822", width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill="#111822", width=1)

    # Fonts
    font_mono = "/System/Library/Fonts/SFNSMono.ttf"
    font_bold = "/System/Library/Fonts/Helvetica.ttc"
    
    f_badge = ImageFont.truetype(font_mono, 13)
    f_title = ImageFont.truetype(font_bold, 30)
    f_subtitle = ImageFont.truetype(font_mono, 15)
    f_col_title = ImageFont.truetype(font_bold, 20)
    f_item_title = ImageFont.truetype(font_bold, 15)
    f_item_desc = ImageFont.truetype(font_mono, 13)
    f_footer = ImageFont.truetype(font_mono, 12)

    # Header
    draw.rectangle([(50, 40), (320, 68)], outline="#00e5ff", fill="#07222c", width=1)
    draw.text((65, 47), "hsnlabs • ECONOMIC BENCHMARK", font=f_badge, fill="#00e5ff")

    draw.text((50, 85), "Squad Tradicional vs. High IC Unit Economics", font=f_title, fill="#ffffff")
    draw.text((50, 125), "Por que 1 operador alavancado entrega mais barato, mais rápido e com zero atrito de coordenação.", font=f_subtitle, fill="#8b949e")

    # Column 1: Traditional Squad
    c1_left, c1_top, c1_w, c1_h = 50, 170, 530, 430
    draw.rectangle([(c1_left, c1_top), (c1_left + c1_w, c1_top + c1_h)], outline="#30363d", fill="#0d1117", width=1)
    draw.rectangle([(c1_left, c1_top), (c1_left + c1_w, c1_top + 50)], fill="#161b22")
    draw.text((c1_left + 20, c1_top + 15), "SQUAD TRADICIONAL (8 A 12 PESSOAS)", font=f_col_title, fill="#ff5555")

    items_c1 = [
        ("Composição da Folha", "1 PM, 1 Tech Lead, 1 Designer, 4-6 Devs, 1 QA, 1 Scrum Master"),
        ("Custo Anual Consolidado", "R$ 1.8M a R$ 2.8M / ano (salários, encargos, licenças SaaS)"),
        ("Imposto de Coordenação", "Alta latência: Dailies, Plannings, Retros, 1:1s e handoffs entre silos"),
        ("Tempo até 1º Release", "8 a 16 semanas (especificação -> aprovação -> sprint -> homologação)"),
        ("Risco Principal", "Diluição de contexto, reuniões de alinhamento e débitos de processo")
    ]

    curr_y = c1_top + 65
    for title, desc in items_c1:
        draw.text((c1_left + 20, curr_y), "• " + title, font=f_item_title, fill="#ffffff")
        draw.text((c1_left + 35, curr_y + 22), desc, font=f_item_desc, fill="#8b949e")
        curr_y += 68

    # Column 2: High IC Model
    c2_left = 620
    draw.rectangle([(c2_left, c1_top), (c2_left + c1_w, c1_top + c1_h)], outline="#00ff88", fill="#091410", width=2)
    draw.rectangle([(c2_left, c1_top), (c2_left + c1_w, c1_top + 50)], fill="#0f261c")
    draw.text((c2_left + 20, c1_top + 15), "HIGH IC MODEL (1 OPERADOR + AGENTES)", font=f_col_title, fill="#00ff88")

    items_c2 = [
        ("Composição da Folha", "1 Operador Sênior (High IC) + Stack Agêntico (MCP, LLMs, Scripts)"),
        ("Custo Anual Consolidado", "R$ 600k a R$ 1.0M / ano (remuneração de topo + infra de IA)"),
        ("Imposto de Coordenação", "Quase zero: context switching mínimo, zero reuniões de passagem de bastão"),
        ("Tempo até 1º Release", "3 a 7 dias (da hipótese ao deploy funcional e instrumentado)"),
        ("Vantagem Estrutural", "Contexto integral na cabeça do construtor; ciclo feedback em tempo real")
    ]

    curr_y = c1_top + 65
    for title, desc in items_c2:
        draw.text((c2_left + 20, curr_y), "✓ " + title, font=f_item_title, fill="#00ff88")
        draw.text((c2_left + 35, curr_y + 22), desc, font=f_item_desc, fill="#c9d1d9")
        curr_y += 68

    # Footer
    draw.line([(50, 620), (width - 50, 620)], fill="#21262d", width=1)
    draw.text((50, 635), "FONTE: FRAMEWORK HI-C (2026) • MATRIZ DE EFICIÊNCIA DE ENGENHARIA hsnlabs", font=f_footer, fill="#6e7681")
    draw.text((width - 320, 635), "NEWSLETTER AGENTES [×] GENTE", font=f_footer, fill="#00e5ff")

    out_path = "/Users/hugosoares/site_hsn_labs/matriz_economica_high_ic.png"
    img.save(out_path, "PNG")
    print(f"Generated: {out_path}")

create_economic_matrix()
