import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from datetime import datetime

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado e Volatilidade Automática.")

# ==============================================================================
# 2. BARRA LATERAL - GERENCIAMENTO DE CHAVES COM CONTINGÊNCIA
# ==============================================================================
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")

# Gera uma lista limpa eliminando espaços e itens vazios
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

if lista_de_chaves:
    st.sidebar.success(f"🔗 {len(lista_de_chaves)} chave(s) de contingência carregada(s)!")
else:
    st.sidebar.warning("⚠️ Insira pelo menos uma API Key válida para operar.")

# ==============================================================================
# 3. INTERFACE PRINCIPAL DE INPUTS
# ==============================================================================
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Exibe o preview da imagem carregada para o usuário
    imagem_carregada = Image.open(uploaded_file)
    st.image(imagem_carregada, caption="Gráfico Carregado com Sucesso", use_container_width=True)

horario_atual_print = st.time_input("⏰ Que horas o print foi tirado no gráfico?", datetime.now().time())

st.markdown("##### 🌐 Tipo de Mercado do Ativo Atual")
tipo_mercado_selecionado = st.radio(
    "Selecione o tipo de mercado do par que você está operando agora:",
    ("Mercado Aberto (Regular / Forex)", "Mercado OTC (Algoritmo da Corretora)"),
    index=1  # Padrão inicia em OTC
)

st.markdown("##### 📐 Calibrador de Precisão Geométrica")
preco_atual_tela = st.number_input("Preço atual do mercado na tela (Ex: 1.08532):", format="%.5f", value=0.00000)

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# ==============================================================================
# 4. DEFINIÇÃO DO PROMPT MESTRE OTIMIZADO
# ==============================================================================
def gerar_prompt_mestre(horario_referencia, preco_referencia, escolha_mercado):
    preco_texto = f"{preco_referencia:.5f}" if preco_referencia > 0 else "Não informado pelo usuário (leia estritamente do eixo vertical direito do print)"
    
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

    return f"""[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro.
Sua postura é de ceticismo extremo, frieza matemática e foco absoluto em proteção de capital.
CONTEXTO DO DIA ATUAL: {tipo_mercado}.

[ANCORAGEM TEMPORAL E ESPACIAL OBRIGATÓRIA]
- O horário exato em que este print foi capturado é: {horario_referencia.strftime('%H:%M:%S')}.
- O preço de referência do último candle atual na tela é: {preco_texto}.
Qualquer cálculo de projeção de tempo futuro DEVE usar este horário exato como ponto de partida inicial zero (Candle 0).

[DIRETRIZ CRÍTICA DE FILTRAGEM BASEADA NO TIPO DE MERCADO]
{diretriz_comportamento}

[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO AUTOMÁTICO]
Antes de qualquer cálculo de taxa, você deve fazer uma varredura visual profunda na imagem para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada:
1. Identifique a macro-tendência visual da tela (Alta, Baixa ou Lateralização Absoluta).
2. Identifique a estrutura de pressão (se os compradores ou vendedores dominam o deslocamento atual).
3. Avalie o estado da volatilidade: 'Notícia/Anormalidade' (velas gigantescas e sem pavio), 'Mercado Parado/Lateral' (velas minúsculas sem deslocamento) ou 'Volatilidade Saudável' (velas com tamanho proporcional que deixam pavios de retração claros).
4. Use esse diagnóstico para calibrar o tamanho da projeção futura e expor o resultado na linha '📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA'.

[OBJETIVO OPERACIONAL: PROJEÇÃO PARA 2 A 7 CANDLES FUTUROS EM M1]
O usuário opera em gráficos de 1 minuto (M1). O objetivo NÃO É operar na próxima vela imediatamente sem critério.
Você deve olhar para o lado direito da tela (o espaço vazio para onde o preço vai se mover) e calcular a trajetória do preço para os próximos 2 a 7 minutos (2 a 7 candles à frente).
Sua missão é identificar um GATILHO OPERACIONAL exato baseado em uma das três estratégias abaixo, aplicando estritamente o tempo de expiração correto para cada uma delas para evitar perdas por milissegundos.

[MATRIZ DE ESTRATÉGIAS PERMITIDAS - SELECIONE A IDEAL PARA O CONTEXTO]
1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver volatilidade saudável com velas deixando muitos pavios recentes. Identifique a taxa de colisão forte onde o preço baterá e deixará pavio na mesma vela. (Para esta estratégia, a expiração DEVE ser para a MESMA VELA do toque).
2. REVERSÃO EM REGIÃO FORTE RESPEITADA: Ative se o preço estiver perdendo força e se aproximando de uma zona forte de Oferta/Demanda ou suporte/resistência macro que foi muito respeitada no passado do print. (Para esta estratégia, a expiração DEVE ser para a PRÓXIMA VELA, dando +1 minuto de respiro para a virada de cor).
3. FLUXO DE VELA / MOMENTUM FORTE (MOVIMENTO TRATOR): Ative se notar velas sequenciais de força (corpos grandes, sem pavio contra, volume visual crescente) indo em direção a uma zona de Oferta/Demanda. Se identificar que o movimento é um 'Trator Institucional' com alta probabilidade de rompimento e ainda houver espaço vazio (vácuo) até o alvo principal, emita uma ordem de FLUXO. Pegue a continuidade surfando a favor da força do movimento atual. (Para esta estratégia, a expiração DEVE ser para a PRÓXIMA VELA para surfar o corpo cheio do momentum seguinte).

[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]
Você está TERMINANTEMENTE PROIBIDO de basear suas decisões em nomenclaturas de velas isoladas (como Martelo, Engolfo, Doji, etc.). Ignore nomes de velas. Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, topos/fundos majoritários, canais (LTA/LTB), zonas de simetria e o espaço vazio que o preço tem para correr.

[DIRETRIZ DE SEGURANÇA E FILTRO DE CONFIANÇA CRUZADA]
- TRAVA DE EXAUSTÃO VISUAL NO FLUXO: Avalie o tamanho do candle de força atual. Se o corpo do candle atual for visualmente discrepante e desproporcional (cerca de 80% ou mais maior do que o tamanho médio dos últimos 5 candles anteriores) e estiver colidindo diretamente com o núcleo de uma região forte de Oferta/Demanda institucional sem espaço vácuo para continuar, ordene o ABORTO por risco crítico de exaustão imediata e reversão abrupta. Não compre topo nem venda fundo de velas esticadas.
- Se escolher Reversão/Retração, ma s o preço estiver em Movimento Trator saudável (velas de tamanho padrão e sequenciais) sem deixar pavios contrários significativos, priorize o fluxo e aborte contra-tendências precoces.
- Responda sempre em um formato limpo, direto, objetivo e estruturado por tópicos."""

# ==============================================================================
# 5. EXECUÇÃO DA ANÁLISE COM CHAMADA À API DO GEMINI
# ==============================================================================
if botao_analise:
    # Validações Iniciais
    if not lista_de_chaves:
        st.error("❌ Erro: Nenhuma chave de API fornecida na barra lateral.")
    elif not uploaded_file:
        st.error("❌ Erro: Por favor, faça o upload de uma imagem do gráfico antes de iniciar.")
    else:
        # Prepara os inputs para a análise
        prompt_final = gerar_prompt_mestre(horario_atual_print, preco_atual_tela, tipo_mercado_selecionado)
        imagem_operacao = Image.open(uploaded_file)
        
        sucesso = False
        
        # Loop de contingência automática pelas chaves disponíveis
        for i, api_key in enumerate(lista_de_chaves):
            try:
                with st.spinner(f"🧠 Analisando estrutura com a Chave [{i+1}]... Aguarde."):
                    # Inicialização do cliente usando a SDK oficial correta (google-genai)
                    client = genai.Client(api_key=api_key)
                    
