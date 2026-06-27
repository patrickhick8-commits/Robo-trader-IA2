import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume e Probabilidade em M1.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (inclua Velas, RSI, Volume e Relógio):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume e mercado..."):
                
                # Prompt avançado de visão computacional para leitura de candlesticks e cálculo de taxa de acerto
                prompt = """
               # =========================================================================
# 🎛️ CONTROLE NATIVO DE DESEMPENHO (WIN / LOSS) - INTEGRADO VIA GITHUB
# =========================================================================
st.sidebar.title("📊 Painel de Performance")

# Inicializa as variáveis na memória se não existirem
if "feedback_trader" not in st.session_state:
    st.session_state["feedback_trader"] = ""
if "tipo_loss" not in st.session_state:
    st.session_state["tipo_loss"] = ""

# Desenha os botões lado a lado na barra lateral
col_win, col_loss = st.sidebar.columns(2)

with col_win:
    if st.button("🟢 WIN", key="btn_win_sidebar", use_container_width=True):
        st.session_state["feedback_trader"] = (
            "\n- VALIDAÇÃO: OPERAÇÃO ANTERIOR FINALIZADA EM WIN! "
            "A leitura implícita de fluxo e as defesas de pavio se confirmaram. Mantenha os filtros."
        )
        st.session_state["tipo_loss"] = ""

with col_loss:
    if st.button("🔴 LOSS", key="btn_loss_sidebar", use_container_width=True):
        st.session_state["feedback_trader"] = "RECALIBRAR"

# Exibe o menu de seleção se o trader clicar em LOSS
if st.session_state["feedback_trader"] == "RECALIBRAR":
    cenario_selecionado = st.sidebar.selectbox(
        "Qual foi a falha do mercado?",
        ["Selecione o motivo...", "1. Tendência (Falso Rompimento / Exaustão)", "2. Lateralização (Rompimento inesperado)"],
        key="select_loss_sidebar"
    )
    
    if "1." in cenario_selecionado:
        st.session_state["tipo_loss"] = (
            "\n- PROTOCOLO DE AUTO-CORREÇÃO: LOSS EM TENDÊNCIA! "
            "A vela sofreu exaustão imediata ou falso rompimento. "
            "Para a próxima análise, ignore fluxos se a vela não tiver o dobro do tamanho médio das anteriores."
        )
    elif "2." in cenario_selecionado:
        st.session_state["tipo_loss"] = (
            "\n- PROTOCOLO DE AUTO-CORREÇÃO: LOSS EM MERCADO LATERAL! "
            "A região de suporte/resistência falhou e foi rompida com forte volume. "
            "Para a próxima análise, ignore defesas fracas por pavios e siga o rompimento real."
        )

# Define o texto final que vai para o prompt da Gemini
texto_correcao_dinamica = st.session_state["tipo_loss"] if st.session_state["feedback_trader"] == "RECALIBRAR" else st.session_state["feedback_trader"]

if st.session_state["feedback_trader"] != "":
    st.sidebar.info("Status registrado para a próxima análise!")

# =========================================================================
# 🧠 PROMPT MESTRE CONFIGURADO COM A VARIÁVEL DE AUTO-AJUSTE
# =========================================================================
prompt = f"""
[ORDER_FLOW_&_PURE_CANDLE_VOLUME]
Analise o desequilíbrio, a movimentação do preço e o fluxo de ordens (Order Flow) de forma 100% implícita e exclusiva na anatomia visual das velas, SEM depender de indicadores de volume na tela:
- VOLUME POR CORPO E MOVIMENTAÇÃO: Avalie o volume financeiro real injetado pelo tamanho e expansão do corpo dos candles. Velas expressivas confirmam volume institucional empurrando o mercado.
- DEFESA E ABSORÇÃO POR PAVIOS: Avalie o volume de agressão contrária pelo tamanho dos pavios. Pavios longos em zonas críticas indicam rejeição em massa, absorção de ordens e virada iminente no fluxo.

[TIME_RULES] Leia o relógio atual no print. Projete o momento do clique de entrada de forma cirúrgica para acontecer entre 2 a 5 velas (minutos) depois do print. A expiração DEVE ser de 1 minuto para fechar exatamente no final da mesma vela de entrada (WIN no candle indicado).

[PROTOCOLO DE PERFORMANCE VISUAL - MEMÓRIA DE SESSÃO]{texto_correcao_dinamica}

Retorne estritamente neste formato markdown limpo:
PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 96% - EXTREMA CONFLUÊNCIA]
HORARIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
TEMPO DE EXPIRACAO: 1 Minuto (Fechamento na mesma vela)
HORARIO DE FECHAMENTO: [HH:MM+1:00]
DIRECAO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
ESTRATEGIA CORRETA APLICADA: [Ex: ALGORITMO DE FLUXO OTC ou REVERSÃO EM SUPORTE TRADICIONAL]

DIAGNOSTICO INSTITUCIONAL DE SINAL (PRICE ACTION & FILTROS DE SEGURANÇA):
- Leitura de Falsos Rompimentos/Pullbacks: [Explique por que o cenário atual é seguro e não se trata de uma armadilha ou falso movimento]
- Filtragem de Ruido e Volume por Corpo: [Análise da clareza e direção real do fluxo das velas]
- Absorcao e Pressao por Pavios: [O que a pressão dos pavios revelou sobre o volume oculto de defesa]
- Filtro de Segurança RSI: [Status técnico da linha do RSI para confluência]
Seja frio, direto e puramente matemático.
"""
