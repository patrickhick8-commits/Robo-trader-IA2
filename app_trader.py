import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção de Entrada Futura (2 a 6 Candles) com Expiração Rígida para Fechamento na Mesma Vela de M1 e Alinhamento à Tendência Majoritária.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição Completa do Prompt Mestre (Alinhamento à Tendência Majoritária + EMA 50 + Janela de 2 a 6 Minutos)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (Gráficos de M1). "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E ALINHAMENTO MANDATÓRIO À TENDÊNCIA MAJORITÁRIA DO MERCADO (TREND FOLLOWING).\n\n"
    
    "[CONFIGURAÇÃO TÉCNICA FIXA DO GRÁFICO]\n"
    "A linha indicadora visível sobreposta às velas no print é estritamente uma **Média Móvel Exponencial de 50 períodos (EMA 50)**. Use-a como o rastreador oficial de tendência.\n\n"
    
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO MÁXIMA ÀS REGRAS DE TEMPO (JANELA REDUZIDA):\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule milimetricamente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura estritamente entre **2 a 6 minutos à frente** (equivalente a uma distância de apenas 2 a 6 candles de M1 após o momento do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. Portanto, o Tempo de Expiração deve ser fixado estritamente em '1 Minuto' (ou para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    
    "[MECÂNICA CORE: ALGORITMO DE RASTREAMENTO POR EMA 50 E TENDÊNCIA]\n"
    "Mapeie o histórico recente de velas exibido no print usando a EMA 50 como o filtro dinâmico de direção:\n"
    "1. FILTRO DE DIREÇÃO MAJORITÁRIA: Se o preço estiver predominantemente ACIMA da EMA 50 e a linha estiver inclinada para cima, a tendência majoritária é de ALTA (Apenas operações de COMPRA são permitidas). Se o preço estiver ABAIXO da EMA 50 e a linha estiver inclinada para baixo, a tendência majoritária é de BAIXA (Apenas operações de VENDA são permitidas).\n"
    "2. RASTREIO DE GATILHOS NA EMA 50 (PULLBACK DINÂMICO): Identifique momentos em que o preço faz uma correção temporária e toca na linha da EMA 50. O toque na EMA 50 a favor da tendência atua como um forte suporte (na alta) ou resistência (na baixa) devido à defesa institucional.\n"
    "3. DEFESA POR PAVIOS NA MÉDIA: Localize se os candles que se aproximam ou tocam a EMA 50 deixam pavios de prevenção/rejeição, confirmando que a média está segurando o preço dentro da janela de tempo permitida.\n\n"
    
    "[MATRIZ DE DECISÃO HÍBRIDA: TENDÊNCIA MAJORITÁRIA VS REVERSÕES PROIBIDAS]\n"
    "Analise o comportamento do preço atual e defina a estratégia com base nestes dois cenários:\n"
    "CENÁRIO A - FLUXO DE CONTINUIDADE AFILHADO À EMA 50: Se o preço romper uma estrutura recente e estiver se distanciando da EMA 50 com velas fortes e a favor da inclinação da média, ative o 'OPERACIONAL DE FLUXO E SEGUIMENTO DE TENDÊNCIA'.\n"
    "CENÁRIO B - PULLBACK DINÂMICO NA EMA 50: Se o preço estiver corrigindo contra o movimento principal e buscando o toque na EMA 50, ative o 'OPERACIONAL DE PULLBACK DA TENDÊNCIA MAJORITÁRIA'. Projete o clique exatamente para o candle que tocará a média (calculando se o toque ocorrerá dentro de 2 a 6 candles no futuro), operando a favor do repique da tendência (COMPRA no suporte da linha em tendência de alta / VENDA na resistência da linha em tendência de baixa). REVERSÕES QUE DESAFIEM A INCLINAÇÃO DA EMA 50 SÃO PROIBIDAS.\n\n"
    
    "[CRITÉRIOS RIGOROSOS DE REJEIÇÃO - QUANDO ABORTAR A OPERAÇÃO]\n"
    "Você deve MARCAR A DIREÇÃO COMO 'OPERAÇÃO ABORTADA' e zerar a assertividade se identificar qualquer um destes sinais de alerta no print:\n"
    "1. PREÇO ENCAVALADO / EMA 50 FLAT: Se a linha da EMA 50 estiver totalmente horizontal (sem inclinação) e cruzando o corpo de várias velas seguidas, o mercado está lateralizado e sem tendência. REJEIÇÃO IMEDIATA.\n"
    "2. ROMPIMENTO EXPRESSIVO DA MÉDIA (VETOR DE INVERSÃO): Uma vela de força (Marubozu) cortando a EMA 50 contra a tendência anterior com corpo cheio e volume, sem deixar pavio de retração na média.\n"
    "3. VELAS DE ANOMALIA (NOTÍCIAS): Velas desproporcionais (3 a 5 vezes maiores que a média do gráfico) que violam a barreira da EMA 50 de forma errática.\n"
    "4. AUSÊNCIA DE ESPAÇO GRÁFICO (CONGESTIONAMENTO): Se o preço estiver colado na média sem espaço para se mover ou projetar a janela de 2 a 6 candles à frente.\n\n"
    
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    
    "[PASSO 2: DETERMINAÇÃO DA TENDÊNCIA PELA EMA 50]\n"
    "Avalie a inclinação da EMA 50 e a posição do preço em relação a ela. O viés é comprador ou vendedor? Descreva a saúde da tendência.\n\n"
    
    "[PASSO 3: APLICAÇÃO DOS CRITÉRIOS DE REJEIÇÃO]\n"
    "Valide se a EMA 50 está flat ou se há alguma violação das 4 regras de rejeição.\n\n"
    
    "[PASSO 4: PROTOCOLO DE FILTRO CONTRA-TENDÊNCIA]\n"
    "Bloqueie qualquer operação que tente adivinhar reversão de topo/fundo se o preço estiver desalinhado com a direção da EMA 50 ou se exigir mais de 6 candles para atingir o alvo.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande ou '0%' se abortada]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 6 minutos para o futuro pós-print, ou 'N/A' se abortada]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique, ou 'N/A' se abortada)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique, ou 'N/A' se abortada]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos permitidos: 'OPERACIONAL DE FLUXO E SEGUIMENTO DE TENDÊNCIA', 'OPERACIONAL DE PULLBACK NA EMA 50' ou 'OPERAÇÃO ABORTADA').\n"
    "- Gatilho específico acionado (Ex: 'Preço testando a EMA 50 como suporte em tendência macro de alta' ou 'Rompimento de pivô com inclinação positiva da EMA 50 dentro do limite de 6 velas').\n"
    "- Descrição minuciosa da combinação (Pullback dinâmico na EMA 50, Continuidade de fluxo afastado da média, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Posição e Inclinação da EMA 50]\n"
    "📊 JUSTIFICATIVA DA REGIÃO, BUSCA E PROJEÇÃO TEMPORAL: [Explique detalhadamente a inclinação da EMA 50, a contagem de 2 a 6 candles estimados até o toque/impulsão na média, e a sincronia matemática do clique com a expiração de 1 minuto para o fechamento da mesma vela]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Comportamento Visual da EMA 50 (Inclinação e Posição do Preço)\n"
    "- Estrutura de Topos e Fundos em Relação à Média\n"
    "- Análise de Filtros de Rejeição (EMA 50 flat? Velas cortando a média sem retração? Projeção estourou o limite de 6 candles?)\n"
    "- Trajetória e Contagem de Candles pós-Print até o Ponto de Entrada na Linha da EMA 50 (Alvo estrito de 2 a 6 candles)\n"
    "- Densidade dos Pavios de Defesa sobre a EMA 50\n"
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
