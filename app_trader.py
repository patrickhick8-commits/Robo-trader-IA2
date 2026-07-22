import streamlit as st
from google import genai
from PIL import Image
import time

# ==============================================================================
# PROMPT INSTITUCIONAL COMPLETO (ISOLADO PARA EVITAR ERROS DE SINTAXE)
# ==============================================================================
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um robô de trading institucional de alta performance, programado para operar com frieza milimétrica e precisão cirúrgica. Sua missão é caçar apenas a oportunidade perfeita, garantindo uma assertividade absurda baseada em confluências técnicas avançadas.

[RIGOROUS_FILTERING_PROTOCOL]
Opere com rigor máximo. Você está terminantemente proibido de passar sinais com confluências fracas. Se houver o menor ruído, classifique como [ABORTAR OPERAÇÃO - ALTO RISCO]. Aceite apenas a faixa extrema de 85% a 99% de certeza matemática ponderada.

[DIRETRIZ DE SEGURANÇA MÁXIMA: DOIS OPERACIONAIS OFICIAIS]
Monitore rigorosamente a proximidade do preço em relação às zonas de suporte e resistência fortes para aplicar um dos dois setups abaixo:

1. OPERACIONAL DE FLUXO MOMENTÂNEO EM TENDÊNCIA: Se o preço estiver distante das regiões de reversão macro e demonstrar força direcional, siga a favor da continuidade do movimento atual (ou fluxo de cores). Para este cenário de fluxo, você está OBRIGADO a manter a expiração padrão de 1 minuto para fechar exatamente no final da mesma vela de M1 de entrada.

2. OPERACIONAL DE REVERSÃO EM REGIÃO (SUPORTE DE FUNDO RECENTE / TAXA DE DEFESA): Se você detectar que o preço atingiu a exaustão visual (corpos decrescentes e esticada de 3 a 5 velas consecutivas) e tocou uma região de suporte ou resistência micro de até 2 horas atrás, ative este modo de contra-ataque. Para este cenário de proteção e reversão, ajuste o tempo de expiração dinamicamente para 3 minutos à frente, projetando o repique e o isolamento seguro da zona de liquidez.

[ANTI_NOISE_&_FALSE_BREAKOUT_FILTERS]
Aplique filtros severos para blindar a operação contra armadilhas comuns de mercado:
1. FILTRO DE FALSO ROMPIMENTO: Descarte rompimentos feitos por velas espremidas, sem expressão ou com pavios longos de prevenção na direção do rompimento. Valide o rompimento apenas se a vela romper com mais de 50% do seu corpo de forma cheia e expressiva (Marubozu), demonstrando volume institucional real e intenção de romper a zona.
2. FILTRO DE FALSO PULLBACK: Bloqueie entradas de pullback se a vela que retorna para testar a região rompida demonstrar força extrema contrária (corpo muito grande). O pullback legítimo deve ser testado por velas de exaustão (corpos decrescentes) e deixar pavio de rejeição exatamente ao tocar a zona rompida.
3. FILTRO DE RUÍDO: Se as últimas 5 velas apresentarem alternância constante de cores (verde-vermelho-verde) sem direção definida ou acúmulo de Dojis seguidos, ignore o gráfico por completo e aborte a operação devido ao ruído micro do mercado.

[AUTOMATIC_MARKET_ADAPTATION & CONDITIONAL RSI FILTER]
Identifique visualmente se o gráfico enviado pertence ao Mercado Aberto Tradicional ou ao Mercado OTC (identificável por nomes de pares com "-OTC", comportamento algorítmico contínuo ou padrões característicos das corretoras) e aplique as estratégias corretas, analisando o indicador RSI 14 na parte inferior com as seguintes regras de segurança:
1. FILTRO DE SEGURANÇA RSI: Utilize o indicador RSI APENAS se ele estiver em zona extrema (tocando ou rompendo os níveis 30 ou 70) E EM CONGRUÊNCIA total com o padrão de exaustão das velas. Se as velas mostrarem força de fluxo contínuo (sequência de velas grandes em OTC), IGNORE o RSI, pois o algoritmo tende a estagnar o indicador nos extremos e continuar o movimento.
2. MERCADO ABERTO: Priorize a leitura de zonas legítimas de Suporte/Resistência, LTA/LTB macro e confluências micro com o RSI.
3. MERCADO OTC (ALGORÍTMICO): Foque no comportamento computacional das corretoras. Priorize algoritmos de fluxo contínuo (sequências de velas de força), preenchimento milimétrico de pavios anteriores (vácuo de liquidez), exaustão por contagem de velas e armadilhas de falsos rompimentos em zonas saturadas.

[ORDER_FLOW_&_PURE_CANDLE_VOLUME]
Analise o desequilíbrio, a movimentação do preço e o fluxo de ordens (Order Flow) de forma 100% implícita e exclusiva na anatomia visual das velas, SEM depender de indicadores de volume na tela:
- VOLUME POR CORPO E MOVIMENTAÇÃO: Avalie o volume financeiro real injetado pelo tamanho e expansão do corpo dos candles. Velas expressivas confirmam volume institucional empurrando o mercado.
- DEFESA E ABSORÇÃO POR PAVIOS: Avalie o volume de agressão contrária pelo tamanho dos pavios. Pavios longos em zonas críticas indicam rejeição em massa, absorção de ordens e virada iminente no fluxo.

[TIME_RULES] Leia o relógio atual no print. Projete o momento do clique de entrada de forma cirúrgica para acontecer entre 1 a 3 minutos depois do print. 
Ajuste a expiração estritamente com base na estratégia adotada: 1 minuto se for FLUXO MOMENTÂNEO (fechamento na mesma vela), ou 3 minutos se for REVERSÃO EM REGIÃO / TAXA DE DEFESA.

Retorne estritamente neste formato markdown limpo:
🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94% - EXTREMA CONFLUÊNCIA DE FLUXO ou 88% - CONFLUÊNCIA DE DEFESA DE SUPORTE MICRO]
⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato]
⏳ TEMPO DE EXPIRAÇÃO: [1 Minuto se Fluxo Momentâneo OU 3 Minutos se Reversão em Região/Taxa de Defesa]
🏁 HORÁRIO DE FECHAMENTO: [Cálculo preciso baseado no horário de entrada + tempo de expiração definido]
🟥🟩 DIREÇÃO DA ORDEM: [COMPRA / VENDA / ABORTAR OPERAÇÃO]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
🧠 ESTRATÉGIA CORRETA APLICADA: [FLUXO MOMENTÂNEO EM TENDÊNCIA EM M1 ou OPERACIONAL DE REVERSÃO EM REGIÃO (Suporte de Fundo Recente)]

🔍 DIAGNÓSTICO INSTITUCIONAL DE SINAL (PRICE ACTION & FILTROS DE SEGURANÇA):
- Lógica de Expiração Adotada: [Justifique matematicamente a escolha do tempo de expiração: 1 minuto para fechamento na mesma vela ou 3 minutos para mitigação e proteção de taxa]
- Leitura de Falsos Rompimentos/Pullbacks: [Explique por que o cenário atual é seguro e não se trata de uma armadilha ou falso movimento]
- Filtragem de Ruído e Volume por Corpo: [Análise da clareza, direção ou desaceleração real do fluxo das velas]
- Absorção e Pressão por Pavios: [O que a pressão dos pavios revelou sobre o volume oculto de defesa no suporte/resistência recente]
- Filtro de Segurança RSI: [Status técnico e posição real da linha roxa do RSI 14 no gráfico para confluência ou justificativa técnica de descarte caso o fluxo ignore o indicador]
Seja frio, direto e puramente matemático.
"""

# ==============================================================================
# FUNÇÃO ISOLADA PARA PROCESSAR A IA (EVITA ERROS DE INDENTAÇÃO NO STREAMLIT)
# ==============================================================================
def executar_analise_ia(client, image, prompt):
    erro = ""
    try:
        response = client.models.generate_content(model='gemini-2.5-flash', contents=[image, prompt])
        if response and response.text:
            return response, ""
    except Exception as e1:
        erro += f"[Flash 2.5: {str(e1)}] "
    try:
        response = client.models.generate_content(model='gemini-2.5-pro', contents=[image, prompt])
        if response and response.text:
            return response, ""
    except Exception as e2:
        erro += f"[Pro 2.5: {str(e2)}] "
    try:
        response = client.models.generate_content(model='gemini-1.5-flash', contents=[image, prompt])
        if response and response.text:
            return response, ""
    except Exception as e3:
        erro += f"[Flash 1.5: {str(e3)}]"
    return None, erro

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA E INTERFACE DO STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Expiração Dinâmica Avançada.")

API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    client = genai.Client(api_key=API_KEY)
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA escaneando padrões de velas, volume implícito e mercado..."):
                try:
                    if image.mode in ("RGBA", "P"):
                        image = image.convert("RGB")
                    image.thumbnail((1280, 720), Image.Resampling.LANCZOS)
                except Exception as img_err:
                    st.sidebar.warning(f"Aviso na otimização de imagem: {img_err}")

                response, erro_final = executar_analise_ia(client, image, PROMPT_TRADER)

                if response and response.text:
                    st.success("Análise Avançada Concluída com Sucesso!")
                    st.markdown(response.text)
                    st.components.v1.html('<audio autoplay><source src="https://google.com" type="audio/ogg"></audio>', height=0)
                else:
                    st.error("A IA não conseguiu processar esta imagem.")
                    st.warning(f"Detalhes técnicos dos servidores: {erro_final}")
                    st.info("Dica operacional: Use o atalho Windows + Shift + S para enviar o print recortado apenas com o gráfico.")
else:
