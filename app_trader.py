import streamlit as st
from google import genai
from PIL import Image
import re
from datetime import datetime, timedelta
import time

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema de Alta Assertividade")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# PROMPT MESTRE RECONFIGURADO - NOVA ESTRATÉGIA COMBINADA ULTRA-COMPLEXA
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (M1). Sua postura é de FRIEZA MÁXIMA E RIGOR ABSOLUTO. Sua missão é proteger o capital e eliminar falsos sinais através de barreiras técnicas inflexíveis. 

[DIRETRIZ DE POSTURA: FRIEZA MÁXIMA]
Ignore qualquer impulso gráfico ou "quase-sinal". Se os critérios matemáticos e geométricos não forem preenchidos perfeitamente, aborte sem hesitação. Não tente adivinhar topos ou fundos sem confluência total.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA MAJORITÁRIA (MACRO) E POSICIONAMENTO DA EMA 9]
- ANALISE DA TENDÊNCIA MAJORITÁRIA: Avalie o cenário macro do gráfico em segundo plano. O preço vem construindo movimentos maiores de alta ou de baixa? Evite operar contra o fluxo macro dominador.
- Rastreie visualmente o fluxo do preço em relação à Média Móvel Exponencial de 9 períodos (EMA 9) para a microtendência.
- COMPRA (CALL): A tendência majoritária deve ser de Alta e o preço operando preferencialmente ACIMA da EMA 9.
- VENDA (PUT): A tendência majoritária deve ser de Baixa e o preço operando preferencialmente ABAIXO da EMA 9.

[PASSO 3: PROTOCOLO AVANÇADO DO INDICADOR RSI (FILTRO INCLINADO)]
- Localize a sub-janela do RSI. 
- FILTRO RSI INCLINADO: Não opere se o RSI estiver de lado. Para operações de fluxo ou reversão, a linha do RSI precisa apresentar uma inclinação angular nítida e agressiva. Se estiver aproximando-se de níveis de sobrecompra/sobrevenda, avalie a velocidade e angulação do vetor da linha. RSI sem inclinação clara invalida entradas de momentum.

[PASSO 4: MAPEAMENTO GEO-ESPACIAL DO PREÇO]
- Analise milimetricamente a REGIÃO QUE O PREÇO ESTÁ OU IRÁ BUSCAR nos próximos minutos. Identifique se o preço está preso em vácuo gráfico ou se há alvos claros de liquidez, zonas de saturação ou blocos de ordens logo à frente.

[PASSO 5: NOVA MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]
Avalie o gráfico com base estrita na fusão dos seguintes pilares operacionais confluentes:

1. REVERSÃO EM REGIÃO DE TENDÊNCIA E LATERALIDADE COM REVERSÃO E PAVIO:
   - Zonas horizontais (Suporte/Resistência) ou inclinadas (LTA/LTB) que demonstrem histórico de bastante respeito.
   - O candle de teste deve demonstrar exaustão severa através de longos pavios de rejeição, confirmando a atuação da força oposta e a iminência da virada de padrão.

2. FLUXO DE VELA EM TENDÊNCIA DE BAIXA E ALTA (ROMPIMENTO DE S/R):
   - Identifique quando o preço rompe uma barreira de S/R com um candle de força (corpo expressivo, sem pavios longos contra o movimento).
   - Valide a urgência institucional e o fluxo de continuidade na direção do rompimento, seguindo a tendência macro instalada.

3. PULLBACK EM TENDÊNCIA DE ALTA, BAIXA E LATERAL COM RETRAÇÃO COM PAVIO:
   - Após o rompimento de zonas horizontais ou inclinadas, aguarde o preço retornar para testar a zona rompida (antigo suporte vira resistência e vice-versa).
   - O candle de teste do pullback DEVE deixar pavio nítido de retração, provando que a zona foi defendida.

4. FLUXO DE CONTINUIDADE PÓS-REVERSÃO DO MERCADO:
   - Assim que ocorrer uma virada estrutural validada e o mercado confirmar a quebra da tendência anterior, pegue a continuidade do fluxo a favor da nova direção recém-estabelecida.

[PASSO 6: PROTOCOLO DE FILTRAGEM DE RUÍDO E REGRAS DE BLOQUEIO]
- BLOQUEIO DE RETRAÇÃO CURTA: Proibido operar retração em velas que deixem pavios minúsculos ou corpos excessivamente curtos sem expressividade (pequenas oscilações de ruído). A retração deve ser clara, longa e impactante.
- FILTRO ANTI-XADREZ: Aborte se houver uma alternância perfeita de cores (verde-vermelho) por mais de 6 a 8 velas seguidas.
- FILTRO DE MICRO-VELAS: Aborte se identificar 3 ou mais Dojis legítimos consecutivos.

[PASSO 7: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]
- Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. Sinais fracos abaixo de 80% devem ser descartados como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

[PASSO 8: CRONOMETRAGEM DE EXECUÇÃO E GESTÃO DE LOTE]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente do relógio visível da plataforma. Expiração fixa de 1 minuto para fechar na mesma vela do clique projetado.
- Defina a recomendação de capital proporcionalmente à taxa: Soros (90-95%), Mão Fixa (85-89%), Mão Leve (80-84%) ou Parada Obrigatória (Abortada).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADA: [Descreva minuciosamente qual combinação exata ocorreu na tela: se foi Reversão com bastante respeito + Pavio, se foi Rompimento + Fluxo, se foi Pullback + Retração Longa de Pavio ou se foi Fluxo Pós-Reversão analisando o alvo do preço]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO MACRO: [TENDÊNCIA MAJORITÁRIA DE ALTA / TENDÊNCIA MAJORITÁRIA DE BAIXA / CONSOLIDAÇÃO LATERAL SEVERA]
📈 LEITURA DO RSI PADRÃO: [Descreva a posição e a INCLINAÇÃO ANGULAR do RSI]
📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Explique a região que o preço está ou irá buscar e por que levará esse tempo exato até o clique]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Avaliação da Tendência Majoritária e Região Synch: [Análise da macro e o alvo que o preço está buscando]
- Comportamento Gráfico do RSI (Filtro Inclinado): [Explique como a angulação inclinada do RSI validou ou se a falta de inclinação bloqueou]
- Verificação de Bloqueios (Retração Curta e Ruídos): [Justifique se a retração foi longa e forte o suficiente para evitar o bloqueio de retração curta]
- Mapeamento das Regiões de Respeito (S/R, LTA/LTB): [Descreva as microzonas]
- Diagnóstico do Fluxo de Continuidade ou Pullback (Cor, Impulso e Corpo): [Análise anatômica das velas, pavios e rompimentos]
- Posicionamento da Média Móvel (EMA 9): [Relação do preço com a EMA 9]
- Justificativa da Gestão de Lote sob Frieza Máxima: [Por que o lote sugerido se adequa a esses fatores rígidos]

Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
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
    imagem_aberta = Image.open(uploaded_file)
    st.image(imagem_aberta, caption="Gráfico Carregado com Sucesso", use_container_width=True)
    
    if st.button("🚀 Iniciar Análise de Alta Assertividade"):
        if not lista_de_chaves:
            st.error("❌ Nenhuma API Key do Gemini foi configurada na barra lateral!")
        else:
            status_placeholder = st.empty()
            resposta_sucesso = False
            resultado = ""
            
            # Loop de contingência para varrer as chaves fornecidas se houver erro
            for i, chave_atual in enumerate(lista_de_chaves):
                status_placeholder.status(f"⏳ Processando análise com a chave de contingência #{i+1}...")
                
                resultado = executar_chamada_gemini(chave_atual, imagem_aberta, PROMPT_TRADER)
                
                if "ERRO_GERADO:" not in resultado:
                    status_placeholder.empty()
                    st.success("✅ Análise gerada com sucesso!")
                    st.markdown(resultado)
                    resposta_sucesso = True
                    break
                else:
                    st.warning(f"⚠️ Chave #{i+1} falhou. Tentando próxima chave da lista...")
            
            if not resposta_sucesso:
                st.error("❌ Todas as chaves de contingência falharam. Verifique os limites ou a validade das chaves no console.")
            
