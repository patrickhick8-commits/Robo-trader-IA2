import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# PROMPT MASTER DEFENSIVO (TRAVA MATEMÁTICA DE SEQUÊNCIA DE CORES)
# ==============================================================================
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade de 80% a 95% usando Price Action Puro com confluência de indicadores.

[RIGOROUS_FILTERING_PROTOCOL]
Opere com rigor técnico extremo. Se houver ruído lateral confuso, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO].

[FILTRO DE SEQUÊNCIA DE CORES OBRIGATÓRIO - ANTI-INVERSÃO]
Antes de emitir qualquer sinal, faça uma contagem matemática das cores dos últimos 3 candles na ponta direita do gráfico:
1. TRAVA ANTI-COMPRA PRECOCE: Se a sequência das últimas velas for majoritariamente VERMELHA (força de queda) e o preço estiver caindo em direção à linha vermelha do tempo, você está PROIBIDO de projetar COMPRA/CALL. Não invente pivô de alta em estruturas que estão derretendo. O fluxo correto neste cenário é estritamente VENDA/PUT ou ABORTAR.
2. TRAVA ANTI-VENDA PRECOCE: Se a sequência das últimas velas for majoritariamente VERDE (força de alta), você está PROIBIDO de projetar VENDA/PUT tentando adivinhar topo precoce. O fluxo correto neste cenário é estritamente COMPRA/CALL ou ABORTAR.

[FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
1. ISOLAMENTO DE LINHAS VERTICAIS/GRADE: Linhas de grade cinzas no fundo são apenas a grade da plataforma. Não as confunda com pavios.
2. TRAVA VISUAL ANTI-ILUSÃO DE PAVIO: Se o corpo das velas vermelhas for sólido e terminar reto na base sem uma linha preta fina e nítida espetada para fora, classifique como CORPO CHEIO/MARUBOZU. 

[REGRA MASTER: CRITÉRIO DE PROJEÇÃO DE TEMPO HÍBRIDO]
Identifique o horário atual pelo relógio da plataforma no print (Ex: XX:38:20).
- FORMATO A: PRÓXIMA VELA IMEDIATA (Sem pular vela -> Ex: XX:39:00). Use se o movimento for de tiro rápido e forte fluxo de mesma cor.
- FORMATO B: VELA FUTURA + 1 (Com folga de tempo -> Ex: XX:40:00). Use apenas se o preço estiver em exaustão lenta com corpos decrescentes.

[DIRETRIZ DE OPERAÇÃO: PRICE ACTION INSTITUCIONAL COM CLIQUE ÚNICO]

1. OPERACIONAL DE REVERSÃO EM REGIÃO (RETRAÇÃO, TAXA DE DEFESA E EXAUSTÃO COMPLETA):
   - TRAVA ANTI-MARUBOZU: ProIBIDO dar sinal de reversão se a última vela fechar cheia. 
   - REGRA DE EXPIRAÇÃO REVERSÃO: Para reversão, você está PROIBIDO de usar 1 minuto. Use obrigatoriamente 2 ou 3 minutos.

2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO:
   - OPERACIONAL DE FLUXO MOMENTÂNEO: Se as últimas velas da ponta direita forem corpos cheios (Marubozu) de mesma cor sequencial rasgando os níveis, você está PROIBIDO de contra-atacar a tendência. Siga a favor da continuidade do fluxo de cores dominante (se velas vermelhas -> VENDA; se velas verdes -> COMPRA). Mantenha a expiração padrão de 1 minuto para fechar na vela seguinte.

Retorne estritamente neste formato markdown limpo:
🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado aplicando a lógica híbrida e os filtros de sequência de cores]
⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se for fluxo de tendência OU 2/3 Minutos se for reversão técnica]
📈 DIREÇÃO DA ENTRADA: [COMPRA / CALL ou VENDA / PUT ou ABORTAR OPERAÇÃO]
🧠 JUSTIFICATIVA TÉCNICA E CONFLUÊNCIAS: [Explique de forma curta e cirúrgica qual foi a contagem de cores das últimas velas que definiu a direção do fluxo ou se causou o aborto da operação]
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
