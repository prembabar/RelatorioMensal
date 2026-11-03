import pandas as pd

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils.dataframe import dataframe_to_rows


# =========================================
# CONFIGURAÇÕES
# =========================================

ARQUIVO_CSV = "participantes.csv"

nome_arquivo = input("Digite o nome do arquivo final: ")
ARQUIVO_SAIDA = f"{nome_arquivo}.xlsx"

DURACAO_AULA = int(input("Digite a duração da aula em minutos: "))
PERCENTUAL_PRESENCA = 0.75


# =========================================
# LEITURA DO CSV
# =========================================

csv = pd.read_csv(
    ARQUIVO_CSV,
    sep=',',
    encoding='utf-8-sig'
)

csv.columns = csv.columns.str.strip()

print(csv.columns)


# converter datas (mais seguro)
csv['Ingressar na hora'] = pd.to_datetime(csv['Ingressar na hora'], errors='coerce')
csv['Hora de saída'] = pd.to_datetime(csv['Hora de saída'], errors='coerce')


# =========================================
# AGRUPAR PARTICIPANTES
# =========================================

relatorio = (
    csv.groupby('Nome (nome original)', as_index=False)
    .agg({
        'E-mail': 'first',
        'Ingressar na hora': 'min',
        'Hora de saída': 'max',
        'Duração (minutos)': 'sum'
    })
)


# =========================================
# AJUSTAR COLUNAS
# =========================================

relatorio['Duração total'] = DURACAO_AULA

# cálculo correto da presença
relatorio['Presença'] = relatorio['Duração (minutos)'] >= (DURACAO_AULA * PERCENTUAL_PRESENCA)
relatorio['Presença'] = relatorio['Presença'].map({True: 'P', False: 'F'})


# ordenar por nome
relatorio = relatorio.sort_values('Nome (nome original)')


# =========================================
# REORGANIZAR COLUNAS (opcional, mas melhora o Excel)
# =========================================

relatorio = relatorio[
    [
        'Nome (nome original)',
        'E-mail',
        'Ingressar na hora',
        'Hora de saída',
        'Duração (minutos)',
        'Duração total',
        'Presença'
    ]
]


# =========================================
# EXPORTAR EXCEL
# =========================================

wb = Workbook()
ws = wb.active
ws.title = 'Presença'

# adicionar dados
for row in dataframe_to_rows(relatorio, index=False, header=True):
    ws.append(row)

# cabeçalho em negrito
for cell in ws[1]:
    cell.font = Font(bold=True)

# formatar datas
for row in ws.iter_rows(min_row=2):
    if row[2].value:
        row[2].number_format = 'dd/mm/yyyy hh:mm:ss'
    if row[3].value:
        row[3].number_format = 'dd/mm/yyyy hh:mm:ss'

# ajustar largura automática
for column_cells in ws.columns:

    length = max(
        len(str(cell.value)) if cell.value is not None else 0
        for cell in column_cells
    )

    ws.column_dimensions[
        column_cells[0].column_letter
    ].width = length + 5


# salvar arquivo
wb.save(ARQUIVO_SAIDA)

print("Relatório gerado com sucesso!")