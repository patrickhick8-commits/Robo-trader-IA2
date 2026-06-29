import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Probabilidade em M1.")

# 2. Configuração da Chave da IA
st.sidebar.title("Configurações")
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # --- MENU DE SELEÇÃO DE MODO OPERACIONAL ---
    st.markdown("### 🛠️ Escolha o Modo Operacional:")
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    
    if "modo_operacao" not in st.session_state:
        st.session_state.modo_operacao = "ANALISE"

    with col_btn1:
        if st.button("🚀 Gerar Nova Análise/Sinal", use_container_width=True):
            st.session_state.modo_operacao = "ANALISE"
    with col_btn2:
        if st.button("🟢 Autoanálise de WIN", use_container_width=True):
            st.session_state.modo_operacao = "WIN"
    with col_btn3:
        if st.button("🔴 Autoanálise de LOSS", use_container_width=True):
            st.session_state.modo_operacao = "LOSS"

    modo = st.session_state.modo_operacao
