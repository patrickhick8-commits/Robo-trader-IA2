import streamlit as st
from google import genai
from PIL import Image
import time

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E INTERFACE
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, Volume Implícito e Expiração Dinâmica Curta de Alta Assertividade.")

# ==============================================================================
# 2. CONFIGURAÇÃO DA CHAVE DA IA NA BARRA LATERAL
# ==============================================================================
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # ==============================================================================
    # 3. CAMPO DE UPLOAD E VISUALIZAÇÃO DO PRINT
    # ==============================================================================
    uploaded_file = st.file_uploader(
        "Arraste o print do gráfico M1 (Recomendado: Zoom aproximado de 30-40 velas, sem indicadores):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # ==============================================================================
        # 4. DISPARO E PROCESSAMENTO DA ANÁLISE
        # ==============================================================================
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # Prompt Ultra Institucional calibrado com a estratégia de 1 a 3 minutos
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita, garantindo uma assertividade absurda baseada em confluências geométricas puras de Price Action, focando em retrações rápidas de alta performance.

                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Você está terminantemente proibido de passar sinais com confluências fracas. Se houver o menor ruído ou indefinição estrutural, classifique imediatamente como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.

                [ESTRATÉGIA PRINCIPAL VITORIOSA: EXAUSTÃO MICRO E RETRAÇÃO DE TAXA]
                Sua principal e mais assertiva forma de operar (especialmente no mercado de Opções Binárias e OTC) deve ser a captura de exaustão imediata de movimento e defesa de taxa:
                1. IDENTIFICAÇÃO DE EXAUSTÃO: Monitore quando o preço realizar esticadas rápidas de 3 a 5 velas consecutivas da mesma cor, onde as últimas velas comecem a diminuir drasticamente o tamanho do corpo (perda de força/momentum) e a deixar pavios de prevenção proeminentes ao tocar suportes ou resistências recentes deixados em um histórico de até 2 horas atrás.
                2. REGRA ESTRITA DE EXPIRAÇÃO (ANTI-LOSS EM OTC): Para operações de fluxo ou retração micro em mercado algorítmico (OTC), você está TERMINANTEMENTE PROIBIDO de passar tempos longos de expiração, como 5 minutos (alto risco de reversão e virada de ciclo macro na sua cara). Defina o tempo de expiração estritamente entre 1 a 3 minutos para pegar o repique exato e o isolamento da zona de liquidez.

                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                Aplique filtros severos para blindar a operação contra armadilhas comuns de mercado:
                1. FILTRO DE FALSO ROMPIMENTO: Só valide rompimentos se a vela romper com mais de 50% de seu corpo cheio (Marubozu), demonstrando volume institucional real. Velas espremidas, sem expressão ou com pavios longos na direção do rompimento indicam falsos movimentos; contra-ataque imediatamente ativando a operação de retração/reversão curta (1 a 3 min).
                2. FILTRO DE FALSO PULLBACK: Bloqueie entradas se a vela que retorna para testar a região rompida demonstrar força extrema contrária. O pullback legítimo deve ser testado por velas de exaustão (corpos decrescentes) deixando pavio exatamente ao tocar a zona.
                3. FILTRO DE RUÍDO: Se as últimas 5 velas apresentarem alternância constante e caótica de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro.

                [AUTOMATIC_MARKET_ADAPTATION]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC e aplique as leituras corretas, ignorando completamente indicadores osciladores de linha como RSI (foque 100% na ação do preço na tela):
                1. MERCADO ABERTO: Priorize a leitura de zonas legítimas e consolidadas de Suporte/Resistência e LTA/LTB macro.
                2. MERCADO OTC (ALGORÍTMICO): Foque no comportamento computacional das corretoras, priorizando sequências de velas de força, preenchimento milimétrico de pavios anteriores (vácuo de liquidez), exaustão por contagem de velas e falsas esticadas em regiões saturadas.

                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                Analise o desequilíbrio e fluxo de ordens (Order Flow) de forma 100% implícita e exclusiva na anatomia visual das velas, SEM depender de indicadores de volume na tela:
                - VOLUME POR CORPO E MOVIMENTAÇÃO: Avalie a força injetada pela expansão ou encolhimento repentino do tamanho dos candles.
                - DEFESA E ABSORÇÃO POR PAVIOS: Pavios longos em zonas críticas de suporte/resistência recente indicam absorção em massa e virada iminente no fluxo de ordens.

                [TIME_RULES] 
                Leia o relógio atual no print enviado. Projete o momento exato do clique de entrada para acontecer de forma cirúrgica entre 1 a 3 minutos depois do print, casando perfeitamente com a expiração rápida da estratégia adotada.

                Retorne estritamente neste formato markdown limpo, direto e profissional:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE EXAUSTÃO]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 a 3 Minutos calculados com base na exaustão imediata]
                🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado no horário de entrada + tempo de expiração definido]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [EXAUSTÃO MICRO E RETRAÇÃO DE TAXA CURTA]

                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION EM GRÁFICO LIMPO):
                - Lógica de Expiração Adotada: [Justifique matematicamente o uso do tempo curto de 1 a 3 minutos com base na mitigação e quebra do ciclo algorítmico]
                - Leitura de Falsos Rompimentos/Pullbacks: [Explique por que o cenário atual é seguro e não se trata de uma armadilha ou falso movimento]
                - Filtragem de Ruído e Volume por Corpo: [Análise da clareza, direção ou desaceleração real do fluxo das velas]
                - Absorção e Pressão por Pavios: [O que a rejeição dos pavios revelou na zona de suporte ou resistência identificada no histórico recente]
                - Filtro de Segurança e Volume Oculto: [Mapeamento estrutural realizado de forma estritamente implícita com base na geometria pura dos candles e ação do preço]

                Seja frio, direto e puramente matemático.
                """
                
                # Lista de modelos de Fallback para prevenir o erro 503 UNAVAILABLE
                modelos_fallback = ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-1.5-flash']
                response = None
                erro_final = ""

                # Sistema de loop de tentativas (Retry/Fallback)
                for modelo_atual in modelos_fallback:
                    try:
                        response = client.models.generate_content(
                            model=modelo_atual,
                            contents=[image, prompt]
                        )
                        if response and response.text:
                            break # Conseguiu resposta com sucesso, sai do loop.
                    except Exception as e:
                        erro_final = str(e)
                        st.sidebar.warning(f"Modelo {modelo_atual} congestionado. Tentando o próximo...")
                        time.sleep(1)

                # Exibe o resultado se pelo menos um modelo respondeu
                if response and response.text:
                    st.success("Análise Avançada Concluída com Sucesso!")
                    st.markdown(response.text)
                    
                    # Injeta o aviso sonoro curto de relógio digital
                    st.components.v1.html(
                        """
                        <audio autoplay>
                          <source src="https://google.com" type="audio/ogg">
                        </audio>
                        """,
                        height=0
                    )
                else:
                    st.error(f"Todos os servidores da Google IA estão sob alta demanda no momento. Detalhes do erro: {erro_final}")
else:
