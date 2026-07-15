import streamlit as st
from google import genai
from PIL import Image
from datetime import datetime

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Projeção Temporal Avançada (3 a 10 Minutos) e Análise de Proximidade.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Interface Principal de Inputs (Adicionado seletor de horário para eliminar alucinações da IA)
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])
horario_atual_print = st.time_input("⏰ Que horas o print foi tirado no gráfico?", datetime.now().time())

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 4. Definição do Prompt Mestre Otimizado
def gerar_prompt_mestre(horario_referencia):
    return (
        "[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro. "
        "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO MATEMÁTICA.\n\n"
        
        f"[ANCORAGEM TEMPORAL OBRIGATÓRIA]\n"
        f"O horário exato em que este print foi capturado é: {horario_referencia.strftime('%H:%M:%S')}. "
        "Qualquer cálculo de projeção de tempo (expiração de 3 a 10 minutos) DEVE usar este horário exato como ponto de partida inicial zero.\n\n"
        
        "[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]\n"
        "Você está TERMINANTEMENTE PROIBIDO de basear suas decisões em nomenclaturas de velas isoladas (como Martelo, Engolfo, Doji, etc.). "
        "Ignore nomes de velas. Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, "
        "topos/fundos majoritários, canais (LTA/LTB), zonas de simetria e o espaço vazio (vácuo de liquidez) que o preço tem para correr antes de bater em uma barreira.\n\n"
        
        "[DIRETRIZ DE SEGURANÇA: REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]\n"
        "Avalie a distância geométrica do preço atual até as zonas de suporte/resistência mais fortes visíveis no print:\n"
        "- Se o preço JÁ ESTIVER tocando ou dentro da zona cinza de rejeição (testando topos/fundos relevantes), ative o [OPERACIONAL DE REVERSÃO EM REGIÃO], projetando exaustão estrutural para uma contra-tendência.\n"
        "- Se o preço ESTIVER DISTANTE e houver espaço livre até o próximo alvo, ative o [FLUXO MOMENTÂNEO DO GRÁFICO] para surfar a continuidade até o alvo estrutural. É proibido antecipar reversões no meio do caminho.\n\n"
        
        "[PASSO A PASSO DA ANÁLISE VISUAL]\n"
        "PASSO 1: Identifique o ativo e defina se é [MERCADO REAL] ou [ALGORITMO OTC].\n"
        "PASSO 2: Verifique se há fluxo de cores (sequência de 4+ velas cheias com pavios mínimos) a favor do movimento.\n"
        "PASSO 3: Identifique a densidade de pavios. Muitos pavios longos na região indicam [OPERACIONAL DE RETRAÇÃO ESTRUTURAL].\n"
        "PASSO 4: Regra do RSI: Se o RSI estiver cruzando as linhas extremas (70/30 ou 80/20) em um ângulo reto, vertical e agressivo, NÃO reverta. Siga o fluxo ou aborte.\n"
        "PASSO 5: Cronometragem: Calcule matematicamente o clique de 3 a 10 minutos à frente baseando-se no tempo necessário para o preço cumprir o deslocamento visual restante.\n"
        "PASSO 6: Atribua taxas rigorosas de assertividade entre 75% a 98% baseando-se estritamente na confluência de fatores. Se faltar clareza visual total na estrutura, ordene o diagnóstico como Abortado (0%).\n\n""Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):\n\n"
        "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]\n"
        "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:SS]\n"
        "⏳ TEMPO DE EXPIRAÇÃO: [Ex: 5 Minutos]\n"
        "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:SS]\n"
        "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
        "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Conservador / Moderado / Abortar]\n"
        "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
        "- Tipo de operacional ativo: ['REVERSÃO EM REGIÃO', 'FLUXO MOMENTÂNEO', ou 'RETRAÇÃO ESTRUTURAL']\n"
        "- Gatilhos visuais e distância métrica até o alvo estrutural.\n"
        "🌐 MODO DE MERCADO DETECTADO: [Mercado]\n"
        "📊 CONTEXTO DO MERCADO MACRO E MICRO: [Tendência e Padrão Estrutural de Topos/Fundos]\n"
        "📈 LEITURA DO RSI PADRÃO: [Ângulo e posição do RSI]\n"
        "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa técnica baseada em deslocamento vetorial]\n\n"
        "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
        "- Resumo analítico detalhado do comportamento visual das massas do mercado na imagem."
    )

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    modelos_contingencia = ['gemini-2.5-flash', 'gemini-2.5-pro']
    
    for modelo in modelos_contingencia:
        try:
            client = genai.Client(api_key=chave_api)
            response = client.models.generate_content(
                model=modelo,
                contents=[imagem_objeto, prompt_comando]
            )
            return response.text
        except Exception as e:
            erro_msg = str(e)
            if "503" in erro_msg or "UNAVAILABLE" in erro_msg:
                st.write(f"⚠️ Modelo {modelo} instável (Erro 503). Chave ativa buscando modelo alternativo...")
                continue
            return f"❌ Erro na API: {erro_msg}"
            
    return "❌ Erro na API: Todos os modelos disponíveis falharam por instabilidade no servidor do Google."

# 5. Execução Lógica Controlada pós-Clique
if botao_analise:
    if not uploaded_file:
        st.error("⚠️ Por favor, faça o upload de uma imagem do gráfico antes de iniciar a análise.")
    elif not lista_de_chaves:
        st.error("⚠️ Insira pelo menos uma Gemini API Key válida na barra lateral antes de analisar.")
    else:
        imagem = Image.open(uploaded_file).convert("RGB")
        st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
        
        with st.spinner("Analisando estrutura pura do preço, distância e tempo futuro..."):
            prompt_dinamico = gerar_prompt_mestre(horario_atual_print)
            
            # Tenta executar usando a primeira chave válida da lista de contingência
            resultado_analise = executar_chamada_gemini(lista_de_chaves[0], imagem, prompt_dinamico)
            
            st.markdown("### 📊 Resultado da Análise da IA")
            st.markdown(resultado_analise)
