import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1 Pro", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Institucional Avançada")
st.write("Análise cirúrgica via Gemini 2.5 Pro: Velas, Tendência, RSI, Médias e Filtro de Mercado Dinâmico (M1).")

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
            with st.spinner("Gemini 2.5 Pro aplicando raciocínio profundo e escaneando o mercado..."):
                
                # Prompt institucional calibrado estritamente para o Gemini 2.5 Pro com inteligência OTC vs Aberto
                prompt = """
                [SYSTEM_ROLE] Aja como um robô de trading institucional de altíssima performance, especialista em Price Action avançado, leitura algorítmica e análise de Opções Binárias (M1). Projete a entrada entre 2 a 5 minutos no futuro com expiração para a mesma vela.
                
                [DETECÇÃO AUTOMÁTICA DE MERCADO (MERCADO ABERTO VS OTC)]
                Antes de buscar gatilhos, analise minuciosamente os textos, títulos do par e a estrutura visual dos candles para definir as diretrizes operacionais:
                1. DETECÇÃO POR TEXTO: Varra o gráfico em busca do sufixo "OTC" no par de moedas ou identificadores textuais da corretora.
                2. DETECÇÃO POR COMPORTAMENTO: Se notar padrões hiperdirecionais artificiais, sequências de 7 a 10 velas da mesma cor sem correções saudáveis ou ausência de gaps de exaustão típicos do mercado tradicional, classifique como ALGORÍTMO OTC. Caso contrário, classifique como MERCADO ABERTO REAL.
                3. MODULAÇÃO DE ENTRADAS CONFORME O MERCADO:
                   - Padrão MERCADO ABERTO: Ative os filtros de proteção baseados em zonas fortes de Suporte e Resistência humanos, rejeições expressivas de pavios nas extremidades e a exaustão matemática do RSI 14 nos níveis 70 e 30. Busque reversões cirúrgicas.
                   - Padrão OTC: Ignore Suportes e Resistências convencionais (padrão algorítmico tende a romper e esticar movimentos). Priorize 100% o FLUXO DE VELA, padrões de continuidade (como Engolfos e Marubozus) colados na tendência imediatista ditada pela EMA 9, operando a favor do momento.

                [INDICADORES INTERNOS DA IA (PROCESSAMENTO VISUAL COGNITIVO)]
                Mesmo que o gráfico enviado esteja limpo, use sua visão computacional avançada de alta precisão para simular internamente no preço o comportamento dos seguintes indicadores:
                1. Média Móvel Exponencial de 9 Períodos (EMA 9): Rastreie a tendência imediata do preço. Avalie se as últimas velas fecham acima ou abaixo desta projeção de curto prazo.
                2. Média Móvel Exponencial de 50 Períodos (EMA 50): Projete esta linha para determinar o suporte/resistência institucional e a tendência macro. Identifique cruzamentos com a EMA 9 ou distanciamentos críticos (retração iminente).
                3. Índice de Força Relativa Padrão (RSI 14): Calcule o momento do mercado. Identifique exaustão caso a força atual equivalha a zonas de sobrecompra (níveis acima de 70) para operações de venda, ou sobrevenda (níveis abaixo de 30) para operações de compra.

                [CANDLE_VOLUME_ANALYSIS] Analise minuciosamente o VOLUME DO MERCADO através de duas vias simultâneas:
                1. VOLUME POR ANATOMIA: Meça o volume implícito e a velocidade do mercado pelo tamanho do corpo dos candles (corpos expandidos = volume e força real; corpos espremidos/Dojis = falta de volume e indecisão).
                2. REJEIÇÃO E FLUXO: Avalie o volume de absorção/rejeição pelo tamanho dos pavios (pavios longos indicam entrada massiva de volume contrário defendendo a zona) e compare a proporção corpo-pavio das últimas 5 velas.
                
                [OPERATIONAL_PARAMETERS] Combine rigorosamente as regras do ambiente detectado (Aberto ou OTC) com a tendência do gráfico. Calcule a assertividade (Sinal válido estritamente de 80% a 99%, abaixo disso retorne ABORTAR OPERAÇÃO - ALTO RISCO).
                
                [TIME_RULES] Clique obrigatoriamente projetado entre 2 a 5 minutos à frente do relógio do print. Expiração rígida para 1 minuto (fechamento na mesma vela do clique).
                
                Retorne estritamente neste formato markdown:
                🌐 AMBIENTE DE MERCADO: [MERCADO ABERTO REAL ou ALGORÍTMO OTC DETECTADO]
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 92%]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]
                🧠 ESTRATÉGIA ADAPTADA: [Ex: FLUXO DE VELA ALGORÍTMICA OTC ou REVERSÃO EM SUPORTE INSTITUCIONAL]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]
                
                🔍 DETALHAMENTO ANATÔMICO (O QUE A IA VIU):
                - Projeção Interna EMA 9/50: [Descreva a posição estimada do preço em relação à linha imaginária das médias]
                - Projeção Interna RSI 14: [Aponte a estimativa de momento do oscilador e exaustão]
                - Volume por Movimentação/Corpo: [Análise do volume implícito pelo tamanho das velas]
                - Rejeição por Pavios: [O que a pressão dos pavios revelou sobre o volume de defesa]
                - Filtro Antiloss Ativado: [Justifique por que escolheu o padrão de operação baseado em OTC ou Aberto]
                Seja extremamente frio, preciso e direto.
                """
                
                try:
                    # Executa a geração de conteúdo focada exclusivamente no modelo Gemini 2.5 Pro
                    response = client.models.generate_content(
                        model='gemini-2.5-pro',
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
                    # Exibe o erro na tela caso a conta gratuita atinja os limites ou instabilidades do servidor Pro
                    st.error(f"Erro no processamento visual da IA: {e}")
                    if "503" in str(e) or "UNAVAILABLE" in str(e):
                        st.info("💡 Os servidores gratuitos do modelo Pro costumam ficar cheios devido à alta demanda. Aguarde alguns segundos e tente novamente.")
                    elif "429" in str(e):
                        st.info("💡 Você atingiu a cota limite de requisições da sua chave. Considere adicionar uma nova linha com uma API Key reserva.")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")
