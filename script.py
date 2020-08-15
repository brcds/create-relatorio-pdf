import pandas as pd
from datetime import datetime
from pdf_reports import pug_to_html, write_report

planilha = pd.read_excel("content/controle_de_gastos.xlsx")
hoje = datetime.now().date()
html = pug_to_html("content/modelo_de_relatorio.pug",
                   planilha=planilha, hoje=hoje)

write_report(html, "controle_de_gastos_rel.pdf")
