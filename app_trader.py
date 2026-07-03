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

# PROMPT MESTRE RECONFIGURADO - INCLUSÃO DE RSI E TENDÊNCIA MAJORITÁRIA
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (M1). Sua postura combina proteção de capital com aproveitamento inteligente de oportunidades, operando através de um filtro técnico de ruído calibrado no nível Médio-Alto para evitar falsos sinais sem engessar as operações.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA MAJORITÁRIA (MACRO) E POSICIONAMENTO DA EMA 9]
- ANALISE DA TENDÊNCIA MAJORITÁRIA: Avalie o cenário macro do gráfico em segundo plano. O preço vem construindo movimentos maiores de alta ou de baixa? Evite operar contra o fluxo macro dominador.
- Rastreie visualmente o fluxo do preço em relação à Média Móvel Exponencial de 9 períodos (EMA 9) para a microtendência.
- COMPRA (CALL): A tendência majoritária deve ser de Alta e o preço operando preferencialmente ACIMA da EMA 9.
- VENDA (PUT): A tendência majoritária deve ser de Baixa e o preço operando preferencialmente ABAIXO da EMA 9.

[PASSO 3: PROTOCOLO DO INDICADOR RSI PADRÃO (CONFLUÊNCIA MANDATÓRIA)]
- Localize visualmente a linha ou sub-janela do RSI (Relative Strength Index) na imagem (Padrão 14 períodos com zonas 70/30 ou 80/20).
- SINAL DE SOBRECOMPRA (FILTRO PUT): Se a linha do RSI estiver tocando ou ultrapassando a banda superior, busque gatilhos de venda (PUT) por exaustão compradora. Se estiver no meio do caminho apontando para cima, valide a continuidade.
- SINAL DE SOBREVENDA (FILTRO CALL): Se a linha do RSI estiver tocando ou rompendo a banda inferior, busque gatilhos de compra (CALL) por exaustão vendedora. Se estiver no meio do caminho apontando para baixo, valide a continuidade.

[PASSO 4: MATRIZ DE ESTRATÉGIA ADAPTATIVA SUPREMA MULTI-CONFLUENTE]
Busque por confluências de Price Action em Suporte, Resistência (S/R horizontais) e Linhas de Tendência (LTA/LTB inclinadas):

1. MATRIZ DE CONTINUIDADE DE FLUXO (IMPULSO E ANATOMIA DO CANDLE):
   - FLUXO POR COR E IMPULSO: Monitore blocos dominantes de velas de mesma cor que demonstrem aceleração rápida.
   - TAMANHO DO CORPO: Avalie a expansão anatômica do corpo do candle recente. Corpos médios a grandes e sólidos confirmam a urgência institucional.

2. MATRIZ DE LATERALIDADE / CONSOLIDAÇÃO HORIZONTAL:
   - REVERSÃO E RETRAÇÃO EM SUPORTE/RESISTÊNCIA: Opere o respeito de zonas horizontais nítidas. Quando o preço testar os limites com velas de perda de pressão e deixar pavios nítidos de rejeição com RSI em zona extrema, valide a retração.

3. MATRIZ DE PÓS-REVERSÃO E VIRADA DE MERCADO:
   - CONTINUIDADE PÓS-REVERSÃO MACRO: Identifique falhas estruturais (como topos/fundos duplos ou CHOCH). Assim que reverter e confirmar o primeiro candle sólido na nova direção alinhada à tendência majoritária, opere o fluxo.

[PASSO 5: PROTOCOLO DE FILTRAGEM DE RUÍDO (NÍVEL: MÉDIO PARA ALTO)]
Aplique uma barreira rigorosa contra manipulações ordinárias, abortando a operação em cenários de alta instabilidade:
- FILTRO ANTI-XADREZ: Aborte se houver uma alternância perfeita de cores (verde-vermelho) por mais de 6 a 8 velas seguidas.
- FILTRO DE MICRO-VELAS: Aborte se identificar 3 ou mais Dojis legítimos consecutivos.
- FILTRO DE RSI EM CONSOLIDAÇÃO INDEFINIDA: Aborte se o RSI estiver travado em linha reta exatamente na linha central (50) sem inclinação ou direção clara.

[PASSO 6: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]
- Avalie os riscos de forma equilibrada. Quanto mais fatores confluírem juntos (ex: Tendência Majoritária a favor + RSI em Extremo + Vela de Força + Suporte), maior a taxa de acerto.
- Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. Sinais fracos abaixo de 80% devem ser descartados como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

[PASSO 7: CRONOMETRAGEM DE EXECUÇÃO E GESTÃO DE LOTE]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente do relógio visível da plataforma. Expiração fixa de 1 minuto para fechar na mesma vela do clique projetado.
- Defina a recomendação de capital proporcionalmente à taxa: Soros (90-95%), Mão Fixa (85-89%), Mão Leve (80-84%) ou Parada Obrigatória (Abortada).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADA: [Construa a confluência técnica exata vista na tela.]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO MACRO: [TENDÊNCIA MAJORITÁRIA DE ALTA / TENDÊNCIA MAJORITÁRIA DE BAIXA / CONSOLIDAÇÃO LATERAL SEVERA]
📈 LEITURA DO RSI PADRÃO: [Descreva a posição do RSI: Sobrecomprado, Sobrevendido ou Neutro com Direção]
📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato para atingir sua zona de entrada]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Avaliação da Tendência Majoritária: [Justifique a direção macro identificada no fundo do gráfico]
- Comportamento Gráfico do RSI: [Explique como a curvatura ou toque do RSI validou ou abortou a operação]
- Mapeamento das Regiões (S/R, LTA/LTB): [Descreva as microzonas]
- Avaliação de Ruído e Volatilidade (Filtro Médio-Alto): [Análise do cenário de estabilidade]
- Diagnóstico do Fluxo de Continuidade (Cor, Impulso e Corpo): [Análise anatômica das velas]
- Posicionamento da Média Móvel (EMA 9): [Relação do preço com a EMA 9]
- Justificativa da Gestão de Lote: [Por que o lote sugerido se adequa a esses fatores]

Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
"""

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_texto):
    try:
        client_objeto = genai.Client(api_key=chave_api)
        chamada = client_objeto.models.generate_content(
            model="gemini-2.5-flash", 
            contents=[imagem_objeto, prompt_texto]
        )
        return chamada.text
    except Exception as erro_objeto:
        return f"ERRO_GERADO: {str(erro_objeto)}"

# --- AREA OPERACIONAL DO SITE ---

uploaded_file = st.file_uploader(
    "Faça o upload do print do seu gráfico (M1):", 
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    imagem_aberta = Image.open(uploaded_file)
    st.image(imagem_aberta, caption="Gráfico Carregado com Sucesso", use_container_width=True)
    
    if st.button("🚀 Iniciar Análise de Alta Assertividade"):
        if not lista_de_chaves:
            st.error("❌ Nenhuma API Key do Gemini foi configurada na barra lateral!")
        else:
            status_placeholder = st.empty()
            resultado_texto = ""
            sucesso = False
            
            for i, chave in enumerate(lista_de_chaves):
                status_placeholder.warning(f"⏳ Processando com a Chave de Contingência {i+1} de {len(lista_de_chaves)}...")
                
                resposta = executar_chamada_gemini(chave, imagem_aberta, PROMPT_TRADER)
                
                if "ERRO_GERADO" not in resposta:
                    resultado_texto = resposta
                    sucesso = True
                    break
                else:
                    st.sidebar.error(f"Falha na Chave {i+1}: {resposta}")
            
            status_placeholder.empty()
            
            if sucesso:
                st.success("🎯 Análise Executada e Filtrada com Sucesso!")
                st.markdown("---")
                st.markdown(resultado_texto)
                st.markdown("---")
            else:
                st.error("🚨 Todas as suas chaves falharam ou estão esgotadas. Verifique a aba de erros na lateral.")
