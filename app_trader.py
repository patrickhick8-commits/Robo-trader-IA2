import streamlit as st
from google import genai
from PIL import Image
import re
from datetime import datetime, timedelta
import time

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema de Alta Assertividade")
st.write("Fusão Total: Projeção Temporal Avançada (3 a 10 Minutos), Reversão Futura por Contagem de Candles, Fluxo de Cores e Retração.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# PROMPT MESTRE RECONFIGURADO - BLINDAGEM DE TENDÊNCIA E PROTEÇÃO ANTI-LOSS EM REVERSÃO
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias. Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA. Sua missão principal é prever a movimentação futura dos candles com base no print do gráfico fornecido, eliminando falsas entradas de reversão contra a tendência macro e micro.

[DIRETRIZ DE SEGURANÇA MÁXIMA: ALINHAMENTO DE TENDÊNCIA EM REVERSÕES]
ATENÇÃO: Você está tomando LOSS por tentar adivinhar reversões (ex: mandar COMPRAR em suporte com microtendência de baixa esmagadora, ou mandar VENDER/PUT em resistência quando o mercado macro é de Alta). 
- PROIBIDO OPERAR REVERSÃO CONTRA A FORÇA INSTITUCIONAL MAIOR.
- Se o preço está subindo forte em direção a uma Resistência (Micro/Macro de ALTA), você está PROIBIDO de abrir uma ordem de VENDA (PUT) a menos que o RSI já tenha entrado na zona neutra e os últimos 2 candles mostrem rejeição real (pavios longos em cima).
- Se o mercado chegar com velas cheias e sem pavios em uma região contra a tendência majoritária, mude o operacional para ROMPIMENTO/FLUXO ou determine OPERAÇÃO ABORTADA.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA MACRO/MICRO E ANÁLISE DE FLUXO DE CORES (MÍNIMO 4 VELAS)]
Analise a sequência de cores e o tamanho dos candles no print do gráfico para definir quem domina o mercado:
- TENDÊNCIA MAJORITÁRIA (MACRO): O gráfico geral aponta para onde? Alta, Baixa ou Lateralização?
- ENTRADA DE FLUXO DE CONTINUIDADE (CALL/PUT): Identifique se há uma sequência de **4 velas ou mais consecutivas da mesma cor**. Estas velas devem possuir **corpos expressivos e poucos pavios (pavios minúsculos ou sem pavio)**, comprovando o domínio absoluto do fluxo institucional de mercado. Se este padrão estiver ativo indo em direção a um suporte/resistência, favoreça o ROMPIMENTO (Fluxo) e NUNCA a reversão.

[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO (MUITO PAVIO)]
- ENTRADA DE FLUXO PARA RETRAÇÃO: Identifique se o preço está se movimentando através de **candles médios que deixam bastante pavio (longas sombras)** de rejeição ao testar ou buscar as regiões mapeadas de Suporte/Resistência ou LTA/LTB. 

[PASSO 4: NOVA LOGICA AVANÇADA DE REVERSÃO INTELIGENTE PROJETADA NO TEMPO (3 A 10 MINUTOS)]
Execute um cálculo preditivo visual com base na distância atual do preço até a zona de interesse mais forte:
1. CONTAGEM DE VELAS E TRAJETÓRIA: Projete quantas velas o mercado precisará para alcançar a região forte de Suporte/Resistência ou LTA/LTB após o momento do print.
2. GATILHO DE REVERSÃO SELECIONADA: Só valide o 'OPERACIONAL DE REVERSÃO EM REGIÃO' se o preço estiver se deslocando com perda de força (candles diminuindo de tamanho ou deixando pavio a favor da tendência macro). Se o deslocamento até o alvo for de 5 ou 6 candles calmos, jogue o clique para 5 a 6 minutos no futuro casando com o toque exato.
3. FILTRO ANTI-ERRO: Se o preço estiver buscando a região com velas explosivas a favor de uma macrotendência forte, ABORTE A REVERSÃO. Não tente segurar o preço com as mãos.

[PASSO 5: REGRA DE PRECISÃO DO RSI (ANTI-FALSO SINAL - PROTEÇÃO DE BANCA)]
Examine a sub-janela do RSI com os seguintes critérios rígidos:
1. BLOQUEIO DE OPERAÇÃO CONTRA MOMENTUM IMEDIATO: Se o RSI cruzou 70 ou 30 com uma inclinação reta e agressiva, PROIBIDO REVERTER NA VELA ATUAL. O mercado vai romper. Aguarde a projeção de tempo (Passo 4) até o preço atingir o alvo real e o RSI começar a inclinar/curvar para o lado.

[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]
Avalie o gráfico com base estrita na fusão dos seguintes pilares operacionais confluentes:
1. REVERSÃO FUTURA PROJETADA (3 A 10 MINUTOS): Toque estimado na zona forte após uma sequência de candles pós-print, desde que ALINHADO ou validado pela fraqueza da tendência oposta.
2. FLUXO DE CONTINUIDADE EM TENDÊNCIA (MÍNIMO 4 VELAS): Padrão de 4 ou mais velas sequenciais da mesma cor e sem pavios expressivos.
3. FLUXO PARA RETRAÇÃO EM REGIÕES ALVO: Velas de tamanho médio buscando zonas de S/R acumulando bastante pavio de rejeição.

[PASSO 7: PROTOCOLO DE FILTRAGEM DE RUÍDO E REGRAS DE BLOQUEIO]
- BLOQUEIO CONTRA TENDÊNCIA CEGA: Proibido abrir ordens de compra em resistências ou vendas em suportes se o preço estiver empurrado por uma macro/microtendência forte sem sinais claros de exaustão fractal.
- BLOQUEIO DE REVERSÃO PREMATURA: Proibido reverter antes do preço cumprir o tempo de deslocamento estimado até a zona alvo mapeada.

[PASSO 8: CRONOMETRAGEM DE EXECUÇÃO E GESTÃO DE LOTE]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **3 a 10 minutos** à frente do horário atual exibido na tela do print (Priorize tempos de 5 a 6 minutos se o deslocamento do preço até a zona exigir esse intervalo).
- Classifique a taxa de acerto de forma realista de **80% a 95%**. Se houver risco ou inconformidade nos padrões de pavio/velas/tendência, defina como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 91% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 3 a 10 minutos para o futuro com base no deslocamento das velas]
⏳ TEMPO DE EXPIRAÇÃO: [Tempo estimado de expiração ideal, ex: 1 Minuto para a mesma vela do toque institucional]
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da ordem]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO: 
- Especifique com precisão qual tipo de operacional isolado foi ativado na tela. Exemplos exatos permitidos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'OPERACIONAL DE FLUXO DE VELA EM TENDÊNCIA', 'OPERACIONAL DE PULLBACK' ou 'OPERACIONAL DE FLUXO DE CONTINUIDADE'.
- Explique em detalhes os gatilhos e a região que o preço está ou irá buscar.
- Descreva minuciosamente qual combinação exata ocorreu na tela: se foi Reversão com bastante respeito + Pavio, se foi Rompimento + Fluxo, se foi Pullback + Retração Longa de Pavio ou se foi Fluxo Reversão analisando o alvo do preço.

🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [TENDÊNCIA MAJORITÁRIA DE ALTA / TENDÊNCIA MAJORITÁRIA DE BAIXA / CONSOLIDAÇÃO LATERAL SEVERA - Explicar se a micro está alinhada ou se é perigosa]
📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA MOMENTUM: [Descreva a posição do RSI e a perda de angulação prevista para o momento do clique futuro]
📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Explique detalhadamente quantas velas faltam para o preço atingir a região após o print e por que o clique foi jogado para X minutos depois, provando matematicamente que o sinal não ignora a tendência macro]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Avaliação da Trajetória do Preço pós-Print: [Explique a coleção de movimentos espaciais dos próximos minutos]
- Análise de Alinhamento de Tendência em Zona Alvo (Filtro de Loss): [Justificativa de como a tendência macro e micro foi respeitada para evitar falsas ordens de reversão]
- Padrão Sequencial de Cores: [Confirmação se existem 4+ velas da mesma cor com poucos pavios para fluxo]
- Densidade e Comportamento dos Pavios: [Análise se há bastante pavio em candles médios confirmando fluxo para retração]
- Comportamento Gráfico do RSI (Filtro Anti-Loss): [Análise de inclinação e exaustão futura]
- Verificação de Bloqueios (Ruídos e Falta de Padrão): [Justificativa técnica dos filtros de segurança]
- Mapeamento das Regiões de Respeito (S/R, LTA/LTB): [Mapeamento das microzonas com base no print]
- Justificativa da Gestão de Lote sob Frieza Máxima: [Por que o lote sugerido se adequa a esses fatores rígidos]

Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
"""

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    """Executa a chamada unificada usando a biblioteca moderna google-genai"""
    try:
        client = genai.Client(api_key=chave_api)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[imagem_objeto, prompt_comando]
        )
        return response.text
    except Exception as e:
        return f"❌ Erro ao processar com a chave atual: {str(e)}"

# Área de Upload da Imagem do Gráfico
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

if uploaded_file and lista_de_chaves:
    if st.button("🧠 Iniciar Análise Avançada por IA"):
