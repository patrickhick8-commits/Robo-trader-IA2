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
        st.error("Por favor, ative a câmera ou envie uma foto do gráfico antes de rodar a detecção.")
    else:
        with st.spinner("IA aplicando filtros máximos de volatilidade e padrões técnicos..."):
            try:
                client = genai.Client(api_key=api_key)
                
                prompt = """
                [SYSTEM_ROLE] Aja como robô de trading institucional de alta performance, operando com frieza absoluta e precisão cirúrgica. Escaneie a imagem enviada, cruze dados gráficos e calcule a taxa de assertividade matemática ponderada.
                [OPERATIONAL_PARAMETERS] Filtro Máximo: Combine EMA 10, RSI 14, volume implícito, rejeição extrema de pavios e zonas de preço. Trava de Assertividade: Apenas envie sinais com assertividade estritamente de 80% a 99%. Filtro de Aborto: Se a confluência técnica for menor que 80%, defina como [ABORTAR OPERAÇÃO - ALTO RISCO].
                [MARKET_STATE_ADAPTATION] 1-Gráfico Parado: Filtre falsos rompimentos. Foque em suporte/resistência horizontais e padrões de reversão por exaustão. 2-Gráfico Volátil: Priorize retração milimétrica em pavios e fluxo de continuidade.
                [FIXED_TIME_LOGIC_RULES] Leia o relógio atual no print. Calcule o momento do clique futuro e sua expiração seguindo rigorosamente estas ordens:
                1. O momento do clique de entrada DEVE ser projetado obrigatoriamente para acontecer entre 2 a 5 velas (minutos) DEPOIS do horário exato do print.
                2. A expiração da operação DEVE ser programada estritamente para o fim da mesma vela em que a entrada foi realizada (expiração para a mesma vela).
                Retorne o sinal gerado de forma muito clara, fria e objetiva na tela.
                """
                
                resposta = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image_to_analyze, prompt]
                )
                
                st.success("🎯 ANÁLISE CONCLUÍDA COM SUCESSO!")
                st.components.v1.html(
                    '<audio autoplay src="https://google.com"></audio>',
                    height=0
                )
                st.markdown(resposta.text)
                
            except Exception as e:
                st.error(f"Falha na comunicação com o servidor Gemini: {e}")
