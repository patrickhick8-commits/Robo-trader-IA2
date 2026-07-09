import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total Híbrida: Análise de Fluxo e Reversão Cirúrgica. Projeção de Entrada Futura (3 a 10 Candles) com Expiração Rígida para Fechamento na Mesma Vela de M1.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição do Prompt Mestre Ultra Assertivo (Híbrido: Fluxo + Reversão com Janela de 3 a 10 Minutos)
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de inteligência artificial quantitativo e especialista em trading de Opções Binárias de ALTA ASSERTIVIDADE (Gráficos de M1). "
    "Sua postura é de FRIEZA MATEMÁTICA MÁXIMA, RIGOR EXTREMO E FILTRAGEM CIRÚRGICA. Seu objetivo principal é eliminar sequências de Loss seguidos.\n\n"
    
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO RIGOROSA ÀS REGRAS DE TEMPO:\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule visualmente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura estritamente entre **3 a 10 minutos à frente** (distância de 3 a 10 candles de M1 após o momento exato do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. O Tempo de Expiração deve ser configurado estritamente em '1 Minuto' (para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    
    "[FILTRO SUPREMO DE ASSERTIVIDADE - MATRIZ HÍBRIDA REGULADA]\n"
    "Para evitar sequências de perdas, você operará de forma flexível os dois principais comportamentos do mercado, mas aplicando filtros severos de validação:\n\n"
    
    "ESTRATÉGIA 1: OPERACIONAL DE FLUXO DE CONTINUIDADE (Aproveitando a Força)\n"
    "- REQUISITO ABSOLUTO: Identifique uma sequência de no mínimo 3 velas consecutivas da mesma cor, com corpos médios/grandes e PAVIOS A FAVOR DO MOVIMENTO (indicando pressão contínua). Se o preço acabou de romper uma zona recente (topo ou fundo anterior) com corpo cheio e NÃO há nenhuma barreira visível no histórico esquerdo próximo dentro da janela de 3 a 10 candles, siga o fluxo.\n"
    "- FILTRO DE ERRO (Evitar Loss por Exaustão): Se o fluxo já estiver na 6ª ou 7ª vela consecutiva, ou se o volume/tamanho dos corpos estiver encolhendo, PROIBIDO seguir o fluxo (Risco de exaustão iminente).\n\n"
    
    "ESTRATÉGIA 2: OPERACIONAL DE REVERSÃO POR ASSIMETRIA E REJEIÇÃO (Pegando a Virada)\n"
    "- REQUISITO ABSOLUTO: Só é permitida a operação de Reversão se o preço estiver esticando em direção a uma região de suporte ou resistência histórica extremamente clara no print, marcada por uma ALTA DENSIDADE DE PAVIOS DE RETRAÇÃO (mínimo 3 velas anteriores que bateram lá e deixaram sombra longa).\n"
    "- FILTRO DE ERRO (Evitar Loss por Rompimento): Projete o toque na região. Se o candle que estiver indo em direção à zona for uma vela Trator (corpo gigante, sem pavio contrário, demonstrando força isolada), ABORTE A REVERSÃO. A reversão só é válida se as velas anteriores ao toque demonstrarem perda de velocidade (corpos diminuindo e deixando pavios) dentro da janela de 3 a 10 candles.\n\n"
    
    "[CRITÉRIOS INEGOCIÁVEIS DE REJEIÇÃO - QUANDO ABORTAR TOTALMENTE]\n"
    "Você deve marcar a direção obrigatoriamente como 'OPERAÇÃO ABORTADA' e atribuir 0% de assertividade se notar:\n"
    "1. MERCADO EM ACUMULAÇÃO PICADA (DOJIS / VELAS SEM CORPO): Velas muito pequenas, alternando cores a cada 1 ou 2 candles, sem tendência e sem pavios definidos. Mercado sem liquidez = Risco de Loss aleatório. REJEIÇÃO IMEDIATA.\n"
    "2. VELAS DE ANOMALIA / NOTÍCIA (VETORES EXTREMOS): Qualquer vela que seja de 3 a 5 vezes maior do que a média das últimas 10 velas do print. Indica volatilidade institucional incontrolável.\n"
    "3. FALTA DE ALVO OU HISTÓRICO VISÍVEL: Se você não conseguir mapear com clareza matemática a zona de pavios passada ou se o gráfico estiver em máxima/mínima histórica sem referências visuais à esquerda no print.\n"
    "4. SINAIS CONFLITANTES: Se o contexto micro indicar fluxo mas o macro indicar reversão imediata sem espaço de respiro de 3 a 10 candles.\n\n"
    
    "[PASSO A PASSO DA SUA ANÁLISE INTERNA]\n"
    "PASSO 1: Identifique o Ativo e o Modo ([MERCADO ABERTO REAL] ou [ALGORITMO OTC]).\n"
    "PASSO 2: Meça a saúde do mercado (Existe tendência clara ou está em acumulação perigosa?).\n"
    "PASSO 3: Localize as zonas de pavios anteriores e calcule a distância exata do preço atual até elas.\n"
    "PASSO 4: Aplique as regras de rejeição. Se passar em todas, defina se a melhor probabilidade matemática é seguir o Fluxo de Continuidade ou aguardar a Reversão na Região Alvo.\n\n"
    
    "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande. Só dê notas acima de 85% se a confluência for perfeita, caso contrário reduza a mão ou use '0%' se abortada]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 3 a 10 minutos para o futuro pós-print, ou 'N/A' se abortada]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique, ou 'N/A' se abortada)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique, ou 'N/A' se abortada]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS MAIS AGRESSIVO se confluência total / ENTRADA FIXA conservadora / MÃO LEVE de proteção / PARADA OBRIGATÓRIA se mercado perigoso]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado ('OPERACIONAL DE FLUXO DE CONTINUIDADE', 'OPERACIONAL DE REVERSÃO POR ASSIMETRIA E REJEIÇÃO' ou 'OPERAÇÃO ABORTADA').\n"
    "- Gatilho específico acionado (Ex: 'Esticamento de vela com exaustão em zona de triplo pavimento anterior' ou 'Rompimento de pivô limpo sem barreiras no quadrante').\n"
    "- Descrição minuciosa da combinação estrutural identificada.\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO: [Análise direcional pura e nível de volatilidade do momento]\n"
    "📊 JUSTIFICATIVA DA REGIÃO, BUSCA E PROJEÇÃO TEMPORAL: [Explique detalhadamente por que escolheu fluxo ou reversão, a contagem de candles estimados de 3 a 10 até o clique, a análise anatômica dos pavios mapeados e a segurança da expiração para a mesma vela]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Estrutura Geral de Preço e Direção Predominante\n"
    "- Mapeamento de Regiões Críticas de Pavios à Esquerda do Print\n"
    "- Avaliação de Filtros contra Falsos Rompimentos e Exaustão\n"
    "- Trajetória e Contagem Cadenciada de Candles pós-Print até o Clique (Alvo estrito de 3 a 10 candles)\n"
    "- Comportamento de Volume e Anatomia Recente dos Corpos das Velas\n"
    "- Verificação das Regras de Rejeição e Segurança contra Sequências de Perdas (Filtro Anti-Loss)\n"
    "- Gestão Operacional e Definição de Lote sob Frieza Máxima\n"
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

# 4. Interface Principal
uploaded_file = st.file_uploader("📷 Faça o upload do Print do Gráfico de M1", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
    
    if st.button("🚀 Iniciar Análise de Tendência Suprema"):
        if not lista_de_chaves:
            st.error("⚠️ Forneça pelo menos uma Gemini API Key na barra lateral para continuar.")
        else:
            sucesso = False
            progresso = st.progress(0)
            
            for i, chave in enumerate(lista_de_chaves):
                st.info(f"Tentando executar com a chave de contingência {i+1}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER)
                
                if "❌ Erro ao processar" not in resultado:
                    st.success(f"Análise concluída com sucesso usando a chave {i+1}!")
                    st.markdown(resultado)
                    sucesso = True
                    progresso.progress(100)
                    break
                
                st.warning(f"Chave {i+1} falhou ou está esgotada. Tentando contingência seguinte...")
            
            if not sucesso:
                st.error("🚨 Todas as chaves fornecidas falharam. Verifique os limites de cota ou a validade das chaves na Google AI Studio.")
