import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Dashboard - Cap 1 - Construindo uma máquina agrícola", layout="wide")

# Título
st.title("🌱 Dashboard - Cap 1 - Construindo uma máquina agrícola")

# Conectar ao banco SQLite
conn = sqlite3.connect("dados_irrigacao.db")
df = pd.read_sql_query("SELECT * FROM leitura_sensores ORDER BY timestamp DESC", conn)
conn.close()

# Mostrar a tabela
st.subheader("📋 Últimas Leituras dos Sensores")
st.dataframe(df)

# Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("💧 Umidade do Solo (%)")
    fig, ax = plt.subplots(figsize=(6, 2.5))  # 👈 ajustado
    ax.plot(df["timestamp"], df["umidade"], marker="o")
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Umidade (%)")
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.subheader("🧪 Simulação de pH (via LDR)")
    fig2, ax2 = plt.subplots(figsize=(6, 2.5))  # 👈 ajustado
    ax2.plot(df["timestamp"], df["ph_analogico"], marker="x", color="orange")
    ax2.set_xlabel("Tempo")
    ax2.set_ylabel("Valor Analógico (simulando pH)")
    ax2.grid(True)
    st.pyplot(fig2)

# Status da bomba
st.subheader("🚰 Status da Irrigação (Última Leitura)")
status = df.iloc[0]["irrigacao_ativa"]
st.metric(label="Bomba de Irrigação", value="ATIVA 💦" if status else "INATIVA 🛑")

# Rodapé
st.caption("Projeto FIAP • Fase 3 – Cap 1 - Construindo uma máquina agrícola")
