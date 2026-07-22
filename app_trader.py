import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(
    page_title="Agente IA Advanced - Matriz Suprema", 
    page_icon="🤖", 
    layout="centered"
)

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção Temporal Avançada (2 a 5 Minutos), Reversão em Região Bastante Respeitada Aonde o Preço Realmente Reverteu, Fluxo de Cores e Retração.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input(
    "Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", 
    type="password"
)
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição Limpa do Prompt Mestre (Otimizado para Janela de 2 a 5 Minutos e Expiração Dinâmica)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias e análise gráfica puramente visual. "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
    "[DIRETRIZ DE SEGURANÇA MÁXIMA: GATILHO DE REVERSÃO POR EXAUSTÃO ESTICADA]\n"
    "ATENÇÃO: Para eliminar os erros anteriores de reversão, aplique a leitura de deslocamento temporal. "
    "Se você detectar que o preço está subindo/descendo agressivamente em direção a uma região de suporte ou resistência forte, "
    "empurrado por velas de força (compradoras/vendedoras cheias), você está PROIBIDO de dar um sinal de reversão imediata.\n"
    "Você deve usar o comportamento esticado como um ÍMÃ: calcule quantas velas essa força institucional precisará "
    "para esticar totalmente e atingir o topo da resistência ou o fundo do suporte mapeado. "
    "Mude o operacional para OPERACIONAL DE REVERSÃO EM REGIÃO, mas jogue o HORÁRIO DO CLIQUE de 2 a 5 minutos para o futuro "
    "(janela ideal de 2 a 5 minutos à frente do print). A lógica é permitir que o mercado termine de esticar a tendência "
    "e fazer a entrada de venda (PUT) ou compra (CALL) cirurgicamente no minuto em que as velas de força perderem o fôlego.\n\n"
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
    "Identifique se há uma sequência de 4 velas ou mais consecutivas da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.\n\n"
    "[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]\n"
    "Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões de S/R ou LTA/LTB.\n\n"
    "[PASSO 4: LOGICA DE REVERSÃO INTELIGENTE POR EXAUSTÃO NO TEMPO EM REGIÃO DE RESPEITO (2 A 5 MINUTOS)]\n"
    "Projete o movimento tempo futuro com base estrita no último candle visível do print enviado. Identifique a região de suporte ou resistência de forte respeito histórico — onde o preço realmente reverteu no passado visível — e calcule o momento exato em que o movimento esticado chegará a esse teto ou fundo máximo para ativar a reversão na janela exata de 2 a 5 minutos à frente.\n\n"
    "[PASSO 5: REGRA DO RSI]\n"
    "Proibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos. Aguarde a disposição de tempo futuro onde ele perderá angulação.\n\n"
    "[PASSO 6: DETERMINAÇÃO DO TEMPO DE EXPIRAÇÃO DA OPERAÇÃO]\n"
    "Defina e ajuste de forma estritamente personalizada o tempo de expiração da ordem de acordo com a mecânica da operação analisada. "
    "Se for Retração Clássica de Pavio, use o tempo restante do candle atual (ou M1). Se for Reversão por Exaustão na Região ou Pullback, projete uma expiração adequada "
    "(ex: M1, M2, M5) que garanta tempo suficiente para o preço respeitar a análise pós-clique. Nunca fixe um tempo padrão; determine caso a caso.\n\n"
    "[PASSO 7: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]\n"
    "Avalie com base em: 1. OPERACIONAL DE REVERSÃO EM REGIÃO BASTANTE RESPEITADA (POR EXAUSTÃO ESTICADA), 2. FLUXO DE CONTINUIDADE (4+ VELAS), 3. FLUXO PARA RETRAÇÃO.\n\n"
    "[PASSO 8: PROTOCOLO DE BLOQUEIO]\n"
    "Bloqueie reversões precoces. Aborte se não houver alvo claro.\n\n"
    "[PASSO 9: CRONOMETRAGEM E GESTÃO]\n"
    "Projete o clique entre 2 a 5 minutos à frente com base no último candle visível. Taxa de acerto de 80% a 95% ou Abortada (0%).\n\n"
    "Retorne o diagnóstico estruturado exatamente neste formato markdown:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 (Janela de 2 a 5 minutos à frente do print)]\n"
    "⏳ TEMPO DE EXPIRAÇÃO DA ORDEM: [Definir aqui o tempo ideal calculado sob medida para este operacional - ex: 1 min, 2 min, 5 min]\n"
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
    "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa do cálculo de 2 a 5 minutos, do histórico de reversão da região escolhida e da expiração escolhida]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Trajetória pós-Print\n"
    "- Análise de Reversão por Exaustão Esticada em Região Histórica (Filtro de Proteção)\n"
    "- Padrão Sequencial de Cores\n"
    "- Densidade dos Pavios\n"
    "- Comportamento do RSI\n"
    "- Verificação de Bloqueios\n"
    "- Regiões de Respeito Comprovado\n"
    "- Gestão de Lote\n"
)

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    try:
        client = genai.Client(api_key=chave_api)
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=[imagem_objeto, prompt_comando]
        )
        return response.text
    except Exception as e:
        return f"❌ Erro da API: {str(e)}"

# 4. Interface Principal 
uploaded_file = st.file_uploader(
    "📷 Faça o upload do Print do seu Gráfico (M1):", 
    type=["png", "jpg", "jpeg"]
)

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
                
                if "❌ Erro da API:" not in resultado:
                    st.success("Análise concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso = True
                    break
                else:
                    st.error(f"Falha na Chave {i+1}:")
                    st.code(resultado)
                    st.warning("Tentando próxima chave de contingência da lista...")
            
            if not sucesso:
                st.error("Todas as chaves fornecidas falharam. Verifique os códigos de erro acima e configure suas credenciais no Google AI Studio.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda para liberar o processamento.")
