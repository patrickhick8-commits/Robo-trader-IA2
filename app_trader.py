# Instale no seu terminal caso ainda não tenha feito: pip install streamlit google-genai pillow
import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA M1 - Mesma Vela", page_icon="⏱️", layout="centered")

st.title("⏱️ Agente IA: Projeção de Tempo + Mesma Vela (M1)")
st.write("Analisa o print em M1, identifica se é Mercado Aberto ou OTC, ajusta o operacional e projeta o clique para 2 a 5 minutos à frente.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Nova inicialização oficial do SDK google-genai
    client = genai.Client(api_key=API_KEY)
    
    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print do gráfico M1 (com RSI e Relógio visíveis):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias
        if st.button("🚀 CALCULAR PROJEÇÃO DE VELA M1"):
            with st.spinner("IA identificando cenário e calculando o minuto exato..."):
                
                # Prompt calibrado para Mercado Aberto vs OTC e Operacional adaptativo
                prompt = """
                Você é um robô de trading de alta frequência especialista em Opções Binárias no tempo gráfico de 1 minuto (M1).
                Sua missão é ler as informações do print enviado, identificar se o cenário é de Mercado Aberto ou OTC, analisar o RSI, Fluxo, Reversão, e calcular as métricas exatas de entrada.

                ETAPA 1: IDENTIFICAÇÃO DO CENÁRIO (ABERTO VS OTC)
                Procure por tags no nome do par (ex: EURUSD-OTC) ou analise o comportamento das velas.
                - Se for MERCADO ABERTO: A análise deve priorizar zonas clássicas de Suporte/Resistência e tendências fundamentadas em Price Action.
                - Se for OTC: A análise deve ignorar notícias e focar em padrões de repetição algorítmica (padrões de cores, ciclos de velas e preenchimento de pavios), considerando que tendências de OTC esticam muito mais e rompem S&R facilmente.

                ETAPA 2: ANÁLISE DE TENDÊNCIA VISUAL
                Determine se o gráfico no print está em:
                - TENDÊNCIA DE ALTA (Topos e fundos ascendentes)
                - TENDÊNCIA DE BAIXA (Topos e fundos descendentes)
                - LATERALIZAÇÃO (Preço preso dentro de um canal horizontal)

                ETAPA 3: CÁLCULO DA TAXA DE ASSERTIVIDADE (0 a 100%)
                Estime visualmente a taxa de assertividade desta estratégia específica considerando as últimas 10 a 20 velas visíveis no print. 

                REGRA DE TEMPO CRUCIAL:
                O usuário quer um horário de clique entre 2 a 5 minutos para frente em relação ao horário atual do print, mas a operação deve expirar na MESMA vela do clique (expiração de exatamente 1 minuto).
                Exemplo: Se o print mostra 15:30 e a estrutura gráfica se confirmará em 3 minutos, determine a Entrada para as 15:33:00 e o Fechamento para as 15:34:00.

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo:

                ⚖️ TIPO DE MERCADO IDENTIFICADO: [MERCADO ABERTO / OTC]
                📈 COMPORTAMENTO DO MERCADO: [ALTA / BAIXA / LATERAL]
                🎯 TAXA DE ASSERTIVIDADE DO PADRÃO: [Defina um valor exato de 0% a 100% com base no histórico visual]

                ⚙️ PARÂMETROS OPERACIONAIS RECOMENDADOS:
                - Payout Mínimo Sugerido: [Se Aberto: 75% | Se OTC: 85%]
                - Gestão de Risco: [Se Aberto: Mão Padrão/Soros | Se OTC: Reduzir valor do clique pela metade / Dividir em taxas]
                - Filtro de Notícias: [Se Aberto: Ativo (Evitar notícias 3 touros) | Se OTC: Inativo (Ignora macroeconomia)]

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [Defina o horário HH:MM:00 exato no futuro, entre 2 a 5 minutos à frente do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [Calcule o horário exato que a vela do clique termina, ex: HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]

                🧠 ESTRATÉGIA PROJETADA: [FLUXO DE VELA ou REVERSÃO DE TENDÊNCIA / PADRÃO ALGORÍTMICO]
                📊 JUSTIFICATIVA DA PROJEÇÃO: Explique resumidamente o porquê do tempo de projeção e valide as ações de acordo com o tipo de mercado identificado (Aberto ou OTC).

                Seja cirúrgico, rápido e extremamente direto na resposta.
                """
                
                try:
                    # Uso do método atualizado da biblioteca google-genai
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
