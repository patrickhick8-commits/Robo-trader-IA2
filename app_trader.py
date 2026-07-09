import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema e Projeção Temporal")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), Fluxo de Cores, EMA 9, Suporte/Resistência, LTA e LTB.")

# 2. Barra Lateral
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# 3. Definição do Prompt Mestre Sem Ruído (Foco em Estrutura Pura + EMA 9)
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em encontrar oportunidades frequentes e de boa precisão para Opções Binárias (M1). Sua postura é de rigidez matemática filtrando ruídos menores: seu objetivo é extrair sinais válidos do gráfico por confluência exata de fatores estruturais.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA E CONFLUÊNCIA COM EMA 9]
- Rastreie visualmente o fluxo do preço em relação à Média Móvel Exponencial de 9 períodos (EMA 9).
- COMPRA (CALL): Preço obrigatoriamente ACIMA da EMA 9 com inclinação ascendente.
- VENDA (PUT): Preço obrigatoriamente ABAIXO da EMA 9 com inclinação descendente.
- Valide as correções rápidas e continuidades de movimento usando a média como linha divisória de viés.

[PASSO 3: MATRIZ DE ESTRATÉGIA ADAPTATIVA MULTI-CONFLUENTE]
Busque de forma ativa por confluências de Price Action em Suporte, Resistência (S/R) e Linhas de Tendência (LTA/LTB). Funda as estratégias para buscar a maior quantidade de confluências possíveis:

1. SE O MERCADO ESTIVER EM TENDÊNCIA NÍTIDA:
   - MODO FLUXO / ROMPIMENTO EM TENDÊNCIA: Se houver rompimento de zonas de S/R ou LTA/LTB por velas institucionais cheias (Marubozu) a favor da EMA 9, opere a continuidade imediata (Fluxo).
   - MODO PULLBACK EM TENDÊNCIA: Monitore o preço testando a zona recém-rompida (antigo suporte que virou resistência ou vice-versa). O sinal deve ocorrer quando a vela de teste tocar a linha e demonstrar exaustão.
   - MODO RETRAÇÃO EM TENDÊNCIA / LTA / LTB: Identifique toques em canais ou linhas de tendência inclinadas onde o preço deixa pavios longos de rejeição, operando a retração a favor do canal.

2. SE O MERCADO ESTIVER EM LATERALIDADE / CONSOLIDAÇÃO:
   - MODO REVERSÃO EM LATERALIDADE (SUPORTE / RESISTÊNCIA HORIZONTAL): Opere o extremo respeito de zonas horizontais nítidas de Suporte (Fundo) e Resistência (Topo). Quando o preço testar os limites com velas de perda de pressão, opere para a reversão.
   - MODO RETRAÇÃO PELOS PAVIOS EM LATERALIDADE: Rastreie o histórico recente de pavios longos nas extremidades da consolidação. Se as velas atuais estiverem demonstrando forte rejeição visual através de pavios ao tocar a barreira horizontal, valide a entrada de retração para a mesma vela.

[PASSO 4: FILTROS ANTI-RUÍDO E MANIPULAÇÃO]
Para filtrar sinais falsos e ruídos menores do gráfico, aplique os seguintes bloqueios mecânicos:
- FILTRO ANTI-XADREZ: Aborte se houver uma alternância perfeita e sem direção de cores (verde-vermelho-verde-vermelho) por mais de 5 velas seguidas.
- FILTRO DE MICRO-VELAS: Aborte se houver uma sequência de Dojis legítimos (linhas horizontais sem corpo). Velas sem volume indicam falta de liquidez e risco de loss por frações de preço.
- FILTRO CONTRA-TENDÊNCIA: Bloqueie qualquer entrada que tente desafiar a inclinação visual da EMA 9 ou a estrutura macro do quadrante.

[PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE]
- Avalie os riscos de forma equilibrada. Quanto mais fatores confluírem juntos (ex: Toque na EMA 9 + Pavio de Retração + Zona de Suporte), maior deve ser a taxa de acerto.
- Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. 
- Só emita "OPERAÇÃO ABORTADA" (e taxa 0%) se o gráfico violar as regras anti-ruído ou estiver sem condições operáveis.

[PASSO 6: CRONOMETRAGEM DE EXECUÇÃO PADRÃO]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente (ex: se o relógio marca 10:15:20, projete o clique para entre 10:17:00 e 10:20:00).
- A expiração deve ser rígida de exatamente 1 minuto para fechar na mesma vela do clique projetado (final da vela de M1).

[PASSO 7: SUGESTÃO DE GERENCIAMENTO DE MÃO DE ENTRADA]
Defina a recomendação de capital com base na taxa calculada de forma matemática:
- Taxa entre 90% e 95%: MÃO DE SOROS / ENTRADA FORTE (Cenário de confluência tripla/máxima).
- Taxa entre 85% e 89%: ENTRADA FIXA padrão (Cenário bom com confluência dupla).
- Taxa entre 80% e 84%: MÃO LEVE / REDUZIDA (Oportunidade isolada de retração ou fluxo simples).
- Operação Abortada: PARADA OBRIGATÓRIA (Cenário sem condições mínimas).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADO: [Descreva o operacional]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / CONSOLIDAÇÃO LATERAL / MERCADO PARADO]
📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para atingir sua zona de entrada e confirmar a confluência]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado
- Mapeamento das Regiões (S/R, LTA/LTB e Zonas de Pullback)
- Comportamento e Retração pelos Pavios
- Posicionamento da EMA 9
- Avaliação de Ruído e Volatilidade
- Diagnóstico do Fluxo de Cores e Volume por Corpo
- Justificativa da Gestão de Lote

Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
"""

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

# 4. Interface Principal de Upload e Execução
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
