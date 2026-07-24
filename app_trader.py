import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# PROMPT MASTER DEFENSIVO ULTRA-CALIBRADO (ANTI-ILUSÃO E VOLUME ACUMULADO)
# ==============================================================================
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade de 80% a 95% usando Price Action Puro com confluência de indicadores.

[RIGOROUS_FILTERING_PROTOCOL]
Opere com rigor técnico extremo. Se houver ruído lateral confuso, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite operações baseadas em Price Action que apresentem gatilhos claros de retração, reversão por exaustão ou fluxo de força institucional.

[FILTRO DE SEQUÊNCIA DE CORES E VOLUME ACUMULADO - RIGOR MÁXIMO]
Antes de emitir qualquer sinal, avalie o volume visual acumulado dos últimos 5 minutos na ponta direita:
1. BLOQUEIO DE COMPRA POR MACRO-FLUXO DE QUEDA: Se o preço veio derretendo em uma sequência forte de velas vermelhas e longas, você está TERMINANTEMENTE PROIBIDO de mandar COMPRA/CALL baseado apenas em pequenas velas verdes milimétricas ou Dojis que aparecem na ponta final. Velas pequenas não anulam o momentum vendedor institucional. Só compre se houver um engolfo verde real (uma vela verde visivelmente maior que o corpo da última vermelha). Caso contrário, siga o fluxo dominante de queda com VENDA/PUT ou classifique como [ABORTAR OPERAÇÃO].
2. BLOQUEIO DE VENDA POR MACRO-FLUXO DE ALTA: Se o preço veio subindo em uma sequência forte de velas verdes longas, você está TERMINANTEMENTE PROIBIDO de mandar VENDA/PUT baseado apenas em pequenas velas vermelhas ou Dojis na ponta. Só venda se houver um engolfo vermelho real.

[FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
1. ISOLAMENTO DE LINHAS VERTICAIS/GRADE: Linhas verticais e horizontais vermelhas, brancas ou cinzas contínuas que cruzam o gráfico de fundo são APENAS indicadores ou grades da plataforma. Você está PROIBIDO de interpretar essas linhas como pavios de candles.
2. TRAVA VISUAL ANTI-ILUSÃO DE PAVIO: Olhe fixamente para as últimas 2 velas da ponta direita. Se o corpo delas for sólido, grande e quadrado na base (terminando sem uma linha preta fina e nítida espetada para fora), classifique como CORPO CHEIO/MARUBOZU. Você está PROIBIDO de inventar pavios onde a grade do gráfico cria linhas contínuas.
3. REGRA DO RSI (14) CALIBRADO E FLEXÍVEL: Localize o indicador RSI (14) na parte inferior e olhe unicamente para o pixel final da linha roxa da ponta direita. O RSI atua como ACELERADOR DE ASSERTIVIDADE (confluência). Se a ponta do RSI estiver em sobrecompra (>65) ou sobrevenda (<35), a assertividade é impulsionada. Se estiver neutro, NÃO aborte a operação se o Price Action for perfeito.

[REGRA MASTER: CRITÉRIO DE PROJEÇÃO DE TEMPO HÍBRIDO]
Identifique o horário atual pelo relógio da plataforma no print (Ex: XX:38:20). Avalie a velocidade e a anatomia da esticada do preço na ponta direita para decidir entre dois formatos de clique único:

- FORMATO A: PRÓXIMA VELA IMEDIATA (Sem pular vela -> Ex: XX:39:00)
  Use este formato se o preço atingiu a taxa através de um PICO RÁPIDO E ISOLADO com velas muito longas E o RSI já estiver nos níveis extremos (>=70 ou <=30). Em picos rápidos, a entrada ocorre no primeiro impacto.
  
- FORMATO B: VELA FUTURA + 1 (Com folga de tempo -> Ex: XX:40:00)
  Use este formato se o preço estiver se movimentando de forma constante com velas médias acumuladas, indicando que o movimento precisa de mais 1 vela de respiro para atingir a exaustão total antes de reverter com segurança.

[DIRETRIZ DE OPERAÇÃO: PRICE ACTION INSTITUCIONAL COM CLIQUE ÚNICO]

1. OPERACIONAL DE REVERSÃO EM REGIÃO (RETRAÇÃO, TAXA DE DEFESA E EXAUSTÃO COMPLETA):
   - TRAVA ANTI-MARUBOZU: Você está TERMINANTEMENTE PROIBIDO de dar sinal de reversão se a última vela fechar cheia (sem pavio de prevenção na zona, ou com pavio menor que 15% do corpo). Se as últimas velas vermelhas/verdes forem sólidas e quadradas na ponta, aborte a reversão imediatamente por risco de rompimento.
   - PROTOCOLO DE RETRAÇÃO (PICO DE PAVIO): Só autorize reversão se houver uma linha preta fina (pavio real) maior que 35% do tamanho total do candle isolando a taxa.
   - REGRA DE EXPIRAÇÃO REVERSÃO: Para reversão, você está PROIBIDO de usar 1 minuto. Use obrigatoriamente 2 ou 3 minutos conforme a exaustão.

2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO:
   - OPERACIONAL DE FLUXO MOMENTÂNEO: Se o preço estiver distante das regiões de reversão macro ou se as últimas velas da ponta direita forem corpos cheios (Marubozu) rasgando os suportes/resistências sem pavio de rejeição, você está PROIBIDO de contra-atacar a tendência. Siga a favor da continuidade do movimento atual (ou fluxo de cores). Para este cenário de fluxo, mantenha a expiração padrão de 1 minuto para fechar exatamente na vela seguinte.

[ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas ou sem expressão.
2. FILTRO DE RUÍDO LATERAL (DENTE DE SERRA): Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde), aborte.

[AUTOMATIC_MARKET_ADAPTATION]
- MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência.
- MERCADO OTC (ALGORÍTMICO): Foque no comportamento algorítmico. Se o OTC engatar uma sequência de velas cheias da mesma cor sem pavio, não tente reverter. Pegue o fluxo de 1 minuto ou aborte por segurança.

[ORDER_FLOW_&_PURE_CANDLE_VOLUME]
1. LEITURA DE EXAUSTÃO: Se o corpo diminuir drasticamente ao tocar uma região, valide a reversão. Se continuar grande e cheio, é fluxo/rompimento.

Retorne estritamente neste formato markdown limpo:
🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado aplicando a lógica híbrida do critério de projeção de tempo]
⏳ TEMPO DE EXPIRAÇÃO: [Indique o tempo exato a ser selecionado na plataforma: 1 Minuto se for estratégia de fluxo OU 2/3 Minutos se for estratégia de reversão]
📈 DIREÇÃO DA ENTRADA: [COMPRA / CALL ou VENDA / PUT ou ABORTAR OPERAÇÃO]
🧠 JUSTIFICATIVA TÉCNICA E CONFLUÊNCIAS: [Explique de forma curta e cirúrgica os motivos baseados nos filtros acima, citando se escolheu a Próxima Vela ou Vela Futura + 1, e justificando a leitura baseando-se estritamente nas regras de volume acumulado, engolfo ou fluxo e na interpretação dos pavios/corpos]
"""

# ==============================================================================
# FUNÇÃO ISOLADA PARA PROCESSAMENTO DA IA
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
# CONFIGURAÇÃO DA INTERFACE VISUAL DO STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Price Action Puro), Tendência, RSI Calibrado e Tempo de Reação Híbrido Avançado.")

# Configuração da Barra Lateral
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    client = genai.Client(api_key=API_KEY)
    
    uploaded_file = st.file_uploader(
        "Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                executar_analise_ia(client, image, PROMPT_TRADER)
else:
    st.info("Por favor, insira sua Gemini API Key na barra lateral para começar.")
