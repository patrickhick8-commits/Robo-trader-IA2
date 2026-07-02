import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema e Projeção Temporal")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

# Campo de texto para as chaves
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

def retornar_prompt():
    return (
        "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (M1). Sua postura é moderadamente agressiva: seu objetivo é extrair o máximo de sinais válidos do gráfico, operando por confluência máxima de fatores sem descartar operações por detalhes mínimos de ruído na tela.\n\n"
        "[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]\n"
        "Escaneie textualmente a imagem em busca do nome do ativo. Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
        "[PASSO 2: FILTROS DE TENDÊNCIA E POSICIONAMENTO DA EMA 9]\n"
        "Rastreie o preço com a EMA 9. COMPRA (CALL): preço acima da EMA 9. VENDA (PUT): preço abaixo da EMA 9. Use a média como suporte móvel ou imã, sem se prender ao atraso da linha.\n\n"
        "[PASSO 3: MATRIZ DE ESTRATÉGIA ADAPTATIVA MULTI-CONFLUENTE]\n"
        "1. MATRIZ DE CONTINUIDADE DE FLUXO (IMPULSO E ANATOMIA): Monitore blocos dominantes de mesma cor, aceleração rápida e velas com corpos sólidos crescentes (Marubozu). Pavios devem ser mínimos contra o movimento, indicando ausência de rejeição. Opere o preenchimento.\n"
        "2. MATRIZ DE LATERALIDADE / CONSOLIDAÇÃO HORIZONTAL: Opere o extremo respeito de zonas nítidas de Suporte (Fundo) e Resistência (Topo). O preço deve demonstrar perda de pressão e deixar pavios longos de rejeição visual para retração ou reversão na mesma vela.\n"
        "3. MATRIZ DE TENDÊNCIA E REVERSÃO: Identifique toques em canais, LTA ou LTB onde o preço deixa pavios longos. Opere a continuidade pós-reversão macro quando o mercado quebra estruturas (SMC/CHOCH) e inicia um novo ciclo de força.\n\n"
        "[PASSO 4: FILTROS ANTI-RUÍDO E MANIPULAÇÃO SUAVIZADOS]\n"
        "Aborte apenas em casos extremos: mercado em xadrez (alternância constante de cor por mais de 8 velas) ou acúmulo de Dojis seguidos (falta de liquidez). Em OTC, opere preenchimento de pavios e fluxos bem marcados.\n\n"
        "[PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]\n"
        "Avalie os riscos de forma equilibrada. Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. Só emita OPERAÇÃO ABORTADA (taxa 0%) se o gráfico estiver completamente plano e sem volume.\n\n"
        "[PASSO 6: CRONOMETRAGEM DE EXECUÇÃO PADRÃO]\n"
        "Projete o HORÁRIO DO CLIQUE para uma janela futura de 2 a 5 minutos com base no relógio do print. Expiração rígida de 1 minuto (mesma vela do clique).\n\n"
        "[PASSO 7: SUGESTÃO DE GERENCIAMENTO DE MÃO DE ENTRADA]\n"
        "Taxa 90-95%: MÃO DE SOROS. Taxa 85-89%: ENTRADA FIXA. Taxa 80-84%: MÃO LEVE. Abortada: PARADA OBRIGATÓRIA.\n\n"
        "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
        "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93%]\n"
        "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos]\n"
        "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto\n"
        "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento]\n"
        "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
        "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]\n\n"
        "🧠 ESTRATÉGIA COMBINADA ATIVADA: [Ex: CONTINUIDADE DE FLUXO POR COR E IMPULSO]\n"
        "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
        "📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / CONSOLIDAÇÃO LATERAL]\n"
        "📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique o porquê do tempo de 2 a 5 minutos]\n\n"
        "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
        "- Ambiente Identificado: [MERCADO ABERTO ou OTC]\n"
        "- Diagnóstico do Fluxo de Continuidade (Cor, Impulso e Corpo): [Análise do tamanho e cor]\n"
        "- Análise de Pavios e Pressão de Rejeição: [Comportamento de pavios]\n"
        "- Mapeamento de Zonas Horizontais (S/R) e Inclinadas (LTA/LTB): [Microzonas estruturais]\n"
        "- Posicionamento da Média Móvel (EMA 9): [Preço em relação à EMA 9]\n"
        "- Avaliação de Ruído e Volatilidade: [Justificativa dos filtros moderados]\n"
        "- Justificativa da Gestão de Lote: [Por que o lote sugerido se adequa]\n\n"
        "Seja frio, preciso e direto. Velocidade e precisão salvam bancas."
    )

def acionar_robo():
    texto_limpo = chaves_input.replace(" ", "")
    if not texto_limpo:
        st.session_state["resultado_trader"] = "ERRO: Preencha sua Gemini API Key na barra lateral esquerda!"
        return
    if "imagem_grafico" not in st.session_state:
        st.session_state["resultado_trader"] = "ERRO: Carregue o print do gráfico antes de executar!"
        return
    try:
        chave_operacional = texto_limpo.split(";").pop(0)
        client = genai.Client(api_key=chave_operacional)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[st.session_state["imagem_grafico"], retornar_prompt()]
        )
        st.session_state["resultado_trader"] = response.text
    except Exception as e:
        st.session_state["resultado_trader"] = f"ERRO_API: {str(e)}"

# --- AREA OPERACIONAL DO SITE ---
uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1:", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.session_state["imagem_grafico"] = Image.open(uploaded_file)

if "imagem_grafico" in st.session_state:
    st.image(st.session_state["imagem_grafico"], caption="Gráfico M1 Carregado para Análise", use_container_width=True)
    st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL", on_click=acionar_robo)
    
    if "resultado_trader" in st.session_state:
        if "ERRO" in st.session_state["resultado_trader"]:
            st.error(st.session_state["resultado_trader"])
        else:
            st.success("Análise Suprema de Confluência Matricial Concluída!")
            st.markdown(st.session_state["resultado_trader"])
