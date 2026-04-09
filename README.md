# 🐼 Jornada Pandas — Do Zero à Engenharia de Dados

> Documentação completa do meu aprendizado em Python, Pandas e integração com SQL, com foco em evoluir para a área de Engenharia de Dados.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?logo=numpy&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-336791?logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20andamento-yellow)

---

## 🎯 Objetivo

Este repositório documenta toda a minha jornada de aprendizado em análise e manipulação de dados com Python e Pandas, com foco direto em evoluir para a área de **Engenharia de Dados** e conquistar as primeiras vagas na área.

A progressão foi desenhada de forma linear e crescente — partindo dos fundamentos essenciais até chegar em habilidades valorizadas no mercado, como integração com bancos de dados SQL, pipelines ETL e boas práticas de desenvolvimento.

---

## 🗺️ Visão Geral da Jornada

| # | Etapa | Descrição | Status |
|---|-------|-----------|--------|
| 01 | Fundamentos do Python para Dados | Estruturas, funções, list comprehension, arquivos | 🟡 Em andamento |
| 02 | Introdução ao Pandas | Series, DataFrames, leitura e escrita de arquivos | ⬜ Pendente |
| 03 | Limpeza e Transformação de Dados | Tratamento de nulos, tipos, filtrar, agrupar | ⬜ Pendente |
| 04 | Análise Exploratória de Dados (EDA) | Estatísticas, correlações, visualizações | ⬜ Pendente |
| 05 | Manipulação Avançada com Pandas | MultiIndex, pivot, merge, join, apply, lambda | ⬜ Pendente |
| 06 | Introdução ao NumPy | Arrays, operações vetorizadas, integração Pandas | ⬜ Pendente |
| 07 | Integração com Bancos de Dados SQL | SQLite, PostgreSQL, SQLAlchemy, pipelines ETL | ⬜ Pendente |

---

## 📘 Etapa 01 — Fundamentos do Python para Dados

Antes de mergulhar no Pandas, é essencial dominar as estruturas e recursos do Python que mais aparecem no dia a dia de quem trabalha com dados.

### 1.1 Estruturas de Dados Essenciais
- **Listas:** sequências ordenadas e mutáveis
- **Tuplas:** sequências imutáveis, ideais para dados fixos
- **Dicionários:** mapeiam chaves a valores, base do modelo JSON
- **Sets:** coleções sem duplicatas, úteis para filtragem e comparação

### 1.2 Funções e Modularização
- Definição com `def`, parâmetros posicionais, nomeados e com valores padrão
- Funções **lambda**: anônimas de uma linha, muito usadas com Pandas
- **Docstrings**: documentar funções com clareza

### 1.3 List Comprehension
```python
quadrados = [x**2 for x in range(10) if x % 2 == 0]
pares = list(filter(lambda x: x % 2 == 0, range(20)))
```

### 1.4 Manipulação de Arquivos
- Leitura e escrita com `open()`, módulos `csv` e `json`
- Context managers (`with`) para fechamento seguro
- Leitura de múltiplos arquivos com `glob` e `os.path`

### 1.5 Tratamento de Erros
- `try / except / finally` para captura de exceções
- Levantamento de erros com `raise`
- Logging básico com o módulo `logging`

### 1.6 Ambiente e Boas Práticas
- Ambientes virtuais com `venv` ou `conda`
- Gerenciamento de dependências com `pip` e `requirements.txt`
- Jupyter Notebook e VS Code como ambientes de desenvolvimento

---

## 📗 Etapa 02 — Introdução ao Pandas

O Pandas é a biblioteca mais utilizada para análise e manipulação de dados em Python.

### 2.1 Instalação
```bash
pip install pandas openpyxl xlrd
```

### 2.2 Series — Estrutura Unidimensional
- Criação a partir de listas, dicionários e arrays NumPy
- Acesso por posição (`.iloc`) e por rótulo (`.loc`)
- Métodos úteis: `.head()`, `.describe()`, `.value_counts()`, `.unique()`

### 2.3 DataFrame — Estrutura Bidimensional
- Criação a partir de dicionários, listas e arquivos externos
- Atributos essenciais: `.shape`, `.dtypes`, `.columns`, `.index`, `.info()`

### 2.4 Leitura e Escrita de Arquivos
```python
df = pd.read_csv('arquivo.csv', sep=',', encoding='utf-8')
df = pd.read_excel('planilha.xlsx', sheet_name='Plan1')
df = pd.read_json('dados.json')
df.to_csv('saida.csv', index=False)
```
- Parâmetros importantes: `sep`, `header`, `index_col`, `usecols`, `dtype`, `na_values`
- Leitura de grandes arquivos com `chunksize`

### 2.5 Seleção e Indexação
```python
df['coluna']                    # selecionar uma coluna
df[['col1', 'col2']]            # selecionar múltiplas colunas
df.loc[0:5, 'nome':'idade']     # seleção por rótulo
df.iloc[0:5, 1:3]               # seleção por posição
df[df['idade'] > 18]            # filtragem booleana
df.query('idade > 18 and cidade == "SP"')
```

---

## 📙 Etapa 03 — Limpeza e Transformação de Dados

Dado sujo é uma realidade em qualquer projeto. Saber limpá-los e transformá-los é uma das habilidades mais valorizadas no mercado.

### 3.1 Valores Ausentes
```python
df.isnull().sum()                        # contagem de nulos por coluna
df.dropna(axis=0, how='any')             # remover linhas com nulos
df.fillna(df.mean(numeric_only=True))    # preencher com média
df.interpolate()                          # interpolação para séries temporais
```

### 3.2 Tipos de Dados e Conversões
```python
df['coluna'].astype('int')
pd.to_datetime(df['data'])
df['data'].dt.year   # extrair componentes de data
```

### 3.3 Renomear, Reorganizar e Filtrar
```python
df.rename(columns={'antigo': 'novo'})
df.drop(columns=['col_inutil'])
df.drop_duplicates(subset=['id'], keep='first')
df.reset_index(drop=True)
```

### 3.4 Transformações com Apply e Map
```python
df['nome'] = df['nome'].str.strip().str.lower()
df['categoria'] = df['valor'].apply(lambda x: 'alto' if x > 1000 else 'baixo')
df['status'].map({'A': 'Ativo', 'I': 'Inativo'})
```

### 3.5 Agrupamento com GroupBy
```python
df.groupby('categoria')['vendas'].sum()

df.groupby(['regiao', 'produto']).agg({
    'vendas': 'sum',
    'quantidade': 'mean'
})
```

---

## 📕 Etapa 04 — Análise Exploratória de Dados (EDA)

A EDA é o processo de investigar um dataset para entender sua estrutura, padrões, anomalias e relações entre variáveis.

### 4.1 Estatísticas Descritivas
```python
df.describe(include='all')
df['valor'].mean(), df['valor'].median()
df['valor'].quantile([0.25, 0.5, 0.75])
df['categoria'].value_counts(normalize=True)
```

### 4.2 Correlações
```python
df.corr(method='pearson')   # ou 'spearman', 'kendall'
df.cov()
```

### 4.3 Visualizações com Matplotlib e Seaborn
```python
import matplotlib.pyplot as plt
import seaborn as sns

df['valor'].hist(bins=30)
sns.boxplot(x='categoria', y='valor', data=df)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.scatterplot(x='idade', y='salario', data=df)
```

### 4.4 Detecção de Outliers
- **IQR:** valores fora de `1.5 * IQR` acima do Q3 ou abaixo do Q1
- **Z-score:** pontos a mais de 3 desvios padrão da média

### 4.5 Perguntas que a EDA deve responder
- Quais são as variáveis mais importantes do dataset?
- Há valores ausentes? Em quais colunas e qual o impacto?
- Existem duplicatas ou inconsistências?
- Quais variáveis estão correlacionadas?
- Qual é a distribuição das variáveis-alvo?

---

## 📔 Etapa 05 — Manipulação Avançada com Pandas

### 5.1 Combinação de DataFrames
```python
pd.concat([df1, df2], axis=0)   # concatenação vertical

pd.merge(pedidos, clientes, on='cliente_id', how='left')
# how: 'inner', 'left', 'right', 'outer'
```

### 5.2 Pivot Tables e Reshaping
```python
pd.pivot_table(df, values='vendas', index='regiao',
               columns='produto', aggfunc='sum')

pd.melt(df, id_vars=['id'], value_vars=['jan', 'fev', 'mar'])
```

### 5.3 Funções Avançadas
```python
# Method chaining com pipe
resultado = (df
    .pipe(remover_nulos)
    .pipe(normalizar_colunas)
    .pipe(calcular_metricas))
```

### 5.4 Séries Temporais
```python
df.set_index('data').resample('M').sum()   # agregar por mês
df['vendas'].rolling(7).mean()             # média móvel de 7 dias
df['vendas'].shift(1)                       # valor do período anterior
df['vendas'].diff()                         # variação em relação ao anterior
```

### 5.5 Performance e Otimização
- Usar `category` dtype para colunas com poucos valores únicos
- Evitar `iterrows()` — preferir vetorização
- Usar `chunksize` para arquivos grandes
- Monitorar memória com `df.memory_usage(deep=True)`

---

## 📒 Etapa 06 — Introdução ao NumPy

O NumPy é a base numérica do ecossistema científico Python. O Pandas é construído sobre ele.

### 6.1 Arrays Básicos
```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
np.zeros((3, 3))
np.arange(0, 10, 2)
np.linspace(0, 1, 100)
```

### 6.2 Operações Vetorizadas
```python
a = np.array([1, 2, 3, 4, 5])
resultado = a * 2 + 10   # sem nenhum loop Python

np.sqrt(a)
np.sum(a, axis=0)
np.mean(a)
```

### 6.3 Integração com Pandas
```python
df['coluna'].to_numpy()         # DataFrame → array
np.where(df['val'] > 0, 'positivo', 'negativo')   # substituição condicional
```

---

## 🗄️ Etapa 07 — Integração com Bancos de Dados SQL

Esta etapa marca a transição de analista para engenheiro de dados.

### 7.1 SQLite — Banco Embutido
```python
import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM vendas WHERE regiao = ?', ('Sul',))
resultados = cursor.fetchall()
conn.close()
```

### 7.2 Pandas + SQLite
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('banco.db')

# Ler tabela como DataFrame
df = pd.read_sql('SELECT * FROM vendas', conn)

# Salvar DataFrame como tabela
df_limpo.to_sql('vendas_limpas', conn, if_exists='replace', index=False)

conn.close()
```

### 7.3 SQLAlchemy — Padrão de Mercado
```python
from sqlalchemy import create_engine

# SQLite
engine = create_engine('sqlite:///banco.db')

# PostgreSQL
engine = create_engine('postgresql://usuario:senha@localhost:5432/meu_banco')

df = pd.read_sql('SELECT * FROM clientes', con=engine)
df.to_sql('clientes_tratados', con=engine, if_exists='replace', index=False)
```

### 7.4 PostgreSQL com Docker
```bash
# Subir um PostgreSQL local
docker run --name pg -e POSTGRES_PASSWORD=senha -p 5432:5432 -d postgres

# Instalar dependências
pip install psycopg2-binary sqlalchemy
```

### 7.5 Pipeline ETL Completo
```python
import pandas as pd
from sqlalchemy import create_engine

# 1. EXTRACT
df = pd.read_csv('dados_brutos.csv')

# 2. TRANSFORM
df = (df
    .dropna(subset=['id', 'valor'])
    .rename(columns={'dt': 'data', 'val': 'valor'})
    .assign(data=lambda x: pd.to_datetime(x['data']))
    .query('valor > 0')
)

# 3. LOAD
engine = create_engine('postgresql://usuario:senha@localhost:5432/db')
df.to_sql('vendas_processadas', con=engine, if_exists='replace', index=False)

print(f"Pipeline concluído: {len(df)} registros carregados.")
```

---

## 🐙 Estrutura do Repositório

```
pandas-jornada/
├── 01_fundamentos_python/
│   ├── estruturas_dados.ipynb
│   └── funcoes_e_erros.ipynb
├── 02_introducao_pandas/
│   ├── series_e_dataframes.ipynb
│   └── leitura_arquivos.ipynb
├── 03_limpeza_dados/
├── 04_eda/
├── 05_pandas_avancado/
├── 06_numpy/
├── 07_sql_integracao/
│   ├── sqlite_basico.ipynb
│   ├── pandas_sql.ipynb
│   └── etl_pipeline.ipynb
├── dados/
├── requirements.txt
└── README.md
```

---

## 🚀 Próximos Passos — Após Esta Jornada

Ao concluir as 7 etapas, os próximos horizontes naturais são:

| Área | Tecnologias |
|------|-------------|
| Orquestração de pipelines | Apache Airflow, Prefect |
| Transformação em SQL | dbt (data build tool) |
| Processamento em escala | Apache Spark, PySpark |
| Containerização | Docker, Docker Compose |
| Cloud & Data Warehouse | AWS S3 + Redshift, Google BigQuery, Snowflake |

---

## 📦 Dependências

```bash
pip install pandas numpy matplotlib seaborn openpyxl sqlalchemy psycopg2-binary jupyter
```

---

> *"A consistência supera o talento. Commite todo dia."* 🚀
