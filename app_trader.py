import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção de Entrada Futura (3 a 10 Candles) com Expiração Rígida para Fechamento na Mesma Vela de M1.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição Limpa do Prompt Mestre (Sem RSI + Foco em Regiões de Pavios e Paradas + Rejeições)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (Gráficos de M1). "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
    
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO MÁXIMA ÀS REGRAS DE TEMPO:\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule milimetricamente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura entre **3 a 10 minutos à frente** (equivalente a uma distância de 3 a 10 candles de M1 após o momento do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. Portanto, o Tempo de Expiração deve ser fixado estritamente em '1 Minuto' (ou para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    
    "[MECÂNICA CORE: ALGORITMO DE BUSCA DE REGIÃO VISUAL (PRICE ACTION PURO)]\n"
    "Mapeie o histórico recente de velas exibido no print para localizar ZONAS DE INTERESSE DE REVERSÃO baseando-se estritamente em dois padrões anatômicos visuais:\n"
    "1. RASTREIO DE ZONAS COM PAVIOS DE RETRAÇÃO: Identifique regiões onde os candles anteriores deixaram longas sombras/pavios seguidos de rejeição e reversão do movimento, provando forte presença de defesa.\n"
    "2. RASTREIO DE PARADA DE CORPO (EXAUSTÃO): Identifique regiões onde os candles anteriores vinham com volume, mas perderam drasticamente o tamanho dos corpos (pararam de andar/travaram a movimentação) e mudaram a direção do gráfico nas velas seguintes.\n\n"
    
    "[CRITÉRIOS RIGOROSOS DE REJEIÇÃO - QUANDO ABORTAR A OPERAÇÃO]\n"
    "Você deve MARCAR A DIREÇÃO COMO 'OPERAÇÃO ABORTADA' e zerar a assertividade se identificar qualquer um destes sinais de alerta no print:\n"
    "1. VELAS DE FORÇA SEM PAVIO (MARUBOZU): Se o preço estiver indo em direção à zona alvo empurrado por velas grandes, cheias e sem pavio nenhum, rejeite por risco de rompimento institucional de fluxo.\n"
    "2. VELAS DE ANOMALIA (VETORES GIGANTES / NOTÍCIAS): Velas desproporcionais (3 a 5 vezes maiores que a média do gráfico) que indicam pico extremo de volatilidade. REJEIÇÃO IMEDIATA.\n"
    "3. MICRO-TENDÊNCIA INSISTENTE (VELAS TRATOR): Sequências longas de 5 ou mais velas consecutivas da mesma cor sem deixar pavio contrário relevante, indicando força que passará direto pela região.\n"
    "4. AUSÊNCIA DE MAPEAMENTO HISTÓRICO: Se a região para onde o preço está indo não tiver um histórico nítido e visível de pavios ou paradas de corpos anteriores no print, a operação está proibida.\n\n"
    
    "[GATILHO DE REVERSÃO POR EXAUSTÃO ESTICADA]\n"
    "Se o preço atual estiver se deslocando de forma saudável (com candles médios e pavios) em direção a uma região validada de retração/parada histórica, você está PROIBIDO de dar um sinal de reversão imediata no exato momento do print.\n"
    "Use essa região mapeada como um ÍMÃ: calcule quantos candles (de 3 a 10 minutos à frente) o preço levará para esticar e testar aquela zona de pavios ou de parada de corpos. Agende o HORÁRIO DO CLIQUE para o exato minuto desse teste futuro, aplicando a expiração rígida para o fechamento da mesma vela.\n\n"
    
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    
    "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
    "Identifique a tendência macro e micro e verifique o fluxo de cores atual do mercado.\n\n"
    
    "[PASSO 3: APLICAÇÃO DOS CRITÉRIOS DE REJEIÇÃO]\n"
    "Valide rigorosamente se a movimentação atual viola alguma das 4 regras de rejeição estipuladas.\n\n"
    
    "[PASSO 4: PROTOCOLO DE BLOQUEIO POR FALTA DE ALVO]\n"
    "Bloqueie reversões se os candles anteriores na região alvo forem cheios e sem histórico de pavios ou paradas, indicando rompimento iminente.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande ou '0%' se abortada]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 3 a 10 minutos para o futuro pós-print, ou 'N/A' se abortada]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique, ou 'N/A' se abortada)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique, ou 'N/A' se abortada]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos permitidos: 'OPERACIONAL DE REVERSÃO EM REGIÃO DE RETRAÇÃO', 'OPERACIONAL DE EXAUSTÃO POR PARADA DE CORPO' ou 'OPERAÇÃO ABORTADA POR CRITÉRIO DE REJEIÇÃO').\n"
    "- Detalhes dos gatilhos observados nos pavios/corpos anteriores do print ou o motivo exato da rejeição.\n"
    "- Descrição minuciosa da combinação (Exaustão com pavio, Parada de movimento com reversão, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência]\n"
    "📊 JUSTIFICATIVA DA REGIÃO, BUSCA E PROJEÇÃO TEMPORAL: [Explique detalhadamente como a região de pavios ou parada foi identificada no histórico do print, a contagem de candles faltantes até ela, e por que a expiração foi cravada para a mesma vela de M1]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Regiões de Reversão Buscadas e Mapeadas no Histórico do Print\n"
    "- Análise de Filtros de Rejeição (Velas Marubozu? Velas de Anomalia? Tendência Trator?)\n"
    "- Trajetória e Contagem de Candles pós-Print até a Zona Alvo\n"
    "- Densidade dos Pavios de Retração Localizados\n"
    "- Comportamento de Volume e Parada de Corpos Identificados\n"
    "- Verificação de Bloqueios de Rompimento\n"
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

# 4. Interface Principal (Elementos Isolados)
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

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
        with st.spinner("Analisando deslocamento de velas, regiões históricas e exaustão de retração..."):
            for i, chave in enumerate(lista_de_chaves):
                st.write(f"Tentando analisar com a chave de contingência {i+1}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER)
                
                if "❌ Erro" not in resultado:
                    st.success("Análise concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso = True
                    break
                else:
                    st.warning(f"Chave {i+1} falhou ou está instável. Tentando próxima da lista...")
            
            if not sucesso:
                st.error("Todas as chaves de contingência fornecidas falharam. Verifique as chaves na Google AI Studio.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda")
