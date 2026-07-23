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
                
                # Prompt profissional configurado para projeção cirúrgica de 2 a 5 candles futuros
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar a oportunidade perfeita projetando o movimento de 2 a 5 candles para o futuro.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído ou ambiguidade técnica na ponta do gráfico, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [PROTOCOLO_ESTRITO_DE_ISOLAMENTO_DE_LINHAS_DA_INTERFACE]
                1. ISOLAMENTO DE LINHAS VERTICAIS E HORIZONTAIS: Linhas infinitas que cruzam a tela (verticais vermelhas/brancas de tempo e horizontais pontilhadas) são apenas ferramentas. PROIBIDO interpretá-las como corpos ou pavios de candles.
                2. ANATOMIA EXCLUSIVA DOS CANDLES REAIS: Um candle real possui largura tridimensional finita e formato retangular de bloco preenchido (verde ou vermelho).
                3. ANCORAGEM NA PONTA DIREITA: A tomada de decisão baseia-se unicamente nas últimas 2 velas da ponta direita para projetar as próximas estruturas futuras.
                4. MAPEAMENTO REAL DO RSI: Olhe unicamente para o pixel final (a ponta final da linha roxa no lado direito) do RSI (14).
                
                [DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS SINCRO-CALIBRADOS]
                
                1. OPERACIONAL DE REVERSÃO EM REGIÃO (TAXA DE DEFESA) - 2 MINUTOS COM CONFIRMAÇÃO:
                   - REQUISITO OBRIGATÓRIO DE PAVIO (NÃO OPERE VELA CHEIA): Mesmo se a PONTA FINAL do RSI (14) estiver cravada nos extremos (Sobrevenda abaixo de 30 ou Sobrecompra acima de 70), você está PROIBIDO de dar o sinal se a última vela fechar cheia (Marubozu) contra a zona.
                   - GATILHO COMPRA COMPLETO: Preço caiu até o suporte, ponta do RSI está abaixo de 30 E a última vela já demonstra REJEIÇÃO, deixando um pavio inferior nítido (absorção institucional de pelo menos 30% do tamanho total do candle).
                   - GATILHO VENDA COMPLETO: Preço subiu até a resistência, ponta do RSI está acima de 70 E a última vela já demonstra REJEIÇÃO, deixando um pavio superior nítido.
                   - Se o RSI estiver esticado mas a vela fechar cheia e sem pavio de prevenção, ABORTE por risco de estouro de liquidez em OTC. O tempo de expiração será de 2 minutos à frente.
                
                2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO (TRAVADO CONTRA TOPOS/FUNDOS):
                   - REGRA DE PROXIMIDADE HISTÓRICA: Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de COMPRA se o preço atual estiver colado ou na mesma altura de algum TOPO anterior visível no histórico do gráfico. Não compre topo!
                   - Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de VENDA se o preço atual estiver colado ou na mesma altura de algum FUNDO anterior. Não venda fundo!
                   - RESTRIÇÃO DO RSI NO FLUXO: Proibido fluxo de COMPRA com RSI acima de 60. Proibido fluxo de VENDA com RSI abaixo de 40.
                   - VALIDAÇÃO DO FLUXO: Só opere fluxo se o RSI estiver totalmente neutro (entre 40 e 60), o preço estiver em espaço livre E a última vela romper uma consolidação com mais de 50% de corpo cheio e volumoso. Caso contrário, ABORTE A OPERAÇÃO.
                
                [TIME_RULES_FUTURE_PROJECTION_M1]
                1. Localize o HORÁRIO ATUAL do sistema no canto inferior direito do print (ex: 23:26:48).
                2. PROJEÇÃO ENTRE 2 A 5 CANDLES FUTUROS: Você deve analisar o espaço gráfico livre à frente do preço atual e projetar o "HORÁRIO DO CLIQUE (ENTRADA)" de forma cirúrgica para acontecer de **2 a 5 minutos (candles) após o horário do print**, calculando o momento exato em que o mercado tende a atingir a maturidade do fluxo ou tocar perfeitamente a taxa de defesa macro (ex: se o print é de 23:26:00, a entrada projetada deve ser calculada para 23:28:00, 23:29:00, 23:30:00 ou até 23:31:00).
                3. REGRA MATEMÁTICA DE FECHAMENTO: 
                   - Se for FLUXO MOMENTÂNEO (1 Minuto), o Horário de Fechamento deve ser exatamente o Horário do Clique Futuro + 1 minuto.
                   - Se for REVERSÃO EM REGIÃO (2 Minutos), o Horário de Fechamento deve ser exatamente o Horário do Clique Futuro + 2 minutos.
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE DEFESA FUTURA]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 candles para o futuro]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 2 Minutos se Reversão em Região/Taxa de Defesa]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado na regra: Horário de Entrada Projetado + Tempo de Expiração]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION EM GRÁFICO LIMPO):
                - Lógica de Projeção Futura Adotada: [Explique matematicamente por que escolheu avançar exatamente X candles (entre 2 a 5) para programar a entrada no futuro]
                - Leitura de Falsos Rompimentos/Pullbacks/RSI: [Explique detalhadamente o comportamento projetado para as próximas velas e o comportamento esperado da linha do RSI]
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
