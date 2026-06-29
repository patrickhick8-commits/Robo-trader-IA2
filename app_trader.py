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
                Aja como um Trader Institucional de Alta Performance e analise este gráfico de M1. 
                Foque em um cenário de WIN limpo, filtrando friamente os ruídos de mercado.

                Retorne o resultado FORMATADO EXATAMENTE como a lista vertical abaixo, um embaixo do outro, sem textos longos introdutórios. Seja direto:

                📌 **MERCADO**: [Diga apenas se está em TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]
                ⏰ **HORÁRIO DA ENTRADA**: [Identifique a hora do print e calcule APENAS UM horário exato específico de 2 a 5 minutos à frente. Exemplo: se o print é 23:19, mostre apenas "23:22". Adicione: Expiração para a mesma vela de M1]
                🎯 **DIREÇÃO**: [COMPRA ou VENDA]
                🧠 **ESTRATÉGIA**: [Nome da estratégia + breve resumo dos indicadores utilizados como RSI, volume e o comportamento minucioso das Velas, Pavios e Cores]
                📊 **TAXA DE ASSERTIVIDADE**: [Defina apenas uma porcentagem exata entre 80% e 99%]
                """
            else:
                prompt_especifico = """
                Aja como um Trader Institucional de Alta Performance e analise este gráfico de M1 focado em um cenário de LOSS (Recuperação). 
                Foque em identificar o erro e mapear a zona de proteção filtrando ruídos.

                Retorne o resultado FORMATADO EXATAMENTE como a lista vertical abaixo, um embaixo do outro, sem textos longos introdutórios. Seja direto:

                📌 **MERCADO**: [Diga se a falha ocorreu em TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERAL]
                ⏰ **HORÁRIO DA ENTRADA (RECUPERAÇÃO)**: [Identifique a hora do print e calcule APENAS UM horário exato específico de 2 a 5 minutos à frente para a reentrada limpa. Exemplo: "23:23". Adicione: Expiração para a mesma vela de M1]
                🎯 **DIREÇÃO**: [COMPRA ou VENDA]
                🧠 **ESTRATÉGIA (CORREÇÃO)**: [Análise da falha anterior + nova estratégia minuciosa de leitura de Velas, Pavios e indicadores para a reentrada]
                📊 **TAXA DE ASSERTIVIDADE**: [Defina apenas uma porcentagem exata entre 80% e 99% para esta zona protegida]
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
