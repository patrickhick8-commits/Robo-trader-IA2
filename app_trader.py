import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado e Volatilidade Automática.")

# 2. Barra Lateral - Gerenciamento de Chaves
st.sidebar.markdown("### 🔑 Configuração da API")
api_key = st.sidebar.text_input("Insira sua Gemini API Key:", type="password")

# 3. Interface Principal de Inputs
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

st.markdown("##### 🌐 Calibração do Ambiente de Negociação")
tipo_mercado = st.radio(
    "Selecione o tipo de mercado atual:",
    ["Mercado Aberto (Real/Macro)", "Mercado OTC (Algoritmo da Corretora)"],
    help="O mercado OTC opera sob algoritmos proprietários, enquanto o aberto segue fluxo interbancário e notícias."
)

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 4. Prompt Mestre Otimizado
def gerar_prompt_mestre(contexto_mercado):
    return f"""
[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro. Sua postura é de ceticismo extremo, frieza matemática e foco absolutista em proteção de capital.

[DETECÇÃO VISUAL OBRIGATÓRIA - AUTO EXTRAÇÃO]
Antes de processar qualquer estratégia, você deve analisar minuciosamente os eixos e elementos visuais da imagem para extrair:
1. HORÁRIO DO PRINT: Localize o relógio da plataforma (geralmente nos cantos ou no eixo horizontal inferior) e determine o horário aproximado do último candle.
2. PREÇO ATUAL DA TELA: Localize a linha de cotação atual ou o eixo vertical direito para identificar o preço aproximado em andamento.
Se os números estiverem muito pequenos ou pixelados, faça uma estimativa lógica e madura baseada na posição do preço atual em relação às taxas visíveis. Jamais deixe esses campos em branco.

[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO]
Faça uma varredura visual profunda na imagem enviada para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada:
1. Identifique a macro-tendência visual da tela (Alta, Baixa ou Lateralização).
2. Identifique a estrutura de pressão (compradores ou vendedores dominando o deslocamento atual).
3. Avalie o estado da volatilidade: 'Notícia/Anormalidade' (velas gigantescas e sem pavio), 'Mercado Parado/Lateral' (velas minúsculas sem deslocamento) ou 'Volatilidade Saudável' (velas proporcionais com pavios de retração claros).
4. O usuário parametrizou o ambiente de trading atual como: {contexto_mercado}.

[OBJETIVO OPERACIONAL: PROJEÇÃO PARA 2 A 7 CANDLES FUTUROS EM M1]
O usuário opera em gráficos de 1 minuto (M1). Avalie o comportamento do preço próximo às regiões visuais do gráfico. 
Sua missão é identificar se há um GATILHO OPERACIONAL válido baseado em uma das três estratégias abaixo:
1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver volatilidade saudável com pavios longos recentes.
2. REVERSÃO EM REGIÃO FORTE: Ative se o preço estiver perdendo força (velas diminuindo de tamanho) ao se aproximar de Suporte/Resistência ou Zonas de Oferta/Demanda evidentes.
3. FLUXO DE VELA / MOMENTUM (MOVIMENTO TRATOR): Ative se notar velas sequenciais de força (corpos grandes, sem pavio contra) indo em direção a uma zona, indicando alta probabilidade de rompimento. Pegue a continuidade.

[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]
Ignore completamente nomenclaturas de velas isoladas (Martelo, Engolfo, Doji, etc.). Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, topos/fundos majoritários, canais (LTA/LTB) e o espaço vazio que o preço tem para correr.

[DIRETRIZ DE SEGURANÇA E FILTROS DE RISCO]
- Em Mercado OTC: Ignore lógica macroeconômica. Redobre o ceticismo em suporte/resistência saturados (mais de 3 toques). Prefira micro-tendências e fluxos curtos.
- Em Mercado Aberto: Velas desproporcionais e picos isolados podem indicar notícias. Ordene o ABORTO por segurança se o gráfico estiver caótico.
- Se o preço estiver esticado e colado em cima de uma região forte sem espaço para se mover, ordene o ABORTO por risco de exaustão imediata.

Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):

📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Descreva em poucas palavras o cenário visual de tendência e volatilidade]
⏰ HORÁRIO DO PRINT DETECTADO AUTOMATICAMENTE: [Indique o horário aproximado extraído visualmente da imagem, ex: 14:32:05]
📈 PREÇO ATUAL DA TELA DETECTADO AUTOMATICAMENTE: [Indique o preço aproximado extraído visualmente do eixo, ex: 1.09432]
🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO OCULTO / ABORTAR OPERAÇÃO]
📊 TAXA DE ACERTO ESTIMADA: [Se o veredito for de entrada, forneça uma estimativa estatística de assertividade de 0% a 100% com base nos filtros de risco mitigados. Se for abortada, coloque 0%]
⏱️ HORÁRIO ESTIMADO DA ENTRADA (GATILHO): [Calcule o minuto futuro aproximado do toque/clique baseado no horário detectado no print e na distância visual até a região, ex: 14:35:00]
🧠 TIPO DE OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE', 'FLUXO DE VELA / MOMENTUM' ou 'NENHUM - OPERAÇÃO ABORTADA']
🎯 TAXA GATILHO DA OPERAÇÃO: [Com base no preço que você detectou na tela, determine matematicamente qual o valor exato da taxa limite/gatilho para o clique ou alerta]
📝 JUSTIFICATIVA TÉCNICA E ESTRUTURAL: [Apresente uma defesa detalhada, fria e puramente baseada no Price Action do porquê tomou essa decisão, mapeando o comportamento dos players e zonas de rejeição da imagem]
"""

# 5. Execução da Análise
if botao_analise:
    if not api_key:
        st.error("Por favor, insira sua Gemini API Key na barra lateral.")
    elif not uploaded_file:
        st.error("Por favor, faça o upload do print do gráfico.")
    else:
        with st.spinner("🧠 Analisando imagem e extraindo métricas automaticamente..."):
            try:
                # Inicializa o cliente oficial da SDK do Gemini
                client = genai.Client(api_key=api_key)
                
                # Abre a imagem salva
                imagem = Image.open(uploaded_file)
                
                # Gera o prompt dinâmico
                prompt_final = gerar_prompt_mestre(tipo_mercado)
                
                # CORREÇÃO: Utilizando o endpoint correto e estável da API oficial do Google
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[imagem, prompt_final]
                )
                
                st.markdown("### 📊 Resultado da Análise Suprema")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Erro ao processar a análise: {e}")
