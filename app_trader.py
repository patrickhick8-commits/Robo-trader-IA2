import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Contexto de Mercado e Volatilidade.")

# 2. Barra Lateral - Gerenciamento de Chaves e Conexão
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

# AJUSTE CRÍTICO: Entradas manuais para evitar alucinações da IA
col1, col2 = st.columns(2)
with col1:
    preco_atual = st.text_input("Preço/Taxa Atual da Tela (ex: 1.12345):", placeholder="Digite a taxa atual")
with col2:
    horario_print = st.text_input("Horário Atual do Gráfico (ex: 15:34):", placeholder="HH:MM")

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 4. Prompt Mestre Otimizado (Focado em Contexto e Estrutura Semântica)
def gerar_prompt_mestre(contexto_mercado, preco, horario):
    return f"""
[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro. Sua postura é de ceticismo extremo, frieza matemática e foco absolutista em proteção de capital.

[DADOS DO AMBIENTE RECEBIDOS]
- Ambiente de Trading: {contexto_mercado}
- Preço/Taxa Atual de Referência: {preco}
- Horário do Último Candle: {horario}

[PROTOCOLO OBRIGATÓRIO: AUDITORIA VISUAL DE VOLATILIDADE E CONTEXTO]
Faça uma varredura visual profunda na imagem enviada para mapear a ESTRUTURA, o CONTEXTO e a VOLATILIDADE de forma automatizada:
1. Identifique a macro-tendência visual da tela (Alta, Baixa ou Lateralização).
2. Identifique a estrutura de pressão (compradores ou vendedores dominando o deslocamento atual).
3. Avalie o estado da volatilidade: 'Notícia/Anormalidade' (velas gigantescas e sem pavio), 'Mercado Parado/Lateral' (velas minúsculas sem deslocamento) ou 'Volatilidade Saudável' (velas proporcionais com pavios de retração claros).

[OBJETIVO OPERACIONAL: PROJEÇÃO PARA 2 A 7 CANDLES FUTUROS EM M1]
O usuário opera em gráficos de 1 minuto (M1). Avalie o comportamento do preço próximo às regiões visuais do gráfico. 
Sua missão é identificar se há um GATILHO OPERACIONAL válido baseado em uma das três estratégias abaixo:
1. RETRAÇÃO EM TAXA FUTURA DE M1: Ative se houver volatilidade saudável com pavios longos recentes.
2. REVERSÃO EM REGIÃO FORTE: Ative se o preço estiver perdendo força (velas diminuindo de tamanho) ao se aproximar de Suporte/Resistência ou Zonas de Oferta/Demanda evidentes.
3. FLUXO DE VELA / MOMENTUM (MOVIMENTO TRATOR): Ative se notar velas sequenciais de força (corpos grandes, sem pavio contra) indo em direção a uma zona, indicando alta probabilidade de rompimento. Pegue a continuidade.

[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]
Ignore completamente nomenclaturas de velas isoladas (Martelo, Engolfo, Doji, etc.). Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, topos/fundos majoritários, canais (LTA/LTB) e o espaço vazio que o preço tem para correr.

[DIRETRIZ DE SEGURANÇA E FILTROS DE RISCO]
- Em Mercado OTC: Ignore lógica macroeconômica. Redobre o ceticismo em suporte/resistência saturados (mais de 3 toques), pois tendem a romper para capturar liquidez. Prefira micro-tendências e fluxos curtos.
- Em Mercado Aberto: Velas desproporcionais e picos isolados podem indicar notícias. Ordene o ABORTO por segurança se o gráfico estiver caótico.
- Se o preço estiver esticado e colado em cima de uma região forte sem espaço para se mover, ordene o ABORTO por risco de exaustão imediata.

Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):

📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Descreva em poucas palavras o cenário visual de tendência e volatilidade]
⏰ HORÁRIO DE REFERÊNCIA: {horario}
📈 PREÇO ATUAL DE REFERÊNCIA: {preco}
🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO OCULTO / ABORTAR OPERAÇÃO]
⚠️ DETECTADO RISCO OCULTO NA ESTRUTURA? [Sim (especifique em uma frase curta qual é o risco) / Não, estrutura totalmente limpa]
🧠 OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE', 'FLUXO DE VELA / MOMENTUM' ou 'NENHUM - OPERAÇÃO ABORTADA']
🎯 REGIÃO ALVO PARA ENTRADA: [Indique visualmente onde o usuário deve agir baseado no preço de referência fornecido, ex: 'Levemente acima/abaixo da taxa informada na próxima zona de pavios']
"""

# 5. Execução da Análise
if botao_analise:
    if not api_key:
        st.error("Por favor, insira sua Gemini API Key na barra lateral.")
    elif not uploaded_file:
        st.error("Por favor, faça o upload do print do gráfico.")
    elif not preco_atual or not horario_print:
        st.error("Por favor, preencha o Preço Atual e o Horário de Referência para evitar erros de leitura da IA.")
    else:
        with st.spinner("🧠 Analisando padrões gráficos e estrutura de mercado..."):
            try:
                # Inicializa o cliente oficial da nova SDK do Gemini
                client = genai.Client(api_key=api_key)
                
                # Abre a imagem salva
                imagem = Image.open(uploaded_file)
                
                # Gera o prompt dinâmico
                prompt_final = gerar_prompt_mestre(tipo_mercado, preco_atual, horario_print)
                
                # Executa a chamada multimodal usando o modelo ideal para visão (Gemini 2.5 Flash ou Pro)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[imagem, prompt_final]
                )
                
                st.markdown("### 📊 Resultado da Análise Suprema")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Erro ao processar a análise: {e}")
