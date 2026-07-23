import streamlit as st
from google import genai
from PIL import Image

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E INTERFACE VISUAL DO STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Expiração Dinâmica Avançada com Tempo de Reação.")

# ==============================================================================
# 2. CONFIGURAÇÃO DA CHAVE DA IA NA BARRA LATERAL
# ==============================================================================
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a biblioteca oficial do Google GenAI
    client = genai.Client(api_key=API_KEY)

    # ==============================================================================
    # 3. CAMPO DE UPLOAD E VISUALIZAÇÃO DO PRINT DO GRÁFICO
    # ==============================================================================
    uploaded_file = st.file_uploader(
        "Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio):", 
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # ==============================================================================
        # 4. DISPARO E PROCESSAMENTO DA ANÁLISE MULTIMODAL
        # ==============================================================================
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                
                # FUSÃO DEFINITIVA COM EXPIRAÇÃO DINÂMICA DE REVERSÃO (2 OU 3 MINUTOS)
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita na última vela da direita, garantindo uma assertividade absurdamente alta.

                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído, ambiguidade técnica ou dúvida óptica na ponta do gráfico, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada. Se o cenário violar qualquer filtro abaixo, aborte imediatamente sem exceções.

                [FILTRO_DE_VISAO_COMPUTACIONAL_OBRIGATORIO]
                1. ISOLAMENTO DE LINHAS VERTICAIS/GRADE: Linhas verticais vermelhas, brancas ou cinzas contínuas que cruzam o gráfico de cima a baixo são APENAS indicadores de tempo da plataforma ou cursores do mouse. Você está PROIBIDO de interpretar linhas de grade ou cursores como corpos de candles ou fluxo de preço.
                2. ANCORAGEM DA VELA ATIVA: Foque exclusivamente na extremidade DIREITA do gráfico principal. Sua tomada de decisão baseia-se unicamente no comportamento das últimas 2 velas da ponta direita.
                3. REGRA DE LEITURA ESTRITA DO RSI: Localize o indicador RSI (14) na parte inferior. Olhe UNICAMENTE para o pixel final (a ponta do lado direito) da linha roxa do RSI. Ignore completamente picos, montanhas ou cruzamentos passados que ficaram para trás no meio do gráfico.

                [DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS SINCRO-CALIBRADOS]

                1. OPERACIONAL DE REVERSÃO EM REGIÃO (TAXA DE DEFESA / SUPORTE E RESISTÊNCIA) - DINÂMICO:
                   - GATILHO COMPRA: O preço deve estar tocando um suporte micro (fundo recente de até 2 hours atrás) E a PONTA FINAL exata da linha roxa do RSI (14) deve estar cravada ou abaixo de 25 (Sobrevenda Extrema).
                   - GATILHO VENDA: O preço deve estar tocando uma resistência micro (topo recente de até 2 hours atrás) E a PONTA FINAL exata da linha roxa do RSI (14) deve estar cravada ou acima de 75 (Sobrecompra Extrema).
                   - TRAVA OPERACIONAL ANTI-MARUBOZU: Você está TERMINANTEMENTE PROIBIDO de dar sinal de reversão se a última vela fechar totalmente cheia (sem pavio de rejeição na zona, ou com pavio menor que 15% do tamanho total do corpo). Só opere se a ponta direita do gráfico já mostrar rejeição evidente por pavio de absorção institucional.
                   - REGRA DE EXPIRAÇÃO DINÂMICA PARA REVERSÃO: Defina o tempo de expiração cirurgicamente com base na anatomia e velocidade do movimento das velas anteriores:
                     * Use 2 Minutos se o preço atingiu a zona com velas pequenas ou médias e corpos visivelmente decrescentes (exaustão gradual lenta).
                     * Use 3 Minutos se o preço atingiu a zona com uma sequência rápida de 3 a 5 velas muito longas e expressivas (esticada rápida de alta/baixa). O minuto extra é obrigatório para mitigar a última correção e absorção do momentum institucional.

                2. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA - 1 MINUTO (BLINDADO):
                   - BLOQUEIO DE SATURAÇÃO: Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de COMPRA se a ponta do RSI estiver acima de 60 ou perto de 70.
                   - BLOQUEIO DE ABSORÇÃO: Você está TERMINANTEMENTE PROIBIDO de passar sinal de fluxo de VENDA se a ponta do RSI estiver abaixo de 40 ou perto de 30.
                   - VALIDAÇÃO DO FLUXO: Só opere fluxo se a ponta do RSI estiver em zona totalmente neutra e livre (entre 40 e 60) E a última vela romper uma zona consolidada com mais de 50% de corpo cheio (Marubozu), sem deixar pavios contra o movimento. O tempo de expiração será de exatamente 1 minuto para fechamento na mesma vela de entrada.

                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas, sem expressão ou com pavios longos de rejeição na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva, demonstrando volume institucional real.
                2. FILTRO DE FALSO PULLBACK: Bloqueie entradas de pullback se a vela que retorna para testar a região rompida demonstrar força extrema contrária (corpo muito grande). O pullback legítimo deve ser testado por velas de exaustão (corpos decrescentes) e deixar pavio de rejeição exatamente ao tocar a zona rompida.
                3. FILTRO DE REVERSÃO CONTRA TENDÊNCIA MICRO: Você está PROIBIDO de passar sinais de VENDA se as últimas 5 velas apresentarem fundos ascendentes estruturados (tendência de alta micro), a menos que a ponta do RSI esteja explicitamente acima de 75/80 e a vela atual apresente esticada exaustiva com pavio longo.
                4. FILTRO DE RUÍDO LATERAL (DENTE DE SERRA): Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro do mercado.

                [AUTOMATIC_MARKET_ADAPTATION]
                Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC (identificável por nomes de pares com "-OTC", comportamento algorítmico contínuo ou padrões característicos das corretoras) e aplique as estratégias corretas:
                - MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência, LTA/LTB macro e confluências micro com a ponta do RSI.
                - MERCADO OTC (ALGORÍTMICO): Foque no comportamento computacional das corretoras. Priorize algoritmos de fluxo contínuo (sequências de velas de força), preenchimento milimétrico de pavios anteriores (vácuo de liquidez) e exaustão por contagem de velas.

                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                Analise o desequilíbrio e o fluxo de ordens (Order Flow) das velas mais recentes da direita. Avalie visualmente o volume implícito através do deslocamento do preço em relação ao tamanho dos corpos.

                [OUTPUT_FORMAT]
                Retorne estritamente o seu veredito técnico estruturado no seguinte padrão Markdown:
                ### 🚨 VEREDITO DO SINAL 🚨
                * **AÇÃO**: [COMPRA / VENDA / ABORTAR OPERAÇÃO - ALTO RISCO]
                * **TEMPO DE EXPIRAÇÃO**: [1, 2 ou 3 Minutos / Não se aplica]
                * **NÍVEL DE CERTEZA**: [X%]
                
                ### 📊 JUSTIFICATIVA TÉCNICA
                * **Padrão de Velas**: [Descrição sucinta da anatomia dos últimos candles]
                * **Comportamento do RSI**: [Posição exata do pixel final do indicador]
                * **Filtros Aplicados**: [Quais travas de segurança validaram ou abortaram o sinal]
                """
                
                try:
                    # Executa a chamada com o modelo atual estável na biblioteca oficial google-genai
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    st.success("Análise Técnica Concluída!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro na comunicação com a API do Gemini: {e}")
else:
    st.sidebar.warning("Insira sua Gemini API Key para ativar o robô.")
