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
            with st.spinner("IA identificando tipo de mercado e aplicando filtros anti-manipulação..."):
                
                # Prompt mestre com ajuste de assertividade realista entre 80% e 96%
                prompt = """
                [SYSTEM_ROLE] Você é um superalgoritmo HFT de fundos soberanos e analista quantitativo focado em trading de altíssima precisão. Sua postura é de extrema frieza e ceticismo matemático. Sua missão prioritária é PRESERVAÇÃO DE CAPITAL.

                [PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
                Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
                - Se encontrar a sigla '-OTC' ou variações de mercado fechado da corretora, classifique como [AMBIENTE: ALGORITMO OTC].
                - Se for um par de moedas comum sem a sigla OTC, classifique como [AMBIENTE: MERCADO ABERTO REAL].

                [PASSO 2: FILTROS AGRESSIVOS DE MANIPULAÇÃO POR CENÁRIO]

                 SE FOR CONFIGURADO COMO MERCADO OTC:
                 - FILTRO ANTI-CAPTURA DE LIQUIDEZ: Pavios longos em OTC NÃO significam retração segura; são armadilhas para induzir o trader de varejo a operar reversão. O algoritmo de OTC tende a continuar o movimento para quebrar essas ordens. 
                 - REGRA OPERACIONAL EM OTC: Ignore sinais de retração isolada. Foque 100% em FLUXO DE VELA DE CORPO CHEIO (Marubozu) a favor do preenchimento desses pavios (alvos de liquidez do algoritmo). Opere a favor do fluxo dominante.

                 SE FOR CONFIGURADO COMO MERCADO ABERTO:
                 - FILTRO DE EXAUSTÃO INSTITUCIONAL: Aqui os pavios longos são válidos e representam defesa real de grandes players (SMC - Order Blocks).
                 - REGRA OPERACIONAL EM MERCADO ABERTO: Valide operações de RETRAÇÃO E REVERSÃO na mesma vela (M1) se o preço tocar extremidades exatas de Suporte/Resistência ou LTA/LTB com confluência de exaustão de volume. Nunca opere fluxo se o preço estiver esticado perto de barreiras de preço cheio.

                [PASSO 3: FILTRO ANTI-RUÍDO MECÂNICO GERAL]
                Aborte imediatamente (DIREÇÃO DA ORDEM: OPERAÇÃO ABORTADA) caso detecte:
                - Mercado em xadrez/picotado (Velas alternando cores seguidamente).
                - Padrão de 3 ou mais Dojis/Micro-velas consecutivas (Ausência de liquidez).

                [PASSO 4: SISTEMA DE CÁLCULO E CALIBRAGEM DE ASSERTIVIDADE]
                - Avalie rigorosamente os riscos com base no cenário gráfico e confluências encontradas.
                - Se o cenário for elegível para operação, defina a taxa de acerto estritamente dentro da faixa de **80% a 96%**. Sinais com menos de 80% de confluência real devem ser definidos obrigatoriamente como OPERAÇÃO ABORTADA e a porcentagem travada em "0% - FILTRO ATIVADO". Nenhum sinal pode passar de 96% para evitar métricas ilusórias.

                [PASSO 5: CRONOMETRAGEM DE EXECUÇÃO]
                Verifique o relógio do print e calcule o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de 2 a 5 minutos. Expiração rígida para 1 minuto (mesma vela do clique).

                Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 87% ou 94% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva bem grande e destacado)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM:00 do fechamento real da ordem]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]

                🧠 ESTRATÉGIA: [Ex: PREENCHIMENTO DE PAVIO (FLUXO OTC) ou RETRAÇÃO EM ORDER BLOCK (MERCADO ABERTO)]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / MERCADO PICOTADO LATERAL]

                🔍 DETALHAMENTO ANATÔMICO E CONFIGURAÇÃO ANTI-MANIPULAÇÃO:
                - Ambiente Detectado: [MERCADO ABERTO ou OTC - Explique o que foi identificado na imagem]
                - Filtro de Manipulação Aplicado: [Explique o comportamento do algoritmo ou dos players reais com base no ambiente identificado]
                - Condição da Tendência Macro: [Alinhamento e direção geral do preço]
                - Análise Estatística de Volume Oculto: [Nível de volume estimado pelo tamanho dos candles]
                - Justificativa do Filtro Agressivo: [Argumente friamente por que essa operação se enquadra na taxa de acerto definida ou por que foi estritamente abortada para proteger a banca]

                Seja extremamente frio, preciso e direto na resposta. Velocidade e precisão salvam bancas.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Avançada com Calibragem de Assertividade Concluída!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")
