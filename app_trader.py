import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado, Volatilidade e Janela de Projeção.")

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

# 4. Prompt Mestre Corrigido com Janela de 2 a 7 Velas e Regras de Expiração Estritas
def gerar_prompt_mestre(contexto_mercado):
    return f"""
[SYSTEM_ROLE] Você é o núcleo de processamento lógico de um algoritmo quantitativo sênior de visão computacional. Sua operação é puramente matemática, destituída de viés emocional. Sua postura combina frieza analítica absoluta com precisão geométrica cirúrgica para a tomada de decisões em Opções Binárias (M1).

[DETECÇÃO VISUAL OBRIGATÓRIA - AUTO EXTRAÇÃO]
Antes de processar qualquer estratégia, analise minuciosamente os eixos e elementos visuais da imagem para extrair o HORÁRIO DO PRINT e o PREÇO ATUAL DA TELA com precisão decimal. 

[JANELA DE PROJEÇÃO FUTURA (2 A 7 VELAS) E PROTOCOLO DE EXPIRAÇÃO]
O usuário opera estritamente em gráficos de 1 minuto (M1). Suas projeções NÃO são para a próxima vela imediata. Você deve estimar friamente o tempo de deslocamento do preço:
1. JANELA FUTURA DE TOQUE: Olhe para o espaço vazio à direita da tela. Calcule visualmente quantas velas de 1 minuto (de 2 a 7 candles à frente) o preço levará para atingir a zona de simetria ou gatilho calculada.
2. REGRA DE EXPIRAÇÃO POR OPERACIONAL:
   - Se o operacional ativado for 'RETRAÇÃO EM TAXA FUTURA': O gatilho é o toque na taxa. A expiração deve ser estritamente para a MESMA VELA DO TOQUE (M1 corrente dentro do minuto projetado).
   - Se o operacional ativado for 'REVERSÃO EM REGIÃO FORTE': A expiração deve ser calculada para o término do movimento de correção (geralmente de 2 a 5 minutos à frente, dependendo da força da região).
   - Se o operacional for 'FLUXO DE VELA', 'MOMENTUM' ou 'FLUXO TRATOR': A expiração deve ser para o fechamento da PRÓXIMA VELA (M1) ou acompanhar a projeção do vácuo até o alvo majoritário (2 a 3 minutos).

[MÉTODO DE ASSERTIVIDADE VIA ZONAS DE SIMETRIA]
Execute o rastreamento estrito de linhas de simetria de corpo, confluência de múltiplos pavios e cálculo de vácuo (espaço vazio restante até o alvo). O ambiente foi parametrizado como: {contexto_mercado}.

[EXECUÇÃO FRIA: REGRAS DE ABORTO EXCLUSIVAS]
Você só emitirá o veredito de 'ABORTAR OPERAÇÃO' se o gráfico estiver 100% plano/morto por mais de 10 candles ou em anomalia irracional de notícias brutas (gaps colossais sequenciais). Caso contrário, determine a taxa e projete o clique futuro.

Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):

📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Descreva friamente a tendência macro, micro e o comportamento atual da volatilidade em poucas palavras]
⏰ HORÁRIO DO PRINT DETECTADO AUTOMATICAMENTE: [Indique o horário exato extraído por lógica matemática da imagem, ex: 10:15:23]
📈 PREÇO ATUAL DA TELA DETECTADO AUTOMATICAMENTE: [Indique a taxa decimal extraída do eixo, ex: 1.34521]
🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO GEOMÉTRICO / ABORTAR OPERAÇÃO]
🟢/🔴 AÇÃO OPERACIONAL E DIREÇÃO: [COMPRA (CALL) / VENDA (PUT) / NENHUMA - OPERAÇÃO ABORTADA]
📊 TAXA DE ACERTO ESTIMADA: [Forneça um percentual estatístico frio de probabilidade de vitória de 0% a 100% com base nas confluências. Operações abortadas = 0%]
⚡ DETECTOU ZONA DE SIMETRIA OU MÚLTIPLOS PAVIOS? [Mapeie de forma cirúrgica o nível geométrico exato e classifique se é de corpo ou de pavio]
⏳ PROJEÇÃO DE TEMPO DA JANELA: [Indique explicitamente quantos candles/minutos futuros faltam para o preço tocar no gatilho, obrigatoriamente dentro da janela de 2 a 7 minutos. Ex: 'Toque estimado em 4 candles à frente']
⏱️ HORÁRIO ESTIMADO DA ENTRADA: [Calcule o minuto futuro provável do clique somando a projeção de tempo ao horário detectado no print, ex: 10:19:00]
⏰ TEMPO DE EXPIRAÇÃO DA ORDEM: [Defina de forma ultra detalhada a expiração exata do clique na corretora de acordo com o operacional escolhido. Ex: 'Expiração para a mesma vela do toque (Retração - M1)' ou 'Expiração para 3 minutos à frente (Reversão/Fluxo)']
🧠 TIPO DE OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE', 'FLUXO DE VELA', 'MOMENTUM', 'FLUXO TRATOR' ou 'NENHUM - OPERAÇÃO ABORTADA']
🎯 TAXA GATILHO DA OPERAÇÃO: [Defina com precisão decimal máxima o ponto exato do clique na plataforma baseado na zona calculada]
📝 JUSTIFICATIVA TÉCNICA E ESTRUTURAL DETALHADA: [Exponha uma defesa puramente matemática, fria e mecânica do Price Action. Justifique detalhadamente a escolha do tipo de operacional, a direção de COMPRA ou VENDA, e prove matematicamente por que escolheu esse tempo específico de expiração baseado no vácuo gráfico]
"""

# 5. Execução da Análise
if botao_analise:
    if not api_key:
        st.error("Por favor, insira sua Gemini API Key na barra lateral.")
    elif not uploaded_file:
        st.error("Por favor, faça o upload do print do gráfico.")
    else:
        with st.spinner("🧠 Projetando cliques na janela futura e calculando tempos de expiração com Gemini 3.5..."):
            try:
                # Inicializa o cliente oficial da SDK do Gemini
                client = genai.Client(api_key=api_key)
                
                # Abre a imagem salva
                imagem = Image.open(uploaded_file)
                
                # Gera o prompt dinâmico
                prompt_final = gerar_prompt_mestre(tipo_mercado)
                
                # Executa a geração usando o modelo estável mais recente (Gemini 3.5 Flash)
                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=[imagem, prompt_final]
                )
                
                st.markdown("### 📊 Resultado da Análise Suprema")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Erro ao processar a análise: {e}")
