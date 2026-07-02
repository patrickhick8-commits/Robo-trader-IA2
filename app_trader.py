import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema e Projeção Temporal")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

# Campo de texto para as chaves
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# PROMPT MESTRE SUPERCONFLUENTE
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em encontrar oportunidades frequentes e de boa precisão para Opções Binárias (M1). Sua postura é moderadamente agressiva: seu objetivo é extrair o máximo de sinais válidos do gráfico, operando por confluência máxima de fatores sem descartar operações por detalhes mínimos de ruído na tela.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA E POSICIONAMENTO DA EMA 9]
- Rastreie visualmente o fluxo do preço em relação à Média Móvel Exponencial de 9 períodos (EMA 9).
- COMPRA (CALL): O preço deve estar preferencialmente operando ACIMA da EMA 9.
- VENDA (PUT): O preço deve estar preferencialmente operando ABAIXO da EMA 9.
- Use a média apenas como barreira flutuante ou imã de preço, permitindo cliques imediatos se as velas demonstrarem força de deslocamento, sem se prender à inclinação ou ao atraso da linha.

[PASSO 3: MATRIZ DE ESTRATÉGIA ADAPTATIVA SUPREMA MULTI-CONFLUENTE]
Busque de forma ativa por confluências avançadas de Price Action em Suporte, Resistência (S/R horizontais) e Linhas de Tendência (LTA/LTB inclinadas). Una as dinâmicas gráficas para encontrar o ponto exato do clique:

1. MATRIZ DE CONTINUIDADE DE FLUXO (IMPULSO E ANATOMIA DO CANDLE):
   - FLUXO POR COR E IMPULSO: Monitore blocos dominantes de velas de mesma cor que demonstrem aceleração rápida e impulso direcional.
   - TAMANHO DO CORPO (VOLUME INSTITUCIONAL): Avalie a expansão anatômica do corpo do candle recente. Corpos grandes, sólidos e crescentes (como Marubozu ou velas de força) confirmam a urgência e a entrada de volume financeiro pesado a favor do movimento.
   - COMPORTAMENTO OPERACIONAL DE PAVIOS NO FLUXO: Se o candle de força apresentar pavios mínimos ou inexistentes na direção do movimento (pavio superior pequeno na alta ou pavio inferior pequeno na baixa), isso confirma a ausência de recuperação/absorção contrária. Opere a favor da continuidade do fluxo para o preenchimento da região.

2. MATRIZ DE LATERALIDADE / CONSOLIDAÇÃO HORIZONTAL:
   - REVERSÃO E RETRAÇÃO EM SUPORTE/RESISTÊNCIA: Opere o extremo respeito de zonas horizontais nítidas de Suporte (Fundo) e Resistência (Topo). Quando o preço testar os limites com velas de perda de pressão e deixar pavios longos de rejeição, valide o clique de retração ou reversão para a mesma vela.
   - RETRAÇÃO PELOS PAVIOS EM LATERALIDADE: Rastreie o histórico recente de pavios longos nas extremidades da consolidação. Se as velas atuais estiverem demonstrando forte rejeição visual através de pavios ao tocar a barreira horizontal, valide a entrada de retração para a mesma vela.

3. MATRIZ DE TENDÊNCIA (ALTA OU BAIXA) E REVERSÃO:
   - RETRAÇÃO EM TENDÊNCIA / LTA / LTB: Identifique toques em canais ou linhas de tendência inclinadas onde o preço deixa pavios longos de rejeição, operando a retração a favor do canal.
   - CONTINUIDADE PÓS-REVERSÃO MACRO: Identifique o momento exato em que o mercado encerra um ciclo (ex: falha de topo/fundo duplo ou quebra de estrutura CHOCH) e inicia uma nova tendência de Alta ou de Baixa. Opere o fluxo de continuidade e o preenchimento de pavios imediatamente após a confirmação dessa reversão macro, surfando o início do novo movimento de força dos candles.

[PASSO 4: FILTROS ANTI-RUÍDO E MANIPULAÇÃO SUAVIZADOS]
Não seja excessivamente rígido ao filtrar o gráfico. Só aborte a operação em casos extremos de mercado totalmente parado:
- FILTRO ANTI-XADREZ: Aborte apenas se houver uma alternância perfeita e sem direção de cores por mais de 8 velas seguidas. Pequenas oscilações normais intercaladas devem ser operadas.
- FILTRO DE MICRO-VELAS: Aborte apenas se houver uma sequência longa de Dojis legítimos (linhas horizontais finas). Velas pequenas com corpos mínimos e pavios curtos ainda são elegíveis para operação.
- EM OTC: Permita operações de retração de pavios e fluxo de continuidade se as regiões estiverem bem marcadas, aproveitando o fluxo comprador/vendedor para preenchimento de zonas.

[PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]
- Avalie os riscos de forma equilibrada. Quanto mais fatores confluírem juntos (ex: Impulso de Cor + Vela de Corpo Cheio + Ausência de Pavio contrário + EMA 9 confirmando), maior deve ser a taxa de acerto.
- Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. 
- Só emita "OPERAÇÃO ABORTADA" (e taxa 0%) se o gráfico estiver completamente plano, sem tendência alguma e sem zonas visíveis. Se o cenário for minimamente operável, determine uma direção dentro da faixa estipulada.

[PASSO 6: CRONOMETRAGEM DE EXECUÇÃO PADRÃO]
- Localize o relógio oficial da plataforma no print. 
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente (ex: se o relógio marca 10:15:20, projete o clique para entre 10:17:00 e 10:20:00).
- A expiração deve ser rígida de exatamente 1 minuto para fechar na mesma vela do clique projetado.

[PASSO 7: SUGESTÃO DE GERENCIAMENTO DE MÃO DE ENTRADA]
Defina a recomendação de capital com base na taxa calculada de forma matemática:
- Taxa entre 90% e 95%: MÃO DE SOROS / ENTRADA FORTE (Cenário de confluência tripla/máxima).
- Taxa entre 85% e 89%: ENTRADA FIXA padrão (Cenário bom com confluência dupla).
- Taxa entre 80% e 84%: MÃO LEVE / REDUZIDA (Oportunidade isolada de retração, fluxo simples ou impulso moderado).
- Operação Abortada: PARADA OBRIGATÓRIA (Cenário sem condições mínimas).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADA: [Construa a confluência exata vista na tela. Exemplos: CONTINUIDADE DE FLUXO POR COR E IMPULSO (VELA DE CORPO CHEIO SEM REJEIÇÃO) ou REVERSÃO EM LATERALIDADE (SUPORTE HORIZONTAL RESPEITADO) ou FLUXO DE CONTINUIDADE PÓS-REVERSÃO DO MERCADO]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / CONSOLIDAÇÃO LATERAL / IMPULSO DE FLUXO DIRECIONAL / VIRADA DE FLUXO PÓS-REVERSÃO]
📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para atingir sua zona de entrada e confirmar a confluência das estratégias selecionadas]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Diagnóstico do Fluxo de Continuidade (Cor, Impulso e Corpo): [Descreva a sequência de cores das velas, o tamanho anatômico do corpo e o nível de impulso institucional identificado]
- Análise de Pavios e Pressão de Rejeição: [Explique como o comportamento dos pavios recentes confirmou a ausência de defesa contrária no fluxo ou o extremo respeito da lateralidade]
- Mapeamento de Zonas Horizontais (S/R) e Inclinadas (LTA/LTB): [Descreva as microzonas ou suportes/resistências laterais identificados na movimentação dos candles]
- Posicionamento da Média Móvel (EMA 9): [Descreva a posição do preço acima ou abaixo da EMA 9 apenas como ponto dinâmico de referência]
- Avaliação de Ruído e Volatilidade: [Explique por que o cenário foi considerado aceitável para clique com filtros moderados]
- Justificativa da Gestão de Lote: [Explique por que o lote sugerido se adequa perfeitamente a essa combinação de fatores]

Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
"""

# --- AREA OPERACIONAL DO SITE ---

uploaded_file = st.file_uploader(
    "Arraste o print completo do gráfico M1:", type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico M1 Carregado", use_container_width=True)

    if st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL"):
        # Limpa o texto eliminando espaços vazios
        texto_limpo = chaves_input.replace(" ", "")
        
        if not texto_limpo:
            st.error("ERRO: Preencha sua Gemini API Key na barra lateral esquerda antes de rodar!")
        else:
            # Separa os textos por ponto e vírgula e pega o primeiro de forma segura
            lista_de_chaves_limpas = texto_limpo.split(";")
            chave_operacional = lista_de_chaves_limpas[0]

            if not chave_operacional:
                st.error("ERRO: A primeira chave informada está vazia ou é inválida!")
            else:
                with st.spinner("IA escaneando padrões..."):
                    try:

