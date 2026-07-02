import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema de Alta Assertividade")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# PROMPT MESTRE RECONFIGURADO - FILTRO DE RUÍDO MÉDIO/ALTO
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (M1). Sua postura combina proteção de capital com aproveitamento inteligente de oportunidades, operando através de um filtro técnico de ruído calibrado no nível Médio-Alto para evitar falsos sinais sem engessar as operações.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA E POSICIONAMENTO DA EMA 9]
- Rastreie visualmente o fluxo do preço em relação à Média Móvel Exponencial de 9 períodos (EMA 9).
- COMPRA (CALL): O preço deve estar operando preferencialmente ACIMA da EMA 9.
- VENDA (PUT): O preço deve estar preferencialmente operando ABAIXO da EMA 9.
- Use a média como barreira flutuante ou suporte/resistência móvel, permitindo cliques imediatos se os candles demonstrarem força técnica clara.

[PASSO 3: MATRIZ DE ESTRATÉGIA ADAPTATIVA SUPREMA MULTI-CONFLUENTE]
Busque por confluências de Price Action em Suporte, Resistência (S/R horizontais) e Linhas de Tendência (LTA/LTB inclinadas):

1. MATRIZ DE CONTINUIDADE DE FLUXO (IMPULSO E ANATOMIA DO CANDLE):
   - FLUXO POR COR E IMPULSO: Monitore blocos dominantes de velas de mesma cor que demonstrem aceleração rápida.
   - TAMANHO DO CORPO: Avalie a expansão anatômica do corpo do candle recente. Corpos médios a grandes e sólidos (velas de força) confirmam a urgência institucional. Pavios contra o movimento devem ser pequenos para atestar a continuidade.

2. MATRIZ DE LATERALIDADE / CONSOLIDAÇÃO HORIZONTAL:
   - REVERSÃO E RETRAÇÃO EM SUPORTE/RESISTÊNCIA: Opere o respeito de zonas horizontais nítidas de Suporte (Fundo) e Resistência (Topo). Quando o preço testar os limites com velas de perda de pressão e deixar pavios nítidos de rejeição, valide o clique de retração ou reversão para a mesma vela.
   - RETRAÇÃO PELOS PAVIOS: Se as velas atuais estiverem demonstrando rejeição visual através de pavios ao tocar barreiras horizontais ou inclinadas consolidadas, valide a entrada.

3. MATRIZ DE PÓS-REVERSÃO E VIRADA DE MERCADO:
   - CONTINUIDADE PÓS-REVERSÃO MACRO: Identifique falhas estruturais (como topos/fundos duplos ou quebras de estrutura CHOCH). Assim que o mercado reverter e confirmar o primeiro candle sólido na nova direção, opere o fluxo de continuidade.

[PASSO 4: PROTOCOLO DE FILTRAGEM DE RUÍDO (NÍVEL: MÉDIO PARA ALTO)]
Aplique uma barreira rigorosa e equilibrada contra manipulações ordinárias, abortando a operação em cenários de alta instabilidade:
- FILTRO ANTI-XADREZ (NÍVEL ALTO): Aborte obrigatoriamente se houver uma alternância perfeita de cores (verde-vermelho-verde-vermelho) por mais de 6 a 8 velas seguidas, indicando exaustão completa de tendência e ruído micro.
- FILTRO DE MICRO-VELAS (NÍVEL MÉDIO-ALTO): Aborte se identificar 3 ou mais Dojis legítimos (linhas horizontais sem corpo) consecutivos. No entanto, permita operações se as velas forem pequenas mas contarem com corpos mínimos e pavios de retração nítidos em zonas fortes de S/R.
- FILTRO EM OTC (NÍVEL MÉDIO): Permita pullbacks e retrações desde que as regiões de preço estejam fortemente marcadas no histórico visual e confluam com a direção imediata dos candles.

[PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]
- Avalie os riscos de forma equilibrada. Quanto mais fatores confluírem juntos (ex: Impulso de Cor + Vela de Corpo Cheio + Suporte Horizontal), maior deve ser a taxa de acerto.
- Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. Sinais fracos abaixo de 80% devem ser descartados como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

[PASSO 6: CRONOMETRAGEM DE EXECUÇÃO PADRÃO]
- Localize o relógio oficial da plataforma no print. Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente (ex: se o relógio marca 10:15:20, projete o clique para entre 10:17:00 e 10:20:00). Expiração fixa de 1 minuto para fechar na mesma vela do clique projetado.

[PASSO 7: SUGESTÃO DE GERENCIAMENTO DE MÃO DE ENTRADA]
Defina a recomendação de capital de forma estritamente proporcional à taxa calculada:
- Taxa entre 90% e 95%: MÃO DE SOROS / ENTRADA FORTE (Alta confluência e proteção contra ruído).
- Taxa entre 85% e 89%: ENTRADA FIXA padrão (Cenário operável estável).
- Taxa entre 80% e 84%: MÃO LEVE / REDUZIDA (Oportunidade isolada sob volatilidade permitida).
- Operação Abortada: PARADA OBRIGATÓRIA (Stop Loss / Preservação de capital).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADA: [Construa a confluência técnica exata vista na tela. Exemplos: REVERSÃO EM LATERALIDADE COM FILTRO DE RUÍDO ATIVADO ou CONTINUIDADE DE FLUXO POR COR E IMPULSO]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / CONSOLIDAÇÃO LATERAL / VIRADA DE FLUXO PÓS-REVERSÃO]
📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para atingir sua zona de entrada]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Mapeamento das Regiões (S/R, LTA/LTB): [Descreva as microzonas ou suportes/resistências horizontais e inclinados que o preço tende a respeitar]
- Avaliação de Ruído e Volatilidade (Filtro Médio-Alto): [Explique por que o cenário foi considerado seguro e passou no filtro de ruído médio-alto]
- Diagnóstico do Fluxo de Continuidade (Cor, Impulso e Corpo): [Análise do tamanho anatômico do corpo das velas e o nível de impulso identificado]
- Comportamento de Pavios e Pressão de Rejeição: [Explique se a presença dos pavios recentes confirmou a exaustão ou o extremo respeito da lateralidade]
- Posicionamento da Média Móvel (EMA 9): [Descreva a posição do preço acima ou abaixo da EMA 9 apenas como ponto dinâmico de referência]
- Justificativa da Gestão de Lote: [Explique por que o lote sugerido se adequa perfeitamente a essa combinação de fatores]

Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
"""

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_texto):
    try:
        client_objeto = genai.Client(api_key=chave_api)
        chamada = client_objeto.models.generate_content(
            model="gemini-2.5-flash", contents=[imagem_objeto, prompt_texto]
        )
        return chamada.text
    except Exception as erro_objeto:
        return f"ERRO_GERADO: {str(erro_objeto)}"

# --- AREA OPERACIONAL DO SITE ---

uploaded_file = st.file_uploader(
    "Arraste o print completo do gráfico M1 (Obrigatório conter o Relógio da Plataforma visível, Velas, RSI e Volume):", 
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.session_state["imagem_grafico"] = Image.open(uploaded_file)

if "imagem_grafico" in st.session_state:
    st.image(st.session_state["imagem_grafico"], caption="Gráfico M1 Carregado para Análise de Confluência Suprema", use_container_width=True)
    
    if st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL"):
        if not lista_de_chaves:
            st.error("ERRO: Nenhuma chave foi preenchida na barra lateral esquerda!")
        else:
            with st.spinner("IA aplicando Filtros e Verificação Técnica Avançada..."):
                chave_operacional = lista_de_chaves
                resposta_final = executar_chamada_gemini(chave_operacional, st.session_state["imagem_grafico"], PROMPT_TRADER)
                
            if "ERRO_GERADO:" in resposta_final:
                st.error(resposta_final)
                st.warning("Verifique sua chave na barra lateral.")
            else:
                st.success("Análise Suprema de Confluência Matricial Concluída!")
                st.markdown(resposta_final)
else:
    if not lista_de_chaves:
        st.warning("Insira pelo menos uma Gemini API Key válida na barra lateral para ativar o Agente.")
