import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume e Probabilidade em M1.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (inclua Velas, RSI, Volume e Relógio):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume e mercado..."):
                
                # Prompt avançado focado 100% em volume implícito por Price Action e padrões
                prompt = """
                [SYSTEM_ROLE] Aja como robô institucional especialista em Price Action puro, Order Flow e análise de Opções Binárias (M1). Projete a entrada entre 2 a 5 minutos no futuro com expiração para a mesma vela.
                
                [CANDLE_VOLUME_ANALYSIS] Analise minuciosamente o VOLUME IMPLÍCITO do mercado através das confluências visuais de Price Action:
                1. VOLUME POR CORPO E MOVIMENTAÇÃO: Meça o volume injetado pelo tamanho real do corpo dos candles. Velas expressivas (Marubozu) indicam alto volume institucional e direcional contínuo. Velas minúsculas (Dojis ou corpos espremidos) provam falta de volume e desinteresse dos grandes players.
                2. VOLUME POR PAVIOS (REJEIÇÃO): Avalie o volume de absorção e defesa. Pavios longos e expressivos revelam que um volume massivo contrário entrou na extremidade para defender e reverter a zona de preço, capturando liquidez.
                3. PADRÕES DE CANDLES INSTITUCIONAIS: Identifique padrões gráficos que confirmem a injeção desse volume implícito, tais como Engolfos, Martelos, Pin Bars, Harâmis ou Estrelas da Manhã/Noite. Use a confluência desses padrões para validar a força do sinal.
                
                [OPERATIONAL_PARAMETERS] Identifique a Tendência (Alta, Baixa ou Lateral), analise as barras de volume inferiores e o RSI. Calcule a assertividade (Sinal válido estritamente de 80% a 99%, abaixo disso retorne ABORTAR OPERAÇÃO).
                
                [TIME_RULES] Clique obrigatoriamente projetado entre 2 a 5 minutos à frente do relógio do print. Expiração rígida para 1 minuto (fechamento na mesma vela do clique).
                
                Retorne estritamente neste formato markdown:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 87%]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]
                🧠 ESTRATÉGIA: [FLUXO DE VELA ou REVERSÃO DE TENDÊNCIA]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]
                
                🔍 DETALHAMENTO ANATÔMICO (O QUE A IA VIU):
                - Volume Implícito por Movimentação/Corpo: [Descreva o volume implícito medido pela força/tamanho do corpo das velas]
                - Absorção por Pavios: [Descreva a força do volume oposto de defesa identificado nos pavios]
                - Padrões de Candles Detectados: [Mencione os padrões de candlestick que confirmaram a entrada de volume]
                - Indicadores (Volume Barras/RSI): [Situação visual das barras inferiores e do RSI]
                Seja frio, preciso e direto.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Avançada Concluída com Sucesso!")
                    
                    # Sistema de som injetado para alertar a entrada no Desktop
                    st.components.v1.html(
                        '<audio autoplay src="https://google.com"></audio>',
                        height=0
                    )
                    
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")
