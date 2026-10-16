import os
from PIL import Image, ImageDraw, ImageFont

def create_org_flattening_chart():
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
    f_col_title = ImageFont.truetype(font_bold, 18)
    f_level = ImageFont.truetype(font_bold, 13)
    f_level_desc = ImageFont.truetype(font_mono, 11)
    f_footer = ImageFont.truetype(font_mono, 12)

    # Header
    draw.rectangle([(50, 40), (330, 68)], outline="#00e5ff", fill="#07222c", width=1)
    draw.text((65, 47), "hsnlabs • ORGANIZATIONAL DESIGN", font=f_badge, fill="#00e5ff")

    draw.text((50, 85), "O Achatamento Hierárquico: Pirâmide vs. Losango", font=f_title, fill="#ffffff")
    draw.text((50, 125), "Como a automação da coordenação colapsa a média gerência e conecta a diretoria ao executor.", font=f_subtitle, fill="#8b949e")

    # Box 1: Left - Pirâmide Tradicional
    b1_left, b1_top, b1_w, b1_h = 50, 170, 530, 430
    draw.rectangle([(b1_left, b1_top), (b1_left + b1_w, b1_top + b1_h)], outline="#30363d", fill="#0d1117", width=1)
    draw.rectangle([(b1_left, b1_top), (b1_left + b1_w, b1_top + 45)], fill="#161b22")
    draw.text((b1_left + 20, b1_top + 14), "ESTRUTURA TRADICIONAL (PIRÂMIDE)", font=f_col_title, fill="#e6edf3")

    # Layers of Pyramid
    pyramid_layers = [
        ("NÍVEL 1: C-LEVEL / VPs", "Diretrizes estratégicas e alocação de capital", "#21262d", 200, 320),
        ("NÍVEL 2: DIRETORES E GMs", "Traduzem diretrizes para roadmaps setoriais", "#262c36", 160, 360),
        ("NÍVEL 3: GERENTES MÉDIOS & PMS", "Roteadores de contexto, cobrança e relatórios", "#3b2426", 110, 420),
        ("NÍVEL 4: TECH LEADS & COORDENADORES", "Supervisão técnica direta e divisão de sprints", "#2d2426", 70, 460),
        ("NÍVEL 5: EXECUTORES (PLENOS / JUNIORES)", "Execução fracionada em tickets e tarefas", "#1c2128", 30, 500)
    ]

    p_y = b1_top + 60
    for name, desc, col, pad_x, box_w in pyramid_layers:
        x_start = b1_left + (b1_w - box_w) // 2
        draw.rectangle([(x_start, p_y), (x_start + box_w, p_y + 55)], outline="#484f58", fill=col, width=1)
        draw.text((x_start + 15, p_y + 10), name, font=f_level, fill="#ffffff" if col != "#3b2426" else "#ff7b72")
        draw.text((x_start + 15, p_y + 30), desc, font=f_level_desc, fill="#8b949e")
        p_y += 66

    # Box 2: Right - Modelo Losango / Flat
    b2_left = 620
    draw.rectangle([(b2_left, b1_top), (b2_left + b1_w, b1_top + b1_h)], outline="#00e5ff", fill="#091016", width=2)
    draw.rectangle([(b2_left, b1_top), (b2_left + b1_w, b1_top + 45)], fill="#07222c")
    draw.text((b2_left + 20, b1_top + 14), "ESTRUTURA HIGH IC (FLAT & ALAVANCADA)", font=f_col_title, fill="#00e5ff")

    hic_layers = [
        ("LIDERANÇA EXECUTIVA / FUNDADORES", "Problemas de negócio, alocação de capital e metas de receita", "#0f261c", 160, 360),
        ("HIGH ICs (OPERADORES DE ALTO IMPACTO)", "Propriedade end-to-end, julgamento crítico e execução autônoma", "#00ff88", 50, 470),
        ("CAMADA AGÊNTICA & INFRAESTRUTURA", "Runtimes de IA, MCP, bancos legados, testes e automação", "#0c2d38", 120, 400)
    ]

    h_y = b1_top + 80
    for name, desc, col, pad_x, box_w in hic_layers:
        x_start = b2_left + (b2_w_pad := (b1_w - box_w) // 2)
        if col == "#00ff88":
            draw.rectangle([(x_start, h_y), (x_start + box_w, h_y + 80)], outline="#00ff88", fill="#062d1f", width=2)
            draw.text((x_start + 20, h_y + 16), name, font=f_level, fill="#00ff88")
            draw.text((x_start + 20, h_y + 42), desc, font=f_level_desc, fill="#ffffff")
            h_y += 105
        else:
            draw.rectangle([(x_start, h_y), (x_start + box_w, h_y + 65)], outline="#388bfd", fill=col, width=1)
            draw.text((x_start + 20, h_y + 12), name, font=f_level, fill="#e6edf3")
            draw.text((x_start + 20, h_y + 36), desc, font=f_level_desc, fill="#8b949e")
            h_y += 90

    # Notes on right box
    draw.text((b2_left + 40, b1_top + 365), "• Eliminação de 3 camadas intermediárias de aprovação", font=f_level_desc, fill="#7ee787")
    draw.text((b2_left + 40, b1_top + 390), "• Span of Control do C-Level expande de 1:7 para 1:30+", font=f_level_desc, fill="#7ee787")

    # Footer
    draw.line([(50, 620), (width - 50, 620)], fill="#21262d", width=1)
    draw.text((50, 635), "ANÁLISE DE DESIGN ORGANIZACIONAL • CASOS: META FLATTENING & SHOPIFY CRAFTER TRACK", font=f_footer, fill="#6e7681")
    draw.text((width - 320, 635), "NEWSLETTER AGENTES [×] GENTE", font=f_footer, fill="#00e5ff")

    out_path = "/Users/hugosoares/site_hsn_labs/achatamento_organizacional_high_ic.png"
    img.save(out_path, "PNG")
    print(f"Generated: {out_path}")

create_org_flattening_chart()
