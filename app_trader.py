import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from datetime import datetime

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
horario_atual_print = st.time_input("⏰ Que horas o print foi tirado no gráfico?", datetime.now().time())

# SELETOR DE MERCADO INDEPENDENTE DO DIA DA SEMANA
st.markdown("##### 🌐 Tipo de Mercado do Ativo Atual")
tipo_mercado_selecionado = st.radio(
    "Selecione o tipo de mercado do par que você está operando agora:",
    ("Mercado Aberto (Regular / Forex)", "Mercado OTC (Algoritmo da Corretora)"),
    index=1  # Padrão inicia em OTC
)

st.markdown("##### 📐 Calibrador de Precisão Geométrica")
preco_atual_tela = st.number_input("Preço atual do mercado na tela (Ex: 1.08532):", format="%.5f", value=0.00000)

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 4. Definição do Prompt Mestre Otimizado (Filtro de Confiança Cruzada + Adaptação Inteligente Aberto/OTC)
def gerar_prompt_mestre(horario_referencia, preco_referencia, escolha_mercado):
    preco_texto = f"{preco_referencia:.5f}" if preco_referencia > 0 else "Não informado pelo usuário (leia estritamente do eixo vertical direito do print)"
    
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

    return (
        f"[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro.\n"
        f"Sua postura é de ceticismo extremo, frieza matemática e foco absoluto em proteção de capital.\n"
        f"CONTEXTO DO DIA ATUAL: {tipo_mercado}.\n\n"
        
        f"[ANCORAGEM TEMPORAL E ESPACIAL OBRIGATÓRIA]\n"
        f"- O horário exato em que este print foi capturado é: {horario_referencia.strftime('%H:%M:%S')}.\n"
        f"- O preço de referência do último candle atual na tela é: {preco_texto}.\n""Qualquer cálculo de projeção de tempo futuro DEVE usar este horário exato como ponto de partida inicial zero (Candle 0).\n\n"
        
        "[DIRETRIZ CRÍTICA DE FILTRAGEM BASEADA NO TIPO DE MERCADO]\n"
        f"{diretriz_comportamento}\n\n"
        
        "[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO AUTOMÁTICO]\n"
        "Antes de qualquer cálculo de taxa, você deve fazer uma varredura visual profunda na imagem para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada:\n"
        "1. Identifique a macro-tendência visual da tela (Alta, Baixa ou Lateralização Absoluta).\n"
        "2. Identifique a estrutura de pressão (se os compradores ou vendedores dominam o deslocamento atual).\n"
        "3. Avalie o estado da volatilidade: 'Notícia/Anormalidade' (velas gigantescas e sem pavio), 'Mercado Parado/Lateral' (velas minúsculas sem deslocamento) ou 'Volatilidade Saudável' (velas com tamanho proporcional que deixam pavios de retração claros).\n"
        "4. Use esse diagnóstico para calibrar o tamanho da projeção futura e expor o resultado na linha '📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA'.\n\n"
        
        "[OBJETIVO OPERACIONAL: PROJEÇÃO PARA 2 A 7 CANDLES FUTUROS EM M1]\n"
        "O usuário opera em gráficos de 1 minuto (M1). O objetivo NÃO É operar na próxima vela imediatamente sem critério.\n"
        "Você deve olhar para o lado direito da tela (o espaço vazio para onde o preço vai se mover) e calcular a trajetória do preço para os próximos 2 a 7 minutos (2 a 7 candles à frente).\n"
        "Sua missão é identificar um GATILHO OPERACIONAL exato baseado em uma das três estratégias abaixo, aplicando estritamente o tempo de expiração correto para cada uma delas para evitar perdas por milissegundos.\n\n"
        
        "[MATRIZ DE ESTRATÉGIAS PERMITIDAS - SELECIONE A IDEAL PARA O CONTEXTO]\n"
        "1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver volatilidade saudável com velas deixando muitos pavios recentes. "
        "Identifique a taxa de colisão forte onde o preço baterá e deixará pavio na mesma vela. (Para esta estratégia, a expiração DEVE ser para a MESMA VELA do toque).\n"
        "2. REVERSÃO EM REGIÃO FORTE RESPEITADA: Ative se o preço estiver perdendo força e se aproximando de uma zona forte de Oferta/Demanda ou suporte/resistência macro que foi muito respeitada no passado do print. "
        "(Para esta estratégia, a expiração DEVE ser para a PRÓXIMA VELA, dando +1 minuto de respiro para a virada de cor).\n"
        "3. FLUXO DE VELA / MOMENTUM FORTE (MOVIMENTO TRATOR): Ative se notar velas sequenciais de força (corpos grandes, sem pavio contra, volume visual crescente) indo em direção a uma zona de Oferta/Demanda. "
        "Se identificar que o movimento é um 'Trator Institucional' com alta probabilidade de rompimento e ainda houver espaço vazio (vácuo) até o alvo principal, emita uma ordem de FLUXO. Pegue a continuidade surfando a favor da força do movimento atual. "
        "(Para esta estratégia, a expiração DEVE ser para a PRÓXIMA VELA para surfar o corpo cheio do momentum seguinte).\n\n"
        
        "[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]\n"
        "Você está TERMINANTEMENTE PROIBIDO de basear suas decisões em nomenclaturas de velas isoladas (como Martelo, Engolfo, Doji, etc.). "
        "Ignore nomes de velas. Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, "
        "topos/fundos majoritários, canais (LTA/LTB), zonas de simetria e o espaço vazio que o preço tem para correr.\n\n"
        
        "[DIRETRIZ DE SEGURANÇA E FILTRO DE CONFIANÇA CRUZADA]\n"
        "- TRAVA DE EXAUSTÃO VISUAL NO FLUXO: Avalie o tamanho do candle de força atual.Se o corpo do candle atual for visualmente discrepante e desproporcional (cerca de 80% ou mais maior do que o tamanho médio dos últimos 5 candles anteriores) e estiver colidindo diretamente com o núcleo de uma região forte de Oferta/Demanda institucional sem espaço vácuo para continuar, ordene o ABORTO por risco crítico de exaustão imediata e reversão abrupta. Não compre topo nem venda fundo de velas esticadas.\n"
        "- Se escolher Reversão/Retração, mas o preço estiver em Movimento Trator saudável (velas de tamanho padrão e sequenciais) sem deixar pavios anteriores, vire o sinal para FLUXO IMEDIATO a favor do trator, a menos que o preço já tenha colidido de forma exausta no meio da região.\n"
        "- Se a zona alvo calculada estiver muito perto (menos de 2 candles de distância) ou muito longe (mais de 7 candles de distância), recalibre o alvo geométrico.\n"
        "- Se a volatilidade visual for caótica por notícias de impacto extremo (gaps, velas sem corpo lógico), aborte por segurança.\n\n"
        
        "Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):\n\n"
        "📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Tendência / Força / Estado da Volatilidade - Descreva em poucas palavras o cenário visual]\n"
        "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]\n"
        "🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO OCULTO / ABORTAR OPERAÇÃO]\n"
        "⚠️ DETECTADO RISCO OCULTO NA ESTRUTURA? [Sim (especifique em uma frase curta se foi Exaustão de Vela ou outro risco) / Não, estrutura totalmente limpa]\n"
        "🧠 OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE' ou 'FLUXO DE VELA / MOMENTUM (MOVIMENTO TRATOR)']\n"
        "🎯 TAXA GATILHO DA OPERAÇÃO: [Insira a taxa/preço exato calculado do eixo vertical para por o alerta ou fazer o clique na corretora]\n"
        "⏰ JANELA DE MINUTOS PREVISTA: [Ex: Entre 2 e 7 minutos após o horário do print - Estimativa de clique entre HH:MM e HH:MM]\n"
        "⏳ TEMPO DE EXPIRAÇÃO: [Defina estritamente baseado no operacional ativo: 'Mesma vela de M1 (Retração)' ou 'Próxima vela / M1 + 1 Minuto (Reversão ou Fluxo)']\n"
        "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
