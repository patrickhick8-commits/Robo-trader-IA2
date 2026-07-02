import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema e Projeção Temporal")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

if lista_de_chaves:
    # Seleciona a primeira chave válida da contingência
    chave_ativa = lista_de_chaves[0]
    
    # Inicializa o cliente oficial da nova SDK do Google GenAI
    client = genai.Client(api_key=chave_ativa)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (Obrigatório conter o Relógio da Plataforma visível, Velas, RSI e Volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise de Confluência Suprema", use_container_width=True)
        
        if st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL"):
            with st.spinner("IA aplicando Filtros Anti-Ruído e Verificação de Tendência..."):
                
                prompt = """
                [SYSTEM_ROLE] Você é um superalgoritmo HFT (High-Frequency Trading) e analista quantitativo focado em trading de precisão matemática para Opções Binárias (M1). Sua postura é extremamente cética. Sua prioridade número um é a PRESERVAÇÃO DE CAPITAL. Se o cenário apresentar ruído ou lateralidade, você DEVE abortar.

                Analise as seguintes camadas visuais no print enviado de forma estrita:

                [1. FILTRO DE TENDÊNCIA E LATERALIDADE - CRÍTICO ANTI-LOSS]
                - Se o gráfico apresentar velas pequenas (Dojis) alternando cores consecutivamente (verde, vermelha, verde, vermelha), o mercado está sem direção (lateralizado). Você deve emitir obrigatoriamente: DIREÇÃO EXATA DA ORDEM: OPERAÇÃO ABORTADA.
                - Identifique a tendência macro visual das velas: não opere contra a tendência predominante dos últimos 20 candles.

                [2. REGRA DE AMBIENTE: ABERTO VS OTC]
                - Localize o nome do ativo. Se contiver 'OTC', os pavios longos são armadilhas (absorção falsa do algoritmo). Foque apenas no preenchimento do corpo da vela a favor do fluxo atual.
                - Se for Mercado Aberto, os pavios longos em zonas de suporte/resistência são válidos como rejeição institucional para operações de retração.

                [3. PROJEÇÃO DE INDICADORES REALISTAS]
                - Atenção: NÃO invente dados. Analise apenas os indicadores que estão de fato plotados na imagem (como RSI ou Médias). Se o RSI não estiver visível, desconsidere-o da pontuação e baseie-se estritamente na ação do preço (Price Action) e quebras de estrutura (SMC/BOS).

                [4. CRITÉRIO MATEMÁTICO DE ASSERTIVIDADE]
                - Avalie os riscos de 0 a 100 com base em: alinhamento de tendência, volume do candle gatilho e proximidade de zonas de defesa.
                - Se a confluência não atingir pelo menos 90% de probabilidade matemática real, defina a ordem como OPERAÇÃO ABORTADA. Não mascare resultados com taxas falsas de 92% se o gráfico estiver feio.

                [5. PROJEÇÃO TEMPORAL REGRADA]
                - Verifique o relógio do print. Projete o horário do clique exatamente para a próxima vela limpa que tocará na região de interesse, limitando-se de 2 a 5 minutos no futuro. Exigido expiração para a mesma vela (1 minuto).

                Retorne o diagnóstico estruturado exatamente neste formato markdown limpo:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Apenas valores reais baseados nos filtros. Se for Abortada, escreva '0% - FILTRO ATIVADO']

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado para o futuro]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento]
                🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]

                🧠 ESTRATÉGIA COMBINADA: [Ex: FLUXO DE CONTINUIDADE OTC ou RETRAÇÃO EM SUPORTE]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / MERCADO PICOTADO LATERAL]

                🔍 DETALHAMENTO TÉCNICO (FILTROS APLICADOS):
                - Condição de Tendência: [Descreva o alinhamento das últimas 20 velas]
                - Validação de Pavios e Ruído: [Explique por que o sinal é seguro ou por que foi abortado devido ao ruído]
                - Estrutura de Mercado (SMC/SR): [Zonas reais identificadas e proximidade do preço]
                - Justificativa da Decisão: [Seja direto e frio sobre o motivo de arriscar ou proteger o capital]
                """
                
                try:
                    # Executa a chamada utilizando o modelo multimodal mais recente e performático para visão computacional
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar com a chave atual: {str(e)}")
                    st.warning("Tentando chave de contingência seguinte se disponível...")
else:
    st.warning("Insira pelo menos uma Gemini API Key válida na barra lateral para ativar o Agente.")
