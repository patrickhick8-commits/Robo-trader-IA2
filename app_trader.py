import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado e Volatilidade Automática.")

# 2. Barra Lateral - Apenas Gerenciamento de Chaves
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Interface Principal de Inputs
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

st.markdown("##### 🌐 Calibração do Ambiente de Negociação")
tipo_mercado = st.radio(
    "Selecione o tipo de mercado atual:",
    ["Mercado Aberto (Real/Macro)", "Mercado OTC (Algoritmo da Corretora)"],
    help="O mercado OTC opera sob algoritmos proprietários baseados em captação de liquidez interna, enquanto o aberto segue fluxo interbancário e notícias."
)

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 4. Definição do Prompt Mestre Otimizado (Leitura Automatizada por Visão Computacional)
def gerar_prompt_mestre(contexto_mercado):
    return (
        "[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro. "
        "Sua postura é de ceticismo extremo, frieza matemática e foco absolutista em proteção de capital.\n\n"
        
        "[DETECÇÃO E ANCORAGEM VISUAL AUTOMÁTICA EM COMPUTAÇÃO GRÁFICA]\n"
        "Você deve ler a imagem enviada de ponta a ponta para extrair as seguintes métricas ocultas antes de calcular qualquer projeção:\n"
        "1. HORÁRIO DO PRINT: Localize o relógio da plataforma de trade ou os eixos do gráfico para determinar com precisão cirúrgica o horário exato da última vela gerada. Use esse tempo detectado como ponto zero inicial para projeções futuras.\n"
        "2. PREÇO ATUAL DA TELA: Localize o eixo vertical direito (escala de preço) e identifique a taxa exata da cotação do último candle fechado ou atual em andamento.\n"
        f"3. AMBIENTE DE TRADING: O usuário parametrizou o ambiente atual como: {contexto_mercado}.\n\n"
        
        "[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO AUTOMÁTICO]\n"
        "Antes de qualquer cálculo de taxa, você deve fazer uma varredura visual profunda na imagem para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada:\n"
        "1. Identifique a macro-tendência visual da tela (Alta, Baixa ou Lateralização Absoluta).\n"
        "2. Identifique a estrutura de pressão (se os compradores ou vendedores dominam o deslocamento atual).\n"
        "3. Avalie o estado da volatilidade: 'Notícia/Anormalidade' (velas gigantescas e sem pavio), 'Mercado Parado/Lateral' (velas minúsculas sem deslocamento) ou 'Volatilidade Saudável' (velas com tamanho proporcional que deixam pavios de retração claros).\n"
        "4. Use esse diagnóstico para calibrar o tamanho da projeção futura e expor o resultado na linha '📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA'.\n\n"
        
        "[OBJETIVO OPERACIONAL: PROJEÇÃO PARA 2 A 7 CANDLES FUTUROS EM M1]\n"
        "O usuário opera em gráficos de 1 minuto (M1). O objetivo NÃO É operar na próxima vela.\n"
        "Você deve olhar para o lado direito da tela (o espaço vazio para onde o preço vai se mover) e calcular a trajetória do preço para os próximos 2 a 7 minutos (2 a 7 candles à frente).\n"
        "Sua missão é identificar um GATILHO OPERACIONAL exato baseado em uma das três estratégias abaixo. "
        "A expiração da ordem deve ser para a MESMA VELA DO TOQUE OU FECHAMENTO (Operação em M1 dentro do próprio minuto futuro projetado).\n\n"
        
        "[MATRIZ DE ESTRATÉGIAS PERMITIDAS - SELECIONE A IDEAL PARA O CONTEXTO]\n"
        "1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver volatilidade saudável com velas deixando muitos pavios recentes. Identifique a taxa de colisão forte onde o preço baterá e deixará pavio na mesma vela.\n"
        "2. REVERSÃO EM REGIÃO FORTE RESPEITADA: Ative se o preço estiver perdendo força e se aproximando de uma zona forte de Oferta/Demanda ou suporte/resistência macro que foi muito respeitada no passado do print.\n"
        "3. FLUXO DE VELA / MOMENTUM FORTE (MOVIMENTO TRATOR): Ative se notar velas sequenciais de força (corpos grandes, sem pavio contra, volume visual crescente) indo em direção a uma zona de Oferta/Demanda. EM VEZ DE MANDAR ABORTAR, se você identificar que o movimento é um 'Trator Institucional' com alta probabilidade de rompimento e ainda houver espaço vazio (vácuo) até o alvo principal, emita uma ordem de FLUXO. Pegue a continuidade surfando a favor da força do movimento atual.\n\n"
        
        "[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]\n"
        "Você está TERMINANTEMENTE PROIBIDO de basear suas decisões em nomenclaturas de velas isoladas (como Martelo, Engolfo, Doji, etc.). "
        "Ignore nomes de velas. Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, "
        "topos/fundos majoritários, canais (LTA/LTB), zonas de simetria e o espaço vazio que o preço tem para correr.\n\n"
        
        "[DIRETRIZ DE SEGURANÇA, INTELIGÊNCIA DE MERCADO E FILTRO DE CONFIANÇA CRUZADA]\n"
        f"- Se o ambiente for 'Mercado OTC (Algoritmo da Corretora)', ignore completamente qualquer lógica macroeconômica. Redobre o ceticismo em zonas de suporte/resistência saturadas (mais de 3 toques), pois algoritmos de OTC tendem a romper regiões óbvias para capturar a liquidez dos varejistas. Dê preferência estrita para micro-tendências e fluxos curtos de continuidade.\n"
        f"- Se o ambiente for 'Mercado Aberto (Real/Macro)', atente-se a distorções geométricas severas e picos repentinos de volume que possam sinalizar a proximidade de notícias econômicas de alto impacto. Caso ocorra, ordene o aborto imediato por segurança estrutural.\n"
        "- Se escolher Reversão/Retração, mas o preço estiver em Movimento Trator sem deixar pavios anteriores, vire o sinal para FLUXO IMEDIATO a favor do trator, a menos que o preço já tenha colidido de forma exausta no meio da região.\n"
        "- Se escolher Fluxo, mas o preço estiver muito esticado e esmagado exatamente em cima do núcleo de uma região forte de Oferta/Demanda institucional sem espaço para andar, ordene o ABORTO por risco de exaustão imediata.\n"
        "- Se a zona alvo calculada estiver muito perto (menos de 2 candles de distância) ou muito longe (mais de 7 candles de distância), recalibre o alvo geométrico.\n"
        "- Se a volatilidade visual for caótica por notícias de impacto extremo (gaps, velas sem corpo lógico), aborte por segurança.\n\n"
        
        "Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):\n\n"
        "📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Tendência / Força / Estado da Volatilidade - Descreva em poucas palavras o cenário visual]\n"
        "⏰ HORÁRIO DO PRINT IDENTIFICADO AUTOMATICAMENTE: [Ex: Você detectou visualmente HH:MM:SS na imagem]\n"
        "📈 PREÇO ATUAL DA TELA IDENTIFICADO AUTOMATICAMENTE: [Ex: Você detectou visualmente a taxa X.XXXXX no eixo]\n"
        "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]\n"
        "🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO OCULTO / ABORTAR OPERAÇÃO]\n"
        "⚠️ DETECTADO RISCO OCULTO NA ESTRUTURA? [Sim (especifique em uma frase curta qual é o risco) / Não, estrutura totalmente limpa]\n"
        "🧠 OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE' ou 'FLUXO DE VELA / MOMENTUM (MOVIMENTO TRATOR)']\n"
        "🎯 TAXA GATILHO DA OPERAÇÃO: [Insira a taxa/preço exato calculado do eixo vertical para por o alerta ou fazer o clique na corretora]\n"
        "⏰ JANELA DE MINUTOS PREVISTA: [Ex: Entre 2 e 7 minutos após o horário detectado do print - Estimativa de clique entre HH:MM e HH:MM]\n"
        "⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto - Expiração na mesma vela M1 futura do gatilho]\n"
        "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
        "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Conservador / Moderado / Abortar]\n"
        "💡 JUSTIFICATIVA GEOMÉTRICA E ESTRUTURAL:\n- Explique detalhadamente o porquê o preço vai respeitar a taxa ou o fluxo com base no operacional escolhido, detalhando o comportamento do Movimento Trator ou o vácuo de preço na tela se essa for a escolha.\n\n"
        "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
        "- Resumo analítico do comportamento visual das massas do mercado na imagem."
    )

# 5. Execução de Chamada da API com Contingência
def ejecutar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    modelos_contingencia = ['gemini-2.5-flash', 'gemini-2.5-pro']
    for modelo in modelos_contingencia:
        try:
            client = genai.Client(api_key=chave_api)
            response = client.models.generate_content(
                model=modelo,
                contents=[imagem_objeto, prompt_comando]
            )
            return response.text
        except Exception as e:
            st.sidebar.warning(f"Falha usando o modelo {modelo} com a chave atual: {e}")
            continue
    return None

# 6. Bloco de Processamento Principal ao Clicar no Botão
if botao_analise:
    if not lista_de_chaves:
        st.error("❌ Por favor, adicione pelo menos uma Gemini API Key válida na barra lateral.")
    elif not uploaded_file:
        st.error("❌ Por favor, faça o upload de uma imagem do seu gráfico antes de iniciar.")
    else:
