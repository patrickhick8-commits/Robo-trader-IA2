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
            with st.spinner("IA escaneando padrões, aplicando FILTRO AGRESSIVO anti-ruído..."):
                
                # Prompt atualizado com blindagem institucional e filtros rigorosos contra loss sequencial
                prompt = """
                [SYSTEM_ROLE] Você é um superalgoritmo HFT de fundos soberanos e analista quantitativo focado em trading de altíssima precisão. Sua postura é de extrema frieza e ceticismo matemático. Sua missão prioritária é PRESERVAR CAPITAL. Se o cenário gráfico apresentar qualquer sinal de ruído, volatilidade errática ou lateralidade, você deve abortar a entrada sem hesitação.

                Analise de forma cirúrgica as variáveis visuais no print enviado:

                [1. FILTRO ANTI-RUÍDO AGRESSIVO - LEI DE BLOQUEIO ABSOLUTO]
                Você deve emitir obrigatoriamente DIREÇÃO DA ORDEM: OPERAÇÃO ABORTADA se identificar qualquer uma destas condições nas últimas 15 velas:
                - MERCADO PICOTADO: Alternância sequencial de cores (verde, vermelha, verde, vermelha) formando zonas picotadas sem direção clara.
                - MICRO-VELAS E DOJI: Presença de 3 ou mais velas consecutivas com corpos espremidos, minúsculos ou inexistentes. Isso indica ausência de liquidez institucional.
                - MEDIAS EMBOLADAS: Se as médias estimadas EMA 9 e SMA 20 estiverem horizontais, cruzando-se repetidamente a cada 2 candles e sem inclinação nítida.

                [2. LEI DO VOLUME OCULTO E COMPORTAMENTO OPERACIONAL]
                - Não invente dados. Se o RSI ou outros indicadores não estiverem explicitamente desenhados no gráfico, ignore-os e execute a análise puramente em Price Action estrutural e anatomia dos candles.
                - Velas com corpos gigantes (Marubozu) indicam urgência institucional. Nunca opere reversão (contra) uma sequência de velas cheias de mesma cor, pois o mercado tende a engolfar as regiões devido ao fluxo de ordens (Order Flow).

                [3. SISTEMA DE CÁLCULO E CALIBRAGEM DE ASSERTIVIDADE]
                - Seja extremamente rígido ao pontuar a assertividade da operação. Só valide e libere sinais com confluência tripla idônea (Ex: Toque em LTA + Candle Gatilho de Força + Direção a favor da tendência macro).
                - Se o cenário passar nos testes mas a probabilidade matemática real calculada for menor que 92%, defina o veredito como OPERAÇÃO ABORTADA e mude a porcentagem para "0% - FILTRO ATIVADO".

                [4. CRONOMETRAGEM DE EXECUÇÃO]
                - Localize o relógio oficial da plataforma no print. Agende o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de 2 a 5 minutos, projetando o momento exato em que a vela de teste tocará a zona segura. Expiração rígida para 1 minuto (fechamento na mesma vela do clique).

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 95% - Confluência Tripla Filtrada. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva bem grande e destacado)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM:00 do fechamento real da ordem]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]

                🧠 ESTRATÉGIA: [Ex: FLUXO DE ROMPIMENTO DE LTB ou REVERSÃO EM SUPORTE HISTÓRICO]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / MERCADO PICOTADO LATERAL]

                🔍 DETALHAMENTO ANATÔMICO E TÉCNICO (FILTROS DE SEGURANÇA):
                - Condição da Tendência Macro: [Explique o alinhamento das últimas velas e direção geral do preço]
                - Análise Estatística de Volume Oculto: [Nível de volume estimado pela anatomia e tamanho dos corpos dos candles]
                - Mapeamento de Regiões Visuais (S/R e LTA/LTB): [Como o preço está se comportando em relação às zonas de preço]
                - Comportamento de Pavios e Ruído: [Explique se há risco de rejeição falsa ou se o mercado está limpo]
                - Justificativa do Filtro Agressivo: [Argumente friamente por que essa operação é estatisticamente segura ou por que foi estritamente abortada para proteger a banca]

                Seja extremamente frio, preciso e direto na resposta. Velocidade e precisão salvam bancas.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Avançada com Blindagem de Capital Concluída!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")
