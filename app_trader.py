import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# PROMPT MASTER DEFENSIVO RECALIBRADO - FLUXO PREVENTIVO & REVERSÃO EXTREMA
# ==============================================================================
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar a oportunidade perfeita utilizando análise preditiva avançada de Candlesticks (Price Action Puro), Taxas Divididas e RSI Calibrado.

[RIGOROUS_FILTERING_PROTOCOL]
Opere com rigor técnico extremo. Se houver ruído lateral confuso ou indefinição, retorne [ABORTAR OPERAÇÃO - ALTO RISCO].

[PROTOCOLO DE CONTROLE DE DELAY VISUAL E ENTRADA PROTEGIDA]
Você deve considerar que o usuário leva cerca de 15 a 20 segundos para enviar o print e processar a resposta. 
1. TRAVA DE TAXA RUIM (NÃO PEGUE VELA EM ANDAMENTO): Se a sua estratégia indicar FLUXO (Continuidade), e a vela atual já tiver se movimentado demais ou esticado na direção do movimento, você está PROIBIDO de mandar entrar na vela atual. Projete a entrada estritamente para a ABERTURA DA PRÓXIMA VELA REDONDA FUTURA.
2. CÁLCULO DE HORÁRIO PREDITIVO: Localize o relógio da plataforma (Ex: 23:58:05). Se o segundo estiver acima de :00, arredonde o "Horário do Clique" para o próximo minuto exato cheio da plataforma (Ex: 23:59:00 ou 00:00:00) para dar tempo hábil ao trader de programar a operação sem pressa.

[DIRETRIZ OPERACIONAL - FORMATO A: FLUXO E CONTINUIDADE (1 MINUTO)]
- REQUISITOS: Rompimento claro de suportes/resistências anteriores com velas de corpo cheio e expansivo.
- REGRA DE PROTEÇÃO: Monitore o momentum. Se o mercado engatar sequências fortes da mesma cor em OTC, siga a tendência para a próxima vela redonda isolada (1 minuto de expiração).
- BLOQUEIOS CORES: Proibido comprar em derretimento macro sem engolfo real. Proibido vender em alta macro sem engolfo real.

[DIRETRIZ OPERACIONAL - FORMATO B: REVERSÃO LEGÍTIMA EM TAXA DIVIDIDA (2 A 3 MINUTOS)]
- REQUISITOS (MODELO VITORIOSO DO BITCOIN CASH): Aplique este formato sempre que identificar o esgotamento total de um movimento.
- PADRÃO DE EXAUSTÃO OCULTA: As últimas 3 velas da tendência anterior precisam demonstrar uma perda drástica e progressiva de volume (corpos diminuindo consecutivamente: Vela Grande -> Vela Média -> Vela Pequena/Doji).
- GATILHO DE TAXA DIVIDIDA MILIMÉTRICA: A última vela de exaustão deve travar ou deixar pavio exatamente em cima de uma linha horizontal de simetria histórica (onde o preço mudou de cor simetricamente no passado). Isso caracteriza absorção institucional e formação de bloco de ordens contrário.
- CONFLUÊNCIA EXTRA DO RSI (14): A linha roxa deve estar em sobrevenda extrema (<30) para COMPRA/CALL ou sobrecompra extrema (>70) para VENDA/PUT.
- EXPIRAÇÃO: Use obrigatoriamente 2 ou 3 minutos para permitir que a nova micro-tendência se desenvolva com folga acima/abaixo da taxa defendida.

[FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO - ANTI-LINHA DE TIMING]
1. ISOLAMENTO DA LINHA VERTICAL DO TIMER: A linha vertical vermelha espessa pertencente ao timer da plataforma NÃO é pavio de candle. Ignore-a e analise apenas o contorno preto original das velas.
2. MARUBOZU DE ROMPIMENTO VS VELA DE EXAUSTÃO: Se o candle for grande, sólido e romper uma linha cinza sem diminuir os anteriores, é fluxo. Se os candles anteriores vierem encolhendo e pararem na linha, é exaustão em taxa dividida.

Retorne estritamente neste formato markdown limpo:
🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - REVERSÃO POR EXAUSTÃO INSTITUCIONAL EM TAXA DIVIDIDA]
⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado para o próximo minuto cheio, garantindo tempo de reação]
⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto para Estratégia de Fluxo OU 2/3 Minutos para Estratégia de Reversão de Exaustão]
📈 DIREÇÃO DA ENTRADA: [COMPRA / CALL ou VENDA / PUT ou ABORTAR OPERAÇÃO]
🧠 JUSTIFICATIVA TÉCNICA E CONFLUÊNCIAS: [Explique detalhadamente e de forma cirúrgica a escolha com base nas regras acima. Se for Reversão, cite o encolhimento das últimas 3 velas, o travamento na simetria da Taxa Dividida e o esgotamento no RSI. Se for Fluxo, certifique que a entrada foi projetada para a abertura da próxima vela para evitar taxas ruins e subidas excessivas]
"""

# ==============================================================================
# FUNÇÃO ISOLADA PARA PROCESSAMENTO DA IA (MODELO ATUALIZADO)
# ==============================================================================
def executar_analise_ia(client, image, prompt):
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=[image, prompt]
        )
        st.success("Análise Concluída com Sucesso!")
        st.markdown(response.text)
    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
            st.error("⚠️ Limite diário de requisições da sua API Key foi atingido (Cota Gratuita).")
            st.info("💡 **Dica:** Ative o faturamento 'Pay-as-you-go' no Google AI Studio para liberar o poder total da API de forma ilimitada.")
        else:
            st.error(f"Erro ao processar a análise com o Gemini: {e}")

# ==============================================================================
# CONFIGURAÇÃO DA INTERFACE VISUAL DO STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise preditiva de Velas, Fluxo Direcional, Taxas Divididas e Tempo de Reação Blindado contra Delay.")

# Configuração da Barra Lateral
st.sidebar.header("🔑 Configurações de Acesso")
api_key = st.sidebar.text_input("Insira sua Gemini API Key:", type="password")

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Como usar:")
st.sidebar.write("1. Obtenha sua chave no Google AI Studio.")
st.sidebar.write("2. Tire um print da tela do seu gráfico.")
st.sidebar.write("3. Certifique-se de que o relógio da plataforma apareça no print.")
st.sidebar.write("4. Faça o upload da imagem e clique em 'Iniciar Análise Cirúrgica'.")

# Área Principal de Upload
uploaded_file = st.file_uploader("Arraste ou selecione o print do seu gráfico (PNG, JPG, JPEG):", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico Carregado Pronto para Análise", use_container_width=True)
    
    # Botão de Ação
    if st.button("🚀 Iniciar Análise Cirúrgica", type="primary"):
        if not api_key:
            st.warning("⚠️ Por favor, insira sua Gemini API Key na barra lateral antes de continuar.")
        else:
            with st.spinner("Escaneando Taxas Divididas, exaustão de velas e projetando tempo futuro..."):
                client = genai.Client(api_key=api_key)
                executar_analise_ia(client, image, PROMPT_TRADER)
else:
    st.info("💡 Aguardando o upload do print do gráfico para iniciar o escaneamento preditivo institucional.")
