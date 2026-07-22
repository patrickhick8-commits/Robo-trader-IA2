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

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input(
    "Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", 
    type="password"
)
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Prompt Mestre Otimizado (Sem Alucinação Temporal e Focado em Filtros Reais)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um assistente de validação estatística e analista visual de Price Action "
    "focado em Opções Binárias. Sua função NÃO é dar sinais de entrada cronometrados com horas e minutos, "
    "mas sim atuar como um filtro de risco rigoroso para o trader humano.\n\n"
    
    "[REGRA DE SEGURANÇA CRÍTICA: PROIBIÇÃO DE ALUCINAÇÃO DE HORÁRIOS E TAXAS]\n"
    "1. Você está PROIBIDO de estipular horários exatos de relógio (como HH:MM:00) para cliques ou expirações, "
    "pois você não tem sincronia de milissegundos com o mercado real.\n"
    "2. Você está PROIBIDO de inventar porcentagens de acerto fixas (ex: 85%, 90%), pois isso gera falsa segurança. "
    "Sua classificação de viabilidade deve ser qualitativa (ALTA, MÉDIA, BAIXA ou ABORTADA).\n\n"
    
    "[DIRETRIZES DE LEITURA VISUAL]\n"
    "- TENDÊNCIA E MATRIZ DE VELAS: Avalie visualmente a força dominante dos últimos candles (corpos cheios vs. pavios longos).\n"
    "- FILTRO DE EXAUSTÃO ESTICADA: Se o preço estiver se deslocando agressivamente com velas grandes e cheias em direção a um suporte/resistência, "
    "alerte o trader que a reversão imediata é perigosa e que ele deve aguardar o travamento ou perda de ângulo da tendência.\n"
    "- COMPORTAMENTO DO RSI: Se houver um indicador RSI visível e ele estiver cruzando as linhas extremas de forma totalmente vertical/agressiva, "
    "classifique como cenário de alto risco contra a tendência imediata.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown:\n\n"
    "🚦 CLASSIFICAÇÃO DE VIABILIDADE DA OPERAÇÃO: [ALTA / MÉDIA / BAIXA / ABORTADA]\n"
    "🧠 OPERACIONAL MAIS SEGURO PARA O CENÁRIO: [Ex: Reversão por Exaustão / Retração de Pavio / Continuidade de Fluxo / Aguardar Fora do Mercado]\n"
    "⏳ DIRETRIZ DE EXPIRAÇÃO RECOMENDADA: [Defina a lógica de tempo com base no tempo de tela, ex: 'Para o fim da mesma vela (M1)', 'Para 2 a 3 velas à frente (M2/M3) após o travamento', ou 'Expiração de M5 para consolidação']\n"
    "🟥🟩 DIREÇÃO DO FLUXO PREDOMINANTE: [COMPRADOR / VENDEDOR / INDEFINIDO]\n\n"
    
    "🔍 ANÁLISE ANATÔMICA DO PRINT:\n"
    "- **Contexto Macro/Micro:** [Descreva brevemente a estrutura de mercado visível no print: tendência, lateralização ou rompimento]\n"
    "- **Comportamento das Velas Recentes:** [Análise visual se os últimos candles demonstram força de impulsão ou exaustão por pavios]\n"
    "- **Mapeamento de Regiões:** [Identifique visualmente se o preço está próximo de fundos/topos anteriores ou se está em 'vazio gráfico']\n"
    "- **Filtro de Bloqueio Ativado?:** [Sim/Não - Justifique se há perigo iminente de tomar um 'loss' por operar contra uma força institucional esticada]\n\n"
    
    "⚠️ AVISO DE GESTÃO DE RISCO:\n"
    "[Forneça uma recomendação de gerenciamento conservadora baseada estritamente na feiura ou clareza do gráfico analisado.]"
)

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    try:
        # Inicializando o cliente oficial do Google GenAI
        client = genai.Client(api_key=chave_api)
        
        # Mudança Crítica: Alterado de 'gemini-2.5-pro' para 'gemini-2.5-flash'
        # Isso garante o uso da cota gratuita e resolve o erro 429 RESOURCE_EXHAUSTED
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[imagem_objeto, prompt_comando]
        )
        return response.text
    except Exception as e:
        return f"❌ Erro da API: {str(e)}"

# 4. Interface Principal 
uploaded_file = st.file_uploader(
    "📷 Faça o upload do Print do seu Gráfico:", 
    type=["png", "jpg", "jpeg"]
)

botao_analise = st.button("🧠 Iniciar Filtro de Segurança por IA")

# 5. Execução Lógica Controlada pós-Clique
if botao_analise:
    if not uploaded_file:
        st.error("⚠️ Por favor, faça o upload de uma imagem do gráfico antes de iniciar a análise.")
    elif not lista_de_chaves:
        st.error("⚠️ Insira pelo menos uma Gemini API Key válida na barra lateral antes de analisar.")
    else:
        imagem = Image.open(uploaded_file)
        st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
        
        sucesso = False
        with st.spinner("Analisando anatomia das velas, regiões de respeito e filtros de bloqueio..."):
            for i, chave in enumerate(lista_de_chaves):
                st.write(f"Tentando analisar com a chave de contingência {i+1}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER)
                
                if "❌ Erro da API:" not in resultado:
                    st.success("Análise de risco concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso = True
                    break
                else:
                    st.error(f"Falha na Chave {i+1}:")
                    st.code(resultado)
                    st.warning("Tentando próxima chave de contingência da lista...")
            
            if not sucesso:
                st.error("Todas as chaves fornecidas falharam. Verifique suas credenciais e permissões no Google AI Studio.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda para liberar o processamento.")

