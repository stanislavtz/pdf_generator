import pandas as pd
from fpdf import FPDF


class PDF(FPDF):
    topic = ""

    def footer(self):
        self.set_y(-15)                        # 15 mm from the bottom edge
        self.set_font('Arial', 'I', size=10)
        self.set_text_color(200, 200, 200)
        self.cell(w=0, h=10, txt=self.topic, border=0, align='R')


pdf = PDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')

pdf.set_font('Arial', 'B', size=24)
pdf.set_text_color(100, 100, 100)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.topic = row["Topic"]                   # footer text for this topic's pages
    pdf.cell(w=0, h=6, txt=row["Topic"], border=0, align='L')
    pdf.line(10, 17, 207, 17)

    for _ in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("Python_Notepad.pdf")
