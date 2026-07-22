import streamlit as st
from google import genai
from PIL import Image
import datetime

# 1. Configuração da Página
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Projeção Temporal Avançada (3 a 10 Minutos), Reversão Dinâmica em Região, Fluxo de Cores e Retração.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# Seletor de Modelo para evitar problemas de obsolescência futura
modelo_selecionado = st.sidebar.selectbox(
    "🤖 Versão do Motor Gemini:",
    ["gemini-1.5-flash", "gemini-2.5-flash"]
)

# 3. Definição Limpa do Prompt Mestre
PROMPT_TRADER = (
    "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias. "
    "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
    "[DIRETRIZ DE SEGURANÇA MÁXIMA: GATILHO DE REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]\n"
    "ATENÇÃO: Mude seu comportamento dinamicamente com base na proximidade do preço em relação às zonas demarcadas. "
    "Mapeie as regiões de suporte e resistência fortes. Se você detectar que o preço JÁ ESTIVER NA REGIÃO de reversão, "
    "ative o [OPERACIONAL DE REVERSÃO EM REGIÃO], projetando o enfraquecimento e a exaustão das velas dentro da zona para "
    "uma entrada contra a tendência.\n"
    "CASO CONTRÁRIO (se o preço estiver distante da região de reversão), você está PROIBIDO de forçar uma reversão antecipada. "
    "Nesse cenário, você deve ignorar a reversão e entrar imediatamente a favor do [FLUXO MOMENTÂNEO DO GRÁFICO], surfando a "
    "continuidade do movimento atual do preço até que ele se aproxime do alvo principal.\n\n"
    "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
    "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
    "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
    "Identifique se há uma sequência de 4 velas ou mais consecutiveis da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.\n\n"
    "[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]\n"
    "Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões de S/R ou LTA/LTB.\n\n"
    "[PASSO 4: LOGICA DE OPERAÇÃO DINÂMICA (REVERSÃO OU FLUXO MOMENTÂNEO)]\n"
    "Avalie a distância até a zona de respeito. Se estiver nela, projete o clique de reversão de 3 a 10 minutos (ideal 5 a 6 min). "
    "Se estiver longe, configure a entrada para seguir o fluxo momentâneo da tendência atual.\n\n"
    "[PASSO 5: REGRA DO RSI]\n"
    "Proibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos. Aguarde a perda de angulação ou siga o fluxo.\n\n"
    "[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]\n"
    "Avalie com base em: 1. OPERACIONAL DE REVERSÃO EM REGIÃO (SE JÁ NA REGIÃO), 2. FLUXO MOMENTÂNEO DO GRÁFICO (SE LONGE DA REGIÃO), 3. FLUXO DE CONTINUIDADE (4+ VELAS), 4. FLUXO PARA RETRAÇÃO.\n\n"
    "[PASSO 7: PROTOCOLO DE BLOQUEIO]\n"
    "Bloqueie reversões precoces fora da região demarcada. Aborte se o fluxo momentâneo estiver sem volume ou sem alvo claro.\n\n"
    "[PASSO 8: CRONOMETRAGEM E GESTÃO]\n"
    "Projete o clique entre 3 a 10 minutos à frente baseando-se estritamente no HORÁRIO ATUAL DO SISTEMA fornecido. Taxa de acerto de 80% a 95% ou Abortada (0%).\n\n"
    "Retorne o diagnóstico estruturado exatamente neste formato markdown:\n\n"
    "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado]\n"
    "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00]\n"
    "⏳ TEMPO DE EXPIRAÇÃO: [Tempo]\n"
    "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00]\n"
    "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
    "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Gerenciamento]\n"
    "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
    "- Tipo de operacional isolado ativado (Exemplos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'FLUXO MOMENTÂNEO DO GRÁFICO', 'OPERACIONAL DE FLUXO DE VELA EM TENDÊNCIA', ou 'OPERACIONAL DE FLUXO DE CONTINUIDADE').\n"
    "- Detalhes dos gatilhos e a proximidade da região alvo.\n"
    "- Descrição minuciosa da combinação (Reversão em região, Fluxo momentâneo por distância, Rompimento+Fluxo, etc).\n"
    "🌐 MODO DE MERCADO DETECTADO: [Mercado]\n"
    "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência]\n"
    "📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA/A FAVOR DO MOMENTUM: [RSI]\n"
    "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa]\n\n"
    "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
    "- Ambiente Identificado\n"
    "- Trajetória pós-Print\n"
    "- Análise de Reversão em Região vs Fluxo Momentâneo (Filtro de Posição)\n"
    "- Padrão Sequencial de Cores\n"
    "- Densidade dos Pavios\n"
    "- Comportamento do RSI\n"
    "- Verificação de Bloqueios\n"
    "- Regiões de Respeito e Alvos Disponíveis\n"
    "- Gestão de Lote\n"
)

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando, modelo):
    try:
        client = genai.Client(api_key=chave_api)
        
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        prompt_sincronizado = f"[INFORMAÇÃO DE CONTEXTO] HORÁRIO ATUAL DO SISTEMA DO TRADER: {hora_atual}\n\n{prompt_comando}"
        
        response = client.models.generate_content(
            model=modelo,
            contents=[imagem_objeto, prompt_sincronizado],
            config={
                'temperature': 0.0
            }
        )
        return response.text
    except Exception as e:
        return f"ERRO_API: {str(e)}"

# 4. Interface Principal
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
        with st.spinner("Analisando distância da região, fluxo momentâneo e tempo futuro..."):
            for i, chave in enumerate(lista_de_chaves):
                st.write(f"Tentando analisar com a chave de contingência {i+1} usando o modelo {modelo_selecionado}...")
                resultado = executar_chamada_gemini(chave, imagem, PROMPT_TRADER, modelo_selecionado)
                
                if "ERRO_API:" not in resultado:
                    st.success("Análise concluída com sucesso!")
                    st.markdown(resultado)
                    sucesso = True
                    break
                else:
                    st.error(f"❌ Falha na Chave {i+1}. Detalhe técnico: {resultado.replace('ERRO_API:', '')}")
                    st.warning("Tentando próxima chave da lista...")
            
            if not success:
                st.error("🚨 Todas as chaves falharam. Certifique-se de escolher um modelo suportado por sua API key no menu lateral.")

if not lista_de_chaves:
    st.info("💡 Lembrete: Insira as chaves de API na barra lateral esquerda para liberar o processamento.")
