import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Probabilidade em M1.")

# 2. Configuração da Chave da IA
st.sidebar.title("Configurações")
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # --- MENU DE SELEÇÃO DE MODO OPERACIONAL ---
    st.markdown("### 🛠️ Escolha o Modo Operacional:")
    
    # Criando apenas 2 colunas para os botões de WIN e LOSS
    col_btn1, col_btn2 = st.columns(2)
    
    # Define o modo inicial como WIN por padrão, já que tiramos o botão de "ANÁLISE"
    if "modo_operacao" not in st.session_state:
        st.session_state.modo_operacao = "WIN"

    with col_btn1:
        if st.button("🟢 Autoanálise de WIN", use_container_width=True):
            st.session_state.modo_operacao = "WIN"
    with col_btn2:
        if st.button("🔴 Autoanálise de LOSS", use_container_width=True):
            st.session_state.modo_operacao = "LOSS"

    modo = st.session_state.modo_operacao

    # Confirmação visual do modo ativo para o usuário
    if modo == "WIN":
        st.success("Modo Atual Selecionado: 🟢 Autoanálise de WIN")
    elif modo == "LOSS":
        st.error("Modo Atual Selecionado: 🔴 Autoanálise de LOSS")

    # --- ÁREA DE INPUT E DETECÇÃO (O PRINT PARA A IA) ---
    st.markdown("---")
    st.markdown("### 📸 Enviar Print do Gráfico")
    
    # Campo para o usuário arrastar ou selecionar o print do gráfico
    uploaded_file = st.file_uploader("Carregue o print do seu gráfico (M1):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Abre a imagem usando a biblioteca PIL
        image = Image.open(uploaded_file)
        # Exibe uma miniatura do print na tela
        st.image(image, caption="Print carregado com sucesso!", use_container_width=True)

        # Botão centralizado para disparar a IA
        if st.button("🔍 Detectar Gráfico e Gerar Análise", use_container_width=True):
            st.info("Processando imagem e gerando o relatório inteligente...")
            
            # Ajusta o prompt de acordo com o botão ativo (WIN ou LOSS)
            if modo == "WIN":
                prompt_especifico = """
                Aja como um Trader Institucional de Alta Performance e analise minunciosamente este gráfico de M1. 
                Foque em identificar um cenário com padrão de WIN claro e de altíssima assertividade, filtrando friamente todos os ruídos de mercado.

                Seu relatório final deve seguir OBRIGATORIAMENTE esta estrutura detalhada:

                1. IDENTIFICAÇÃO DO HORÁRIO E PROJEÇÃO (Tempo de Espera de 2 a 5 minutos):
                   - Identifique a hora exata atual do print no gráfico (Exemplo: 23:19).
                   - Com base nisso, liste opções exatas de horários para a próxima entrada cirúrgica respeitando a janela de 2 a 5 minutos à frente (Exemplo: Entrada às 23:21, 23:22 ou 23:23).
                   - ATENÇÃO: A expiração da operação deve ser rigorosamente para a mesma vela de M1 (fim da vela do minuto sugerido).

                2. DIREÇÃO DA OPERAÇÃO:
                   - Defina de forma direta e sem hesitação: COMPRA (CALL) ou VENDA (PUT).

                3. CONTEXTO DO MERCADO:
                   - Classifique de forma cirúrgica se o mercado está em TENDÊNCIA (Alta/Baixa) ou LATERAL (Consolidação).

                4. ESTRATÉGIA, INDICADORES E PADRÕES:
                   - Detalhe a estratégia técnica utilizada.
                   - Descreva o comportamento dos indicadores visuais (RSI, Suporte/Resistência, Volume Implícito, Médias Móveis se houver).
                   - Faça a leitura milimétrica das Velas: Cor, Tamanho do corpo e comportamento dos Pavios de rejeição.

                5. TAXA DE ASSERTIVIDADE (Filtro Anti-Ruído):
                   - Defina uma taxa matemática real de assertividade para este sinal, variando estritamente entre 80% e 99%.
                   - Justifique o motivo dessa alta taxa com base na ausência de ruídos na zona escolhida.
                """
            else:
                prompt_especifico = """
                Aja como um Trader Institucional de Alta Performance e analise minunciosamente este gráfico de M1 focado em um cenário de LOSS (Mapeamento de Erro/Defesa). 
                Foque em identificar o que causou o loss (falso rompimento, notícia oculta, exaustão), filtrando friamente os ruídos de mercado para recalibrar a próxima entrada para acerto.

                Seu relatório final deve seguir OBRIGATORIAMENTE esta estrutura detalhada:

                1. IDENTIFICAÇÃO DO HORÁRIO E PROJEÇÃO DE RECUPERAÇÃO (Tempo de Espera de 2 a 5 minutos):
                   - Identifique a hora exata atual do print no gráfico (Exemplo: 23:19).
                   - Projete opções exatas de horários de entrada para reentrada ou nova operação filtrada de 2 a 5 minutos à frente (Exemplo: Entrada às 23:21, 23:22 ou 23:23).
                   - ATENÇÃO: A expiração da operação deve ser rigorosamente para a mesma vela de M1.

                2. DIREÇÃO DA OPERAÇÃO (Recuperação):
                   - Defina de forma direta e sem hesitação: COMPRA (CALL) ou VENDA (PUT).

                3. CONTEXTO DO MERCADO NO MOMENTO DA FALHA:
                   - Classifique de forma cirúrgica se o mercado mudou para TENDÊNCIA (Alta/Baixa) ou se prendeu em estrutura LATERAL (Consolidação).

                4. ANÁLISE DE FALHA DA ESTRATÉGIA E INDICADORES:
                   - Explique o que falhou na leitura anterior (Ex: RSI sobrecomprado que continuou subindo, pavio que rompeu suporte).
                   - Explique os novos padrões de velas (Cor, Tamanho e Pavio) que redesenharam a zona de proteção.

                5. NOVA TAXA DE ASSERTIVIDADE FILTRADA:
                   - Estipule a nova taxa matemática de assertividade para a reentrada limpa, variando estritamente entre 80% e 99%.
                   - Explique friamente como os ruídos anteriores foram eliminados para garantir essa segurança.
                """
            
            # Código que faz a chamada oficial para a API do Gemini
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image, prompt_especifico]
                )
                st.markdown("### 📊 Resultado da Análise da IA:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro ao chamar a API do Gemini: {e}")
