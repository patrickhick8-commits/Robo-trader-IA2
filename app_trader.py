import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção de Entrada Futura (3 a 10 Candles) com Expiração Rígida para Fechamento na Mesma Vela de M1 e Alinhamento à Tendência Majoritária.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição do Prompt Mestre com Alinhamento à Tendência Majoritária
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (Gráficos de M1). "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E ALINHAMENTO MANDATÓRIO À TENDÊNCIA MAJORITÁRIA DO MERCADO (TREND FOLLOWING).\n\n"
    
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO MÁXIMA ÀS REGRAS DE TEMPO:\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule milimetricamente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura entre **3 a 10 minutos à frente** (equivalente a uma distância de 3 a 10 candles de M1 após o momento do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. Portanto, o Tempo de Expiração deve ser fixado estritamente em '1 Minuto' (ou para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    
    "[MECÂNICA CORE: ALGORITMO DE RASTREAMENTO DE TENDÊNCIA E PONTOS DE ENTRADA]\n"
    "Mapeie o histórico recente de velas exibido no print para localizar a direção majoritária e os pontos de conexão com o fluxo dominante:\n"
    "1. RASTREIO DA TENDÊNCIA MAJORITÁRIA (DIREÇÃO DO MERCADO): Identifique a força predominante no print através da inclinação visual das micro/macro tendências, topos e fundos ascendentes (alta) ou descendentes (baixa).\n"
    "2. RASTREIO DE ZONAS DE PULLBACK (RETRAÇÃO A FAVOR): Identifique regiões de suporte/resistência rompidos ou médias móveis visíveis onde o preço tende a corrigir temporariamente para continuar o movimento principal [1].\n"
    "3. RASTREIO DE ZONAS COM PAVIOS DE CONTINUIDADE: Localize regiões onde os candles a favor da tendência deixaram pavios de mínima (em tendência de alta) ou máxima (em tendência de baixa), provando defesa e impulsão dos blocos de ordens dominantes.\n\n"
    
    "[MATRIZ DE DECISÃO HÍBRIDA: TENDÊNCIA MAJORITÁRIA VS REVERSÕES PROIBIDAS]\n"
    "Analise o comportamento do preço atual e defina a estratégia com base nestes dois cenários:\n"
    "CENÁRIO A - FLUXO DE CONTINUIDADE DA TENDÊNCIA: Se você identificar uma sequência de velas com corpos expressivos alinhadas à tendência majoritária do print, ative o 'OPERACIONAL DE FLUXO E SEGUIMENTO DE TENDÊNCIA'. Projete a entrada para a continuação do movimento, pegando impulsão a favor da massa [1].\n"
    "CENÁRIO B - RETRAÇÃO EM PULLBACK DA TENDÊNCIA: Se o preço estiver realizando uma correção (fluxo de velas contra a tendência principal), mas estiver se APROXIMANDO de uma zona de suporte/resistência historicamente forte a favor da tendência majoritária, mude a análise para 'OPERACIONAL DE PULLBACK DA TENDÊNCIA'. Espere o toque na região e mande a ordem A FAVOR do movimento majoritário (comprando em suporte na alta, ou vendendo em resistência na baixa). OPERAÇÕES DE REVERSÃO PURA CONTRA A TENDÊNCIA PRINCIPAL SÃO ESTRITAMENTE PROIBIDAS.\n\n"
    
    "[CRITÉRIOS RIGOROSOS DE REJEIÇÃO - QUANDO ABORTAR A OPERAÇÃO]\n"
    "Você deve MARCAR A DIREÇÃO COMO 'OPERAÇÃO ABORTADA' e zerar a assertividade se identificar qualquer um destes sinais de alerta no print:\n"
    "1. EXAUSTÃO EXTREMA E PERDA DE TENDÊNCIA: O preço atinge um topo/fundo histórico sem força para romper, demonstrando lateralização travada onde não há tendência clara definida.\n"
    "2. VELAS DE ANOMALIA CONTRA O FLUXO (NOTÍCIAS): Velas desproporcionais (3 a 5 vezes maiores que a média do gráfico) que quebram o padrão estrutural da tendência majoritária de forma violenta. REJEIÇÃO IMEDIATA.\n"
    "3. SINAL CONTRÁRIO SEM CONFIRMAÇÃO (FALSO ROMPIMENTO): Velas trator que tentam reverter a tendência principal sem histórico prévio de sustentação na nova zona.\n"
    "4. AUSÊNCIA DE MAPEAMENTO HISTÓRICO: Se o print não mostrar claramente a direção macro dominante ou se o gráfico estiver em acumulação severa (velas picadas/sem direção), a operação está proibida.\n\n"
    
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    
    "[PASSO 2: DETERMINAÇÃO DA TENDÊNCIA MAJORITÁRIA]\n"
    "Avalie a estrutura de mercado atual. O mercado é predominantemente de ALTA, BAIXA ou LATERAL? Identifique o fluxo de ordens institucional/varejo dominante no print [1].\n\n"
    
    "[PASSO 3: APLICAÇÃO DOS CRITÉRIOS DE REJEIÇÃO]\n"
    "Valide rigorosamente se a movimentação atual viola alguma das 4 regras de rejeição estipuladas.\n\n"
    
    "[PASSO 4: PROTOCOLO DE FILTRO CONTRA-TENDÊNCIA]\n"
    "Bloqueie e aborte qualquer entrada que sugira operar contra a tendência majoritária, mesmo que pareça uma reversão atraente de topo ou fundo.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande ou '0%' se abortada]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 3 a 10 minutos para o futuro pós-print, ou 'N/A' se abortada]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique, ou 'N/A' se abortada)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique, ou 'N/A' se abortada]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos permitidos: 'OPERACIONAL DE FLUXO E SEGUIMENTO DE TENDÊNCIA', 'OPERACIONAL DE PULLBACK DA TENDÊNCIA MAJORITÁRIA' ou 'OPERAÇÃO ABORTADA').\n"
    "- Gatilho específico acionado (Ex: 'Correção em candle de M1 buscando suporte em macro de alta' ou 'Rompimento de pivô alinhado à tendência majoritária').\n"
    "- Descrição minuciosa da combinação (Pullback de alta, Continuidade de fluxo de baixa, Rompimento estrutural, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência Majoritária Identificada]\n"
    "📊 JUSTIFICATIVA DA REGIÃO, BUSCA E PROJEÇÃO TEMPORAL: [Explique detalhadamente o mapeamento da tendência dominante, o cálculo de candles faltantes para o clique a favor do movimento, a distância até a zona de pullback, e por que a expiração foi cravada para a mesma vela de M1]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Direção da Tendência Majoritária Detectada no Print\n"
    "- Estrutura de Topos e Fundos Recentes\n"
    "- Análise de Filtros de Rejeição (Tentativa de contra-tendência detectada? Velas de Anomalia? Vilosidade lateral?)\n"
    "- Trajetória e Contagem de Candles pós-Print até o Ponto de Entrada Futuro\n"
    "- Densidade dos Pavios de Impulsão/Continuidade Localizados\n"
    "- Comportamento de Volume e Sustentação dos Corpos\n"
    "- Verificação de Bloqueios de Contra-Tendência\n"
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
                else:
                    st.warning(f"Chave {i+1} falhou ou está esgotada. Chutando contingência seguinte...")
            
            if not sucesso:
                st.error("🚨 Todas as chaves fornecidas falharam. Verifique os limites de cota ou a validade das chaves na Google AI Studio.")
