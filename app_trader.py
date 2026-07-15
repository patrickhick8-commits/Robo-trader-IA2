import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção Temporal Avançada (3 a 10 Minutos), Reversão Futura por Contagem de Candles, Fluxo de Cores e Retração.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição Limpa do Prompt Mestre
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias. "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
    "[DIRETRIZ DE SEGURANÇA MÁXIMA: GATILHO DE REVERSÃO POR EXAUSTÃO ESTICADA]\n"
    "ATENÇÃO: Para eliminar os erros anteriores de reversão, aplique a leitura de deslocamento temporal. "
    "Se você detectar que o preço está subindo/descendo agressivamente em direção a uma região de suporte ou resistência forte, "
    "empurrado por velas de força (compradoras/vendedoras cheias), você está PROIBIDO de dar um sinal de reversão imediata.\n"
    "Você deve usar o comportamento esticado como um ÍMÃ: calcule quantas velas essa força institucional precisará "
    "para esticar totalmente e atingir o topo da resistência ou o fundo do suporte mapeado. "
    "Mude o operacional para OPERACIONAL DE REVERSÃO EM REGIÃO, mas jogue o HORÁRIO DO CLIQUE de 3 a 10 minutos para o futuro "
    "(janela ideal de 5 a 6 minutos à frente do print). A lógica é permitir que o mercado termine de esticar a tendência "
    "e fazer a entrada de venda (PUT) ou compra (CALL) cirurgicamente no minuto em que as velas de força perderem o fôlego.\n\n"
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
    "Identifique se há uma sequência de 4 velas ou mais consecutivas da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.\n\n"
    "[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]\n"
    "Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões de S/R ou LTA/LTB.\n\n"
    "[PASSO 4: LOGICA DE REVERSÃO INTELIGENTE POR EXAUSTÃO NO TEMPO (3 A 10 MINUTOS)]\n"
    "Projete o momento exato em que o movimento esticado chegará ao teto máximo da região de respeito e ative a reversão para o minuto da exaustão.\n\n"
    "[PASSO 5: REGRA DO RSI]\n"
    "Proibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos. Aguarde a projeção de tempo futuro onde ele perderá angulação.\n\n"
    "[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]\n"
    "Avalie com base em: 1. OPERACIONAL DE REVERSÃO EM REGIÃO (POR EXAUSTÃO ESTICADA), 2. FLUXO DE CONTINUIDADE (4+ VELAS), 3. FLUXO PARA RETRAÇÃO.\n\n"
    "[PASSO 7: PROTOCOLO DE BLOQUEIO]\n"
    "Bloqueie reversões precoces. Aborte se não houver alvo claro.\n\n"
    "[PASSO 8: CRONOMETRAGEM E GESTÃO]\n"
    "Projete o clique entre 3 a 10 minutos à frente. Taxa de acerto de 80% a 95% ou Abortada (0%).\n\n"
    "Retorne o diagnóstico estruturado exatamente neste formato markdown:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: [Tempo]\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Gerenciamento]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'OPERACIONAL DE FLUXO DE VELA EM TENDÊNCIA', 'OPERACIONAL DE PULLBACK' ou 'OPERACIONAL DE FLUXO DE CONTINUIDADE').\n"
    "- Detalhes dos gatilhos e a região alvo.\n"
    "- Descrição minuciosa da combinação (Reversão com pavio, Rompimento+Fluxo, Pullback, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [Mercado]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência]\n"
    "📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA MOMENTUM: [RSI]\n"
    "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Trajetória pós-Print\n"
    "- Análise de Reversão por Exaustão Esticada (Filtro de Proteção)\n"
    "- Padrão Sequencial de Cores\n"
    "- Densidade dos Pavios\n"
    "- Comportamento do RSI\n"
    "- Verificação de Bloqueios\n"
    "- Regiões de Respeito\n"
    "- Gestão de Lote\n"
)

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    try:
        client = genai.Client(api_key=chave_api)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[imagem_objeto, prompt_comando]
        )
        return response.text
    except Exception as e:
        return f"❌ Erro ao processar com a chave atual: {str(e)}"

# 4. Interface Principal (Elementos Isolados de Qualquer Condicional)
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 5. Execução Lógica Controlada pós-Clique
if botao_analise:
    if not uploaded_file:
        st.error("⚠️ Por favor, faça o upload de uma imagem do gráfico antes de iniciar a análise.")
    elif not lista_de_chaves:
        st.error("⚠️ Insira pelo menos uma Gemini API Key válida na barra lateral antes de analisar.")
    else:
        imagem = Image.open(uploaded_file)
        st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
        
        sucesso = False
        with st.spinner("Analisando deslocamento de velas, tempo futuro e exaustão de reversão..."):
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
                st.error("Todas as chaves de contingência fornecidas falharam. Verifique as chaves na Google AI Studio.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda para liberar o processamento.")
