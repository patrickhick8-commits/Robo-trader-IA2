import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema de Alta Assertividade")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# PROMPT MESTRE CONFIGURADO PARA ALTÍSSIMA PRECISÃO, FRIEZA E VELAS LONGAS (LONGE DA TAXA)
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (M1) operando em modo ULTRA-RIGOROSO e FRIO. Sua missão é eliminar qualquer adivinhação. Você está proibido de enviar entradas baseadas em retrações curtas ou finais de movimento. Busque exclusivamente por velas de alta expansão volumétrica (Marubozu / Velas Elefantes / Início de Impulso Institucional) onde o candle fechará GRANDE e MUITO LONGE da taxa de entrada. Se o cenário for de indecisão, aborte imediatamente.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTRO DE TENDÊNCIA MAJORITÁRIA E EXPLOSÃO DA EMA 9]
- ANÁLISE MACRO: Identifique a tendência dominante do gráfico de fundo. Nunca opere contra ela.
- POSICIONAMENTO CRÍTICO (EMA 9): 
  - COMPRA (CALL): O preço deve ter acabado de romper ou estar se afastando agressivamente ACIMA da EMA 9 com uma vela de força sem pavio superior longo.
  - VENDA (PUT): O preço deve ter acabado de romper ou estar se afastando agressivamente ABAIXO da EMA 9 com uma vela de força sem pavio inferior longo.

[PASSO 3: PROTOCOLO RSI PARA EVITAR FINAL DE MOVIMENTO]
- ANALISE O RSI (Padrão 14):
  - Para CALL: O RSI não pode estar sobrecomprado. Ele deve estar saindo da região neutra ou cruzando a linha 50 apontando para CIMA com forte inclinação angular, indicando espaço para o candle crescer livremente.
  - Para PUT: O RSI não pode estar sobrevendido. Ele deve estar saindo da região neutra ou cruzando a linha 50 apontando para BAIXO com forte inclinação angular, indicando espaço livre para derretimento do preço.

[PASSO 4: FILTRO DA ANATOMIA DO CANDLE (EVITANDO LOSS NA TAXA)]
Você só aprovará a entrada se a anatomia dos candles recentes demonstrar Força Impulsiva Real:
- PROIBIDO: Entrar em velas pequenas, velas com pavios gigantes em ambos os lados, ou padrões de exaustão.
- OBRIGATÓRIO: O sinal deve ocorrer no início ou na confirmação de um fluxo de rompimento, garantindo que a vela de entrada seja um candle de corpo cheio e expressivo, terminando isolado da taxa de abertura.

[PASSO 5: PROTOCOLO DE FILTRAGEM DE RUÍDO AGRESSIVO (FRIEZA TOTAL)]
Aborte imediatamente a operação se notar qualquer um dos seguintes cenários (Taxa de Acerto cai para 0%):
- VELAS PEQUENAS/DOJIS: Se houver acúmulo de velas de corpo curto na região de interesse.
- TIPO XADREZ: Alternância de cores de velas (verde/vermelha) nas últimas 4 a 6 velas.
- PROXIMIDADE DE TAXA DE REVERSÃO: Se houver um suporte ou resistência forte imediatamente na frente do candle que possa fazê-lo retrair e fechar perto da taxa.

[PASSO 6: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]
- Seja cirúrgico. Classifique a taxa de acerto estritamente dentro da faixa de **85% a 98%**. 
- Se houver qualquer risco de o candle terminar perto da taxa de clique por falta de volume, defina como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

[PASSO 7: CRONOMETRAGEM DE EXECUÇÃO EM MOMENTO DE EXPLOSÃO]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente do relógio visível da plataforma. Expiração fixa de 1 minuto para fechar na mesma vela do clique projetado, pegando a continuação do estouro do preço.

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 88% ou 95% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADA: [Construa a confluência técnica exata vista na tela.]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO MACRO: [TENDÊNCIA MAJORITÁRIA DE ALTA / TENDÊNCIA MAJORITÁRIA DE BAIXA / CONSOLIDAÇÃO LATERAL SEVERA]
📈 LEITURA DO RSI PADRÃO: [Descreva a posição do RSI: Em forte expansão para cima/baixo, evitando exaustão]
📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique matematicamente por que este momento iniciará uma vela de corpo grande e distante da taxa de entrada]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Avaliação da Tendência Majoritária: [Justifique a direção macro identificada no fundo do gráfico]
- Comportamento Gráfico do RSI: [Explique como a curvatura ou toque do RSI validou ou abortou a operação]
- Mapeamento das Regiões (S/R, LTA/LTB): [Descreva as microzonas]
- Avaliação de Ruído e Volatilidade (Filtro de Frieza Máxima): [Análise do cenário de estabilidade e volume]
- Diagnóstico do Fluxo de Continuidade (Vela Grande Garantida): [Análise anatômica provando o tamanho esperado do corpo do candle]
- Posicionamento da Média Móvel (EMA 9): [Relação do preço com a EMA 9]
- Justificativa da Gestão de Lote: [Por que o lote sugerido se adequa a esses fatores]

Seja extremamente frio, preciso e direto. Não adivinhe, use pura confluência de volume e força institucional.
"""

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_texto):
    try:
        client_objeto = genai.Client(api_key=chave_api)
        chamada = client_objeto.models.generate_content(
            model="gemini-2.5-flash", 
            contents=[imagem_objeto, prompt_texto]
        )
        return chamada.text
    except Exception as erro_objeto:
        return f"ERRO_GERADO: {str(erro_objeto)}"

# --- AREA OPERACIONAL DO SITE ---

uploaded_file = st.file_uploader(
    "Faça o upload do print do seu gráfico (M1):", 
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico Carregado", use_container_width=True)
    
    if st.button("🚀 Analisar com Frieza e Alta Precisão"):
        if not lista_de_chaves:
            st.error("Por favor, insira pelo menos uma Gemini API Key na barra lateral.")
        else:
            sucesso = False
            # Tenta rodar as chaves de contingência caso uma falhe
            for i, chave in enumerate(lista_de_chaves):
                with st.spinner(f"Processando análise com a chave {i+1}..."):
                    resultado = executar_chamada_gemini(chave, image, PROMPT_TRADER)
                    
                    if "ERRO_GERADO" not in resultado:
                        st.success("Análise concluída com sucesso!")
                        st.markdown(resultado)
                        sucesso = True
                        break
                    else:
                        st.warning(f"Chave {i+1} falhou ou está instável. Tentando próxima...")
            
            if not sucesso:
                st.error("Todas as chaves de API falharam. Verifique suas conexões e limites da API Gemini.")
