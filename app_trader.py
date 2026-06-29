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
                Analise este gráfico focado em um cenário de WIN. 
                Identifique os padrões de Candlesticks (cor, tamanho, pavio), 
                tendência, RSI e volume implícito que validaram o acerto.
                """
            else:
                prompt_especifico = """
                Analise este gráfico focado em um cenário de LOSS. 
                Identifique as falhas, quebras de padrão de Candlesticks,
                reversões inesperadas e o que causou o erro na operação.
                """
            
            # Código que faz a chamada oficial para a API do Gemini
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash', # ou o modelo de sua preferência
                    contents=[image, prompt_especifico]
                )
                st.markdown("### 📊 Resultado da Análise da IA:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro ao chamar a API do Gemini: {e}")
