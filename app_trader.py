import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E INTERFACE VISUAL DO STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Price Action Puro), Tendência, RSI Calibrado, Volume Implícito e Expiração Dinâmica Avançada.")

# ==============================================================================
# 2. CONFIGURAÇÃO DA CHAVE DA IA NA BARRA LATERAL
# ==============================================================================
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a biblioteca oficial do Google GenAI
    client = genai.Client(api_key=API_KEY)

    # ==============================================================================
    # 3. CAMPO DE UPLOAD E VISUALIZAÇÃO DO PRINT DO GRÁFICO
    # ==============================================================================
    uploaded_file = st.file_uploader(
        "Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # ==============================================================================
        # 4. DISPARO E PROCESSAMENTO DA ANÁLISE MULTIMODAL
        # ==============================================================================
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # PROMPT UNIFICADO E CALIBRADO: PRICE ACTION + RSI FLEXÍVEL
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade de 80% a 95% usando Price Action Puro com confluência de indicadores.

                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor técnico, mas mantenha a flexibilidade para ler exaustões rápidas de mercado. Se houver ruído lateral confuso, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite operações baseadas em Price Action que apresentem gatilhos claros de retração, reversão por exaustão ou fluxo de força institucional.

                [FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
                1. ISOLAMENTO DE LINHAS VERTICAIS/GRADE: Linhas verticais vermelhas, brancas ou cinzas contínuas que cruzam o gráfico de cima a baixo são APENAS indicadores de tempo da plataforma ou cursores do mouse. Você está PROIBIDO de interpretar linhas de grade ou cursores como corpos de candles ou fluxo de preço.
                2. ANCORAGEM DA VELA ATIVA: Foque exclusivamente na extremidade DIREITA do gráfico principal. Sua tomada de decisão baseia-se unicamente no comportamento de Price Action das últimas 2 velas da ponta direita.
                3. REGRA DO RSI (14) CALIBRADO E FLEXÍVEL: Localize o indicador RSI (14) na parte inferior e olhe unicamente para o pixel final da linha roxa da ponta direita. 
                   - O RSI agora atua como ACELERADOR DE ASSERTIVIDADE (confluência). 
                   - Se a ponta do RSI estiver em sobrecompra (>65) ou sobrevenda (<35), a assertividade da operação é impulsionada.
                   - Se o RSI estiver em zona neutra (perto de 50), você NÃO deve abortar a operação se o Price Action das velas (esticada, exaustão ou pavio) indicar reversão perfeita em suporte/resistência.

                [DIRETRIZ DE OPERAÇÃO: PRICE ACTION INSTITUCIONAL COM CLIQUE ÚNICO]

                1. OPERACIONAL DE REVERSÃO EM REGIÃO (RETRAÇÃO, TAXA DE DEFESA E EXAUSTÃO):
                   - GATILHO COMPRA: O preço deve apresentar uma esticada exaustiva de baixa (velas vermelhas expressivas seguidas por perda visível de tamanho de corpo) tocando um suporte micro (fundo recente de até 2 horas atrás) OU deixando um pavio de rejeição inferior nítido (maior que 35% do tamanho total da vela).
                   - GATILHO VENDA: O preço deve apresentar uma esticada exaustiva de alta (velas verdes expressivas seguidas por perda visível de tamanho de corpo) tocando uma resistência micro (topo recente de até 2 horas atrás) OU deixando um pavio de rejeição superior nítido (maior que 35% do tamanho total da vela).
                   - REGRA DE EXPIRAÇÃO DINÂMICA PARA REVERSÃO: Defina o tempo de expiração com base na velocidade do movimento das velas anteriores:
                     * Use 2 Minutos se o preço atingiu a zona com velas pequenas ou médias e corpos visivelmente decrescentes (exaustão gradual lenta).
                     * Use 3 Minutos se o preço atingiu a zona com uma sequência rápida de 3 a 5 velas muito longas e expressivas (esticada rápida de alta/baixa). O minuto extra é obrigatório para mitigar a última correção e absorção do momentum institucional.

                2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO:
                   - VALIDAÇÃO DO FLUXO: Só opere fluxo se a última vela romper uma zona consolidada recente com mais de 50% de corpo cheio (Marubozu), sem deixar pavios contra o movimento atual. O tempo de expiração será de exatamente 1 minuto para fechamento na mesma vela de entrada.

                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas, sem expressão ou com pavios longos de rejeição na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva, demonstrando volume institucional real.
                2. FILTRO DE RUÍDO LATERAL (DENTE DE SERRA): Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro do mercado.

                [AUTOMATIC_MARKET_ADAPTATION]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC (identificável por nomes de pares com "-OTC", comportamento algorítmico contínuo ou padrões característicos das corretoras) e aplique as estratégias corretas:
                - MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência, LTA/LTB macro e confluências micro com o RSI.
                - MERCADO OTC (ALGORÍTMICO): Foque no comportamento computacional das corretoras. Priorize algoritmos de fluxo contínuo (sequências de velas de força), preenchimento milimétrico de pavios anteriores (vácuo de liquidez) e exaustão por contagem de velas.

                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                1. VOLUME IMPLÍCITO POR CORPO: Avalie o volume através do tamanho do corpo real da vela em relação às últimas 5 velas. Corpos progressivamente maiores indicam injeção de volume institucional.
                2. LEITURA DE EXAUSTÃO: Se o corpo diminuir drasticamente ao tocar uma região de suporte ou resistência, interprete como exaustão de fluxo e perda de pressão institucional, validando a reversão.

                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado com margem de segurança]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU Dinâmico (2 ou 3 Minutos) se Reversão conforme a anatomia das velas anteriores]
                📈 DIREÇÃO DA ENTRADA: [COMPRA / CALL ou VENDA / PUT ou ABORTAR OPERAÇÃO]
                🧠 JUSTIFICATIVA TÉCNICA E CONFLUÊNCIAS: [Explique de forma curta e cirúrgica os motivos baseados nos filtros acima]
                """
                
                try:
                    # Executa a chamada com o modelo atualizado Gemini 3.6-Flash
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Concluída com Gemini 3.6!")
                    st.markdown(response.text)
                except Exception as e:
                    if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                        st.error("⚠️ Limite diário de requisições da sua API Key foi atingido (Cota Gratuita).")
                        st.info("💡 **Dica:** Ative o faturamento 'Pay-as-you-go' no Google AI Studio para liberar o poder total do Gemini 3.6 de forma ilimitada.")
                    else:
                        st.error(f"Erro ao processar a análise com o Gemini: {e}")
else:
    st.info("Por favor, insira sua Gemini API Key na barra lateral para começar.")
