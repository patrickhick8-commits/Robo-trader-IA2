import streamlit as st
from google import genai
from PIL import Image
import datetime

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E INTERFACE
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito, Expiração Dinâmica e Tempo de Reação Técnico.")

# ==============================================================================
# 2. CONFIGURAÇÃO DA CHAVE DA IA E PARÂMETROS NA BARRA LATERAL
# ==============================================================================
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

st.sidebar.markdown("---")
st.sidebar.subheader("⏱️ Configuração de Latência")

# Seleção do tempo de reação estimado do trader/infraestrutura
tempo_reacao_segundos = st.sidebar.slider(
    "Tempo de Reação Estimado (em segundos):",
    min_value=1,
    max_value=10,
    value=3,
    help="Tempo que você leva para ver o sinal, abrir a corretora e clicar (incluindo delay da internet)."
)

if API_KEY:
    try:
        # Inicializa o cliente com a nova biblioteca oficial do Google
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        st.error(f"Erro ao inicializar o cliente Gemini: {e}")
        st.stop()

    # ==============================================================================
    # 3. CAMPO DE UPLOAD E VISUALIZAÇÃO DO PRINT
    # ==============================================================================
    uploaded_file = st.file_uploader(
        "Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # ==============================================================================
        # 4. DISPARO E PROCESSAMENTO DA ANÁLISE
        # ==============================================================================
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            # Captura o horário exato em que o botão foi clicado no servidor
            horario_clique_botao = datetime.datetime.now()
            
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # Injeta as variáveis de tempo reais do sistema diretamente no prompt
                prompt = f"""
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita, garantindo uma assertividade absurda baseada em confluências técnicas avançadas.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Você está terminantemente proibido de passar sinais com confluências fracas. Se houver o menor ruído, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS]
                Monitore rigorosamente a proximidade do preço em relação各自 das zonas de suporte e resistência fortes para aplicar um dos dois setups abaixo:
                
                1. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA: Se o preço estiver distante das regiões de reversão macro e demonstrar força direcional, siga a favor da continuidade do movimento atual (ou fluxo de cores). Para este cenário de fluxo, você está OBRIGADO a manter a expiração padrão de 1 minuto para fechar exatamente no final da mesma vela de M1 de entrada.
                
                2. OPERACIONAL DE REVERSÃO EM REGIÃO (SUPORTE DE FUNDO RECENTE / TAXA DE DEFESA): Se você detectar que o preço atingiu a exaustão visual (corpos decrescentes e esticada de 3 a 5 velas consecutivas) e tocou uma região de suporte ou resistência micro de até 2 horas atrás, ative este modo de contra-ataque. Para este cenário de proteção e reversão, ajuste o tempo de expiração dinamicamente para 3 minutos à frente, projetando o repique e o isolamento seguro da zona de liquidez.
                
                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                Aplique filtros severos para blindar a operação contra armadilhas comuns de mercado:
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas, sem expressão ou com pavios longos de prevenção na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva (Marubozu), demonstrando volume institucional real e intenção de romper a zona.
                2. FILTRO DE FALSO PULLBACK: Bloqueie entradas de pullback se a vela que retorna para testar a região rompida demonstrar força extrema contrária (corpo muito grande). O pullback legítimo deve ser testado por velas de exaustão (corpos decrescentes) e deixar pavio de rejeição exatamente ao tocar a zona rompida.
                3. FILTRO DE RUÍDO: Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro do mercado.
                
                [AUTOMATIC_MARKET_ADAPTATION & CONDITIONAL RSI FILTER]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC (identificável por nomes de pares com "-OTC", comportamento algorítmico contínuo ou padrões característicos das corretoras) e aplique as estratégias corretas, analisando o indicador RSI 14 na parte inferior com as seguintes regras de segurança:
                1. FILTRO DE SEGURANÇA RSI: Utilize o indicador RSI APENAS se ele estiver em zona extrema (tocando ou rompendo os níveis 30 ou 70) E EM CONGRUÊNCIA total com o padrão de exaustão das velas. Se as velas mostrarem força de fluxo contínuo (sequência de velas grandes em OTC), IGNORE o RSI, pois o algoritmo tende a estagnar o indicador nos extremos e continuar o movimento.
                2. MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência, LTA/LTB macro e confluências micro com o RSI.
                3. MERCADO OTC (ALGORÍTMICO): Foque no comportamento computacional das corretoras. Priorize algoritmos de fluxo contínuo (sequências de velas de força), preenchimento milimétrico de pavios anteriores (vácuo de liquidez), exaustão por contagem de velas e armadilhas de falsos rompimentos em zonas saturadas.
                
                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                Analise o desequilíbrio, a movimentação do preço e o fluxo de ordens (Order Flow) de forma 100% implícita e exclusiva na anatomia visual das velas, SEM depender de indicadores de volume na tela:
                - VOLUME POR CORPO E MOVIMENTAÇÃO: Avalie o volume financeiro real injetado pelo tamanho e expansão do corpo dos candles. Velas expressivas confirmam volume institucional empurrando o mercado.
                - DEFESA E ABSORÇÃO POR PAVIOS: Avalie o volume de agressão contrária pelo tamanho dos pavios. Pavios longos in zonas críticas indicam rejeição em massa, absorção de ordens e virada iminente no fluxo.
                
                [TIME_RULES & REACTION DELAY]
                - Horário atual de processamento do servidor: {horario_clique_botao.strftime('%H:%M:%S')}.
                - Tempo de reação/latência humana e de rede configurado pelo trader: {tempo_reacao_segundos} segundos.
                
                Instrução de Tempo: Cruze visualmente o relógio interno exibido na imagem (print) com o horário do servidor fornecido. Você deve projetar o 'HORÁRIO DO CLIQUE (ENTRADA)' para a próxima virada de vela viável (próximo minuto ou bloco técnico), somando obrigatoriamente os {tempo_reacao_segundos} segundos de margem de reação para que o trader consiga executar a ordem sem pegar um 'delay de taxa' ruim na IQ Option/Quotex.
                
                Ajuste a expiração estritamente com base na estratégia adotada: 1 minuto se for FLUXO MOMENTÂNEO (fechamento na mesma vela), ou 3 minutos se for REVERSÃO EM REGIÃO / TAXA DE DEFESA.
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:SS exato considerando o tempo de reação calculado]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 3 Minutos se Reversão em Região/Taxa de Defesa]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado no horário de entrada + tempo de expiração definido]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]
                """
                
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    st.success("Análise Concluída com Margem de Reação!")
                    st.markdown(response.text)
                    
                except Exception as e:
