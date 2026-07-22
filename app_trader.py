import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Expiração Dinâmica Avançada.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio - Não precisa de indicador de volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # Prompt institucional completo com filtros anti-ruído, anti-falso rompimento e fluxo de ordens
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita, garantindo uma assertividade absurdda baseada em confluências técnicas avançadas.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Você está terminantemente proibido de passar sinais com confluências fracas. Se houver o menor ruído, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [DIRETRIZ DE SEGURANÇA MÁXIMA: REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]
                Monitore rigorosamente a proximidade do preço em relação各自 zonas de suporte e resistência fortes:
                1. OPERACIONAL DE REVERSÃO EM REGIÃO: Se você detectar que o preço JÁ ESTIVER NA REGIÃO de suporte/resistência ou extremidade saturada, ative este modo de reversão contra a tendência. Para este cenário, você está OBRIGADO A AJUSTAR O TEMPO DE EXPIRAÇÃO para uma faixa de 2 a 10 minutos à frente, projetando a exaustão e o recuo seguro do preço dentro da zona defensiva.
                2. OPERACIONAL DE FLUXO MOMENTÂNEO: Se o preço estiver distante das regiões de reversão, você está PROIBIDO de contra-atacar a tendência. Siga a favor da continuidade do movimento atual (ou fluxo de cores). Para este cenário de fluxo, mantenha a expiração padrão de 1 minuto para fechar exatamente no final da mesma vela de entrada.
                
                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                Aplique filtros severos para blindar a operação contra armadilhas comuns de mercado:
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas, sem expressão ou com pavios longos de rejeição na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva (Marubozu), demonstrando volume institucional real e intenção de romper a zona.
                2. FILTRO DE FALSO PULLBACK: Bloqueie entradas de pullback se a vela que retorna para testar a região rompida demonstrar força extrema contrária (corpo muito grande). O pullback legítimo deve ser testado por velas de exaustão (corpos decrescentes) e deixar pavio de rejeição exatamente ao tocar a zona rompida.
                3. FILTRO DE RUÍDO: Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro do mercado.
                
                [AUTOMATIC_MARKET_ADAPTATION]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC (identificável por nomes de pares com "-OTC", comportamento algorítmico contínuo ou padrões característicos das corretoras) e aplique as estratégias corretas:
                1. MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência, LTA/LTB, confluências micro com RSI 14 (exaustão em 70/30) e validação pelo volume implícito dos candles.
                2. MERCADO OTC (ALGORÍTMICO): Descarte regras de notícias e foque no comportamento computacional das corretoras. Priorize algoritmos de fluxo contínuo (sequências de velas de força), preenchimento milimétrico de pavios anteriores (vácuo de liquidez), exaustão por contagem de velas e armadilhas de falsos rompimentos in zonas saturadas.
                
                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                Analise o desequilíbrio, a movimentação do preço e o fluxo de ordens (Order Flow) de forma 100% implícita e exclusiva na anatomia visual das velas, SEM depender de indicadores de volume na tela:
                - VOLUME POR CORPO E MOVIMENTAÇÃO: Avalie o volume financeiro real injetado pelo tamanho e expansão do corpo dos candles. Velas expressivas confirmam volume institucional empurrando o mercado.
                - DEFESA E ABSORÇÃO POR PAVIOS: Avalie o volume de agressão contrária pelo tamanho dos pavios. Pavios longos em zonas críticas indicam rejeição em massa, absorção de ordens e virada iminente no fluxo.
                
                [TIME_RULES] Leia o relógio atual no print. Projete o momento do clique de entrada de forma cirúrgica para acontecer entre 2 a 5 velas (minutos) depois do print. 
                Ajuste a expiração estritamente com base na estratégia adotada: 2 a 10 minutos se for REVERSÃO EM REGIÃO (para dar tempo de o preço corrigir), ou 1 minuto se for FLUXO MOMENTÂNEO (para fechar na mesma vela).
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 96% - EXTREMA CONFLUÊNCIA]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo OU 2 a 10 Minutos calculados se Reversão em Região]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado no horário de entrada + tempo de expiração definido]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [Ex: OPERACIONAL DE REVERSÃO EM REGIÃO com tempo estendido ou FLUXO MOMENTÂNEO EM TENDÊNCIA]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION & FILTROS DE SEGURANÇA):
                - Lógica de Expiração Adotada: [Justifique matematicamente a escolha do tempo de expiração com base na distância da região]
                - Leitura de Falsos Rompimentos/Pullbacks: [Explique por que o cenário atual é seguro e não se trata de uma armadilha ou falso movimento]
                - Filtragem de Ruído e Volume por Corpo: [Análise da clareza e direção real do fluxo das velas]
                - Absorção e Pressão por Pavios: [O que a pressão dos pavios revelou sobre o volume oculto de defesa]
                - Filtro de Segurança RSI: [Status técnico da linha do RSI para confluência]
                Seja frio, direto e puramente matemático.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar a imagem: {e}")
