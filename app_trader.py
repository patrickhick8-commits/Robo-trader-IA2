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

# 4. Prompt Mestre Altamente Estruturado
def gerar_prompt_mestre(contexto_mercado):
    return f"""
[SYSTEM_ROLE] Você é o núcleo de processamento lógico de um algoritmo quantitativo sênior de visão computacional. Sua operação é puramente matemática, destituída de viés emocional ou hesitação. Sua postura combina frieza analítica absoluta com precisão geométrica cirúrgica para a tomada de decisões em Opções Binárias (M1).

[DETECÇÃO VISUAL OBRIGATÓRIA - AUTO EXTRAÇÃO]
Antes de processar qualquer estratégia, analise minuciosamente os eixos e elementos visuais da imagem para extrair o HORÁRIO DO PRINT e o PREÇO ATUAL DA TELA com precisão decimal. Jamais deixe esses campos em branco.

[BLOQUEIO CRÍTICO ANTI-ROMPIMENTO EM RETRAÇÃO FUTURA]
Para mitigar perdas por rompimento na estratégia de 'RETRAÇÃO EM TAXA FUTURA', aplique rigorosamente as seguintes leis físicas:
1. REGRA DO PICO DE VELA E EXTENSÃO: Se a vela atual que está indo em direção à taxa gatilho for um "Marubozu" ou um candle esticado (ocupando o tamanho equivalente a 2 ou 3 velas normais anteriores do histórico), ABORTE A RETRAÇÃO imediatamente. Velas de esticamento massivo possuem momentum institucional e rompem simetrias em mais de 85% dos casos.
2. REGRA DO TOQUE SEGURO (MÍNIMO DE PAVIOS): Só recomende a entrada de retração se houver no passado recente (últimos 15-20 candles) pelo menos 3 pavios longos e isolados ancorados exatamente sobre a mesma simetria horizontal. Se a linha tiver histórico de corpos travados ou poucos pavios, ignore o sinal por alto risco de rompimento.
3. LEI DA EXAUSTÃO PROGRESSIVA: Para aceitar uma retração futura, as últimas 2 ou 3 velas anteriores ao toque DEVEM demonstrar perda de volume (corpos encolhendo gradativamente). Se os corpos estiverem aumentando de tamanho conforme se aproximam da taxa, mude o veredito para 'ABORTAR' ou mude para 'FLUXO TRATOR'. Não opere retração contra momentum ascendente/descendente de aceleração.

[FILTRO CRÍTICO ANTI-LOSS PARA FLUXO DE VELA]
4. LEI DO VÁCUO SEGURO: Só valide o Fluxo de Vela se houver um espaço livre (vácuo) de pelo menos 1 a 2 corpos de vela até a próxima barreira visual (suporte, resistência, linha de tendência ou número redondo). Se a última vela fechou colada ou muito perto de uma barreira do passado, ABORTE o fluxo imediatamente.
5. PROTOCOLO DE EXPIRAÇÃO DE FLUXO (M1): A expiração para operações de Fluxo de Vela/Momentum deve ser estritamente para o FECHAMENTO DA PRÓXIMA VELA (fim do próximo minuto cheio no relógio, M1 corrente).

[NOVAS REGRAS DE PRICE ACTION AVANÇADO]
6. LEI DO PREENCHIMENTO DE VÁCUO: Avalie a distância (vácuo) entre a última vela e a taxa gatilho. Se o espaço for milimétrico, assuma que o preço irá sugar e preencher a região. Mude a operação para FLUXO até o toque no alvo.
7. ASSIMETRIA DE PAVIOS: Certifique-se de que os pavios de referência nos gráficos do passado sejam longos (ocupando mais de 60% do candle total). Rejeite zonas com pavios curtos ou corpos cheios travados na linha.
8. ALINHAMENTO DE MICRO-TENDÊNCIA: Analise o padrão geométrico dos últimos 20 candles. Se houver uma micro-tendência direcional clara, proíba operações de retração contra ela (ex: não dê PUT em tendência de alta forte).

[JANELA DE PROJEÇÃO FUTURA (2 A 7 VELAS) E PROTOCOLO DE EXPIRAÇÃO]
O usuário opera estritamente em gráficos de 1 minuto (M1). Estime o tempo de deslocamento do preço:
1. JANELA FUTURA DE TOQUE: Calcule visualmente quantas velas de 1 minuto (de 2 a 7 candles à frente) o preço levará para atingir a zona calculada.
2. REGRA DE EXPIRAÇÃO POR OPERACIONAL:
   - RETRAÇÃO EM TAXA FUTURA: Expiração estritamente para a MESMA VELA DO TOQUE (M1 corrente dentro do minuto projetado).
   - REVERSÃO EM REGIÃO FORTE: Expiração calculada para o término do movimento de correção (de 2 a 5 minutos à frente).
   - FLUXO DE VELA / MOMENTUM / FLUXO TRATOR: Expiração para o fechamento da PRÓXIMA VELA (M1) ou acompanhar o vácuo até o alvo majoritário (2 a 3 minutos).

[MÉTODO DE ALTA ASSERTIVIDADE VIA ZONAS DE SIMETRIA E MICRO-REGIÕES]
Execute o rastreamento estrito de linhas de simetria de corpo, confluência de múltiplos pavios e cálculo de vácuo (espaço vazio restante até o alvo). O ambiente foi parametrizado como: {contexto_mercado}.

Sua resposta DEVE ser estritamente estruturada seguindo o padrão de tags abaixo para que o parser do código consiga organizar a interface gráfica do usuário. Não adicione textos fora das tags:

[TAXA] O valor decimal exato da taxa calculada, ex: 1.34521
[HORARIO] O horário estimado para a entrada, ex: 10:18:00
[ACAO] Ação exata em texto puro: COMPRA (CALL), VENDA (PUT) ou OPERAÇÃO ABORTADA
[DETALHES]
📊 CONTEXTO E VOLATILIDADE DETECTADA PELA IA: [Detalhes]
⏰ HORÁRIO DO PRINT DETECTADO AUTOMATICAMENTE: [Detalhes]
📈 PREÇO ATUAL DA TELA DETECTADO AUTOMATICAMENTE: [Detalhes]
🚨 VEREDITO REAL DE CONFIANÇA: [Detalhes]
📊 TAXA DE ACERTO ESTIMADA: [Detalhes]
⚡ DETECTOU ZONA DE SIMETRIA OU MÚLTIPLOS PAVIOS? [Detalhes]
⏳ PROJEÇÃO DE TEMPO DA JANELA: [Detalhes]
⏰ TEMPO DE EXPIRAÇÃO DA ORDEM: [Detalhes]
🧠 TIPO DE OPERACIONAL ATIVADO: [Detalhes]
📝 JUSTIFICATIVA TÉCNICA E ESTRUTURAL DETALHADA: [Detalhes]
"""

# 5. Execução da Análise
if botao_analise:
    if not api_key:
        st.error("Por favor, insira sua Gemini API Key na barra lateral.")
    elif not uploaded_file:
        st.error("Por favor, faça o upload do print do gráfico.")
    else:
        with st.spinner("🧠 Varrendo eixos gráficos, simetrias e aplicando filtros anti-loss..."):
            try:
                # Inicializa o cliente oficial da SDK do Gemini
                client = genai.Client(api_key=api_key)
                
                # Abre a imagem salva
                imagem = Image.open(uploaded_file)
                
                # Gera o prompt dinâmico blindado
                prompt_final = gerar_prompt_mestre(tipo_mercado)
                
                # Executa o modelo de visão estável de produção vigente (gemini-3.6-flash)
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=[imagem, prompt_final]
                )
                
                texto_resposta = response.text
                
                # Parsing inteligente dos blocos prioritários
                taxa = "Não detectada"
                horario = "Não estimado"
                acao = "OPERAÇÃO ABORTADA"
                detalhes_markdown = texto_resposta
                
                for linha in texto_resposta.split('\n'):
                    if linha.startswith("[TAXA]"):
                        taxa = linha.replace("[TAXA]", "").strip()
                    elif line_clean := linha.strip():
                        if line_clean.startswith("[HORARIO]"):
                            horario = line_clean.replace("[HORARIO]", "").strip()
                        elif line_clean.startswith("[ACAO]"):
                            acao = line_clean.replace("[ACAO]", "").strip()
                
                # Limpa as tags de controle do texto de detalhes final
                if "[DETALHES]" in detalhes_markdown:
                    detalhes_markdown = detalhes_markdown.split("[DETALHES]")[-1].strip()
                
                st.success("✅ Análise Computacional Concluída com Sucesso!")
                
                # ----------------------------------------------------
                # PAINEL DE SINAIS DE ACESSO RÁPIDO (UM AO LADO DO OUTRO / NO TOPO)
                # ----------------------------------------------------
                st.markdown("### 🎯 SINAL DE ENTRADA IMEDIATO")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(label="🎯 TAXA GATILHO", value=taxa)
                with col2:
                    st.metric(label="⏱️ HORÁRIO ESTIMADO", value=horario)
                with col3:
                    if "COMPRA" in acao or "CALL" in acao:
                        st.success(f"🟢 {acao}")
                    elif "VENDA" in acao or "PUT" in acao:
                        st.error(f"🔴 {acao}")
                    else:
                        st.warning(f"⚪ {acao}")
                
                # ----------------------------------------------------
                # PAINEL DETALHADO VERTICAL (UM EMBAIXO DO OUTRO)
                # ----------------------------------------------------
                st.markdown("---")
                st.markdown("### 📊 Relatório Técnico Detalhado Sequencial")
                
                # Imprime todas as especificações do Price Action empilhadas sequencialmente
                st.markdown(detalhes_markdown)
                
            except Exception as e:
                st.error(f"Erro ao processar a análise: {e}")
