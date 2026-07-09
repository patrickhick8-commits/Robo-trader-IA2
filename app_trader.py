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
                
                # Prompt unificado com todas as suas diretrizes exatas e inteligência de mercado
                prompt = """
                Você é um especialista em análise técnica avançada e um scanner gráfico de alta precisão. Sua inteligência foi rigorosamente calibrada para aplicar o máximo de filtros técnicos simultâneos, rastreando estritamente a entrada perfeita para garantir vitórias consistentes (WIN).
                Sua missão é escanear a imagem enviada, cruzar os dados gráficos e calcular uma taxa de assertividade extrema baseada nos seguintes critérios analíticos:

                0. IDENTIFICAÇÃO DO TIPO DE MERCADO:
                - Identifique visualmente (por textos no gráfico, marcas d'água, ativos ou comportamento das velas) se o gráfico é de MERCADO ABERTO ou MERCADO OTC (Over-The-Counter).
                - Se for MERCADO ABERTO: Respeite rigorosamente zonas de suporte/resistência macro, pullbacks tradicionais e exaustão de volume.
                - Se for MERCADO OTC: Considere algoritmos de continuidade de fluxo de cor, tendências longas e micro-rompimentos, adaptando a análise ao comportamento de fluxo contínuo do OTC.

                1. Filtros Técnicos de Price Action e Fluxo:
                - Análise de Price Action: Identifique suportes, resistências, canais e linhas de tendência (LTB/LTA) macro e micro.
                - Métricas de Rejeição (Retração): Meça a força de equilíbrio do preço com base no tamanho dos pavios em zonas críticas. Pavios longos isolados ou repetidos indicam defesa institucional.
                - Fluxo de Velas pelas Cores: Analise a sequência e a alternância das cores das velas (verde/vermelha) para identificar a persistência do movimento e a exaustão do preço.
                - Força da Tendência Atual: Avalie as estruturas de alta ou baixa através de topos e fundos descendentes ou ascendentes.
                - Volume do Mercado (Tamanho e Pavios): Monitore o volume institucional interpretado pelo tamanho do corpo das velas (expressão de força) e o tamanho dos pavios (força de absorção e contra-ataque de compradores e vendedores).

                2. Padrões Avançados de Confirmação:
                - Rompimento de Região: Só valide rompimentos se a vela romper com corpo cheio (mais de 50% fora da zona) e demonstrar força real pelo volume e tamanho da vela.
                - Pullback: Confirme a inversão de polaridade (antigo suporte vira resistência e vice-versa) após o rompimento validado.
                - Retração em Região de Pavio Respeitado: Identifique zonas onde pavios anteriores provaram que o preço é rejeitado sistematicamente, operando a favor da tendência principal.

                3. Critérios e Gatilhos de Entrada (Operacional):
                Ao identificar o cenário ideal, determine o gatilho exato com base nas regras abaixo:
                - Entrada na Abertura da Vela (Fluxo para Continuação): Execute imediatamente na abertura da próxima vela quando houver um rompimento com volume expressivo, corpo cheio, sem pavio de rejeição contra o movimento, seguindo o fluxo da tendência.
                - Entrada para Retração (Região de Pavio): Aguarde a vela atual nascer, fazer o movimento de explosão contra a zona de suporte/resistência e pegue a operação estritamente no toque da região de pavios anteriormente respeitados, visando o fechamento da mesma vela.
                - Entrada em Pullback: Aguarde o preço romper a região e retornar para testar a zona rompida. A entrada deve ser feita exatamente no teste (toque) da linha rompida.

                Analise o gráfico enviado, processe todos os filtros de forma simultânea e forneça o veredito final detalhado e estruturado estritamente neste formato markdown limpo e destacado:

                🌐 TIPO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94%] (Escreva bem grande e destacado)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato entre 2 a 5 minutos à frente do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM (VEREDITO FINAL): [CALL (Compra) / PUT (Venda) / NEUTRO (Aguardar)]

                🧠 ESTRATÉGIA PRINCIPAL: [FLUXO DE VELA, REVERSÃO DE TENDÊNCIA, PULLBACK ou RETRAÇÃO EM PAVIO]
                ⚡ GATILHO OPERACIONAL RECOMENDADO: [Descreva detalhadamente qual dos 3 gatilhos do item 3 deve ser ativado e como agir]

                📊 CONTEXTO DO MERCADO: [Mencione se está em TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]

                🔍 DETALHAMENTO TÉCNICO (O QUE A IA VIU):
                - Análise de Price Action e Tendência: [Descreva a estrutura detectada]
                - Métricas de Rejeição e Fluxo de Cores: [Descreva o comportamento dos pavios e cores das velas]
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
