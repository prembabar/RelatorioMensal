# Sistema de Automação de Relatórios de Presença

Sistema desenvolvido em Python para automatizar a organização de relatórios de participantes de reuniões do Zoom, facilitando o controle de presença e ausência de alunos em aulas online.

O projeto utiliza arquivos CSV exportados pelo Zoom e planilhas Excel para processar os dados, calcular a frequência dos participantes e gerar relatórios organizados.

## Objetivo

Reduzir o trabalho manual de organização e conferência de presença dos alunos, automatizando duas etapas principais:

- Processamento individual dos relatórios de participantes.
- Consolidação de vários relatórios em uma única planilha mensal de frequência.

## Tecnologias utilizadas

- **Python 3.14**
- **Pandas:** manipulação e organização dos dados.
- **OpenPyXL:** criação e formatação de planilhas Excel.

## Estrutura do projeto

```text
Sistema-Relatorios-Presenca/
│
├── relatorioMensal.py
├── relatorioMensalCompleto.py
├── participantes.csv
│
├── relatorios/
│   ├── Materia_01-04-2026.xlsx
│   ├── Materia_08-04-2026.xlsx
│   └── Materia_15-04-2026.xlsx
│
└── README.md
```

## Funcionalidades

### 1. relatorioMensal.py

Responsável pelo processamento individual dos relatórios exportados pelo Zoom.

Funcionalidades:

- Leitura automática do arquivo CSV de participantes.
- Organização dos nomes e informações dos participantes.
- Processamento dos horários de entrada e saída.
- Cálculo da duração de participação.
- Definição da duração total da aula.
- Cálculo da frequência com base no percentual mínimo de presença.
- Exportação dos dados organizados para Excel.
- Possibilidade de definir o nome do arquivo de saída.

**Critério de presença:** o sistema utiliza inicialmente 75% da duração total da aula como percentual mínimo para considerar o aluno presente.

### 2. relatorioMensalCompleto.py

Responsável por reunir diversos relatórios individuais em uma única planilha.

Funcionalidades:

- Leitura de vários arquivos Excel de uma pasta específica.
- Identificação dos participantes de cada aula.
- Organização das aulas em colunas.
- Identificação de presença e ausência.
- Consolidação da frequência dos alunos.
- Geração de uma planilha final com os resultados.

Os nomes das aulas podem utilizar o nome da matéria e a data, facilitando a identificação de cada encontro.

## Instalação

É necessário ter o Python instalado na máquina.

Instale as bibliotecas utilizadas pelo projeto:

```bash
python -m pip install pandas openpyxl
```

## Como utilizar

### Etapa 1 — Gerar o relatório individual

1. Exporte o relatório de participantes da reunião no Zoom em formato CSV.
2. Coloque o arquivo `participantes.csv` na mesma pasta do código `relatorioMensal.py`.
3. Execute:

```bash
python relatorioMensal.py
```

4. Informe o nome desejado para o arquivo Excel.
5. Informe a duração total da aula em minutos.

O sistema irá processar os dados e gerar uma planilha Excel organizada.

### Etapa 2 — Consolidar os relatórios

1. Crie uma pasta chamada `relatorios`.
2. Coloque dentro dela todos os relatórios Excel gerados na etapa anterior.
3. Execute:

```bash
python relatorioMensalCompleto.py
```

4. O sistema irá reunir os relatórios encontrados e gerar uma planilha consolidada de presença e ausência.

**Importante:** mantenha os arquivos individuais organizados dentro da pasta `relatorios` para que o sistema consiga localizá-los.

## Resultado esperado

Ao final do processamento, será gerada uma planilha Excel contendo os participantes e suas respectivas frequências nas aulas.

Exemplo ilustrativo:

| Participante | Matéria - 01/04 | Matéria - 08/04 | Matéria - 15/04 |
|---|---|---|---|
| Aluno 1 | P | P | F |
| Aluno 2 | F | P | P |
| Aluno 3 | P | P | P |

Legenda:

- **P:** Presença.
- **F:** Falta.

## Possíveis melhorias futuras

- Integração direta com a API do Zoom.
- Download automático dos relatórios de reuniões.
- Filtro de reuniões por matéria, turma e período.
- Consolidação automática de relatórios mensais.
- Interface gráfica para facilitar a utilização.
- Geração de dashboards de frequência.

## Autor

Projeto desenvolvido como solução de automação de processos administrativos e acadêmicos, utilizando Python para otimizar a organização e o controle de frequência de alunos em aulas online.
