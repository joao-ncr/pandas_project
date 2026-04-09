# Trilha de Estudos — Engenharia de Dados

> **Base já dominada:** Python (avançado) · SQL (avançado) · Git & GitHub

---

## ✅ Quando posso buscar meu primeiro estágio?

**Ao concluir a Etapa 2** você já tem perfil competitivo para estágios.
A Etapa 1 sozinha já abre portas em startups e empresas menores.
As Etapas 3, 4 e 5 são para crescimento (pleno, sênior, especialização).

**O que mais pesa nas entrevistas:**
- Projetos reais no GitHub com README bem escrito
- Saber explicar as decisões técnicas dos seus projetos
- SQL continua sendo o item mais cobrado em testes técnicos

---

## Etapa 1 — Pandas & Análise de Dados

### Conteúdo
- DataFrames, Series, indexação e slicing
- Merge, join, groupby, pivot tables
- Limpeza de dados (nulos, duplicatas, tipos)
- Matplotlib / Seaborn para visualização
- Integração com SQL (`read_sql`, `to_sql`)

### Projetos
- Análise exploratória de dataset público (ex: IBGE, Kaggle)
- Dashboard de vendas com gráficos (CSV → Pandas → Matplotlib)
- Limpeza e transformação de dados brutos + relatório em Jupyter
- Pipeline de análise documentado no GitHub com README

---

## Etapa 2 — Ambiente de Dados: Docker · Airflow · dbt

### Conteúdo
- Docker e Docker Compose para isolar serviços
- Apache Airflow: DAGs, operadores, agendamento
- dbt: models, testes, documentação e lineage
- Conceitos de ELT vs ETL e data warehouse
- PostgreSQL como warehouse local

### Projetos
- Pipeline ELT com Airflow + PostgreSQL (ingestão diária de API pública)
- Modelagem dimensional com dbt (fatos e dimensões)
- Ambiente dockerizado com Airflow + Postgres + dbt
- Testes de qualidade de dados com `dbt test`

---

## Etapa 3 — Cloud & Data Lake: AWS ou GCP

### Conteúdo
- S3 / GCS (armazenamento de objetos, particionamento)
- Glue / BigQuery / Athena / Redshift
- Formatos colunares: Parquet, Delta Lake, Iceberg
- IAM, permissões e boas práticas de segurança
- Medallion architecture (bronze / silver / gold)

### Projetos
- Data lake em S3/GCS com camadas bronze → silver → gold
- ETL serverless com AWS Lambda ou Cloud Functions
- Query em Parquet com Athena/BigQuery (sem servidor)
- Custo e otimização: particionamento e compressão

---

## Etapa 4 — Processamento em Larga Escala: Spark & Streaming

### Conteúdo
- PySpark: RDDs, DataFrames, Spark SQL
- Spark Streaming ou Kafka para dados em tempo real
- Databricks (ou EMR) como plataforma gerenciada

### Projetos
- Processamento de dataset grande (ex: dados do IBGE) com PySpark
- Pipeline de streaming simulado com Kafka + Spark Streaming
- Comparação PySpark vs Pandas em performance (notebook)

---

## Etapa 5 — Projeto de Portfólio Completo (end-to-end)

Combine tudo em um projeto real publicado no GitHub:

- Ingestão de fonte pública (API → S3/GCS) com Airflow
- Transformação com dbt ou PySpark (camadas silver/gold)
- Armazenamento em data warehouse (BigQuery, Redshift ou DuckDB)
- Dashboard final com Metabase, Superset ou Looker Studio
- README com arquitetura, diagramas e decisões técnicas
- CI/CD com GitHub Actions para testes dbt e lint

---

## Dicas Gerais

- **Ferramentas gratuitas para começar:** PostgreSQL local + Docker resolve a Etapa 2 inteira. AWS Free Tier e BigQuery Sandbox do GCP são suficientes para a Etapa 3.
- **DuckDB** é uma excelente alternativa local ao BigQuery para estudar formatos colunares.
- **Spark** é útil mas não obrigatório para entrar no mercado — muitos engenheiros trabalham só com dbt + Airflow + cloud.

## Referências Gratuitas

- Airflow: [docs.astronomer.io](https://docs.astronomer.io)
- dbt: [docs.getdbt.com](https://docs.getdbt.com)
- YouTube: canal **DataWithMarc**
