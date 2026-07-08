import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção de Entrada Futura (3 a 10 Candles) com Expiração Rígida para Fechamento na Mesma Vela de M1.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição Limpa do Prompt Mestre
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (Gráficos de M1). "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
    "[DIRETRIZ DE SEGURANÇA E CRONOMETRAGEM CRÍTICA: FECHAMENTO NA MESMA VELA M1]\n"
    "ATENÇÃO MÁXIMA ÀS REGRAS DE TEMPO:\n"
    "1. PROJEÇÃO DO CLIQUE DA ENTRADA: Calcule milimetricamente o deslocamento do preço e jogue o HORÁRIO DO CLIQUE da entrada para uma janela futura entre **3 a 10 minutos à frente** (equivalente a uma distância de 3 a 10 candles de M1 após o momento do print do gráfico).\n"
    "2. TEMPO DE EXPIRAÇÃO OBRIGATÓRIO: A operação DEVE SEMPRE terminar e fechar no tempo da MESMA VELA de M1 em que o clique foi realizado. Portanto, o Tempo de Expiração deve ser fixado estritamente em '1 Minuto' (ou para o final da mesma vela do clique), garantindo que o HORÁRIO DE FECHAMENTO DA ORDEM seja exatamente 1 minuto após o clique de entrada. Nunca use expirações longas.\n\n"
    "[GATILHO DE REVERSÃO POR EXAUSTÃO ESTICADA]\n"
    "Se você detectar que o preço está subindo/descendo agressivamente em direção a uma região de suporte ou resistência forte, "
    "empurrado por velas de força (compradoras/vendedoras cheias), você está PROIBIDO de dar um sinal de reversão imediata no momento do print.\n"
    "Use o comportamento esticado como um ÍMÃ: calcule quantas velas essa força institucional precisará (de 3 a 10 candles futuros) "
    "para esticar totalmente e atingir o topo da resistência ou o fundo do suporte mapeado. "
    "Mude o operacional para OPERACIONAL DE REVERSÃO EM REGIÃO, projete o clique da entrada para o minuto exato do toque futuro (3 a 10 min à frente) "
    "e defina a expiração para fechar na mesma vela, capturando a retração isolada desse candle de exaustão institucional.\n\n"
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
    "Identifique se há uma sequência de 4 velas ou mais consecutivas da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.\n\n"
    "[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]\n"
    "Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões de S/R ou LTA/LTB.\n\n"
    "[PASSO 4: LOGICA DO RSI]\n"
    "Prohibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos no momento do print. Aguarde a projeção de tempo futuro (de 3 a 10 min) onde ele perderá angulação e atingirá a exaustão junto com o preço.\n\n"
    "[PASSO 5: PROTOCOLO DE BLOQUEIO]\n"
    "Bloqueie reversões precoces. Aborte se não houver alvo de suporte/resistência claro mapeado no print para frear o preço.\n\n"
    "Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado destacado e em tamanho grande]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 3 a 10 minutos para o futuro pós-print]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Configuração fixa para fechar na mesma vela M1 do clique)\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 exato correspondente ao final da mesma vela do clique]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos exatos permitidos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'OPERACIONAL DE FLUXO DE VELA EM TENDÊNCIA', 'OPERACIONAL DE PULLBACK' ou 'OPERACIONAL DE FLUXO DE CONTINUIDADE').\n"
    "- Detalhes dos gatilhos e a região alvo.\n"
    "- Descrição minuciosa da combinação (Reversão com pavio, Rompimento+Fluxo, Pullback, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência]\n"
    "📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA MOMENTUM: [Descreva o RSI projetado para o momento do clique futuro]\n"
    "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Explique detalhadamente quantos candles faltam para atingir a região após o print e por que a expiração foi cravada para a mesma vela de M1 do clique]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Trajetória e Contagem de Candles pós-Print\n"
    "- Análise de Reversão por Exaustão Esticada (Filtro de Proteção)\n"
    "- Padrão Sequencial de Cores\n"
    "- Densidade dos Pavios\n"
    "- Comportamento do RSI\n"
    "- Verificação de Bloqueios\n"
    "- Regiões de Respeito (S/R, LTA/LTB)\n"
    "- Gestão de Lote sob Frieza Máxima\n"
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

# 4. Interface Principal (Elementos Isolados)
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
