import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção de Entrada Futura (2 a 6 Candles) com Expiração Rígida para Fechamento na Mesma Vela de M1 e Contexto Puro de Mercado.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição do Prompt Mestre com Alinhamento à Tendência Majoritária por Contexto Puro (Sem Médias Móveis)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (Gráficos de M1). "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E ALINHAMENTO MANDATÓRIO À TENDÊNCIA MAJORITÁRIA DO MERCADO POR CONTEXTO DE PRICE ACTION PURO.\n\n"
    
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO MÁXIMA ÀS REGRAS DE TEMPO (JANELA REDUZIDA):\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule milimetricamente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura estritamente entre **2 a no máximo 6 minutos à frente** (equivalente a uma distância de apenas 2 a 6 candles de M1 após o momento do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. Portanto, o Tempo de Expiração deve ser fixado estritamente em '1 Minuto' (ou para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    
    "[MECÂNICA CORE: ALGORITMO DE CONTEXTO E GEOMETRIA DAS VELAS]\n"
    "Mapeie o histórico recente de velas exibido no print ignorando qualquer linha de indicador técnico. Foque apenas no comportamento do preço:\n"
    "1. FILTRO DE TENDÊNCIA POR CONTEXTO: Identifique a tendência majoritária através da estrutura anatômica do gráfico. Se o mercado constrói Topos e Fundos Ascendentes com sequências de blocos de velas compradoras expressivas, a tendência é de ALTA (Priorize COMPRA). Se constrói Topos e Fundos Descendentes com sequências de blocos de velas vendedoras expressivas, a tendência é de BAIXA (Priorize VENDA).\n"
    "2. RASTREIO VISUAL DE REGIÕES DE PAVIOS: Localize faixas horizontais de preço onde os candles anteriores deixaram longos pavios (sombras), comprovando rejeição de preço e forte zona de interesse ou reversão no passado recente.\n"
    "3. ANATOMIA DO CORPO DO CANDLE (EXAUSTÃO OU IMPULSÃO): Avalie o tamanho relativo dos corpos. Se os candles estão crescendo em direção ao fluxo, indica força e impulsão. Se os corpos estão encolhendo drasticamente ao atingir uma região de pavios anterior, indica perda de pressão (exaustão).\n\n"
    
    "[MATRIZ DE DECISÃO HÍBRIDA: TENDÊNCIA DO FLUXO VS RETRAÇÃO EM REGIÃO]\n"
    "Analise o comportamento do preço atual e defina a estratégia com base nestes dois cenários de Price Action:\n"
    "CENÁRIO A - OPERACIONAL DE FLUXO E SEGUIMENTO DE TENDÊNCIA: Se você identificar uma sequência forte de velas da mesma cor, com corpos firmes que romperam zonas recentes e estão livres de barreiras visíveis imediatas, projete a entrada a favor da continuidade dessa força estrutural.\n"
    "CENÁRIO B - OPERACIONAL DE PULLBACK DA TENDÊNCIA MAJORITÁRIA: Se o preço estiver fazendo uma correção temporária (velas contra a tendência principal do gráfico), mas estiver buscando o teste de uma região de suporte/resistência anterior (onde o gráfico já deixou pavios marcantes ou travas de corpos), mude a análise. Projete o clique de entrada a favor do repique da tendência principal no exato momento do toque dentro da janela de 2 a 6 candles. ENTRADAS EM CONTRA-TENDÊNCIA PURA SÃO PROIBIDAS.\n\n"
    
    "[CRITÉRIOS RIGOROSOS DE REJEIÇÃO - QUANDO ABORTAR A OPERAÇÃO]\n"
    "Você deve MARCAR A DIREÇÃO COMO 'OPERAÇÃO ABORTADA' e zerar a assertividade se identificar qualquer um destes sinais de alerta no print:\n"
    "1. MERCADO EM ACUMULAÇÃO/LATERALIZAÇÃO TRANCADA: Se o gráfico apresentar velas picadas, alternando cores constantemente sem nenhuma direção ou estrutura definida de topos e fundos. REJEIÇÃO IMEDIATA.\n"
    "2. VELAS DE ANOMALIA (NOTÍCIAS): Velas gigantescas desproporcionais (3 a 5 vezes maiores que a média do gráfico) que rasgam as regiões sem deixar pavios de retração.\n"
    "3. VELAS MARUBOZU (FORÇA SECA COM CORTE DE REGIÃO): Velas cheias sem pavio nenhum que engolfam e cruzam uma região de interesse contra a sua projeção, demonstrando fluxo institucional imparável.\n"
    "4. AUSÊNCIA DE MAPEAMENTO HISTÓRICO: Se a região para onde o preço caminha não apresentar um histórico nítido e visível de pavios ou paradas no print, a operação está proibida.\n\n"
    
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    
    "[PASSO 2: DETERMINAÇÃO DO CONTEXTO DO MERCADO]\n"
    "Avalie a estrutura pura do preço. O mercado está em fluxo de Alta, fluxo de Baixa ou Consolidação? Descreva a anatomia dos últimos 5 a 10 candles.\n\n"
    
    "[PASSO 3: APLICAÇÃO DOS CRITÉRIOS DE REJEIÇÃO]\n"
    "Valide rigorosamente se as velas atuais violam alguma das 4 regras de rejeição estipuladas.\n\n"
    
    "[PASSO 4: PROTOCOLO DE FILTRO DE CONTRA-TENDÊNCIA]\n"
    "Bloqueie qualquer clique que sugira operar contra a força dominante do contexto do mercado ou que estoure o limite máximo de 6 candles futuros.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande ou '0%' se abortada]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 6 minutos para o futuro pós-print, ou 'N/A' se abortada]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique, ou 'N/A' se abortada)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique, ou 'N/A' se abortada]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓORA]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos permitidos: 'OPERACIONAL DE FLUXO E SEGUIMENTO DE TENDÊNCIA', 'OPERACIONAL DE PULLBACK DA TENDÊNCIA MAJORITÁRIA' ou 'OPERAÇÃO ABORTADA').\n"
    "- Gatilho específico acionado (Ex: 'Velas de correção buscando região de pavios anteriores a favor do contexto de alta' ou 'Rompimento confirmado de topo anterior com velas de impulsão livres').\n"
    "- Descrição minuciosa da combinação (Retração em zona de pavios, Continuidade de fluxo estrutural, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Estrutura Pura de Preço Detectada]\n"
    "📊 JUSTIFICATIVA DA REGIÃO, BUSCA E PROJEÇÃO TEMPORAL: [Explique detalhadamente o mapeamento do contexto atual, o cálculo de deslocamento de 2 a 6 candles estimados até o ponto do clique de entrada, a densidade das regiões de pavios identificadas, e por que a expiração foi fixada para o fechamento da mesma vela de M1]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Contexto Geral e Direção Estrutural do Preço (Topos e Fundos)\n"
    "- Regiões de Pavios e Suportes/Resistências Mapeados no Histórico\n"
    "- Análise de Filtros de Rejeição (Mercado em acumulação severa? Velas de Anomalia presentes? Projeção fora do limite de 6 candles?)\n"
    "- Trajetória e Contagem de Candles pós-Print até a Zona Alvo da Operação\n"
    "- Densidade e Comportamento dos Pavios de Rejeição Identificados\n"
    "- Comportamento de Volume e Sustentação dos Corpos (Impulsão vs Exaustão)\n"
    "- Verificação de Bloqueios de Operações em Contra-Tendência\n"
    "- Gestão de Lote sob Frieza Máxima\n"
)

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    try:
        client = genai.Client(api_key=chave_api)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[imagem_objeto, prompt_comando]
        )
        return response.text
    except Exception as e:
        return f"❌ Erro ao processar com a chave atual: {str(e)}"

# 4. Interface Principal
uploaded_file = st.file_uploader("📷 Faça o upload do Print do Gráfico de M1", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
    
    if st.button("🚀 Iniciar Análise de Tendência Suprema"):
        if not lista_de_chaves:
            st.error("⚠️ Forneça pelo menos uma Gemini API Key na barra lateral para continuar.")
        else:
            sucesso = False
            progresso = st.progress(0)
            
            for i, chave in enumerate(lista_de_chaves):
                st.info(f"Tentando executar com a chave de contingência {i+1}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER)
                
                if "❌ Erro ao processar" not in resultado:
                    st.success(f"Análise concluída com sucesso usando a chave {i+1}!")
                    st.markdown(resultado)
                    sucesso = True
                    progresso.progress(100)
                    break
                
