import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(
    page_title="Agente IA Advanced - Analisador de Cenários", 
    page_icon="📊", 
    layout="centered"
)

st.title("📊 Agente IA Trader Pro: Validador de Cenários")
st.write("Análise Visual de Price Action: Filtro de Segurança, Detecção de Exaustão e Validação de Região de Respeito.")

# 2. Barra Lateral e Seleção de Modelos
st.sidebar.markdown("### 🛠️ Configurações do Sistema")
chaves_input = st.sidebar.text_input(
    "Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", 
    type="password"
)
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# Lista dinâmica de modelos disponíveis solicitada por você
modelos_disponiveis = ['gemini-3.6-flash', 'gemini-2.5-flash', 'gemini-2.0-flash']
modelo_selecionado = st.sidebar.selectbox(
    "Escolha o Modelo do Gemini:",
    options=modelos_disponiveis,
    index=0  # Define o gemini-3.6-flash como padrão inicial
)

# 3. Prompt Mestre Altamente Estruturado
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um assistente avançado de validação estatística e analista visual de Price Action "
    "focado em Opções Binárias. Sua função é analisar o print do gráfico e fornecer dados exatos de execução.\n\n"
    
    "[DIRETRIZES DE LEITURA VISUAL E HORÁRIO]\n"
    "1. Localize visualmente o relógio atual do mercado ou o tempo restante da vela no print fornecido.\n"
    "2. Determine a direção exata com base na anatomia das velas e regiões de suporte/resistência.\n"
    "3. Calcule uma taxa de assertividade estatística estimada para o padrão gráfico identificado.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown (Siga rigorosamente cada item):\n\n"
    
    "🎯 DADOS CRÍTICOS DA OPERAÇÃO:\n"
    "- **🟢 Direção da Entrada:** [Defina estritamente se é COMPRA (CALL), VENDA (PUT) ou AGUARDAR FORA DO MERCADO]\n"
    "- **📈 Taxa de Assertividade Estimada:** [Calcule uma porcentagem de 0% a 100% baseada na clareza do padrão visual analisado]\n"
    "- **⏱️ Horário Sugerido para Entrada:** [Identifique o relógio no print e estipule o gatilho, ex: 'Na abertura da próxima vela após o fechamento do candle atual de HH:MM' ou 'Ao tocar na taxa X no minuto Y']\n\n"
    
    "🧠 OPERACIONAL E TEMPO:\n"
    "- **Estratégia Aplicada:** [Ex: Reversão por Exaustão / Retração de Pavio / Continuidade de Fluxo]\n"
    "- **Tempo de Expiração:** [Ex: Para o fim da mesma vela (M1), Para 2 a 3 velas à frente (M2/M3), ou Fim da vela de M5]\n\n"
    
    "🔍 ANÁLISE ANATÔMICA DO PRINT:\n"
    "- **Contexto de Mercado:** [Descreva brevemente a estrutura visível: tendência forte, lateralização ou rompimento]\n"
    "- **Comportamento das Velas:** [Análise visual se os últimos candles demonstram força de impulsão ou exaustão por pavios]\n"
    "- **Mapeamento de Regiões:** [Identifique visualmente se o preço está próximo de fundos/topos anteriores ou em vazio gráfico]\n"
    "- **Filtro de Bloqueio Ativado?:** [Sim/Não - Justifique se há perigo iminente de tomar um 'loss' por operar contra força institucional esticada]\n\n"
    
    "⚠️ AVISO DE GESTÃO DE RISCO:\n"
    "[Forneça uma recomendação de gerenciamento conservadora baseada estritamente na feiura ou clareza do gráfico analisado.]"
)

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando, modelo_alvo):
    try:
        client = genai.Client(api_key=chave_api)
        # Nota: Parâmetros descontinuados (temperature, top_p, top_k) foram omitidos para o Gemini 3.x
        response = client.models.generate_content(
            model=modelo_alvo,
            contents=[imagem_objeto, prompt_comando]
        )
        return True, response.text
    except Exception as e:
        return False, str(e)

# 4. Interface Principal 
uploaded_file = st.file_uploader(
    "📷 Faça o upload do Print do seu Gráfico:", 
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)

botao_analise = st.button("🧠 Iniciar Filtro de Segurança por IA")

# 5. Execução Lógica Controlada pós-Clique
if botao_analise:
    if not uploaded_file:
        st.error("⚠️ Por favor, faça o upload de uma imagem do gráfico antes de iniciar a análise.")
    elif not lista_de_chaves:
        st.error("⚠️ Insira pelo menos uma Gemini API Key válida na barra lateral antes de analisar.")
    else:
        sucesso_geral = False
        with st.spinner(f"Analisando anatomia gráfica com o modelo {modelo_selecionado}..."):
            for i, chave in enumerate(lista_de_chaves):
                st.write(f"Tentando analisar com a chave de contingência {i+1}...")
                
                # Executa passando o modelo escolhido dinamicamente pelo selectbox
                sucesso, resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER, modelo_selecionado)
                
                if sucesso:
                    st.success("Análise de risco concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso_geral = True
                    break
                else:
                    st.error(f"Falha na Chave {i+1}:")
                    st.code(resultado)
                    st.warning("Tentando próxima chave de contingência da lista...")
            
            if not sucesso_geral:
                st.error("Todas as chaves fornecidas falharam. Verifique suas credenciais e permissões no Google AI Studio.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda para liberar o processamento.")
