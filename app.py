import streamlit as st
import pandas as pd
import sqlite3
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import joblib
import os

MODELO_PATH = "models/modelo_irrigacao.pkl"

# --- Função para carregar dados do SQLite ---
@st.cache_data
def carregar_dados_sqlite():
    con = sqlite3.connect("db/sensores.db")
    df = pd.read_sql_query("SELECT * FROM leituras", con)
    con.close()
    return df

# --- Função para treinar e salvar modelo ---
def treinar_e_salvar_modelo(df):
    X = df[["umidade", "nutrientes", "hora"]]
    y = df["precisa_irrigar"]
    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)
    os.makedirs("models", exist_ok=True)
    joblib.dump(modelo, MODELO_PATH)
    return modelo

# --- Função para carregar modelo salvo ou treinar se não existir ---
def carregar_ou_treinar_modelo(df):
    try:
        if os.path.exists(MODELO_PATH):
            modelo = joblib.load(MODELO_PATH)
            st.info("✅ Modelo carregado de 'models/modelo_irrigacao.pkl'")
        else:
            raise FileNotFoundError  # força treino se arquivo não existir
    except (EOFError, FileNotFoundError, Exception):
        st.warning("⚠️ Modelo ausente ou corrompido. Treinando novo...")
        modelo = treinar_e_salvar_modelo(df)
        st.success("🎉 Novo modelo treinado e salvo.")
    return modelo

# --- Interface Streamlit ---
st.title("🌾 FarmTech Solutions - Sistema de Irrigação Inteligente")
df = carregar_dados_sqlite()

st.subheader("📈 Dados dos Sensores")
st.dataframe(df)

modelo = carregar_ou_treinar_modelo(df)

# --- Avaliação do modelo ---
st.subheader("📊 Avaliação (base completa)")
y_pred = modelo.predict(df[["umidade", "nutrientes", "hora"]])
from sklearn.metrics import classification_report
import pandas as pd

report = classification_report(df["precisa_irrigar"], y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df.style.format(precision=2), use_container_width=True)

# --- Previsão interativa ---
st.subheader("🔮 Faça uma Previsão")
umidade_input = st.slider("Umidade do Solo (%)", 0, 100, 50)
nutrientes_input = st.slider("Nível de Nutrientes (%)", 0, 100, 70)
hora_input = st.slider("Hora do dia", 0, 23, 12)

entrada = pd.DataFrame([[umidade_input, nutrientes_input, hora_input]],
                        columns=["umidade", "nutrientes", "hora"])

predicao = modelo.predict(entrada)[0]
resultado = "💧 Deve irrigar!" if predicao == 1 else "🌞 Solo adequado, sem irrigação."
st.success(f"Resultado: {resultado}")
