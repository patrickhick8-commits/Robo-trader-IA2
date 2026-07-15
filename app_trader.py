import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Projeção Temporal Avançada (3 a 10 Minutos) e Análise de Proximidade.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição Limpa do Prompt Mestre
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias e Price Action Avançado Estrutural. "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
    "[REGRA DE OURO: PROIBIDO PADRÕES DE VELAS]\n"
    "ATENÇÃO: Você está PROIBIDO de basear suas decisões em padrões isolados de velas (como Martelo, Engolfo, Doji, etc.). "
    "Sua análise deve ignorar nomes de velas e focar puramente na ESTRUTURA DINÂMICA DO PREÇO e na anatomia física dos candles.\n\n"
    "[REGRA OPERACIONAL DA ANATOMIA DO PREÇO: RETRAÇÃO VS PULLBACK]\n"
    "Sua tomada de decisão sobre zonas estruturais e zonas ocultas deve seguir estritamente duas regras:\n"
    "1. SE O GRÁFICO APRESENTAR BASTANTE PAVIO (Alta densidade de pavios e rejeição): Você deve operar focado em RETRAÇÃO INSTANTÂNEA nas zonas estruturais ou ocultas mapeadas.\n"
    "2. SE O GRÁFICO APRESENTAR VELAS DE FORÇA OU DE CONTINUAÇÃO (Corpos cheios, expressivos e sem pavio): Você está PROIBIDO de operar retração. Você deve, obrigatoriamente, ESPERAR O ROMPIMENTO E O PULLBACK da região (ou seguir o fluxo momentâneo) para projetar a sua entrada.\n\n"
    "[ANÁLISE ESTRUTURAL DO PREÇO E LIQUIDEZ]\n"
    "Mapeie topos e fundos majoritários, canais de preço, linhas de tendência (LTA/LTB) e ZONAS OCULTAS de suporte/resistência (Order Blocks, Imbalances ou Acumulações antigas). "
    "Avalie a agressividade com que o mercado se move e calcule o espaço livre que o preço tem para correr antes de encontrar uma barreira real.\n\n"
    "[DIRETRIZ DE SEGURANÇA MÁXIMA: GATILHO DE REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]\n"
    "Mude seu comportamento dinamicamente com base na proximidade do preço em relação às zonas estruturais demarcadas:\n"
    "- Se você detectar que o preço JÁ ESTIVER NA REGIÃO de reversão forte (testando topos/fundos relevantes ou simetrias fortes), "
    "ative o [OPERACIONAL DE REVERSÃO EM REGIÃO], aplicando o filtro de anatomia (retração se houver pavio, ou aguardando o pullback se for vela de força).\n"
    "- CASO CONTRÁRIO (se o preço estiver distante da região de reversão), você está PROIBIDO de antecipar reversões. "
    "Nesse cenário, entre imediatamente a favor do [FLUXO MOMENTÂNEO DO GRÁFICO], surfando a continuidade do movimento atual até o próximo alvo estrutural de liquidez.\n\n"
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
    "Identifique se há uma sequência de 4 velas ou mais consecutivas da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.\n\n"
    "[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]\n"
    "Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões estruturais de S/R ou LTA/LTB.\n\n"
    "[PASSO 4: LOGICA DE OPERAÇÃO DINÂMICA (REVERSÃO OU FLUXO MOMENTÂNEO)]\n"
    "Avalie a distância até a zona de respeito baseado na estrutura do preço. Se estiver nela, projete o clique de reversão de 3 a 10 minutos (ideal 5 a 6 min). ""Se estiver longe, configure a entrada para seguir o fluxo momentâneo da tendência atual.\n\n"
    "[PASSO 5: REGRA DO RSI]\n"
    "Proibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos. Aguarde a perda de angulação ou siga o fluxo estrutural.\n\n"
    "[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]\n"
    "Avalie com base em: 1. LEITURA DA ESTRUTURA DO PREÇO (ALTA ASSERTIVIDADE), 2. ANATOMIA DA VELA (PAVIO = RETRAÇÃO | FORÇA = PULLBACK), 3. OPERACIONAL DE REVERSÃO EM REGIÃO (SE JÁ NA REGIÃO), 4. FLUXO MOMENTÂNEO DO GRÁFICO (SE LONGE DA REGIÃO), 5. FLUXO DE CONTINUIDADE (4+ VELAS).\n\n"
    "[PASSO 7: PROTOCOLO DE BLOQUEIO]\n"
    "Bloqueie retrações contra velas de força cheias. Aborte operações que vão contra a estrutura vigente sem confirmação de rompimento ou sem alvo claro.\n\n"
    "[PASSO 8: CRONOMETRAGEM E GESTÃO DE ALTA ASSERTIVIDADE]\n"
    "Projete o clique entre 3 a 10 minutos à frente. Atribua taxas rigorosas de assertividade entre 75% a 98% baseando-se unicamente "
    "na confluência dos fatores estruturais filtrados. Se não houver clareza técnica total na estrutura, ordene a operação como Abortada (0%).\n\n"
    "Retorne o diagnóstico estruturado exatamente neste formato markdown:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: [Tempo]\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Gerenciamento]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'FLUXO MOMENTÂNEO DO GRÁFICO', 'OPERACIONAL DE PULLBACK', ou 'OPERACIONAL DE RETRAÇÃO EM ZONA STRUCT').\n"
    "- Detalhes dos gatilhos, anatomia observada nos candles (força ou pavio) e a proximidade da região alvo estrutural.\n"
    "- Descrição minuciosa da combinação (Estrutura do preço + Retração por pavio em zona oculta, Vela de força + Espera de Pullback, Quebra de pivô + Fluxo momentâneo, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [Mercado]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência e Padrão Estrutural de Topos/Fundos]\n"
    "📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA/A FAVOR DO MOMENTUM: [RSI]\n"
    "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa baseada no deslocamento estrutural, anatomia das velas e tempo]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Trajetória pós-Print e Leitura de Estrutura do Preço (Topos, Fundos e Pivôs)\n"
    "- Análise de Reversão em Região vs Fluxo Momentâneo (Filtro de Posição Estrutural)\n"
    "- Decisão por Anatomia: Presença de pavios expressivos (Retração) ou corpo cheio (Pullback/Fluxo)\n"
    "- Padrão Sequencial de Cores e Força do Fluxo\n"
    "- Densidade dos Pavios e Regiões de Retração Estrutural\n"
    "- Comportamento do RSI e Angulação do Preço\n"
    "- Verificação de Bloqueios de Estrutura (Filtro de proteção contra velas cheias)\n"
    "- Regiões de Respeito e Alvos Disponíveis na Estrutura (Incluindo Zonas Ocultas)\n"
    "- Gestão de Lote\n"
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
            if "503" in erro_msg or "UNAVAILABLE" in erro_msg:st.write(f"⚠️ Modelo {modelo} instável (Erro 503). Chave ativa buscando modelo alternativo...")
                continue
            return f"❌ Erro na API: {erro_msg}"
            
    return "❌ Erro na API: Todos os modelos disponíveis falharam por instabilidade no servidor do Google."

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
        imagem = Image.open(uploaded_file).convert("RGB")
        st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
        
        sucesso = False
        with st.spinner("Analisando estrutura pura do preço, anatomia dos candles e tempo futuro..."):
            for i, chave in enumerate(lista_de_chaves):
                st.write(f"Tentando analisar com a chave de contingência {i+1}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER)
                
                if "❌ Erro na API:" not in resultado:
                    st.success("Análise concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso = True
                    break
                else:
                    st.warning(f"Chave {i+1} falhou. Detalhes: {resultado}")
                    st.write("Tentando próxima chave da lista...")
            
            if not sucesso:
                st.error("Todas as chaves de contingência fornecidas falharam. O servidor do Google pode estar sobrecarregado universalmente. Tente novamente em alguns instantes.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda para liberar o processamento.")
