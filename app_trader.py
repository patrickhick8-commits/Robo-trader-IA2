import streamlit as st
from google import genai
from PIL import Image
import time

# 1. Configuração da Página e Ocultação OBRIGATÓRIA do Streamlit Padrão
st.set_page_config(page_title="IA TraderPro - Sistema de Elite", page_icon="🤖", layout="centered")

# CSS Customizado Avançado para Clonar o Design da Segunda Tela
st.markdown("""
    <style>
    /* Fundo Totalmente Preto e Fonte Esportiva/Moderna */
    .stApp {
        background-color: #121212 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    
    /* Oculta completamente a barra superior nativa e rodapés do Streamlit */
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    
    /* Bloco Container Centralizado */
    .panel-container {
        text-align: center;
        max-width: 450px;
        margin: auto;
        padding-top: 10px;
    }
    
    /* Botão Sair Vermelho Alinhado ao Topo Direito */
    .top-bar {
        display: flex;
        justify-content: flex-end;
        width: 100%;
        max-width: 450px;
        margin: 0 auto 20px auto;
    }
    .btn-sair {
        background-color: #d32f2f;
        color: #ffffff;
        padding: 8px 18px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 14px;
        text-decoration: none;
        display: flex;
        align-items: center;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Título Logo Grande */
    .brand-logo {
        color: #ffffff;
        font-size: 54px;
        font-weight: 700;
        margin-bottom: 15px;
        letter-spacing: -1.5px;
    }
    .brand-logo span {
        color: #00bfa5;
    }
    
    /* Subtítulo de Comando */
    .headline-text {
        color: #ffffff;
        font-size: 19px;
        font-weight: 400;
        line-height: 1.5;
        margin-bottom: 35px;
        padding: 0 15px;
    }

    /* Modifica os botões superiores de captura para estilo vazado com borda ciano */
    div.stButton > button {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 2px solid #00bfa5 !important;
        border-radius: 8px !important;
        width: 100% !important;
        padding: 14px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        margin-bottom: 10px !important;
    }
    div.stButton > button:hover {
        background-color: rgba(0, 191, 165, 0.1) !important;
        border-color: #00bfa5 !important;
        color: #ffffff !important;
    }

    /* Customização do Botão de Disparo Base (Cinza Escuro / Inativo) */
    .action-container div.stButton > button {
        background-color: #262626 !important;
        color: #666666 !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 17px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-top: 20px !important;
    }
    
    /* Quando a imagem é injetada, o botão muda para Ciano Ativo */
    .active-btn div.stButton > button {
        background-color: #00bfa5 !important;
        color: #121212 !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 17px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-top: 20px !important;
        cursor: pointer !important;
        box-shadow: 0px 4px 15px rgba(0, 191, 165, 0.4) !important;
    }
    .active-btn div.stButton > button:hover {
        background-color: #00a68f !important;
        color: #121212 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Estado interno da sessão para gerenciar os cliques de Câmera/Arquivo
if "modo_captura" not in st.session_state:
    st.session_state.modo_captura = None# 2. Renderização da Interface Visual Superior Clonada com o Novo Nome
st.markdown("""
    <div class='top-bar'>
        <a href='#' class='btn-sair'>[→ Sair</a>
    </div>
    <div class='panel-container'>
        <div class='brand-logo'>IA Trader<span>🤖</span>Pro</div>
        <div class='headline-text'>Envia o gráfico e descubra se existe uma oportunidade agora</div>
    </div>
""", unsafe_allow_html=True)

# Chave de API inserida estrategicamente na sidebar para manter a tela limpa
API_KEY = st.sidebar.text_input("Configuração - Gemini API Key:", type="password")

# Seletor de entrada por botões vazados lado a lado
col1, col2 = st.columns(2)
with col1:
    if st.button("📷 Ativar Câmera"):
        st.session_state.modo_captura = "camera"
with col2:
    if st.button("📁 Anexar foto"):
        st.session_state.modo_captura = "arquivo"

image_to_analyze = None

# Exibição Condicional da Ferramenta de Captura Selecionada
if st.session_state.modo_captura == "camera":
    img_camera = st.camera_input("Posicione a câmera do celular/PC no gráfico")
    if img_camera:
        image_to_analyze = Image.open(img_camera)

elif st.session_state.modo_captura == "arquivo":
    img_file = st.file_uploader("Selecione o arquivo de print de tela M1", type=["png", "jpg", "jpeg"])
    if img_file:
        image_to_analyze = Image.open(img_file)

# Preview da Imagem Carregada na Tela
if image_to_analyze:
    st.image(image_to_analyze, caption="Gráfico M1 Pronto para Scanner", use_container_width=True)

# Define o estilo visual do botão principal baseado na presença da imagem
classe_botao = "active-btn" if image_to_analyze else "action-container"

st.markdown(f"<div class='{classe_botao}'>", unsafe_allow_html=True)
executar = st.button("DETECTAR ENTRADA")
st.markdown("</div>", unsafe_allow_html=True)

# 3. Processamento e Execução do Motor de IA com Regras de Filtros Máximos
if executar:
    if not API_KEY:
        st.error("Chave de API ausente. Insira sua Gemini API Key na barra lateral para inicializar.")
    elif image_to_analyze is None:
        st.warning("Nenhum gráfico carregado. Por favor, ative a câmera ou anexe uma foto primeiro.")
    else:
        start_time = time.perf_counter()
        client = genai.Client(api_key=API_KEY)
        
        with st.spinner("IA aplicando filtros máximos de volatilidade e padrões técnicos..."):
        prompt = """
        [SYSTEM_ROLE]
        Você é um robô de trading institucional de alta performance...
        """
