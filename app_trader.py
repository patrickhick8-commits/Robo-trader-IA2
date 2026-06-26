import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="IA TraderPro - Sistema de Elite", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #121212 !important; font-family: sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; }
    .panel-container { text-align: center; max-width: 450px; margin: auto; padding-top: 10px; }
    .top-bar { display: flex; justify-content: flex-end; width: 100%; max-width: 450px; margin: 0 auto 20px auto; }
    .btn-sair { background-color: #d32f2f; color: #ffffff; padding: 8px 18px; border-radius: 6px; font-weight: 600; text-decoration: none; text-transform: uppercase; }
    .brand-logo { color: #ffffff; font-size: 54px; font-weight: 700; margin-bottom: 15px; }
    .brand-logo span { color: #00bfa5; }
    .headline-text { color: #ffffff; font-size: 19px; margin-bottom: 35px; }
    div.stButton > button { background-color: transparent !important; color: #ffffff !important; border: 2px solid #00bfa5 !important; border-radius: 8px !important; width: 100% !important; padding: 14px !important; font-size: 16px !important; }
    .action-container div.stButton > button { background-color: #262626 !important; color: #666666 !important; border: none !important; }
    .active-btn div.stButton > button { background-color: #00bfa5 !important; color: #121212 !important; border: none !important; box-shadow: 0px 4px 15px rgba(0, 191, 165, 0.4) !important; }
    </style>
""", unsafe_allow_html=True)

if "modo_captura" not in st.session_state:
    st.session_state.modo_captura = None

st.markdown("""
    <div class='top-bar'><a href='#' class='btn-sair'>[→ Sair</a></div>
    <div class='panel-container'>
        <div class='brand-logo'>IA Trader<span>🤖</span>Pro</div>
        <div class='headline-text'>Envie o gráfico e descubra se existe uma oportunidade agora</div>
    </div>
""", unsafe_allow_html=True)

api_key = st.text_input("Insira sua Gemini API Key para inicializar:", type="password", key="gemini_api_key")

if not api_key:
    st.warning("Chave de API ausente. Insira sua Gemini API Key no campo acima para inicializar.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    if st.button("📷 Ativar Câmera"): st.session_state.modo_captura = "camera"
with col2:
    if st.button("📁 Anexar foto"): st.session_state.modo_captura = "arquivo"

image_to_analyze = None

if st.session_state.modo_captura == "camera":
    img_camera = st.camera_input("Posicione a câmera no gráfico")
    if img_camera: image_to_analyze = Image.open(img_camera)
elif st.session_state.modo_captura == "arquivo":
    img_file = st.file_uploader("Selecione o arquivo de print de tela M1", type=["png", "jpg", "jpeg"])
    if img_file: image_to_analyze = Image.open(img_file)

if image_to_analyze:
    st.image(image_to_analyze, caption="Gráfico M1 Pronto para Scanner", width=380)

classe_botao = "active-btn" if image_to_analyze else "action-container"

st.markdown(f"<div class='{classe_botao}'>", unsafe_allow_html=True)
executar = st.button("DETECTAR ENTRADA")
st.markdown("</div>", unsafe_allow_html=True)

if executar:
    if not image_to_analyze:
        st.error("Por favor, envie uma foto do gráfico antes de rodar a detecção.")
    else:
        with st.spinner("IA aplicando filtros máximos de volatilidade..."):
            try:
                client = genai.Client(api_key=api_key)
                
                prompt = """
                Aja como robô de trading institucional de alta performance. 
                Escaneie o print M1 enviado, cruze dados gráficos (EMA 10, RSI 14, volume, rejeição de pavios, suporte/resistência).
                Calcule a assertividade (mínimo 80% para operar, caso contrário retorne ABORTAR OPERAÇÃO).
                Analise volatilidade e adapte filtros. Estipule o momento exato do clique e expiração de forma variável baseado nos pavios, tamanho de velas e fluxo.
                Retorne o sinal gerado de forma limpa e direta na tela.
                """
                
                resposta = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image_to_analyze, prompt]
                )
                st.success("🎯 ANÁLISE CONCLUÍDA COM SUCESSO!")
                st.markdown(resposta.text)
            except Exception as e:
                st.error(f"Falha na comunicação com o servidor Gemini: {e}")
