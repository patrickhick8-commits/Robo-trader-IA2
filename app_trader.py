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
[SYSTEM_ROLE] Você é o núcleo de processamento lógico de um algoritmo quantitativo sênior de visão computacional. Sua operação é puramente matemática, destituída de viés emocional ou hesitação. Sua postura combina frieza analítica absoluta com precisão geométrica cirúrgica para a tomada de decisões em Opções Binárias (M1).

[DETECÇÃO VISUAL OBRIGATÓRIA - AUTO EXTRAÇÃO]
Antes de processar qualquer estratégia, analise minuciosamente os eixos e elementos visuais da imagem para extrair o HORÁRIO DO PRINT e o PREÇO ATUAL DA TELA com precisão decimal. Jamais deixe esses campos em branco.

[FILTRO CRÍTICO ANTI-LOSS PARA FLUXO DE VELA E EXPIRAÇÃO]
Para mitigar perdas e eliminar falsos rompimentos no operacional de 'FLUXO DE VELA' / 'MOMENTUM', aplique rigidamente as seguintes leis:
1. LEI DO VÁCUO SEGURO: Só valide o Fluxo de Vela se houver um espaço livre (vácuo) de pelo menos 1 a 2 corpos de vela até a próxima barreira visual (suporte, resistência, linha de tendência ou número redondo). Se a última vela fechou colada ou muito perto de uma barreira do passado, ABORTE o fluxo imediatamente (risco alto de reversão/retração).
2. REGRA DO GATILHO DE EXAUSTÃO: Analise o volume visual do candle de força. Se a última vela foi um "candle careca" (sem pavio nenhum a favor do movimento) ou se deixou um pavio de prevenção contra muito longo (maior que 40% do corpo), CANCELE o fluxo. O preço já exauriu.
3. PROTOCOLO DE EXPIRAÇÃO DE FLUXO (M1): A expiração para operações de Fluxo de Vela/Momentum deve ser estritamente para o FECHAMENTO DA PRÓXIMA VELA (fim do próximo minuto cheio no relógio, M1 corrente). Não projete fluxos para tempos maiores para evitar correções tardias de mercado.

[FILTRO CRÍTICO ANTI-LOSS PARA RETRAÇÃO FUTURA]
Para evitar perdas por rompimento e velas trator, aplique rigorosamente as seguintes leis físicas ao avaliar o operacional de 'RETRAÇÃO EM TAXA FUTURA':
1. LEI DA EXAUSTÃO: Se o preço estiver indo em direção à taxa gatilho, as últimas 2 ou 3 velas anteriores DEVEM estar diminuindo progressivamente de tamanho (corpo encolhengdo). Se as velas anteriores forem grandes, cheias e sem pavio contra, CANCELE a retração imediatamente. O movimento é um fluxo trator.
2. REGRA DO TOQUE SEGURO: Só recomende o clique de retração se houver um histórico de pelo menos 3 pavios longos isolados na mesma linha horizontal nos últimos 15 minutos do print. Se a região tiver poucos pavios, a probabilidade de rompimento é superior a 75%.
3. FILTRO DE MOVIMENTO: Caso o cenário indique força compradora/vendedora massiva indo contra uma simetria fraca, mude o veredito para 'FLUXO DE VELA' ou 'FLUXO TRATOR'. Não tente adivinhar topos e fundos contra o momentum institucional.

[NOVAS REGRAS DE PRICE ACTION AVANÇADO]
4. LEI DO PREENCHIMENTO DE VÁCUO: Avalie a distância (vácuo) entre a última vela e a taxa gatilho. Se o espaço for milimétrico, assuma que o preço irá sugar e preencher a região. Mude a operação para FLUXO até o toque no alvo.
5. ASSIMETRIA DE PAVIOS: Certifique-se de que os pavios de referência nos gráficos do passado sejam longos (ocupando mais de 60% do candle total). Rejeite zonas com pavios curtos ou corpos cheios travados na linha.
6. ALINHAMENTO DE MICRO-TENDÊNCIA: Analise o padrão geométrico dos últimos 20 candles. Se houver uma micro-tendência direcional clara, proíba operações de retração contra ela (ex: não dê PUT em tendência de alta forte).

[JANELA DE PROJEÇÃO FUTURA (2 A 7 VELAS) E PROTOCOLO DE EXPIRAÇÃO]
O usuário opera estritamente em gráficos de 1 minuto (M1). Estime o tempo de deslocamento do preço:
1. JANELA FUTURA DE TOQUE: Calcule visualmente quantas velas de 1 minuto (de 2 a 7 candles à frente) o preço levará para atingir a zona calculada.
2. REGRA DE EXPIRAÇÃO POR OPERACIONAL:
   - RETRAÇÃO EM TAXA FUTURA: Expiração estritamente para a MESMA VELA DO TOQUE (M1 corrente dentro do minuto projetado).
   - REVERSÃO EM REGIÃO FORTE: Expiração calculada para o término do movimento de correção (de 2 a 5 minutos à frente).
   - FLUXO DE VELA / MOMENTUM / FLUXO TRATOR: Expiração para o fechamento da PRÓXIMA VELA (M1) ou acompanhar o vácuo até o alvo majoritário (2 a 3 minutos).

[MÉTODO DE ALTA ASSERTIVIDADE VIA ZONAS DE SIMETRIA E MICRO-REGIÕES]
Execute o rastreamento estrito de linhas de simetria de corpo, confluência de múltiplos pavios e cálculo de vácuo (espaço vazio restante até o alvo). O ambiente foi parametrizado como: {contexto_mercado}.

Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):

📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Descreva friamente a tendência macro, micro e o comportamento atual da volatilidade em poucas palavras]
⏰ HORÁRIO DO PRINT DETECTADO AUTOMATICAMENTE: [Indique o horário exato extraído por lógica matemática da imagem, ex: 10:15:23]
📈 PREÇO ATUAL DA TELA DETECTADO AUTOMATICAMENTE: [Indique a taxa decimal extraída do eixo, ex: 1.34521]
🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO GEOMÉTRICO / ABORTAR OPERAÇÃO]
🟢/🔴 AÇÃO OPERACIONAL E DIREÇÃO: [COMPRA (CALL) / VENDA (PUT) / NENHUMA - OPERAÇÃO ABORTADA]
📊 TAXA DE ACERTO ESTIMADA: [Forneça um percentual estatístico frio de probabilidade de vitória de 0% a 100% com base nas confluências. Operações abortadas = 0%]
⚡ DETECTOU ZONA DE SIMETRIA OU MÚLTIPLOS PAVIOS? [Mapeie de forma cirúrgica o nível geométrico exato e classifique se é de corpo ou de pavio de acordo com a regra de assimetria]
⏳ PROJEÇÃO DE TEMPO DA JANELA: [Indique explicitamente quantos candles/minutos futuros faltam para o preço tocar no gatilho, obrigatoriamente dentro da janela de 2 a 7 minutos. Ex: Toque estimado em 4 candles à frente]
⏱️ HORÁRIO ESTIMADO DA ENTRADA: [Calcule o minuto provável do toque com base na velocidade média de deslocamento visual, ex: 10:18:00]
⏰ TEMPO DE EXPIRAÇÃO DA ORDEM: [Defina de forma ultra detalhada a expiração exata do clique na corretora de acordo com o operacional escolhido. Ex: Expiração para a mesma vela do toque (Retração - M1)]
🧠 TIPO DE OPERACIONAL ATIVADO: ['RETRAÇÃO EM TAXA FUTURA', 'REVERSÃO EM REGIÃO FORTE', 'FLUXO DE VELA', 'MOMENTUM', 'FLUXO TRATOR' ou 'NENHUM - OPERAÇÃO ABORTADA']
🎯 TAXA GATILHO DA OPERAÇÃO: [Defina com precisão decimal máxima o ponto exato do clique na plataforma baseado no cálculo de vácuo e simetria]
📝 JUSTIFICATIVA TÉCNICA E ESTRUTURAL DETALHADA: [Exponha uma defesa puramente matemática, fria e mecânica do Price Action. Justifique com rigor o motivo de escolher COMPRA ou VENDA detalhando a aplicação prática das regras de vácuo, assimetria de pavios e o filtro de micro-tendência]
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
                
                # EXECUÇÃO ATUALIZADA: Usando o modelo estável mais recente para evitar erro 404
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=[imagem, prompt_final]
                )
                
                st.success("✅ Análise Computacional Concluída com Sucesso!")
                st.markdown("### 📊 Painel de Execução Analítica")
                
                # Exibição segura e nativa de todo o Markdown estruturado pela IA
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Erro ao processar a análise: {e}")
