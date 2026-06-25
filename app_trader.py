import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Volume Oculto", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Volume por Comportamento das Velas")
st.write("Análise de Velas, Tendência, RSI, Volume Implícito (sem indicador na tela) e Probabilidade em M1.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print do gráfico M1 (Velas, RSI e Relógio visíveis):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE COMPLETA"):
            with st.spinner("IA escaneando padrões de velas, volume e mercado..."):
                
                # Prompt atualizado para estimar volume por Price Action puro (corpos e pavios das velas)
                prompt = """
                Você é um robô de trading institucional de alta performance, especialista em Price Action puro, análise de fluxo de ordens (Order Flow) e análise técnica visual para Opções Binárias (M1).
                Sua missão é analisar minuciosamente a imagem enviada com foco absoluto na anatomia das velas e nas métricas do mercado para projetar um clique de 2 a 5 minutos no futuro com expiração para a mesma vela.

                Analise as seguintes variáveis visuais na imagem:
                1. ANATOMIA DAS VELAS: Cor das últimas 5 velas (verde/vermelha), tamanho do corpo (velas expressivas ou sem força) e presença de pavios (pavio longo em cima = rejeição de alta; pavio longo embaixo = rejeição de baixa; sem pavio = força total).
                2. ESTIMAÇÃO DE VOLUME IMPLÍCITO: Mesmo que NÃO haja um indicador de volume na tela, deduza o Volume de Negociação baseado no tamanho dos corpos das velas e na velocidade dos movimentos recentes (Velas com corpos muito grandes e sem pavios indicam alto volume institucional; velas muito pequenas e cheias de dojis/pavios longos indicam baixo volume e indecisão).
                3. MOMENTO DO GRÁFICO: Identifique se o mercado está em Tendência de Alta, Tendência de Baixa ou Lateralizado/Consolidado.
                4. TAXA DE ASSERTIVIDADE: Calcule uma porcentagem matemática aproximada de acerto para a entrada (0% a 100%) baseada na confluência de todos esses fatores e no RSI (14, 70/30).

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 87%] (Escreva bem grande e destacado)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato entre 2 a 5 minutos à frente do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]

                🧠 ESTRATÉGIA: [FLUXO DE VELA ou REVERSÃO DE TENDÊNCIA]
                📊 CONTEXTO DO MERCADO: [Mencione se está em TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]

                🔍 DETALHAMENTO ANATÔMICO (O QUE A IA VIU):
                - Anatomia das Velas: [Descreva a cor predominante, se o tamanho dos corpos está diminuindo/aumentando e o que os pavios indicam]
                - Análise Estatística de Volume Implícito: [Explique o nível de volume que você estimou através do tamanho e força das velas. Ex: 'Alto volume de fluxo comprador detectado por velas de corpo cheio e sem pavios superiores.']
- Situação do RSI: [Indique a posição visual da linha do RSI]

                Seja extremamente frio, preciso e direto na resposta. Velocidade e precisão salvam bancas.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Avançada Concluída com Sucesso!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")