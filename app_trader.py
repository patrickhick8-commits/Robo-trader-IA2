import streamlit as st
from google import genai
from PIL import Image
import time

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E INTERFACE
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Expiração Dinâmica Avançada com Tempo de Reação.")

# ==============================================================================
# 2. CONFIGURAÇÃO DA CHAVE DA IA NA BARRA LATERAL
# ==============================================================================
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # ==============================================================================
    # 3. CAMPO DE UPLOAD E VISUALIZAÇÃO DO PRINT
    # ==============================================================================
    uploaded_file = st.file_uploader(
        "Arraste o print do gráfico M1 (Recomendado: Zoom aproximado de 30-40 velas, sem indicadores):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # ==============================================================================
        # 4. DISPARO E PROCESSAMENTO DA ANÁLISE
        # ==============================================================================
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # Prompt de Alta Performance recalibrado para equilíbrio entre segurança e agressividade técnica
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita, garantindo uma assertividade absurda baseada em confluências técnicas avançadas.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído sem confluência, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
                1. ISOLAMENTO DE LINHAS VERTICAIS: Linhas verticais vermelhas, brancas ou cinzas contínuas que cruzam o gráfico de cima a baixo são APENAS indicadores de tempo da plataforma ou cursores do mouse. Você está PROIBIDO de interpretar linhas verticais contínuas como corpos de candles ou fluxo de preço.
                2. IDENTIFICAÇÃO DOS CANDLES REAIS: Foque única e exclusivamente nos retângulos preenchidos (verdes e vermelhos) que possuem pavios (linhas finas superiores e inferiores). 
                3. CORRELAÇÃO DO RSI: Ao ler o gráfico do RSI (14) na parte inferior, correlacione o nível da linha roxa exatamente com a posição vertical do candle ativo na extrema DIREITA do gráfico principal acima.
                
                [DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS]
                Monitore rigorosamente a proximidade do preço em relação às zonas de suporte e resistência fortes para aplicar um dos dois setups abaixo:
                
                1. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA: Se o preço estiver distante das regiões de reversão macro e demonstrar força direcional, siga a favor da continuidade do movimento atual. Mantenha a expiração padrão de 1 minuto para fechar exatamente no final da mesma vela de M1 de entrada.
                
                2. OPERACIONAL DE REVERSÃO EM REGIÃO (SUPORTE DE FUNDO RECENTE / TAXA DE DEFESA): Se você detectar que o preço atingiu a exaustão visual (corpos decrescentes ou esticada exaustiva rápida de 2 a 4 velas consecutivas) tocando uma região de suporte ou resistência micro, E o RSI (14) estiver esticado tocando ou rompendo os níveis extremos (Sobrevenda abaixo de 30 ou Sobrecompra acima de 70), ative este modo de contra-ataque imediatamente. Para este cenário de reversão, ajuste o tempo de expiração para 2 minutos à frente.
                
                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas ou com pavios longos de rejeição na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva (Marubozu).
                2. FILTRO DE REVERSÃO CONTRA A TENDÊNCIA MICRO: Você está PROIBIDO de passar sinais de VENDA em estruturas de alta, A MENOS que o RSI (14) esteja explicitamente tocando ou acima do nível de 70/80 (sobrecomprado). Se o RSI estiver esticado no limite, a exaustão matemática invalida a tendência e autoriza o clique. Se o RSI estiver neutro (entre 40 e 60), aborte por falta de exaustão real.
                3. EXCEÇÃO AO FILTRO DE RUÍDO: Alternâncias de cores (verde-vermelho) nas últimas velas indicam ruído lateral, MAS se a vela atual disparar de forma exaustiva tocando uma taxa de defesa com o RSI totalmente sobrecomprado (>70) ou sobrevendido (<30), a reversão por exaustão INSTITUCIONAL prevalece sobre o ruído. Opere a reversão de 2 minutos. Se o RSI não estiver nos extremos, aborte imediatamente.
                
                [AUTOMATIC_MARKET_ADAPTATION]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC e aplique as estratégias corretas de Price Action puro combinado com a exaustão visual do RSI (14).
                
                [TIME_RULES] Leia o relógio atual no print. Projete o momento do clique de entrada de forma cirúrgica para acontecer entre 1 a 3 minutos depois do print (Tempo de Reação). 
                Ajuste a expiração estritamente com base na estratégia adotada: 1 minuto se for FLUXO MOMENTÂNEO, ou 2 minutos se for REVERSÃO EM REGIÃO / TAXA DE DEFESA.
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 2 Minutos se Reversão em Região/Taxa de Defesa]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado no horário de entrada + tempo de expiração definido]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION EM GRÁFICO LIMPO):
                - Lógica de Expiração Adotada: [Justifique matematicamente a escolha do tempo de expiração: 1 minuto para fechamento na mesma vela ou 2 minutos para mitigação e proteção de taxa]
                - Leitura de Falsos Rompimentos/Pullbacks/RSI: [Explique por que o cenário atual é seguro em relação ao RSI e que não se trata de uma armadilha de liquidez varejista.]
                """
                
                try:
                    # Configurado com o modelo solicitado: gemini-3.6-flash
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=[image, prompt]
                    )
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar análise: {e}")
else:
    st.info("Por favor, insira sua Gemini API Key na barra lateral para começar.")

