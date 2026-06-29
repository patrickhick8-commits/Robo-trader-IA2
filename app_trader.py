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
            with st.spinner("IA aplicando raciocínio profundo nos padrões de velas e indicadores..."):
                
                # Prompt avançado completo com foco em volume por Price Action e indicadores internos
                prompt = """
                [SYSTEM_ROLE] Aja como robô institucional especialista em Price Action puro, Order Flow e análise de Opções Binárias (M1). Projete a entrada entre 2 a 5 minutos no futuro com expiração para a mesma vela.
                
                [INDICADORES INTERNOS DA IA (PROCESSAMENTO VISUAL COGNITIVO)]
                Mesmo que o gráfico enviado no print esteja totalmente limpo e sem indicadores na tela, você deve usar sua visão computacional avançada para rastrear o comportamento histórico do preço e projetar internamente os seguintes indicadores:
                1. Média Móvel Exponencial de 9 Períodos (EMA 9): Rastreie a tendência imediata do preço. Avalie se as últimas velas fecham acima ou abaixo desta projeção de curto prazo.
                2. Média Móvel Exponencial de 50 Períodos (EMA 50): Projete esta linha para determinar o suporte/resistência dinâmico institucional e a tendência macro. Identifique cruzamentos com a EMA 9 ou distanciamentos críticos (retração iminente).
                3. Índice de Força Relativa Padrão (RSI 14): Calcule o momento do mercado. Identifique exaustão caso a força atual equivalha a zonas de sobrecompra (níveis acima de 70) para operações de venda, ou sobrevenda (níveis abaixo de 30) para operações de compra.

                [CANDLE_VOLUME_ANALYSIS] Analise minuciosamente o VOLUME DO MERCADO através de duas vias simultâneas:
                1. VOLUME POR ANATOMIA: Meça o volume implícito e a velocidade do mercado pelo tamanho do corpo dos candles (corpos expandidos = volume e força real; corpos espremidos/Dojis = falta de volume e indecisão).
                2. REJEIÇÃO E FLUXO: Avalie o volume de absorção/rejeição pelo tamanho dos pavios (pavios longos indicam entrada massiva de volume contrário defendendo a zona) e compare a proporção corpo-pavio das últimas 5 velas.
                
                [OPERATIONAL_PARAMETERS] Identifique a Tendência (Alta, Baixa ou Lateral), combine o comportamento das barras de volume inferiores com as projeções da EMA 9, EMA 50 e o momentum do RSI 14. Calcule a assertividade (Sinal válido estritamente de 80% a 99%, abaixo disso retorne ABORTAR OPERAÇÃO).
                
                [TIME_RULES] Clique obrigatoriamente projetado entre 2 a 5 minutos à frente do relógio do print. Expiração rígida para 1 minuto (fechamento na mesma vela do clique).
                
                Retorne estritamente neste formato markdown:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 87%]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]
                🧠 ESTRATÉGIA: [CONFLUÊNCIA EMA 9/50 + RSI, FLUXO DE VELA ou REVERSÃO DE TENDÊNCIA]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]
                
                🔍 DETALHAMENTO ANATÔMICO (O QUE A IA VIU):
                - Projeção Interna EMA 9/50: [Descreva a posição estimada do preço em relação à linha imaginária das médias]
                - Projeção Interna RSI 14: [Aponte a estimativa de momento do oscilador e exaustão]
                - Volume por Movimentação/Corpo: [Análise do volume implícito pelo tamanho das velas]
                - Rejeição por Pavios: [O que a pressão dos pavios revelou sobre o volume de defesa]
                - Indicadores (Volume Barras/RSI): [Situação visual das barras e da linha do RSI real se visível]
                Seja frio, preciso e direto.
                """
                
                try:
                    # ATUALIZADO: Executa a chamada utilizando o modelo 'gemini-1.5-pro' para análise profunda
                    response = client.models.generate_content(
                        model='gemini-1.5-pro',
                        contents=[image, prompt]
                    )
                    st.success("Análise Avançada de Alta Precisão Concluída!")
                    
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
