import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# PROMPT MASTER DEFENSIVO ULTRA-CALIBRADO (VERSÃO ANTI-ILUSÃO & FLUXO OTC)
# ==============================================================================
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade de 80% a 95% usando Price Action Puro com confluência de indicadores.

[RIGOROUS_FILTERING_PROTOCOL]
Opere com rigor técnico extremo. Se houver ruído lateral confuso ou indecisão, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite operações baseadas em Price Action que apresentem gatilhos claros de fluxo de força institucional ou reversões incontestáveis.

[FILTRO CRÍTICO DE BLOQUEIO E LEITURA DE MOMENTUM - PROIBIÇÃO DE COMPRA CONTRA DERRETIMENTO]
1. BLOQUEIO DE COMPRA POR MACRO-FLUXO DE QUEDA (MUITO IMPORTANTE): Se o preço apresentar uma tendência de queda prolongada e direcional (sequência majoritária de velas vermelhas longas nos últimos minutos), você está TERMINANTEMENTE PROIBIDO de projetar COMPRA/CALL baseado em pequenas velas verdes milimétricas, dojis ou pequenos respiros na ponta final. Pequenas velas verdes no final de uma queda macro NÃO são sinais de reversão; são apenas pausas antes do rompimento continuar. Só compre se houver um ENGOLFO VERDE REAL E MASSIVO (uma vela verde cujo corpo englobe e supere com folga todo o corpo da vela vermelha anterior). Se não houver esse engolfo gigante, siga estritamente o fluxo dominante de queda com VENDA/PUT para 1 minuto (próxima vela), pois o preço continuará rompendo.
2. BLOQUEIO DE VENDA POR MACRO-FLUXO DE ALTA: Se o preço veio subindo forte com velas verdes longas, você está TERMINANTEMENTE PROIBIDO de mandar VENDA/PUT baseado apenas em pequenas velas vermelhas na ponta. Só venda se houver um engolfo vermelho massivo.

[FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO - ANTI-LINHA DE TIMING]
1. ISOLAMENTO DA LINHA VERTICAL DO TIMER: Note que a plataforma plota uma linha vertical vermelha espessa (linha do tempo de compra/expiração) exatamente em cima ou colada na última vela da direita. Você está PROIBIDO de confundir essa linha vertical ou as grades cinzas do fundo com pavios superiores ou inferiores de candles. Olhe apenas para os contornos pretos originais do candle.
2. TRAVA VISUAL ANTI-ILUSÃO DE PAVIO: Olhe fixamente para as últimas 2 velas da ponta direita. Se o corpo terminar quadrado na base ou no topo sem uma linha preta fina, nítida e isolada espetada para fora, classifique como CORPO CHEIO/MARUBOZU. Se uma vela vermelha fechar cheia perto de uma suposta zona de suporte, isso não é retração, é FORÇA DE ROMPIMENTO.
3. REGRA DO RSI (14) EM SUPORTES ROMPIDOS: O RSI abaixo de 35 ou acima de 65 sozinho NÃO reverte preço em tendências fortes ou mercado OTC. Se o RSI estiver na sobrevenda (<35) mas o gráfico mostrar velas vermelhas dominantes empurrando o preço para baixo, o preço vai continuar rompendo e arrastando o RSI. Não use o RSI para justificar compras contra fluxos de queda agressivos.

[REGRA MASTER: CRITÉRIO DE PROJEÇÃO DE TEMPO HÍBRIDO]
Identifique o horário atual pelo relógio no canto inferior direito ou na linha do preço (Ex: 22:38:20). Projete a entrada para o fechamento da vela atual, iniciando no próximo minuto exato (Ex: 22:39:00).

- FORMATO A: FLUXO E CONTINUIDADE (1 MINUTO)
  Use este formato se as últimas velas na ponta direita demonstrarem rompimento de níveis anteriores, corpos cheios e ausência de pavios de rejeição reais na direção contrária. A entrada visa acompanhar a força institucional para a vela seguinte fechar na mesma cor.
  
- FORMATO B: VELA FUTURA + 1 (2 A 3 MINUTOS)
  Use este formato APENAS se houver um sinal claro, nítido e indiscutível de reversão (ex: engolfo real ou pavio de rejeição preto que seja maior que 35% do candle total). Se houver dúvida sobre a existência do pavio, use o FORMATO A (Fluxo) ou ABORTE.

[DIRETRIZ DE OPERAÇÃO: PRICE ACTION INSTITUCIONAL COM CLIQUE ÚNICO]

1. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO:
   - Se o preço estiver em um movimento direcional forte e as últimas velas vermelhas/verdes rasgarem suportes ou resistências anteriores, feche os olhos para reversões. Siga o fluxo da tendência atual. Mantenha a expiração estrita de 1 minuto para pegar o encerramento da vela imediatamente seguinte.

2. OPERACIONAL DE REVERSÃO EM REGIÃO (RETRAÇÃO OR EXAUSTÃO):
   - TRAVA ANTI-MARUBOZU: Proibido reversão se a última vela fechar cheia (corpo sólido).
   - Se as velas vermelhas continuarem rompendo as marcas horizontais cinzas pontilhadas sem demonstrar um candle de força compradora expressivo (engolfo), mantenha o viés vendedor (VENDA/PUT).

Retorne estritamente neste formato markdown limpo:
🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 92% - FLUXO INSTITUCIONAL DE QUEDA CONTRA PEQUENAS VELAS DE INDECISÃO]
⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado aplicando a lógica híbrida do critério de projeção de tempo]
⏳ TEMPO DE EXPIRAÇÃO: [Indique o tempo exato a ser selecionado na plataforma: 1 Minuto se for estratégia de fluxo OU 2/3 Minutos se for estratégia de reversão]
📈 DIREÇÃO DA ENTRADA: [COMPRA / CALL ou VENDA / PUT ou ABORTAR OPERAÇÃO]
🧠 JUSTIFICATIVA TÉCNICA E CONFLUÊNCIAS: [Explique de forma curta e cirúrgica os motivos baseados nos filtros acima, demonstrando o entendimento do fluxo de queda dominante, a invalidação de falsos pavios gerados pelas linhas da plataforma e o porquê de seguir a tendência de 1 minuto em vez de tentar adivinhar reversões fracas]
"""

# ==============================================================================
# FUNÇÃO ISOLADA PARA PROCESSAMENTO DA IA
# ==============================================================================
def executar_analise_ia(client, image, prompt):
    try:
        # Utiliza o modelo estável multimodal com a nova biblioteca google-genai
        response = client.models.generate_content(
            model='gemini-2.5-flash',
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
st.write("Análise cirúrgica de Velas (Price Action Puro), Tendência, RSI Calibrado e Tempo de Reação Híbrido Avançado.")

# Configuração da Barra Lateral
st.sidebar.header("🔑 Configurações de Acesso")
api_key = st.sidebar.text_input("Insira sua Gemini API Key:", type="password")

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Como usar:")
st.sidebar.write("1. Obtenha sua chave no Google AI Studio.")
st.sidebar.write("2. Tire um print da tela do seu gráfico (IQ Option, Pocket Option, Exnova, etc.).")
st.sidebar.write("3. Certifique-se de que o relógio da plataforma e o RSI apareçam no print.")
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
            with st.spinner("Analisando macro-fluxo, rejeições e tempo de expiração..."):
                # Inicializa o cliente oficial da biblioteca google-genai
                client = genai.Client(api_key=api_key)
                executar_analise_ia(client, image, PROMPT_TRADER)
else:
    st.info("💡 Aguardando o upload do print do gráfico para iniciar o escaneamento institucional.")
