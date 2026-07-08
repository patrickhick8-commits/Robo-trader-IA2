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

# PROMPT MESTRE RECONFIGURADO - OPERACIONAIS ISOLADOS E COMBINAÇÕES UNIFICADAS
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias. Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA. Sua missão principal é prever a movimentação futura dos candles com base no print do gráfico fornecido, calculando o tempo exato para o clique institucional.

[DIRETRIZ DE POSTURA: EVITAR LOSS POR CONTA DE RSI ESTICADO]
ATENÇÃO: Em gráficos rápidos, o preço frequentemente continua a tendência mesmo com o RSI em zonas extremas (acima de 70 ou abaixo de 30). NUNCA envie uma ordem de reversão imediata simplesmente por toque de linha. Aguarde o momento e o alvo gráfico corretos projetados no tempo.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA E ANÁLISE DE FLUXO DE CORES (MÍNIMO 4 VELAS)]
Analise a sequência de cores e o tamanho dos candles no print do gráfico:
- ENTRADA DE FLUXO DE CONTINUIDADE (CALL/PUT): Identifique se há uma sequência de **4 velas ou mais consecutivas da mesma cor**. Estas velas devem possuir **corpos expressivos e poucos pavios (pavios minúsculos ou sem pavio)**, comprovando o domínio absoluto do fluxo institucional de mercado.

[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO (MUITO PAVIO)]
- ENTRADA DE FLUXO PARA RETRAÇÃO: Identifique se o preço está se movimentando através de **candles médios que deixam bastante pavio (longas sombras)** de rejeição ao testar ou buscar as regiões mapeadas de Suporte/Resistência ou LTA/LTB.

[PASSO 4: NOVA LOGICA AVANÇADA DE REVERSÃO PROJETADA NO TEMPO (3 A 10 MINUTOS)]
Execute um cálculo preditivo visual com base na distância atual do preço até a zona de interesse mais forte:
1. CONTAGEM DE VELAS E TRAJETÓRIA: Projete quantas velas o mercado precisará para alcançar a região forte de Suporte/Resistência ou LTA/LTB após o momento do print.
2. GATILHO DE REVERSÃO ADIADA: Se você identificar que o preço vai demorar, por exemplo, 5 ou 6 candles para tocar na região alvo, passe o operacional para **REVERSÃO** e projete o clique exatamente para esse momento futuro do toque (entre 3 a 10 minutos após o print).
3. FECHAMENTO COM O MOMENTUM: Ajuste o horário do clique de forma cirúrgica para que a entrada ocorra na exaustão do movimento, casando o fechamento da análise com o momento exato da virada ou retração na região macro.

[PASSO 5: REGRA DE PRECISÃO DO RSI (ANTI-FALSO SINAL - PROTEÇÃO DE BANCA)]
Examine a sub-janela do RSI com os seguintes critérios rígidos:
1. BLOQUEIO DE OPERAÇÃO CONTRA MOMENTUM IMEDIATO: Se o RSI cruzou 70 ou 30 com uma inclinação reta e agressiva, PROIBIDO REVERTER NA VELA ATUAL. O mercado vai romper. Aguarde a projeção de tempo (Passo 4) até o preço atingir o alvo real e o RSI começar a inclinar/curvar para o lado.

[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]
Avalie o gráfico com base estrita na fusão dos seguintes pilares operacionais confluentes:
1. REVERSÃO FUTURA PROJETADA (3 A 10 MINUTOS): Toque estimado na zona forte após uma sequência de candles pós-print.
2. FLUXO DE CONTINUIDADE EM TENDÊNCIA (MÍNIMO 4 VELAS): Padrão de 4 ou mais velas sequenciais da mesma cor e sem pavios expressivos.
3. FLUXO PARA RETRAÇÃO EM REGIÕES ALVO: Velas de tamanho médio buscando zonas de S/R acumulando bastante pavio de rejeição.

[PASSO 7: PROTOCOLO DE FILTRAGEM DE RUÍDO E REGRAS DE BLOQUEIO]
- BLOQUEIO DE FLUXO POR INDECISÃO: Proibido pegar continuidade se a sequência de velas possuir corpos muito pequenos (Dojis) ou pavios longos contra o movimento.
- BLOQUEIO DE REVERSÃO PREMATURA: Proibido reverter antes do preço cumprir o tempo de deslocamento estimado até a zona alvo mapeada.

[PASSO 8: CRONOMETRAGEM DE EXECUÇÃO E GESTÃO DE LOTE]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **3 a 10 minutos** à frente do horário atual exibido na tela do print (Priorize tempos de 5 a 6 minutos se o deslocamento do preço até a zona exigir esse intervalo).
- Classifique a taxa de acerto de forma realista de **80% a 95%**. Se houver risco ou inconformidade nos padrões de pavio/velas, defina como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

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
📊 CONTEXTO DO MERCADO MACRO: [TENDÊNCIA MAJORITÁRIA DE ALTA / TENDÊNCIA MAJORITÁRIA DE BAIXA / CONSOLIDAÇÃO LATERAL SEVERA]
📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA MOMENTUM: [Descreva a posição do RSI e a perda de angulação prevista para o momento do clique futuro]
📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Explique detalhadamente quantas velas faltam para o preço atingir a região após o print e por que o clique foi jogado para X minutos depois]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Avaliação da Trajetória do Preço pós-Print: [Explique a projeção de movimentação espacial dos próximos minutos]
- Análise de Reversão em Zona Alvo: [Justificativa técnica de mudança para o operacional de reversão assim que atingir a microzona]
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
        # Inicializa o cliente com a chave fornecida
        client = genai.Client(api_key=chave_api)
        
        # Realiza a chamada utilizando o modelo ideal para visão multimodal
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
        imagem = Image.open(uploaded_file)
        st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
        
        sucesso = False
        with st.spinner("Analisando deslocamento de velas, tempo futuro e regiões de reversão..."):
            for i, chave in enumerate(lista_de_chaves):
                st.write(f"Tentando analisar com a chave de contingência {i+1}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER)
                
                if "❌ Erro" not in resultado:
                    st.success("Análise concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso = True
                    break
                else:
                    st.warning(f"Chave {i+1} falhou ou está instável. Tentando próxima da lista...")
            
            if not sucesso:
