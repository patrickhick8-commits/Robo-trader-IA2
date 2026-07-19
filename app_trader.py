import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado e Volatilidade Automática.")

# 2. Barra Lateral - Apenas Gerenciamento de Chaves
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# Exibe feedback visual sobre o carregamento das chaves na barra lateral
if lista_de_chaves:
    st.sidebar.success(f"✔️ {len(lista_de_chaves)} chave(s) carregada(s) com sucesso!")
else:
    st.sidebar.warning("⚠️ Nenhuma chave carregada ainda.")

# 3. Interface Principal de Inputs (100% Automática)
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

# SELETOR DE MERCADO INDEPENDENTE DO DIA DA SEMANA
st.markdown("##### 🌐 Tipo de Mercado do Ativo Atual")
tipo_mercado_selecionado = st.radio(
    "Selecione o tipo de mercado do par que você está operando agora:",
    ("Mercado Aberto (Regular / Forex)", "Mercado OTC (Algoritmo da Corretora)"),
    index=1  # Padrão inicia em OTC
)

st.markdown("---")
botao_analise = st.button("🧠 Iniciar Análise Avançada por IA", use_container_width=True)

# 4. Definição do Prompt Mestre com Escaneamento Visual Automático
def gerar_prompt_mestre(escolha_mercado):
    # DIRECIONAMENTO INJETADO BASEADO NA ESCOLHA DO USUÁRIO
    if "OTC" in escolha_mercado:
        tipo_mercado = "MERCADO OTC (Over-The-Counter)"
        diretriz_comportamento = (
            "- ESTAMOS EM MERCADO OTC: O gráfico é gerado por algoritmos internos da corretora.\n"
            "- Padrões clássicos de price action falham muito aqui. O OTC adora tendências longas e movimentos direcionais contínuos.\n"
            "- Dê extrema prioridade para a estratégia de FLUXO DE VELA (MOVIMENTO TRATOR) caso note sequências de velas da mesma cor, "
            "pois o algoritmo do OTC tende a manter o fluxo até capturar a liquidez das massas. Só ordene retração se a região macro for absurdamente isolada e forte."
        )
    else:
        tipo_mercado = "MERCADO ABERTO (Regular/Forex)"
        diretriz_comportamento = (
            "- ESTAMOS EM MERCADO ABERTO: O gráfico reflete a liquidez global de grandes bancos e players reais.\n"
            "- Regiões de suporte, resistência, canais (LTA/LTB) e simetrias são respeitados com rigidez.\n"
            "- Dê alta prioridade para estratégias de RETRAÇÃO EM TAXA FUTURA e REVERSÃO EM REGIÃO FORTE, "
            "pois o mercado aberto tende a respeitar o esgotamento natural do preço ao colidir em barreiras institucionais."
        )

    # Estruturação por linhas para evitar que o interpretador Python corte o final do prompt
    linhas_prompt = [
        f"[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro.",
        f"Sua postura é de ceticismo extremo, frieza matemática e foco absoluto em proteção de capital.",
        f"CONTEXTO DO DIA ATUAL: {tipo_mercado}.\n",
        
        "[PROTOCOLO OBRIGATÓRIO DE ESCANEAMENTO OCR E GEOMETRIA GRÁFICA]",
        "Antes de analisar a estrutura técnica, você deve fazer uma leitura de dados na imagem:",
        "1. CALIBRADOR DE PRECISÃO GEOMÉTRICA AUTOMÁTICO: Localize o eixo vertical direito do gráfico. Identifique visualmente qual é o preço/taxa da última vela (candle atual). Utilize este valor exato como sua referência espacial de preço zero.","2. ANCORAGEM TEMPORAL AUTOMÁTICA: Procure no print (seja no rodapé do gráfico, no relógio da plataforma ou no eixo de tempo inferior) o horário exato em que a imagem foi gerada. Se você localizar um horário como por exemplo '23:10', assuma este valor como seu ponto de partida de tempo zero (Candle 0).",
        "Qualquer cálculo de projeção de tempo futuro DEVE usar este horário extraído visualmente como base cronológica inicial.\n",
        
        "[DIRETRIZ CRÍTICA DE FILTRAGEM BASEADA NO TIPO DE MERCADO]",
        f"{diretriz_comportamento}\n",
        
        "[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO AUTOMÁTICO]",
        "Faça uma varredura visual profunda na imagem para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada:",
        "1. Identifique a macro-tendência visual da tela (Alta, Baixa ou Lateralização Absoluta).",
        "2. Identifique a estrutura de pressão (se os compradores ou vendedores dominam o deslocamento atual).",
        "3. Avalie o estado da volatilidade: 'Notícia/Anormalidade' (velas gigantescas e sem pavio), 'Mercado Parado/Lateral' (velas minúsculas sem deslocamento) ou 'Volatilidade Saudável' (velas com tamanho proporcional que deixam pavios de retração claros).",
        "4. Use esse diagnóstico para calibrar o tamanho da projeção futura e expor o resultado na linha '📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA'.\n",
        
        "[OBJETIVO OPERACIONAL: PROJEÇÃO PARA 2 A 7 CANDLES FUTUROS EM M1]",
        "O usuário opera em gráficos de 1 minuto (M1). O objetivo NÃO É operar na próxima vela imediatamente sem critério.",
        "Você deve olhar para o lado direito da tela (o espaço vazio para onde o preço vai se mover) e calcular a trajetória do preço para os próximos 2 a 7 minutos (2 a 7 candles à frente).",
        "Sua missão é identificar um GATILHO OPERACIONAL exato baseado em uma das três estratégias abaixo, aplicando estritamente o tempo de expiração correto para cada uma delas para evitar perdas por milissegundos.\n",
        
        "[MATRIZ DE ESTRATÉGIAS PERMITIDAS - SELECIONE A IDEAL PARA O CONTEXTO]",
        "1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver volatilidade saudável com velas deixando muitos pavios recentes. Identifique a taxa de colisão forte onde o preço baterá e deixará pavio na mesma vela. (Para esta estratégia, a expiração DEVE ser para a MESMA VELA do toque).",
        "2. REVERSÃO EM REGIÃO FORTE RESPEITADA: Ative se o preço estiver perdendo força e se aproximando de uma zona forte de Oferta/Demanda ou suporte/resistência macro que foi muito respeitada no passado do print. (Para esta estratégia, a expiração DEVE ser para a PRÓXIMA VELA, dando +1 minuto de respiro para a virada de cor).",
        "3. FLUXO DE VELA / MOMENTUM FORTE (MOVIMENTO TRATOR): Ative se notar velas sequenciais de força (corpos grandes, sem pavio contra, volume visual crescente) indo em direção a uma zona de Oferta/Demanda. Se identificar que o movimento é um 'Trator Institucional' com alta probabilidade de rompimento e ainda houver espaço vazio (vácuo) até o alvo principal, emita uma ordem de FLUXO. Pegue a continuidade surfando a favor da força do movimento atual. (Para esta estratégia, a expiração DEVE ser para a PRÓXIMA VELA para surfar o corpo cheio do momentum seguinte).\n",
        
        "[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]",
        "Você está TERMINANTEMENTE PROIBIDO de basear suas decisões em nomenclaturas de velas isoladas (como Martelo, Engolfo, Doji, etc.). Ignore nomes de velas. Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, topos/fundos majoritários, canais (LTA/LTB), zonas de simetria e o espaço vazio que o preço tem para correr.\n",v
