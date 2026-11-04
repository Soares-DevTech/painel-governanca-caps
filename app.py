import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestão Rede CAPS-PI", page_icon="🏥", layout="wide")

st.title("🏥 Painel de Governança e Rede CAPS - Piauí")
st.markdown("Aplicativo em nuvem integrado com bases de dados.")

# Menu lateral para escolher a base de dados
menu = st.sidebar.selectbox(
    "Selecione o Módulo:", 
    ["Rede CAPS PI", "Repositório Legal", "Calendário de Governança", "Tipos de CAPS"]
)

if menu == "Rede CAPS PI":
    st.subheader("📍 Rede CAPS do Piauí")
    try:
        df = pd.read_csv("Rede_CAPS_PI.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Arquivo Rede_CAPS_PI.csv não encontrado.")

elif menu == "Repositório Legal":
    st.subheader("⚖️ Repositório Legal")
    try:
        df = pd.read_csv("Repositorio_Legal.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Arquivo Repositório Legal não encontrado.")

elif menu == "Calendário de Governança":
    st.subheader("📅 Calendário de Governança")
    try:
        df = pd.read_csv("Calendario_Governanca.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Arquivo Calendário de Governança não encontrado.")

elif menu == "Tipos de CAPS":
    st.subheader("ℹ️ Tipos de CAPS")
    try:
        df = pd.read_csv("Tipos_de_CAPS.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.warning("Arquivo Tipos de CAPS não encontrado.")

st.markdown("---")
st.caption("Desenvolvido em Python & Streamlit | Pronto para acesso mobile via Android")
