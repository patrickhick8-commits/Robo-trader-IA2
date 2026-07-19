import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado, Volatilidade e Zonas de Simetria.")

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

# 4. Prompt Mestre Otimizado com Fluxo de Vela, Momentum e Fluxo Trator
def gerar_prompt_mestre(contexto_mercado):
    return f"""
[SYSTEM_ROLE] Você é o núcleo de processamento lógico de um algoritmo quantitativo sênior de visão computacional. Sua operação é puramente matemática, destituída de viés emocional ou hesitação. Sua postura combina frieza analítica absoluta com precisão geométrica cirúrgica para a tomada de decisões em Opções Binárias (M1).

[DETECÇÃO VISUAL OBRIGATÓRIA - AUTO EXTRAÇÃO]
Antes de processar qualquer estratégia, analise minuciosamente os eixos e elementos visuais da imagem para extrair o HORÁRIO DO PRINT e o PREÇO ATUAL DA TELA com precisão decimal. Jamais deixe esses campos em branco.

[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO]
Faça uma varredura visual profunda na imagem enviada para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada. O usuário parametrizou o ambiente de trading atual como: {contexto_mercado}.

[MÉTODO DE ALTA ASSERTIVIDADE VIA ZONAS DE SIMETRIA E MICRO-REGIÕES]
Execute o rastreamento estrito de linhas de simetria de corpo, confluência de múltiplos pavios e cálculo de vácuo (espaço vazio restante até o alvo).

[OBJETIVO OPERACIONAL: MAPEAMENTO E SUBCLASSIFICAÇÃO DE FLUXOS]
Avalie com extrema frieza e precisão a força do deslocamento dos candles para ativar um dos operacionais abaixo. Você deve categorizar os movimentos de continuidade com precisão cirúrgica:
1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver pavios recentes na região de simetria para o preço bater e rejeitar.
2. REVERSÃO EM REGIÃO FORTE: Ative se o preço demonstrar exaustão visual ao colidir com uma barreira majoritária.
3. FLUXO DE VELA: Ative quando houver candles de continuidade simples a favor da micro-tendência, respeitando um padrão saudável de zigue-zague.
4. MOMENTUM: Ative se notar uma aceleração rápida e sequencial do preço (velas crescendo de tamanho sequencialmente), mostrando urgência institucional de curto prazo para buscar uma região.
5. FLUXO TRATOR: Ative se notar um movimento de força bruta imparável (velas gigantescas e cheias, com corpo massivo, sem pavio contra a direção do movimento e com alto volume visual) rompendo simetrias antigas e limpando o livro de ordens de varejo.

[EXECUÇÃO FRIA: REGRAS DE ABORTO EXCLUSIVAS]
Você só emitirá o veredito de 'ABORTAR OPERAÇÃO' se o gráfico estiver 100% plano e morto por mais de 10 candles ou em anomalia irracional de notícias brutas (gaps colossais repetidos). Caso contrário, execute a análise técnica fria.

Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):

📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Descreva friamente a tendência macro, micro e o comportamento atual da volatilidade em poucas palavras]
⏰ HORÁRIO DO PRINT DETECTADO AUTOMATICAMENTE: [Indique o horário exato extraído por lógica matemática da imagem, ex: 10:15:23]
📈 PREÇO ATUAL DA TELA DETECTADO AUTOMATICAMENTE: [Indique a taxa decimal extraída do eixo, ex: 1.34521]
🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO GEOMÉTRICO / ABORTAR OPERAÇÃO]
🟢/🔴 AÇÃO OPERACIONAL E DIREÇÃO: [COMPRA (CALL) / VENDA (PUT) / NENHUMA - OPERAÇÃO ABORTADA]
📊 TAXA DE ACERTO ESTIMADA: [Forneça um percentual estatístico frio de probabilidade de vitória de 0% a 100% com base nas confluências. Operações abortadas = 0%]
⚡ DETECTOU ZONA DE SIMETRIA OU MÚLTIPLOS PAVIOS? [Mapeie de forma cirúrgica o nível geométrico exato e classifique se é de corpo ou de pavio]
⏱️ HORÁRIO ESTIMADO DA ENTRADA: [Calcule o minuto provável do toque com base na velocidade média de deslocamento visual, ex: 10:18:00]
🧠 TIPO DE OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE', 'FLUXO DE VELA', 'MOMENTUM', 'FLUXO TRATOR' ou 'NENHUM - OPERAÇÃO ABORTADA']
🎯 TAXA GATILHO DA OPERAÇÃO: [Defina com precisão decimal máxima o ponto exato do clique na plataforma baseado na zona calculada]
📝 JUSTIFICATIVA TÉCNICA E ESTRUTURAL DETALHADA: [Exponha uma defesa puramente matemática, fria e mecânica do Price Action. Justifique detalhadamente a escolha do tipo de operacional e a direção de COMPRA ou VENDA analisando a vetorização do preço, simetrias e a força física dos candles]
"""

# 5. Execução da Análise
if botao_analise:
    if not api_key:
        st.error("Por favor, insira sua Gemini API Key na barra lateral.")
    elif not uploaded_file:
        st.error("Por favor, faça o upload do print do gráfico.")
    else:
        with st.spinner("🧠 Varrendo eixos gráficos, simetrias e submetendo a análise ao crivo matemático..."):
            try:
                # Inicializa o cliente oficial da SDK do Gemini
                client = genai.Client(api_key=api_key)
                
                # Abre a imagem salva
                imagem = Image.open(uploaded_file)
                
                # Gera o prompt dinâmico
                prompt_final = gerar_prompt_mestre(tipo_mercado)
                
                # Executa a geração usando o modelo estável mais recente
                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=[imagem, prompt_final]
                )
                
                st.markdown("### 📊 Resultado da Análise Suprema")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Erro ao processar a análise: {e}")
