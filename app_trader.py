import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Precisão Suprema: Operacional Único de Pullback Mecânico a Favor da Tendência. Janela Futura de 3 a 10 Candles com Expiração Rígida em M1.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição do Prompt de Altíssima Assertividade (Mecânico - Pullback a Favor da Tendência)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (Gráficos de M1). "
    "Sua postura é de FRIEZA MATEMÁTICA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA. Seu foco principal é a PRESERVAÇÃO DE CAPITAL e a eliminação de Loss por sinais falsos.\n\n"
    
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO RIGOROSA ÀS REGRAS DE TEMPO:\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule visualmente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura estritamente entre **3 a 10 minutos à frente** (distância de 3 a 10 candles de M1 após o momento exato do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. O Tempo de Expiração deve ser configurado estritamente em '1 Minuto' (para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    
    "[FILTRO DEFINITIVO ANTI-LOSS: OPERACIONAL ÚNICO DE PULLBACK DA TENDÊNCIA]\n"
    "Para eliminar os falsos sinais e os Loss seguidos, você está PROIBIDO de operar fluxos esticados ou reversões de topo/fundo contra o movimento principal. Você operará uma ÚNICA mecânica altamente assertiva:\n\n"
    
    "MECÂNICA DE FILTRAGEM DO GRÁFICO:\n"
    "1. IDENTIFICAÇÃO DA DIREÇÃO DA MASSA: Avalie o contexto dos últimos 15 candles no print. Se a estrutura constrói fundos mais altos, a tendência majoritária é de ALTA (Apenas ordens de COMPRA são permitidas). Se a estrutura constrói topos mais baixos, a tendência majoritária é de BAIXA (Apenas ordens de VENDA são permitidas).\n"
    "2. MAPEAMENTO DA ZONA DE ROMPIMENTO (A TAXA): Localize o último topo (na alta) ou fundo (na baixa) que foi rompido por candles de corpo cheio. Esta região rompida torna-se a sua linha de teste obrigatória.\n"
    "3. O GATILHO DO CLIQUE SEGURO (O PULLBACK): Projete o movimento futuro dos próximos candles. O clique de entrada só pode acontecer se o preço fizer uma correção temporária (respiro) e retornar para **tocar exatamente na zona que foi rompida anteriormente**. \n"
    "   - Se a tendência majoritária for de ALTA, você dará um clique de COMPRA quando o preço cair e testar o topo rompido (suporte).\n"
    "   - Se a tendência majoritária for de BAIXA, você dará um clique de VENDA quando o preço subir e testar o fundo rompido (resistência).\n"
    "   - Qualquer operação fora desse padrão de toque em pullback deve ser sumariamente ignorada.\n\n"
    
    "[CRITÉRIOS INEGOCIÁVEIS DE REJEIÇÃO - QUANDO ABORTAR IMEDIAMENTE]\n"
    "Se o cenário gráfico apresentar qualquer uma das anomalias abaixo, defina a direção como 'OPERAÇÃO ABORTADA' e fixe a assertividade em '0%':\n"
    "1. GRÁFICO EM ACUMULAÇÃO OU LATERALIDADE TRAVADA: Se as velas estiverem picadas, alternando cores sem sair do lugar e sem formar uma tendência clara de topos e fundos. Mercado lateral é cemitério de opções binárias. REJEIÇÃO IMEDIATA.\n"
    "2. VELAS DE FORÇA SECA (NOTÍCIA/MARUBOZU) NO TOQUE: Se o candle que estiver voltando para testar a região alvo for um vetor gigante, sem pavios, demonstrando força destrutiva que indica que vai rasgar a região em vez de respeitar o pullback. REJEIÇÃO IMEDIATA.\n"
    "3. FALTA DE HISTÓRICO VISÍVEL À ESQUERDA: Se o rompimento ocorreu em uma região vazia do print, impossibilitando calcular milimetricamente a simetria do suporte ou resistência anterior.\n"
    "4. TOQUE FORA DA JANELA TEMPORAL: Se o cálculo visual indicar que o preço precisará de mais de 10 candles ou menos de 3 candles para retornar e tocar na zona de teste.\n\n"
    
    "[FORMATO OBRIGATÓRIO DO DIAGNÓSTICO STRUCTURADO]\n"
    "Retorne o diagnóstico rigorosamente neste formato markdown limpo:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande. Só dê notas acima de 90% se a simetria do pullback for impecável. Se houver risco, aborte ou reduza para 0%]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 3 a 10 minutos para o futuro pós-print, ou 'N/A' se abortada]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique, ou 'N/A' se abortada)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique, ou 'N/A' se abortada]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS PROTEGIDO / ENTRADA FIXA / PARADA OBRIGATÓRIA se mercado confuso]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional: 'OPERACIONAL DE PULLBACK DA TENDÊNCIA MAJORITÁRIA' ou 'OPERAÇÃO ABORTADA'.\n"
    "- Gatilho específico: (Ex: 'Toque de retração no suporte do topo rompido alinhado à micro-tendência de alta').\n"
    "- Descrição detalhada da estrutura anatômica identificada.\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO: [Análise pura da tendência e comportamento dos corpos/pavios]\n"
    "📊 JUSTIFICATIVA DA REGIÃO, BUSCA E PROJEÇÃO TEMPORAL: [Explique matematicamente o ponto do rompimento, a contagem exata de 3 a 10 candles estimados até o toque na taxa e a sincronia da expiração para a mesma vela]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Direção Estrutural Predominante (Filtro Direcional de Alta/Baixa)\n"
    "- Ponto de Rompimento Mapeado e Confirmado\n"
    "- Filtragem de Proteção Anti-Loss (Verificação de velas trator ou acumulações)\n"
    "- Contagem Projetada de Candles pós-Print até o Clique\n"
    "- Comportamento de Pavios e Volume de Exaustão na Correção\n"
    "- Gestão do Lote com Frieza Máxima\n"
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
                
                st.warning(f"Chave {i+1} falhou ou está esgotada. Tentando contingência seguinte...")
            
            if not sucesso:
                st.error("🚨 Todas as chaves fornecidas falharam. Verifique os limites de cota ou a validade das chaves na Google AI Studio.")
