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
                
                # Prompt atualizado para mapear fluxo por cores de velas e padrões institucionais
                prompt = """
                Você é um robô de trading institucional de alta performance, especialista em Price Action puro, análise de fluxo de ordens (Order Flow) e análise técnica visual para Opções Binárias (M1).
                Sua missão é analisar minuciosamente a imagem enviada com foco absoluto na anatomia das velas, cruzamento de indicadores, sequências de cores e métricas estruturais para projetar um clique de 2 a 5 minutos no futuro com expiração para a mesma vela.

                Analise rigorosamente as seguintes variáveis visuais e confluências na imagem:
                1. MAPEAMENTO DE FLUXO POR CORES DE VELAS:
                   - Fluxo de Alta: Identifique sequências dominantes de velas verdes, o tamanho crescente de seus corpos e a ausência ou diminuição de pavios superiores, indicando forte pressão compradora e urgência do mercado.
                   - Fluxo de Baixa: Identifique sequências dominantes de velas vermelhas, corpos expandidos e a ausência ou diminuição de pavios inferiores, indicando forte pressão vendedora e domínio dos ursos.
                   - Quebra de Fluxo: Avalie se velas de cor contrária são engolfadas ou ignoradas rapidamente, confirmando a continuação do fluxo principal.
                2. ANATOMIA DAS VELAS E VOLUME IMPLÍCITO: Deduza o Volume de Negociação baseado no tamanho dos corpos das velas (corpos expandidos/Marubozu = alto volume; corpos espremidos/Dojis = baixo volume) e rejeição/absorção por pavios longos.
                3. PROJEÇÃO DE INDICADORES INTERNOS: 
                   - Média Móvel Exponencial de 9 Períodos (EMA 9): Força imediata e direção do preço a curto prazo.
                   - Média Móvel Simples de 20 Períodos (SMA 20): Tendência média e zonas de pullback dinâmico.
                   - Índice de Força Relativa (RSI 14): Zonas de exaustão, Sobrecompra (>70) ou Sobrevenda (<30).
                4. ZONEAMENTO ESTRUTURAL (S/R e LTA/LTB): Identifique zonas horizontais de Suporte e Resistência, e linhas de tendência inclinadas (LTA / LTB) traçadas pelos fundos e topos do print.
                5. PADRÕES GRÁFICOS VISUAIS: Identifique estruturas macro como OCO (Ombro-Cabeça-Ombro), Topo/Fundo Duplo, Triângulos de afunilamento, Canais ou Caixas de Acumulação que determinam a direção do fluxo.
                6. VALIDAÇÃO DE PADRÕES DE CANDLES (VELAS):
                   - Reversão: Identifique Martelo, Estrela da Manhã/Noite, Engolfo ou Harami exatamente quando o preço tocar em S/R, LTA ou LTB.
                   - Fluxo e Rompimento: Identifique velas de força rompendo zonas consolidadas ou linhas de tendência, indicando continuação imediata.

                [FILTRO DE SEGURANÇA E ACERTIVIDADE EXTREMA]
                - Para emitir um sinal válido, exija confluência clara (Ex: Sequência de fluxo iniciada + Rompimento de padrão gráfico + Médias alinhadas).
                - Se as velas estiverem alternando cores a cada candle (verde, vermelha, verde, vermelha) indicando um mercado sem direção e picotado, ABORTE a operação imediatamente.
                - A taxa calculada deve refletir essa filtragem estrita (Apenas valide operações se o cálculo final resultar entre 88% e 99% de probabilidade).

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 95% - Confluência Tripla Filtrada] (Escreva bem grande e destacado)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato entre 2 a 5 minutos à frente do relógio do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]

                🧠 ESTRATÉGIA: [Ex: FLUXO DE CONTINUIDADE POR VELAS SEQUENCIAIS ou ROMPIMENTO DE TRIÂNGULO]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]

                🔍 DETALHAMENTO ANATÔMICO E TÉCNICO (O QUE A IA VIU):
                - Diagnóstico do Fluxo de Cores: [Descreva a dominância de cores das últimas velas e se há força direcional de alta ou baixa]
                - Posição das Médias (EMA 9 vs SMA 20): [O cruzamento ou alinhamento das duas médias imaginárias]
                - Situação do RSI: [Indique a posição visual da linha do RSI e nível de exaustão]
                - Mapeamento S/R e LTA/LTB: [Como o preço está se comportando em relação às regiões fixas e inclinadas]
                - Padrão Gráfico e de Candle Validado: [Identificação da figura de price action e o gatilho da vela de entrada]
                - Análise Estatística de Volume Implícito: [Explique o nível de volume estimado pela anatomia/força das velas]
                - Filtro de Proteção Ativado: [Justificativa do porquê o sinal passou no teste de segurança e não foi abortado por falta de direção clara]

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
