import streamlit as st
from google import genai
from PIL import Image
import time

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E INTERFACE
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Expiração Dinâmica Avançada com Tempo de Reação.")

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
                
                # Prompt reajustado para evitar falsos travamentos de risco da IA
                prompt = """
                [SYSTEM_ROLE] Você é um especialista em análise gráfica institucional de alta performance. Sua missão é escanear o print do gráfico M1 fornecido e identificar se há uma confluência técnica aceitável para sugerir uma operação ou se o cenário é de indefinição.

                [ANÁLISE DE CONFLUENCIAS]
                Avalie o cenário ponderando os seguintes fatores visuais:
                1. ANATOMIA DOS CANDLES: Identifique a cor, tamanho do corpo e presença de pavios (rejeição) nas últimas 2 a 3 velas da ponta direita.
                2. SUPORTES E RESISTÊNCIAS: Identifique se o preço atual está colado em topos ou fundos anteriores proeminentes no histórico visível.
                3. TENDÊNCIA E RSI: Avalie a direção geral do preço e a posição da ponta final da linha do RSI (se visível).

                [DIRETRIZES OPERACIONAIS DE SUPORTE]
                - REVERSÃO: Sugira se o preço demonstrar rejeição evidente (pavio) ao tocar zonas de suporte/resistência com RSI em regiões extremas.
                - FLUXO: Sugira se houver o rompimento de uma consolidação por uma vela de corpo expressivo, com espaço livre à frente (longe de topos/fundos).
                - FILTRO DE SEGURANÇA: Classifique como [ABORTAR OPERAÇÃO] apenas se o gráfico estiver totalmente lateralizado em caixas muito estreitas (Doji sequenciais) ou sem nenhuma clareza de direção na ponta direita.

                [REGRAS DE TEMPO (M1)]
                1. Localize ou estime o HORÁRIO ATUAL do gráfico (geralmente no eixo horizontal ou nos cantos da tela).
                2. Projete o HORÁRIO DO CLIQUE (ENTRADA) para 1 ou 2 minutos à frente desse horário identificado.
                3. Se a estratégia sugerida for Fluxo, a expiração é de 1 Minuto. Se for Reversão/Retração, a expiração é de 2 Minutos.

                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 87% - Confluência de Retração / Ou 0% se Abortado]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato calculado para o próximo candle ou "N/A" se Abortado]
                ⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto ou 2 Minutos ou "N/A" se Abortado]
                🏁 HORÁRIO DE FECHAMENTO: [Horário de Entrada + Tempo de Expiração ou "N/A" se Abortado]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [A estratégia detectada ou "N/A"]

                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL:
                - Justificativa Técnica: [Explique brevemente o comportamento das últimas velas e o motivo da decisão tomada]
                """
                
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar a análise: {e}")
else:
    st.info("Por favor, insira sua Gemini API Key na barra lateral para começar.")
