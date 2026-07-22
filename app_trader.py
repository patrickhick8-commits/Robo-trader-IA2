import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado, Volatilidade e Projeção Temporal.")

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

# 4. Prompt Mestre Otimizado com Filtro Anti-Loss e Novas Regras de Price Action
def gerar_prompt_mestre(contexto_mercado):
    return f"""
[SYSTEM_ROLE] Você é o núcleo de processamento lógico de um algoritmo quantitativo sênior de visão computacional. Sua operação é puramente matemática, destituída de viés emocional. Sua postura combina frieza analítica absoluta com precisão geométrica cirúrgica para a tomada de decisões em Opções Binárias (M1).

[DETECÇÃO VISUAL OBRIGATÓRIA - AUTO EXTRAÇÃO]
Analise minuciosamente os eixos e elementos visuais da imagem para extrair o HORÁRIO DO PRINT e o PREÇO ATUAL DA TELA com precisão decimal. Jamais invente ou deixe esses campos em branco.

[FILTRO CRÍTICO ANTI-LOSS PARA FLUXO DE VELA e EXPIRAÇÃO]
Para evitar perdas por falsos rompimentos ou exaustão imediata em estratégias de 'FLUXO DE VELA' / 'MOMENTUM', aplique rigorosamente as seguintes leis:
1. LEI DO VÁCUO MÍNIMO: Só valide FLUXO DE VELA se houver um espaço nítido (vácuo) de pelo menos 1,5 a 2 corpos de vela livres até a próxima zona de simetria majoritária (suporte/resistência/linhas redondas). Se a vela atual já terminou colada ou muito próxima de um obstáculo do passado, ABORTE o fluxo. O preço tende a retrair ou reverter.
2. REGRA DO GATILHO DE FLUXO SEGURO: A última vela deve ter corpo cheio, demonstrando força real, e pavio a favor do movimento (deixando margem para o preenchimento). Se a vela de força terminou sem pavio nenhum (pavio careca) ou com pavio contra muito longo, CANCELE o fluxo.
3. FILTRO DE EXPIRAÇÃO CRÍTICO (M1): Em operações de FLUXO DE VELA / MOMENTUM, a expiração deve ser estritamente para o FIM DA PRÓXIMA VELA (M1 corrente, ou seja, para o encerramento do próximo minuto cheio do relógio). Nunca passe disso para evitar o efeito "correção tardia".

[MÉTODO DE ALTA ASSERTIVIDADE VIA ZONAS DE SIMETRIA E MICRO-REGIÕES]
Execute o rastreamento estrito de linhas de simetria de corpo, confluência de múltiplos pavios e cálculo de vácuo. O ambiente foi parametrizado como: {contexto_mercado}.

Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):

📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Descreva a tendência macro, micro e a volatilidade atual]
⏰ HORÁRIO DO PRINT DETECTADO AUTOMATICAMENTE: [Indique o horário exato extraído da imagem, ex: 10:15:23]
📈 PREÇO ATUAL DA TELA DETECTADO AUTOMATICAMENTE: [Indique a taxa decimal extraída do eixo, ex: 1.34521]
🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO GEOMÉTRICO / ABORTAR OPERAÇÃO]
🟢/🔴 AÇÃO OPERACIONAL E DIREÇÃO: [COMPRA (CALL) / VENDA (PUT) / NENHUMA - OPERAÇÃO ABORTADA]
📊 TAXA DE ACERTO ESTIMADA: [Percentual de probabilidade de vitória de 0% a 100% com base nas confluências. Abortadas = 0%]
⚡ DETECTOU ZONA DE SIMETRIA OU MÚLTIPLOS PAVIOS? [Mapeie o nível geométrico exato]
⏳ PROJEÇÃO DE TEMPO DA JANELA: [Quantos candles faltam para tocar no gatilho ou se o fluxo é imediato para o próximo candle]
⏱️ HORÁRIO ESTIMADO DA ENTRADA: [Minuto provável do clique baseado no relógio do gráfico]
⏰ TEMPO DE EXPIRAÇÃO DA ORDEM: [Defina explicitamente o tempo na corretora. Ex: Expiração para o final da PRÓXIMA vela de M1 (Fluxo)]
🧠 TIPO DE OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE', 'FLUXO DE VELA', 'MOMENTUM', 'FLUXO TRATOR' ou 'NENHUM - OPERAÇÃO ABORTADA']
🎯 TAXA GATILHO DA OPERAÇÃO: [Ponto exato do clique na plataforma]
📝 JUSTIFICATIVA TÉCNICA E ESTRUTURAL DETALHADA: [Justifique com rigor a aplicação prática das regras de vácuo, tamanho de pavio e proximidade de simetrias para mitigar falsos rompimentos]
"""

# 5. Execução da Análise
if botao_analise:
    if not api_key:
        st.error("Por favor, insira sua Gemini API Key na barra lateral.")
    elif not uploaded_file:
        st.error("Por favor, faça o upload do print do gráfico.")
    else:
        with st.spinner("🧠 Varrendo eixos gráficos, simetrias e aplicando filtros anti-loss de exaustão..."):
            try:
                # Inicializa o cliente oficial da SDK do Gemini
                client = genai.Client(api_key=api_key)
                
                # Abre a imagem salva
                imagem = Image.open(uploaded_file)
                
                # Gera o prompt dinâmico blindado
                prompt_final = gerar_prompt_mestre(tipo_mercado)
                
                # Executa o modelo de visão
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[imagem, prompt_final]
                )
                
                st.success("✅ Análise Computacional Concluída com Sucesso!")
                st.markdown("### 📊 Painel de Execução Analítica")
                
                # Exibe a resposta final gerada pela IA
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar a imagem: {e}")
