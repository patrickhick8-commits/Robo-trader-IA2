# Instale no seu terminal caso ainda não tenha feito: pip install streamlit google-genai pillow
import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA M1 - Mesma Vela", page_icon="⏱️", layout="centered")

st.title("⏱️ Agente IA: Projeção de Tempo + Mesma Vela (M1)")
st.write("Analisa o print em M1, identifica a tendência, projeta o clique para 2 a 5 minutos à frente e mede a assertividade.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    genai.configure(api_key=API_KEY)
    # Modelo flash para máxima velocidade de resposta visual
    model = genai.GenerativeModel('gemini-2.5-flash') 

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print do gráfico M1 (com RSI e Relógio visíveis):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias
        if st.button("🚀 CALCULAR PROJEÇÃO DE VELA M1"):
            with st.spinner("IA analisando tendência e calculando o minuto exato..."):
                
                # Prompt calibrado para calcular o clique futuro com expiração de 1 minuto na mesma vela
                prompt = """
                Você é um robô de trading de alta frequência especialista em Opções Binárias no tempo gráfico de 1 minuto (M1).
                Sua missão é ler o relógio do print enviado pelo usuário, analisar o RSI (14, 70/30), Fluxo, Reversão, e calcular uma projeção de tempo estrita de 2 a 5 minutos no futuro.

                ETAPA 1: ANÁLISE DE TENDÊNCIA VISUAL
                Determine visualmente se o gráfico no print está em:
                - TENDÊNCIA DE ALTA (Topos e fundos ascendentes, preço acima das médias se houver)
                - TENDÊNCIA DE BAIXA (Topos e fundos descendentes, preço abaixo das médias se houver)
                - LATERALIZAÇÃO / TENDÊNCIA LATERAL (Preço preso dentro de um canal horizontal, sem direção definida)

                ETAPA 2: CÁLCULO DA TAXA DE ASSERTIVIDADE (0 a 100%)
                Estime visualmente a taxa de assertividade desta estratégia específica (Fluxo ou Reversão) considerando as últimas 10 a 20 velas visíveis no print. 
                - Quantos padrões idênticos a esse deram ganho (Win) vs perda (Loss) nas velas anteriores do print? 
                - Entregue um valor exato de 0 a 100% baseado estritamente no histórico visual imediato do gráfico enviado.

                REGRA DE TEMPO CRUCIAL:
                O usuário quer que você determine um horário de clique entre 2 a 5 minutos para frente em relação ao horário do print, mas a operação deve expirar na MESMA vela do clique (ou seja, expiração de exatamente 1 minuto).
                Exemplo: Se o print mostra 15:30 e a estrutura gráfica se confirmará em 3 minutos, determine o Horário de Entrada para as 15:33:00 e informe que a expiração será às 15:34:00 (mesma vela).

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo:

                📈 COMPORTAMENTO DO MERCADO: [ALTA / BAIXA / LATERAL]
                🎯 TAXA DE ASSERTIVIDADE DO PADRÃO: [Defina um valor exato de 0% a 100% com base no histórico do print]

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato no futuro, entre 2 a 5 minutos à frente do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [Calcule o horário exato que a vela do clique termina, ex: HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]

                🧠 ESTRATÉGIA PROJETADA: [FLUXO DE VELA ou REVERSÃO DE TENDÊNCIA]
                📊 JUSTIFICATIVA DA PROJEÇÃO: Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para bater na sua zona de entrada do RSI ou suporte/resistência, validando com a tendência identificada.

                Seja cirúrgico, rápido e extremamente direto na resposta.
                """
                
                try:
                    response = model.generate_content([prompt, image])
                    st.success("Projeção de Vela Concluída!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o agente.")
