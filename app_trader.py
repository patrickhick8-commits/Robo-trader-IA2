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
                
                # Prompt institucional com filtro de bloqueio de fluxo em regiões de topo/fundo
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade absurda.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído ou ambiguidade técnica na ponta do gráfico, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [PROTOCOLO_ESTRITO_DE_ISOLAMENTO_DE_LINHAS_DA_INTERFACE]
                1. ISOLAMENTO DE LINHAS VERTICAIS E HORIZONTAIS: Linhas infinitas que cruzam a tela (verticais vermelhas/brancas de tempo e horizontais pontilhadas da interface) são apenas ferramentas. PROIBIDO interpretá-las como corpos ou pavios de candles.
                2. ANATOMIA EXCLUSIVA DOS CANDLES REAIS: Um candle real possui largura tridimensional finita e formato retangular de bloco preenchido (verde ou vermelho).
                3. ANCORAGEM NA PONTA DIREITA: A tomada de decisão baseia-se unicamente nas últimas 2 velas da ponta direita.
                4. MAPEAMENTO REAL DO RSI: Olhe unicamente para o pixel final (a ponta final da linha roxa no lado direito) do RSI (14).
                
                [DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS SINCRO-CALIBRADOS]
                
                1. OPERACIONAL DE REVERSÃO EM REGIÃO (TAXA DE DEFESA) - 2 MINUTOS:
                   - GATILHO COMPRA: Se o preço caiu forte e a PONTA FINAL do RSI (14) estiver tocando ou abaixo de 30 em zona de suporte.
                   - GATILHO VENDA: Se o preço subiu forte e a PONTA FINAL do RSI (14) estiver tocando ou acima de 70 em zona de resistência.
                   - O tempo de expiração será estritamente de 2 minutos à frente do horário de entrada.
                
                2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO (TRAVADO CONTRA TOPOS/FUNDOS):
                   - REGRA DE PROXIMIDADE HISTÓRICA: Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de COMPRA se o preço atual da ponta direita estiver colado ou na mesma altura de algum TOPO anterior visível no histórico do gráfico, mesmo que o RSI esteja neutro. Não compre topo!
                   - Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de VENDA se o preço atual estiver colado ou na mesma altura de algum FUNDO anterior visível no histórico do gráfico. Não venda fundo!
                   - RESTRIÇÃO DO RSI NO FLUXO: Proibido fluxo de COMPRA com RSI acima de 60. Proibido fluxo de VENDA com RSI abaixo de 40.
                   - VALIDAÇÃO DO FLUXO: Só opere fluxo se o RSI estiver totalmente neutro (entre 40 e 60), o preço estiver em espaço livre (longe de barreiras/topos anteriores) E a última vela romper uma consolidação com mais de 50% de corpo cheio e volumoso (Marubozu real). Caso contrário, ABORTE A OPERAÇÃO por risco de falso rompimento.
                
                [ANTI_NOISE_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas ou com pavios longos de rejeição.
                2. GRÁFICO EM DENTE DE SERRA: Aborte por ruído se houver alternância constante de cores nas últimas 5 velas da direita, A MENOS que o RSI esteja cravado nos extremos (<30 ou >70) autorizando uma reversão institucional de 2 minutos.
                
                [TIME_RULES_M1_STRICT]
                1. Localize o HORÁRIO ATUAL do sistema no canto inferior direito do print (ex: 21:37:18).
                2. O HORÁRIO DO CLIQUE (ENTRADA) deve ser projetado para o próximo minuto redondo limpo (virada de vela).
                3. REGRA MATEMÁTICA DE FECHAMENTO: 
                   - Se a estratégia for FLUXO MOMENTÂNEO (1 Minuto), o Horário de Fechamento deve ser exatamente o Horário do Clique + 1 minuto.
                   - Se a estratégia for REVERSÃO EM REGIÃO (2 Minutos), o Horário de Fechamento deve ser exatamente o Horário do Clique + 2 minutos.
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado na virada de vela futura]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 2 Minutos se Reversão em Região/Taxa de Defesa]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado na regra: Horário de Entrada + Tempo de Expiração]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION EM GRÁFICO LIMPO):
                - Lógica de Expiração Adotada: [Justifique a escolha do tempo baseado na regra de M1 informada]
                - Leitura de Falsos Rompimentos/Pullbacks/RSI: [Explique detalhadamente o comportamento da última vela da extrema direita e a validação de distância em relação a topos/fundos anteriores do histórico]
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
