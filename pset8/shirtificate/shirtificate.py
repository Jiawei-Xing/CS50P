from fpdf import FPDF

name = input("Name: ")

# init pdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False)
pdf.add_page()

# add title
pdf.set_font("helvetica", "B", 30)
pdf.cell(w=0, h=30, txt="CS50 shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

# add shirt
pdf.image("./shirtificate.png", 15, 50, 180, 200)
pdf.set_font("helvetica", "B", 18)
pdf.set_text_color(255)
pdf.cell(w=0, h=150, txt=name+" took CS50", align="C")

pdf.output("shirtificate.pdf")