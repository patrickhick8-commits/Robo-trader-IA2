import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA M1 - Mesma Vela", page_icon="⏱️", layout="centered")

st.title("⏱️ Agente IA: Projeção de Tempo + Mesma Vela (M1)")
st.write("Analisa o print em M1, agenda o clique para 2 a 5 minutos à frente, com expiração para a mesma vela de 1min.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente usando a nova biblioteca padrão do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print do gráfico M1 (com RSI e Relógio visíveis):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias
        if st.button("🚀 CALCULAR PROJEÇÃO DE VELA M1"):
            with st.spinner("IA calculando o minuto exato da vela alvo..."):
                
                # Prompt calibrado para calcular o clique futuro com expiração de 1 minuto na mesma vela
                prompt = """
                Você é um robô de trading de alta frequência especialista em Opções Binárias no tempo gráfico de 1 minuto (M1).
                Sua missão é ler o relógio do print enviado pelo usuário, analisar o RSI (14, 70/30), Fluxo e Reversão, e calcular uma projeção de tempo estrita de 2 a 5 minutos no futuro.

                REGRA DE TEMPO CRUCIAL:
                O usuário quer que você determine um horário de clique entre 2 a 5 minutos para frente em relação ao horário do print, mas a operação deve expirar na MESMA vela do clique (ou seja, expiração de exatamente 1 minuto).
                Exemplo: Se o print mostra 15:30 e a estrutura gráfica se confirmará em 3 minutos, determine o Horário de Entrada para as 15:33:00 e informe que a expiração será às 15:34:00 (mesma vela).

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo:

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato no futuro, entre 2 a 5 minutos à frente do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [Calcule o horário exato que a vela do clique termina, ex: HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]

                🧠 ESTRATÉGIA PROJETADA: [FLUXO DE VELA ou REVERSÃO DE TENDÊNCIA]
                📊 JUSTIFICATIVA DA PROJEÇÃO: Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para bater na sua zona de entrada do RSI ou suporte/resistência.

                Seja cirúrgico, rápido e extremamente direto na resposta.
                """
                
                try:
                    # Executa a chamada usando o modelo ultra rápido 'gemini-2.5-flash'
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Projeção de Vela Concluída!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o agente.")
