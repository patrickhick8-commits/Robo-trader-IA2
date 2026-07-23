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
                
                # Prompt recalibrado com checagem estrita da ponta final do RSI
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar a oportunidade perfeita na última vela da direita, garantindo uma assertividade absurda baseada em confluências técnicas avançadas.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído ou se a leitura técnica for ambígua na ponta do gráfico, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
                1. ISOLAMENTO DE LINHAS VERTICAIS: Linhas verticais contínuas (vermelhas, brancas ou cinzas) que cruzam o gráfico de cima a baixo são ferramentas técnicas de tempo ou cursores da corretora. É TERMINANTEMENTE PROIBIDO interpretá-las como corpos de candles.
                2. ANCORAGEM DA VELA ATIVA: Foque exclusivamente no bloco de candles na extremidade DIREITA do gráfico. A tomada de decisão baseia-se unicamente no comportamento das últimas 2 velas da ponta direita.
                3. REGRA DE LEITURA ESTRITA DO RSI: Ao analisar o RSI (14) na parte inferior, você deve olhar UNICAMENTE para o pixel final (a ponta do lado direito) da linha roxa. Ignore picos, montanhas ou vales que aconteceram no meio ou atrás do gráfico do RSI. Se a ponta final da linha roxa estiver na zona cinza central (entre 40 e 60), considere o RSI como NEUTRO, ignore o histórico passado e ABORTE qualquer sinal de reversão.
                
                [AUTORIDADE MÁXIMA DO OPERACIONAL DE REVERSÃO E EXAUSTÃO]
                Monitore o indicador RSI (14) na parte inferior baseado estritamente na ponta direita final:
                
                - SE A PONTA DIREITA FINAL DO RSI (14) ESTIVER NOS EXTREMOS (Rompendo ou tocando visivelmente a linha de Sobrevenda de 30 ou Sobrecompra de 70): A exaustão matemática ganha prioridade absoluta. Se o preço tocou no suporte/resistência e a ponta atual do RSI provar o extremo (<30 ou >70), emita o sinal de contra-ataque. Para este cenário, use estritamente 2 minutos de expiração.
                - SE A PONTA DO RSI ESTIVER EM ZONA NEUTRA (Entre 40 e 60): Você está PROIBIDO de fazer reversão. Aborte imediatamente por falta de exaustão real no segundo atual.
                
                [OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA]
                - Se o RSI estiver neutro mas o preço romper uma zona consolidada com vela cheia (Marubozu com mais de 50% de corpo rompido) e sem pavios de rejeição contrários, siga o fluxo de cor. Use estritamente 1 minuto de expiração para fechar na mesma vela.
                
                [TIME_RULES] Leia o relógio atual no print no canto inferior direito. Projete o momento do clique de entrada para 1 a 2 minutos à frente do horário atual do sistema.
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 2 Minutos se Reversão em Região/Taxa de Defesa]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado no horário de entrada + tempo de expiração definido]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION EM GRÁFICO LIMPO):
                - Lógica de Expiração Adotada: [Justifique a escolha do tempo de expiração: 1 minuto para fluxo ou 2 minutos para mitigação em reversões]
                - Leitura de Falsos Rompimentos/Pullbacks/RSI: [Explique detalhadamente o comportamento da última vela da extrema direita e a posição exata da PONTA FINAL da linha do RSI provando por que operou ou abortou]
                """
                
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar análise: {e}")
else:
    st.info("Insira sua Gemini API Key na barra lateral para começar.")
