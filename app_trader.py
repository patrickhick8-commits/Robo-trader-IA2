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
                
                # Prompt institucional calibrado com regras matemáticas rígidas de tempo em M1
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade absurda.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído ou ambiguidade técnica na ponta do gráfico, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
                1. ISOLAMENTO DE LINHAS VERTICAIS: Linhas verticais contínuas cruzando o gráfico são marcações técnicas de tempo ou cursores da corretora. PROIBIDO interpretá-las como corpos de candles.
                2. ANCORAGEM DA VELA ATIVA: Foque exclusivamente na extremidade DIREITA do gráfico. A tomada de decisão baseia-se unicamente nas últimas 2 velas da ponta direita.
                3. REGRA DE LEITURA ESTRITA DO RSI: Olhe UNICAMENTE para o pixel final (a ponta do lado direito) da linha roxa do RSI (14). Ignore montanhas ou picos passados que ficaram para trás no meio do gráfico.
                
                [DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS SINCRO-CALIBRADOS]
                
                1. OPERACIONAL DE REVERSÃO EM REGIÃO (TAXA DE DEFESA) - 2 MINUTOS:
                   - GATILHO COMPRA: Se o preço caiu forte e a PONTA FINAL do RSI (14) estiver tocando ou abaixo de 30.
                   - GATILHO VENDA: Se o preço subiu forte e a PONTA FINAL do RSI (14) estiver tocando ou acima de 70.
                   - Se o preço tocar em suporte/resistência e o RSI confirmar exaustão extrema na ponta direita, execute a contra-ataque. O tempo de expiração será estritamente de 2 minutos à frente do horário de entrada.
                
                2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO (BLINDADO):
                   - Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de COMPRA se a ponta do RSI estiver acima de 60 ou perto de 70 (ZONA DE SATURAÇÃO). 
                   - Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de VENDA se a ponta do RSI estiver abaixo de 40 ou perto de 30 (ZONA DE ABSORÇÃO).
                   - VALIDAÇÃO DO FLUXO: Só opere fluxo se a ponta do RSI estiver em zona totalmente neutra e livre (entre 40 e 60) E a última vela romper uma zona consolidada com mais de 50% de corpo cheio (Marubozu), sem pavios contra o movimento. O tempo de expiração será de exatamente 1 minuto para fechamento na próxima vela cheia.
                
                [ANTI_NOISE_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas ou com pavios longos de rejeição.
                2. GRÁFICO EM DENTE DE SERRA: Aborte por ruído se houver alternância constante de cores nas últimas 5 velas da direita, A MENOS que o RSI esteja cravado nos extremos (<30 ou >70) autorizando uma reversão institucional de 2 minutos.
                
                [TIME_RULES_M1_STRICT]
                1. Localize o HORÁRIO ATUAL do sistema no canto inferior direito do print (ex: 21:37:18).
                2. O HORÁRIO DO CLIQUE (ENTRADA) deve ser projetado para o próximo minuto redondo limpo (virada de vela), considerando o tempo de reação (ex: se o print é de 21:37:18, a entrada projetada será 21:38:00 ou 21:39:00).
                3. REGRA MATEMÁTICA DE FECHAMENTO: 
                   - Se a estratégia for FLUXO MOMENTÂNEO (1 Minuto), o Horário de Fechamento deve ser exatamente o Horário do Clique + 1 minuto (ex: Entrada 21:39:00 -> Fechamento 21:40:00).
                   - Se a estratégia for REVERSÃO EM REGIÃO (2 Minutos), o Horário de Fechamento deve ser exatamente o Horário do Clique + 2 minutos (ex: Entrada 21:38:00 -> Fechamento 21:40:00).
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado na virada de vela futura]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 2 Minutos se Reversão em Região/Taxa de Defesa]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado na regra: Horário de Entrada + Tempo de Expiração]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION EM GRÁFICO LIMPO):
                - Lógica de Expiração Adotada: [Justifique a escolha do tempo baseado na regra de M1 informada: 1 minuto para fluxo ou 2 minutos para mitigação em reversões]
                - Leitura de Falsos Rompimentos/Pullbacks/RSI: [Explique detalhadamente o comportamento da última vela da extrema direita e a posição exata da PONTA FINAL da linha do RSI provando por que operou ou abortou]
                """
                
                               try:
                    # Linha atualizada para utilizar a versão 3.6 Flash
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=[image, prompt]
                    )
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar análise: {e}")
