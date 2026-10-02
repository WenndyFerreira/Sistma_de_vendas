# 📊 Sistema de Vendas em Python

Sistema de vendas desenvolvido em **Python** com o objetivo de praticar desenvolvimento de aplicações, manipulação de dados e criação de dashboards interativos.

O projeto permite cadastrar novas vendas, armazenar os dados em um arquivo CSV, visualizar as vendas cadastradas e acompanhar indicadores através de gráficos.

---

## 🚀 Funcionalidades

- 📝 Cadastro de novas vendas
- 📅 Seleção da data da venda
- 👤 Seleção do vendedor
- 💻 Seleção do produto
- 🔢 Registro da quantidade
- 💰 Registro do valor da venda
- ⚠️ Validação de valores e quantidades
- 💾 Armazenamento dos dados em arquivo CSV
- 📋 Visualização das vendas cadastradas
- 💵 Cálculo automático do faturamento total
- 📊 Gráfico de vendas por vendedor e produto
- 🥧 Gráfico de distribuição das vendas por produto

---

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 🖥️ Streamlit
- 🐼 Pandas
- 📊 Plotly
- 📁 CSV

---

## 📚 Bibliotecas utilizadas

```python
import streamlit as st
import pandas as pd
import plotly.express as px
```

---

## 📂 Estrutura do projeto

```text
Sistema-de-Vendas/
│
├── Sistema_de_vendas.py
├── vendas.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone SEU_LINK_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd Sistema-de-Vendas
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Streamlit

```bash
py -m streamlit run Sistema_de_vendas.py
```

O sistema será aberto no navegador.

---

## 📊 Dashboard

O sistema possui um dashboard que apresenta:

### 💰 Faturamento total

Calculado automaticamente através dos valores registrados:

```python
soma = tabela["valor"].sum()
st.metric("Faturamento total", f"R${soma}")
```

### 📊 Vendas por vendedor

Gráfico de barras criado com Plotly:

```python
grafico = px.bar(
    tabela,
    x="vendedor",
    y="valor",
    color="produto"
)

st.plotly_chart(grafico)
```

### 🥧 Vendas por produto

Gráfico de pizza mostrando a participação dos produtos nas vendas:

```python
grafico2 = px.pie(
    tabela,
    names="produto",
    values="valor"
)

st.plotly_chart(grafico2)
```

---

## 🧠 Conceitos praticados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Variáveis
- Condicionais (`if` / `else`)
- Manipulação de DataFrames
- Leitura de arquivos CSV
- Escrita de arquivos CSV
- Validação de dados
- Interface gráfica com Streamlit
- Manipulação de dados com Pandas
- Visualização de dados com Plotly
- Dashboards
- Métricas e indicadores

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Python e Análise e Desenvolvimento de Sistemas**, com foco em colocar em prática conceitos de programação, manipulação e visualização de dados.

---

## 👨‍💻 Autor

**Wenndy Ferreira dos Santos**

Estudante de Análise e Desenvolvimento de Sistemas.

Projeto desenvolvido para fins de estudo e evolução profissional.

---

⭐ Se este projeto foi útil ou interessante, fique à vontade para deixar uma estrela no repositório!
