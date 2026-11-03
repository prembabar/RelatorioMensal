import pandas as pd
from glob import glob

# =====================================
# PASTA DOS RELATÓRIOS
# =====================================

PASTA_RELATORIOS = "relatorios"

# =====================================
# PEGAR ARQUIVOS
# =====================================

arquivos = glob(f"{PASTA_RELATORIOS}/*.xlsx")

print("Arquivos encontrados:")
print(arquivos)

relatorio_final = None

# =====================================
# PROCESSAR
# =====================================

for i, arquivo in enumerate(arquivos):

    print()
    print(f"Lendo arquivo: {arquivo}")

    df = pd.read_excel(arquivo)

    print(df.head())

    # pega primeira coluna = nome
    nome_coluna = df.columns[0]

    # pega última coluna = presença
    presenca_coluna = df.columns[-1]
    
    import os

    aula_nome = os.path.splitext(
        os.path.basename(arquivo)
    )[0]

    temp = df[[nome_coluna, presenca_coluna]].copy()

    temp.columns = ["Participante", aula_nome]

    # remover linhas vazias
    temp = temp.dropna()

    if relatorio_final is None:

        relatorio_final = temp

    else:

        relatorio_final = pd.merge(
            relatorio_final,
            temp,
            on="Participante",
            how="outer"
        )

# =====================================
# PREENCHER FALTAS
# =====================================

relatorio_final = relatorio_final.fillna("F")

# =====================================
# SOMAR
# =====================================

colunas_aulas = relatorio_final.columns[1:]

relatorio_final["Presenças"] = (
    relatorio_final[colunas_aulas] == "P"
).sum(axis=1)

relatorio_final["Faltas"] = (
    relatorio_final[colunas_aulas] == "F"
).sum(axis=1)

# =====================================
# SALVAR
# =====================================

nome_saida = input(
    "Digite o nome do relatório final: "
)

arquivo_saida = f"{nome_saida}.xlsx"

relatorio_final.to_excel(
    arquivo_saida,
    index=False
)

print()
print("Relatório criado com sucesso!")
print(f"Arquivo salvo: {arquivo_saida}")