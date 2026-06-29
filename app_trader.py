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
    
    # Criando apenas 2 colunas para os botões de WIN e LOSS
    col_btn1, col_btn2 = st.columns(2)
    
    # Define um modo padrão inicial caso nenhum botão tenha sido clicado ainda
    if "modo_operacao" not in st.session_state:
        st.session_state.modo_operacao = "AGUARDANDO"

    with col_btn1:
        if st.button("🟩 Autoanálise de WIN", use_container_width=True):
            st.session_state.modo_operacao = "WIN"
            
    with col_btn2:
        if st.button("🟥 Autoanálise de LOSS", use_container_width=True):
            st.session_state.modo_operacao = "LOSS"

    modo = st.session_state.modo_operacao

    # Exibe o modo atual selecionado para confirmação visual do usuário
    if modo == "AGUARDANDO":
        st.info("Aguardando comando... Clique em WIN ou LOSS para iniciar a autoanálise.")
    elif modo == "WIN":
        st.success("Modo Atual: 🟩 Autoanálise de WIN ativada.")
    elif modo == "LOSS":
        st.error("Modo Atual: 🟥 Autoanálise de LOSS ativada.")
