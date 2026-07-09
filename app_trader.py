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
                
                # Prompt calibrado especificamente para CasaTrader, Avalon, IQ Option e Pocket Option
                prompt = """
                Você é um robô de trading de alta frequência especialista em Opções Binárias no tempo gráfico de 1 minuto (M1).
                Sua missão é ler as informações do print enviado, identificar a corretora (CasaTrader, Avalon, IQ Option ou Pocket Option), detectar se o cenário é Mercado Aberto ou OTC, e calcular as métricas exatas de entrada.

                ETAPA 1: IDENTIFICAÇÃO DA PLATAFORMA E CENÁRIO (ABERTO VS OTC)
                - Identifique visualmente a corretora pelas cores, fontes ou disposição do gráfico (IQ Option possui fundo escuro cinza/azul com linhas laranjas/verdes; Pocket Option possui interface cinza escuro/azulada com painel lateral robusto; CasaTrader/Avalon seguem o padrão White Label moderno).
                - Identifique se o par possui a tag '-OTC' ou '_OTC'.
                
                REGRAS ALGORÍTMICAS POR CORRETORA (SE FOR OTC):
                1. CASATRADER / AVALON: O algoritmo foca em fluxo contínuo. Se houver 3 velas da mesma cor a favor da tendência macro, priorize FLUXO DE VELA. Evite reversões contra tendências fortes.
                2. IQ OPTION: O algoritmo busca liquidez em suportes e resistências. Espere o terceiro toque ou o falso rompimento da zona clássica antes de operar a REVERSÃO. O RSI (14) acima de 70 ou abaixo de 30 é altamente manipulado aqui; espere o RSI cruzar de volta para dentro do canal.
                3. POCKET OPTION: Mercado com alto volume de pavios. Priorize RETRAÇÃO DE M1 ou REVERSÃO se a vela anterior tiver deixado um pavio maior que 50% do corpo do candle.

                ETAPA 2: ANÁLISE DE TENDÊNCIA VISUAL
                Determine se o gráfico no print está em: ALTA, BAIXA ou LATERALIZAÇÃO.

                ETAPA 3: CÁLCULO DA TAXA DE ASSERTIVIDADE (0 a 100%)
                Estime visualmente o win rate com base nas últimas 10 a 20 velas do print para o padrão identificado.

                REGRA DE TEMPO CRUCIAL (MESMA VELA):
                Calcule um clique futuro entre 2 a 5 minutos à frente do horário do print. A expiração deve ser de exatamente 1 minuto para fechar na MESMA vela do clique.
                Exemplo: Entrada às 15:33:00 -> Fechamento às 15:34:00.

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo:

                🏢 CORRETORA DETECTADA: [CasaTrader / Avalon / IQ Option / Pocket Option / Não Identificada]
                ⚖️ TIPO DE MERCADO: [MERCADO ABERTO / OTC]
                📈 COMPORTAMENTO DO MERCADO: [ALTA / BAIXA / LATERAL]
                🎯 TAXA DE ASSERTIVIDADE DO PADRÃO: [Valor exato de 0% a 100%]

                ⚙️ PARÂMETROS OPERACIONAIS RECOMENDADOS:
                - Payout Mínimo Sugerido: [Se Aberto: 75% | Se OTC: 85%]
                - Gestão de Risco: [Se Aberto: Mão Fixa ou Soros | Se OTC (IQ/Pocket/CasaTrader): Dividir a entrada em 2 ou 3 taxas na mesma vela para proteção contra delay e volatilidade artificial]
                - Filtro de Notícias: [Se Aberto: Ativo (Evitar notícias fortes) | Se OTC: Inativo (O algoritmo ignora o mundo real)]

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 no futuro, entre 2 a 5 minutos à frente do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM+1:00 exato]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / NEUTRO]

                🧠 ESTRATÉGIA PROJETADA: [FLUXO DE VELA / REVERSÃO DE TENDÊNCIA / RETRAÇÃO DE PAVIO / PADRÃO ALGORÍTMICO]
                📊 JUSTIFICATIVA DA PROJEÇÃO: Explique de forma muito direta o motivo técnico, adaptando a resposta ao comportamento específico do algoritmo da corretora detectada no print.

                Seja cirúrgico, rápido e extremamente direto na resposta.
                """
                
                try:
                    # Executa a geração usando a API atualizada com o prompt alinhado
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
