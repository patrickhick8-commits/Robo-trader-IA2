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

    if modo == "ANALISE":
        st.info("🎯 **Modo Atual:** Gerar nova análise preditiva para entrada rápida.")
        texto_upload = "Arraste ou COLE (Ctrl+V) o print completo do gráfico M1 para gerar o sinal:"
    elif modo == "WIN":
        st.success("🟢 **Modo Atual:** Autoanálise de WIN. Filtragem fina e refinamento de assertividade máxima.")
        texto_upload = "Arraste ou COLE (Ctrl+V) o print do momento exato do seu WIN:"
    elif modo == "LOSS":
        st.error("🔴 **Modo Atual:** Autoanálise de LOSS. Calibragem de filtros anti-ruído e mapeamento de falhas.")
        texto_upload = "Arraste ou COLE (Ctrl+V) o print do momento exato do seu LOSS:"

    # 3. Campo de Upload do Print (Suporta arrastar ou dar Ctrl+V)
    uploaded_file = st.file_uploader(texto_upload, type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Gráfico M1 Carregado para Autoanálise [{modo}]", use_container_width=True)
        
        # Define o botão de execução com base no modo
        texto_botao_disparo = "🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"
        if modo == "WIN":
            texto_botao_disparo = "🔬 EXECUTAR AUTOANÁLISE DE CONFLUÊNCIA DE WIN"
        elif modo == "LOSS":
            texto_botao_disparo = "🛡️ EXECUTAR AUTOANÁLISE DE FILTRAGEM DE LOSS"

        if st.button(texto_botao_disparo):
            with st.spinner("IA executando varredura milimétrica no gráfico..."):
                
                # PROMPT BASE INSTITUCIONAL (Seu prompt original robusto)
                prompt_base = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita, garantindo uma assertividade absurda focada em vitória imediata (WIN) exatamente no candle indicado.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Você está terminantemente proibido de passar sinais com confluências fracas. Se houver o menor ruído, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                Aplique filtros severos para blindar a operação contra armadilhas comuns de mercado:
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas, sem expressão ou com pavios longos de prevenção na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva (Marubozu), demonstrando volume institucional real e intenção de romper a zona.
                2. FILTRO DE FALSO PULLBACK: Bloqueie entradas de pullback se a vela que retorna para testar a região rompida demonstrar força extrema contrária (corpo muito grande). O pullback legítimo deve ser testado por velas de exaustão (corpos decrescentes) e deixar pavio de rejeição exatamente ao tocar a zona rompida.
                3. FILTRO DE RUÍDO: Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro do mercado.
                
                [AUTOMATIC_MARKET_ADAPTATION]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC (identificável por nomes de pares com "-OTC", comportamento algorítmico contínuo ou padrões característicos das corretoras) e aplique as estratégias corretas:
                1. MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência, LTA/LTB, confluências micro com RSI 14 (exaustão em 70/30) e validação pelo volume implícito dos candles.
                2. MERCADO OTC (ALGORÍTMICO): Descarte regras de notícias e foque no comportamento computacional das corretoras. Priorize algoritmos de fluxo contínuo (sequências de velas de força), preenchimento milimétrico de pavios anteriores (vácuo de liquidez), exaustão por contagem de velas e armadilhas de falsos rompimentos em zonas saturadas.
                
                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                Analise o desequilíbrio, a movimentação do preço e o fluxo de ordens (Order Flow) de forma 100% implícita e exclusiva na anatomia visual das velas, SEM depender de indicadores de volume na tela:
                - VOLUME POR CORPO E MOVIMENTAÇÃO: Avalie o volume financeiro real injetado pelo tamanho e expansão do corpo dos candles. Velas expressivas confirmam volume institucional empurrando o mercado.
                - DEFESA E ABSORÇÃO POR PAVIOS: Avalie o volume de agressão contrária pelo tamanho dos pavios. Pavios longos em zonas críticas indicam rejeição em massa, absorção de ordens e virada iminente no fluxo.
                
                [TIME_RULES] Leia o relógio atual no print. Projete o momento do clique de entrada de forma cirúrgica para acontecer entre 2 a 5 velas (minutos) depois do print. A expiração DEVE ser de 1 minuto para fechar exatamente no final da mesma vela de entrada (WIN no candle indicado).
                """

                # --- MÓDULOS DE AUTOANÁLISE E APRENDIZADO DE FILTROS ---
                if modo == "ANALISE":
                    prompt_especifico = """
                    Retorne estritamente neste formato markdown limpo:
                    🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 96% - EXTREMA CONFLUÊNCIA]
                    ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                    ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Fechamento na mesma vela)
                    🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                    🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                    🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                    🧠 ESTRATÉGIA CORRETA APLICADA: [Ex: ALGORITMO DE FLUXO OTC ou REVERSÃO EM SUPORTE TRADICIONAL]
                    
                    🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION & FILTROS DE SEGURANÇA):
                    - Leitura de Falsos Rompimentos/Pullbacks: [Explique por que o cenário atual é seguro e não se trata de uma armadilha ou falso movimento]
                    - Filtragem de Ruído e Volume por Corpo: [Análise da clareza e direção real do fluxo das velas]
                    - Absorção e Pressão por Pavios: [O que a pressão dos pavios revelou sobre o volume oculto de defesa]
                    - Filtro de Segurança RSI: [Status técnico da linha do RSI para confluência]
                    Seja frio, direto e puramente matemático.
                    """
                
                elif modo == "WIN":
                    prompt_especifico = """
                    [ALGORITHM AUTO-LEARNING: WIN REFINEMENT]
                    O usuário acabou de obter uma VITÓRIA (WIN). Faça uma autoanálise profunda do print enviado para mapear o padrão ideal e blindar as próximas ordens, elevando a assertividade geral para o topo absoluto.
                    
                    1. IDENTIFICAÇÃO DO MERCADO: Avalie se esse padrão vitorioso aconteceu em Mercado Aberto ou algoritmo de OTC.
                    2. ENGENHARIA REVERSA DO SUCESSO: Desmonte a anatomia dos candles vitoriosos. Qual foi o gatilho perfeito? (Ex: Padrão de exaustão macro, vácuo de liquidez preenchido milimetricamente em OTC, ou impulsão com corpo Marubozu institucional limpo em Mercado Aberto?).
                    3. REFINAMENTO DE ASSERTIVIDADE: Defina um superfiltro de mercado baseado nessa vitória. O que o usuário deve procurar no gráfico para garantir que a próxima operação repita essa exata taxa de acerto?
                    
                    Retorne estritamente neste formato markdown limpo:
                    🌐 AMBIENTE DE MERCADO IDENTIFICADO: [MERCADO ABERTO ou MERCADO OTC]
                    🧠 MAPEAMENTO DO GATILHO VITORIOSO: [Descreva detalhadamente a confluência mecânica da vela que causou o WIN]
                    📊 COMPORTAMENTO ESPECÍFICO DO FLUXO: [Análise do tamanho dos corpos e posicionamento dos pavios que confirmaram o volume comprador/vendedor correto]
                    📈 PROJETO DE REFINAMENTO (COMO SUBIR A ASSERTIVIDADE): [Crie uma diretriz estrita para que, nas próximas análises nesse mesmo tipo de mercado, o usuário filtre ainda mais e só entre se o cenário tiver exatamente esse nível de perfeição estrutural]"""
