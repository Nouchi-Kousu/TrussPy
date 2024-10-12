from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

# PDF 文件路径
pdf_file = "truss_structure_results.pdf"

# 创建 PDF 文档
doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                        leftMargin=20 * mm, rightMargin=20 * mm,
                        topMargin=20 * mm, bottomMargin=20 * mm)

# 注册字体
pdfmetrics.registerFont(TTFont('SourceHanSerif', './SIMSUN.TTC'))  # 思源宋体
pdfmetrics.registerFont(TTFont('FangSong', './仿宋_GB2312.TTF'))  # 仿宋

# 获取样式
styles = getSampleStyleSheet()

# 大标题样式（思源宋体）
title_style = styles['Title']
title_style.fontName = 'SourceHanSerif'
title_style.fontSize = 24
title_style.textColor = colors.HexColor('#000000')

# 小标题样式（仿宋字体）
subtitle_style = styles['Heading2']
subtitle_style.fontName = 'FangSong'
subtitle_style.fontSize = 12

# 正文样式（仿宋字体）
body_style = styles['Normal']
body_style.fontName = 'FangSong'
body_style.fontSize = 12

# 大量文字内容
long_text = """
这是一个包含大量文字内容的PDF排版示例。该内容将会自动进行换行和分页，并使用仿宋字体来展示。文字内容可以继续增加，以展示ReportLab处理大文本的功能。
""" * 5  # 重复生成大量文本

# 创建内容列表
elements = []

# 添加大标题
elements.append(Paragraph("桁架结构计算结果输出", title_style))
elements.append(Spacer(1, 12))

# 添加日期小标题
current_date = datetime.now().strftime("%Y-%m-%d")
elements.append(Paragraph(f"日期: {current_date}", subtitle_style))
elements.append(Spacer(1, 12))

# 添加横向排列的图片
image1 = Image("./Figure_1.png", width=90*mm, height=60*mm)  # 第一张图片
image2 = Image("./Figure_2.png", width=90*mm, height=60*mm)  # 第二张图片

# 添加两个图片，并在它们之间添加间距
elements.append(Spacer(1, 12))  # 图片之前的间距
elements.append(image1)
elements.append(Spacer(1, 12))  # 图片之间的间距
elements.append(image2)
elements.append(Spacer(1, 12))  # 图片之后的间距

# 添加正文
elements.append(Paragraph(long_text, body_style))

# 生成 PDF
doc.build(elements)

print(f"PDF generated: {pdf_file}")
