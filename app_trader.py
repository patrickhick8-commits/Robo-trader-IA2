import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1 Pro", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Adaptativa de Candlesticks")
st.write("Análise cirúrgica de Velas com Aprendizado Contínuo (Autoanálise de WIN/LOSS via Print).")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente oficial do Google
    client = genai.Client(api_key=API_KEY)

    # Inicializa a sessão de chat na memória do Streamlit para manter o aprendizado
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = client.chats.create(model="gemini-2.5-flash")
        st.session_state.ultima_analise = None
        st.session_state.mostrar_feedback = False

    # 3. Campo de Upload do Print do Gráfico para Análise
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 para análise:", type=["png", "jpg", "jpeg"], key="analise_grafico")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas e calibrando histórico de operações..."):
                
                # Prompt institucional adaptativo
                prompt = """
                [SYSTEM_ROLE] Você é um robô de trading institucional de alta performance com capacidade de autoaprendizado. Analise o gráfico atual levando em consideração TODOS os acertos (WIN) e erros (LOSS) enviados anteriormente nesta conversa para recalibrar sua assertividade de forma milimétrica.
                
                [RIGOROUS_FILTERING_PROTOCOL]
                Opere com rigor máximo. Se houver o menor ruído ou padrão similar a um LOSS anterior, classifique como [ABORTAR OPERAÇÃO - ALTO RISK]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.
                
                [ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
                1. FILTRO DE FALSO ROMPIMENTO: Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva (Marubozu).
                2. FILTRO DE FALSO PULLBACK: O pullback legítimo deve ser testado por velas de exaustão e deixar pavio de rejeição exatamente ao tocar a zona.
                3. FILTRO DE RUÍDO: Se as últimas 5 velas apresentarem alternância constante de cores ou acúmulo de Dojis, aborte.
                
                [AUTOMATIC_MARKET_ADAPTATION]
                1. MERCADO ABERTO: Priorize Suporte/Resistência, LTA/LTB, RSI 14 (exaustão em 70/30) e volume implícito.
                2. MERCADO OTC (ALGORÍTMICO): Foque no fluxo contínuo, preenchimento milimétrico de pavios anteriores e exaustão por contagem de velas.
                
                [ORDER_FLOW_&_PURE_CANDLE_VOLUME]
                - VOLUME POR CORPO: Tamanho e expansão do corpo confirmam volume institucional.
                - DEFESA POR PAVIOS: Pavios longos indicam rejeição em massa e absorção de ordens.
                
                [TIME_RULES] Projete o clique para acontecer entre 2 a 5 velas depois do print. Expiração de 1 minuto.
                
                Retorne estritamente neste formato markdown limpo:
                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 96% - EXTREMA CONFLUÊNCIA]
                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Fechamento na mesma vela)
                🏁 HORÁRIO DE FECHAMENTO: [HH:MM+1:00]
                🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                🧠 ESTRATÉGIA CORRETA APLICADA: [Ex: ALGORITMO DE FLUXO OTC]
                
                🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL:
                - Leitura de Falsos Rompimentos/Pullbacks: [Análise detalhada]
                - Filtragem de Ruído e Volume por Corpo: [Análise de fluxo]
                - Absorção e Pressão por Pavios: [O que os pavios revelaram]
                - Filtro de Segurança RSI: [Status técnico]
                Seja frio, direto e puramente matemático.
                """
                
                try:
                    # Envia a imagem e o prompt dentro da sessão de chat existente
                    response = st.session_state.chat_session.send_message(
                        message=[image, prompt]
                    )
                    st.success("Análise Avançada Concluída com Sucesso!")
                    
                    # Alerta sonoro simulado
                    st.components.v1.html('<audio autoplay src="https://google.com"></audio>', height=0)
                    
                    # Exibe o resultado na tela
                    st.markdown(response.text)
                    
                    # Salva o estado para permitir o feedback do usuário
                    st.session_state.ultima_analise = response.text
                    st.session_state.mostrar_feedback = True
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")

    # 4. Painel de Autoanálise e Aprendizado Contínuo (Aparece após a análise)
    if st.session_state.get("mostrar_feedback"):
        st.divider()
        st.subheader("🔄 Painel de Autoanálise e Recalibração da IA")
        st.write("Informe o resultado da operação e envie o print final para a IA reajustar o algoritmo interno.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🟩 REGISTRAR WIN", use_container_width=True):
                st.session_state.tipo_feedback = "WIN"
                st.session_state.abrir_upload_feedback = True
                
        with col2:
            if st.button("🟥 REGISTRAR LOSS", use_container_width=True):
                st.session_state.tipo_feedback = "LOSS"
                st.session_state.abrir_upload_feedback = True

        # Se um botão de resultado foi clicado, abre a área de upload do resultado
        if st.session_state.get("abrir_upload_feedback"):
            tipo = st.session_state.tipo_feedback
            cor = "Verde" if tipo == "WIN" else "Vermelho"
            
            st.markdown(f"### 📸 Upload do Print do **{tipo}**")
            feedback_file = st.file_uploader(f"Insira o print do resultado ({tipo}) para reajuste técnico:", type=["png", "jpg", "jpeg"], key="print_feedback")
            
            if feedback_file is not None:
                img_feedback = Image.open(feedback_file)
                st.image(img_feedback, caption=f"Print de {tipo} Carregado", use_container_width=True)
                
                if st.button(f"Confirmar Aprendizado de {tipo} 🧠"):
                    with st.spinner("IA processando o print e reajustando parâmetros de filtragem..."):
                        
                        # Construção do prompt cirúrgico de feedback para a IA se autoavaliar
                        if tipo == "LOSS":
                            prompt_feedback = """
                            [AUTOANÁLISE DE LOSS - COMANDO CRÍTICO DE RECALIBRAÇÃO]
                            O sinal anterior que você gerou resultou em um LOSS (Derrota). 
                            Estou te enviando o print do gráfico contendo o resultado final da operação falhada.
                            
                            Sua obrigação técnica agora:
                            1. Compare o gráfico da análise anterior com este print do LOSS.
                            2. Identifique exatamente onde você errou: Houve reversão inesperada? Rompimento falso que você ignorou? O RSI mentiu? O delay do relógio atrapalhou? Houve absorção oculta por pavio contra sua ordem?
                            3. Guarde esse padrão visual exato na sua memória de curto prazo desta sessão. Você está PROIBIDO de passar novos sinais que tenham essa mesma configuração de velas ou confluências fracas.
                            4. Responda com uma breve autocrítica matemática explicando qual foi o erro de leitura visual para blindar as próximas entradas.
                            """
                        else:
                            prompt_feedback = """
                            [AUTOANÁLISE DE WIN - COMANDO DE REFORÇO POSITIVO]
                            O sinal anterior que você gerou resultou em um WIN (Vitória)!
                            Estou te enviando o print do gráfico confirmando o sucesso da operação.
                            
                            Sua obrigação técnica agora:
                            1. Fixe este padrão visual na sua memória técnica desta sessão. As confluências que você utilizou (tamanho de corpo, pavio de rejeição, RSI) estavam perfeitamente calibradas.
                            2. Aumente o peso matemático desses critérios específicos de sucesso para as próximas análises.
                            3. Responda confirmando que memorizou com sucesso o padrão vencedor.
                            """
                        
                        try:
                            # Envia o print do resultado para a mesma sessão de chat da IA
                            feedback_response = st.session_state.chat_session.send_message(
                                message=[img_feedback, prompt_feedback]
                            )
                            st.success(f"Excelente! O algoritmo da IA foi reajustado com base no {tipo}!")
                            st.info(feedback_response.text)

