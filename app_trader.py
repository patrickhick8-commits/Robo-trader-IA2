import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# 1. FUNÇÃO ISOLADA PARA PROCESSAMENTO DA IA (CORRIGIDA COM O SEU PROMPT FORMATADO)
# ==============================================================================
def executar_analise_ia(client, image, prompt):
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=[image, prompt]
        )
        st.success("Análise Concluída com Gemini 3.6!")
        st.markdown(response.text)
    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
            st.error("⚠️ Limite diário de requisições da sua API Key foi atingido (Cota Gratuita).")
            st.info("💡 **Dica:** Ative o faturamento 'Pay-as-you-go' no Google AI Studio para liberar o poder total do Gemini 3.6 de forma ilimitada.")
        else:
            st.error(f"Erro ao processar a análise com o Gemini: {e}")

# ==============================================================================
# 2. CONFIGURAÇÃO DA PÁGINA E INTERFACE VISUAL DO STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Price Action Puro), Tendência, RSI Calibrado e Tempo de Reação Híbrido Avançado.")

# ==============================================================================
# 3. CONFIGURAÇÃO DA CHAVE DA IA NA BARRA LATERAL
# ==============================================================================
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    client = genai.Client(api_key=API_KEY)

    # ==============================================================================
    # 4. CAMPO DE UPLOAD E VISUALIZAÇÃO DO PRINT DO GRÁFICO
    # ==============================================================================
    uploaded_file = st.file_uploader(
        "Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # ==============================================================================
        # 5. DISPARO E PROCESSAMENTO DA ANÁLISE MULTIMODAL (PROMPT INTEGRADO COM O FORMATO)
        # ==============================================================================
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # PROMPT MASTER INTEGRADO COM AS DIRETRIZES DE FORMATO DE RETORNO
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade de 80% a 95% usando Price Action Puro com confluência de indicadores.

                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor técnico extremo. Se houver ruído lateral confuso, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite operações baseadas em Price Action que apresentem gatilhos claros de retração, reversão por exaustão ou fluxo de força institucional.

                [FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
                1. ISOLAMENTO DE LINHAS VERTICAIS/GRADE: Linhas verticais vermelhas, brancas ou cinzas contínuas que cruzam o gráfico de cima a baixo são APENAS indicadores de tempo da plataforma ou cursores do mouse. Você está PROIBIDO de interpretar linhas de grade ou cursores como corpos de candles ou fluxo de preço.
                2. ANCORAGEM DA VELA ATIVA: Foque exclusivamente na extremidade DIREITA do gráfico principal. Sua tomada de decisão baseia-se unicamente no comportamento de Price Action das últimas 2 velas da ponta direita.
                3. REGRA DO RSI (14) CALIBRADO E FLEXÍVEL: Localize o indicador RSI (14) na parte inferior e olhe unicamente para o pixel final da linha roxa da ponta direita. O RSI atua como ACELERADOR DE ASSERTIVIDADE (confluência). Se a ponta do RSI estiver em sobrecompra (>65) ou sobrevenda (<35), a assertividade é impulsionada. Se estiver neutro, NÃO aborte a operação se o Price Action for perfeito.

                [REGRA MASTER: CRITÉRIO DE PROJEÇÃO DE TEMPO HÍBRIDO]
                Identifique o horário atual pelo relógio da plataforma no print (Ex: XX:03:29). Avalie a velocidade e a anatomia da esticada do preço na ponta direita para decidir entre dois formatos de clique único:
                
                - FORMATO A: PRÓXIMA VELA IMEDIATA (Sem pular vela -> Ex: XX:04:00)
                  Use este formato se o preço atingiu a taxa/resistência através de um PICO RÁPIDO E ISOLADO com velas muito longas (esticada agressiva) E o RSI já estiver rompendo ou colado nos níveis extremos (>=70 ou <=30). Em picos rápidos, a reversão/retração ocorre imediatamente no primeiro impacto. Não pule a vela para não perder a oportunidade.
                
                - FORMATO B: VELA FUTURA + 1 (Com folga de tempo -> Ex: XX:05:00)
                  Use este formato se o preço estiver subindo ou descendo de forma lenta, constante, com uma sequência de velas médias acumuladas. Isso significa que o movimento ainda tem fôlego e precisa de mais 1 vela de respiro para atingir a exaustão total e saturação antes de reverter com segurança.

                [DIRETRIZ DE OPERAÇÃO: PRICE ACTION INSTITUCIONAL COM CLIQUE ÚNICO]

                1. OPERACIONAL DE REVERSÃO EM REGIÃO (RETRAÇÃO, TAXA DE DEFESA E EXAUSTÃO COMPLETA):
                   - TRAVA ANTI-MARUBOZU: Você está TERMINANTEMENTE PROIBIDO de dar sinal de reversão se a última vela fechar cheia (sem pavio de prevenção na zona, ou com pavio menor que 15% do corpo). Bloqueie se o pavio for irrelevante ou um mero ruído.
                   - PROTOCOLO DE RETRAÇÃO (PICO DE PAVIO): Priorize entradas se a vela anterior demonstrar forte rejeição em suporte ou resistência micro recente de até 2 hours atrás. O pavio ideal de segurança deve ser maior que 35% do tamanho total do candle para autorizar o clique único.
                   - GATILHO COMPRA: O preço deve apresentar uma esticada exaustiva de baixa (velas vermelhas expressivas seguidas por perda visível de tamanho de corpo) tocando um suporte micro OU deixando um pavio de prevenção inferior nítido (maior que 35% do tamanho total da vela).
                   - GATILHO VENDA: O preço deve apresentar uma esticada exaustiva de alta (velas verdes expressivas seguidas por perda visível de tamanho de corpo) tocando uma resistência micro OU deixando um pavio de rejeição superior nítido (maior que 35% do tamanho total da vela).
                   - REGRA DE EXPIRAÇÃO DINÂMICA PARA REVERSÃO (ALINHADA À CORRETORA): 
                     * Use 2 Minutos na plataforma se o preço atingiu a zona com velas pequenas ou médias e corpos decrescentes (exaustão lenta). Isso cobrirá a vela atual projetada + 2 velas cheias à frente.
                     * Use 3 Minutos na plataforma se o preço atingiu a zona com uma sequência rápida de 3 a 5 velas muito longas e expressivas (esticada rápida). O minuto extra na plataforma garante margem de segurança para absorver o momentum.

                2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO:
                   - VALIDAÇÃO DO FLUXO: Só opere fluxo se a última vela romper uma zona consolidada recente com mais de 50% do seu corpo cheio (Marubozu), sem deixar pavios contra o movimento. O tempo de expiração será de 1 minuto na plataforma (fechamento na próxima vela cheia).

                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas expressivas sem volume ou sem confirmação na zona micro.

                [FORMATO_DE_RETORNO_OBRIGATORIO]
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado com margem de segurança]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 3 Minutos se Reversão / Taxa de Defesa]
                📈 DIREÇÃO DA ENTRADA: [COMPRA / CALL ou VENDA / PUT ou ABORTAR OPERAÇÃO]
                🧠 JUSTIFICATIVA TÉCNICA E CONFLUÊNCIAS: [Explique de forma curta e cirúrgica os motivos baseados nos filtros acima]
                """
                
                # Executa a chamada chamando a função centralizada
                executar_analise_ia(client, image, prompt)
else:
    st.sidebar.warning("Por favor, insira sua Gemini API Key para liberar o aplicativo.")
