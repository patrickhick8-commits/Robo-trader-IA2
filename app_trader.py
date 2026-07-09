import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Volume Oculto", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Volume por Comportamento das Velas")
st.write("Análise de Velas, Tendência, RSI, Volume Implícito, Rompimentos e Filtros OTC/Aberto em M1.")

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
                
                # Prompt mestre ultra calibrado com filtros anti-doji e exaustão de volume implícito
                prompt = """
                Você é um especialista em análise técnica avançada e um scanner gráfico de alta precisão. Sua inteligência foi rigorosamente calibrada para aplicar o máximo de filtros técnicos simultâneos, rastreando estritamente a entrada perfeita para garantir vitórias consistentes (WIN).
                Sua missão é escanear a imagem enviada, cruzar os dados gráficos e calcular uma taxa de assertividade extrema baseada nos seguintes critérios analíticos:

                0. IDENTIFICAÇÃO E ADAPTAÇÃO AO TIPO DE MERCADO:
                - Identifique visualmente se o gráfico é de MERCADO ABERTO ou MERCADO OTC.
                - Se for MERCADO ABERTO: Aplique os filtros tradicionais de Price Action. A assertividade matemática pode chegar a escalas altas (até 100%) se houver confluência exata.
                - Se for MERCADO OTC: Lembre-se que o gráfico é controlado por um algoritmo proprietário sujeito a manipulações e caça de stops. Reduza a tolerância para reversões simples. Se detectar perigo de manipulação ou falso fluxo, aplique um "desconto de segurança" na taxa de assertividade, limitando-a para proteger o capital (filtros mais rígidos).

                1. Regra Rígida de Sincronização de Tempo e Horários:
                - Olhe atentamente para o RELÓGIO DO PRINT (Exemplo: se o print marca 11:34:05, a vela atual em andamento é a de 11:34:00, que fechará exatamente às 11:35:00).
                - Calcule os gatilhos baseando-se estritamente na vela IMEDIATAMENTE posterior ao fechamento da atual.
                - Nunca gere atrasos fantasmas de 2 a 3 minutos à frente se o padrão técnico exigir uma reação imediata na próxima vela.

                2. Filtros Técnicos de Price Action e Fluxo:
                - Análise de Price Action: Identifique suportes, resistências, canais e linhas de tendência (LTB/LTA) macro e micro.
                - Métricas de Rejeição (Retração): Meça a força de equilíbrio do preço com base no tamanho dos pavios em zonas críticas. Pavios longos isolados ou repetidos indicam defesa institucional.
                - Fluxo de Velas pelas Cores: Analise a sequência e a alternância das cores das velas (verde/vermelha) para identificar a persistência do movimento e a exaustão do preço.
                - Força da Tendência Atual: Avalie as estruturas de alta ou baixa através de topos e fundos descendentes ou ascendentes.
                - Volume do Mercado e Filtro Especial de Dojis: Monitore o volume institucional interpretado pelo tamanho do corpo das velas (expressão de força) e o tamanho dos pavios (força de absorção). ATENÇÃO: Velas muito pequenas, sem corpo e cheias de pavios longos (Dojis) indicam que o volume da tendência anterior MORREU. Se um Doji surgir em uma região de suporte/resistência com pavio longo de rejeição, indica exaustão imediata do movimento e alta probabilidade de reversão forte na próxima vela.

                3. Filtro Crítico de Espaço Gráfico, Exaustão Temporal e Seleção de Estratégia Dinâmica:
                - Você deve cruzar o espaço físico (vazio gráfico) entre o preço atual e as próximas zonas de defesa com o relógio do print para selecionar uma das 4 estratégias principais:
                  
                  * [FLUXO DE VELA]: Escolha se houver um rompimento recente de corpo cheio confirmado por volume, com um vazio gráfico amplo à frente e sem pavios de rejeição/Dojis contra o movimento.
                  * [PULLBACK]: Escolha se a vela atual confirmou o rompimento de uma zona e a próxima vela tende a realizar o retorno para testar a linha. ATENÇÃO: Se a vela de teste anterior terminar em Doji com pavio de rejeição contra o rompimento, CANCELE o pullback de continuação imediatamente, pois o volume de rompimento falhou.
                  * [RETRAÇÃO EM PAVIO]: Escolha se o preço estiver testando uma zona consolidada onde pavios anteriores provaram que o preço é rejeitado sistematicamente na mesma vela.
                  * [REVERSÃO DE TENDÊNCIA DINÂMICA]: Escolha se o preço estiver muito esticado ou se surgir um Doji de exaustão indicando perda total de volume e força da tendência atual. Cancele o fluxo ou pullback intermediário na hora e projete a operação contra o movimento anterior para ganhar na reversão.

                4. Critérios e Gatilhos de Entrada (Operacional):
                - Determine o gatilho cirúrgico baseado estritamente na estratégia escolhida no item 3. Detalhe o minuto exato da ação em milissegundos para evitar atrasos na execução por parte do trader.

                Analise o gráfico enviado, processe todos os filtros de forma simultânea e forneça o veredito final detalhado e estruturado estritamente neste formato markdown limpo e destacado:

                🌐 TIPO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🚨 ALERTA DE MANIPULAÇÃO / EXAUSTÃO / DOJI: [Indique riscos de falsos rompimentos, caça de stops ou se a presença de Dojis/pavios longos indica perda de volume e exaustão do movimento atual]

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Calcule e exiba uma taxa de assertividade matemática exata de 0% a 100% considerando os riscos do mercado, Dojis e espaço gráfico] (Escreva bem grande e destacado)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato sincronizado perfeitamente com a regra do item 1]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00 baseado no horário do clique]
                🟥🟩 DIREÇÃO DA ORDEM (VEREDITO FINAL): [CALL (Compra) / PUT (Venda) / NEUTRO (Aguardar)]

                🧠 ESTRATÉGIA PRINCIPAL SELECIONADA: [FLUXO DE VELA / REVERSÃO DE TENDÊNCIA DINÂMICA / PULLBACK / RETRAÇÃO EM PAVIO]
                ⚡ GATILHO OPERACIONAL RECOMENDADO: [Descreva em detalhes como o trader deve agir. Aplique a sincronia exata de tempo explicada no item 1, detalhando em qual vela e minuto exato o clique deve ocorrer para não perder a oportunidade por atraso]

                📊 CONTEXTO DO MERCADO: [Mencione se está em TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]

                🔍 DETALHAMENTO TÉCNICO (O QUE A IA VIU):
                - Análise de Price Action e Espaço Gráfico: [Descreva o cálculo do vazio gráfico feito pela IA e por que a estratégia escolhida dentre as 4 é a mais segura]
                - Análise de Anatomia (Dojis e Cores): [Descreva o comportamento dos corpos, pavios e se a presença de Dojis validou a exaustão ou continuidade]
                - Volume Implícito Calculado: [Explique o nível de volume estimado pela força de corpos e pavios]
                - Situação do RSI: [Indique a posição visual da linha do RSI se estiver visível no print]

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
