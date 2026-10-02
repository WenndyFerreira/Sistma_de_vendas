##Sistma_de_vendas.py


import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# -Sistema de Vendas- ")

tabela = pd.read_csv("vendas.csv")

st.write("Cadastrar Vendas: ")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao = st.sidebar.button("Cadastrar venda")

if botao:
    if valor <=0 or quantidade <=0:
        st.error("Valor e quantidade devem ser maiores que zero!")
    else:
        nova_venda = [data, vendedor, produto, quantidade, valor]
        tabela.loc[len(tabela)] = nova_venda
        tabela.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada!")


st.write("## -Vendas Cadastradas- ")
st.dataframe(tabela)


st.write("## -Dashboard- ")
soma = tabela["valor"].sum()
st.metric("Faturamento total", f"R${soma}")

grafico = px.bar(tabela, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico)

grafico2 = px.pie(tabela, names="produto", values="valor")
st.plotly_chart(grafico2)




