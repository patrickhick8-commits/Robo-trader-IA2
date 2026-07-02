import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema e Projeção Temporal")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

if lista_de_chaves:
    # Seleciona a primeira chave válida da contingência
    chave_ativa = lista_de_chaves[0]
    
    # Inicializa o cliente oficial da nova SDK do Google GenAI
    client = genai.Client(api_key=chave_ativa)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (Obrigatório conter o Relógio da Plataforma visível, Velas, RSI e Volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise de Confluência Suprema", use_container_width=True)
        
        if st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL"):
            with st.spinner("IA aplicando Filtros Anti-Ruído e Verificação de Tendência..."):
                
                prompt = """
                [SYSTEM_ROLE] Você é um superalgoritmo HFT (High-Frequency Trading) de fundos soberanos e analista quantitativo focado em trading de altíssima precisão e mitigação rígida de risco para Opções Binárias (M1). Sua postura é de extrema frieza e ceticismo matemático. Sua missão prioritária é a PRESERVAÇÃO DE CAPITAL.

                [PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
                Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
                - Se encontrar a sigla '-OTC' ou variações de mercado fechado da corretora, classifique como [AMBIENTE: ALGORITMO OTC].
                - Se for um par de moedas comum sem a sigla OTC, classifique como [AMBIENTE: MERCADO ABERTO REAL].

                [PASSO 2: FILTROS DE TENDÊNCIA E CONFLUÊNCIA COM EMA 9]
                - Rastreie visualmente o fluxo do preço e calcule a posição implícita ou explícita da Média Móvel Exponencial de 9 períodos (EMA 9).
                - COMPRA (CALL): Preço obrigatoriamente ACIMA da EMA 9 e média inclinada para cima.
                - VENDA (PUT): Preço obrigatoriamente ABAIXO da EMA 9 e média inclinada para baixo.

                [PASSO 3: MATRIZ DE ESTRATÉGIA COMBINADA (FLUXO E REVERSÃO COM EXTREMO RESPEITO)]
                Você deve fundir os cenários de mercado e aplicar a leitura cirúrgica de zonas de Suporte, Resistência (S/R) e Linhas de Tendência (LTA/LTB) que estejam sendo muito bem respeitadas:

                1. SE O MERCADO ESTIVER EM TENDÊNCIA NITIDA:
                   - MODO FLUXO EM TENDÊNCIA: Se houver rompimento de zonas de S/R ou LTA/LTB por velas institucionais cheias (Marubozu) a favor da EMA 9, opere a continuidade imediata (Fluxo).
                   - MODO REVERSÃO EM TENDÊNCIA: Só opere reversão em tendência se o preço atingir uma região de exaustão extrema macro, como o terceiro ou quarto toque perfeitamente simétrico em uma LTA/LTB ou uma zona de pullback isolada, com rejeição imediata por pavio.

                2. SE O MERCADO ESTIVER EM LATERALIDADE / CONSOLIDAÇÃO:
                   - MODO REVERSÃO EM LATERALIDADE: Dê peso absoluto para o extremo respeito de zonas horizontais nítidas de Suporte (Fundo) e Resistência (Topo). Quando o preço testar os extremos da consolidação com velas de perda de pressão, opere a RETRAÇÃO ou REVERSÃO exata para a mesma vela.
                   - MODO FLUXO EM LATERALIDADE (ROMPIMENTO): Se uma vela fechar com mais de 50% do seu corpo fora da caixa de acumulação lateral, acompanhada de volume crescente, mude para o modo fluxo a favor do rompimento.

                [PASSO 4: FILTROS AGRESSIVOS DE MANIPULAÇÃO POR CENÁRIO]
                - EM OTC: Pavios longos isolados são perigosos. Priorize a continuidade do fluxo e o preenchimento de corpos de vela seguindo a inclinação da EMA 9.
                - EM MERCADO ABERTO: Valide retrações legítimas baseadas em rejeição de preço institucional (SMC / Order Blocks).
                - FILTRO ANTI-XADREZ: Se o mercado estiver alternando cores a cada candle (verde, vermelha, verde, vermelha) de forma picotada sem tocar linhas limpas de S/R, ABORTE IMEDIATAMENTE.
                - FILTRO DE MICRO-VELAS: Presença de 3 ou mais Dojis consecutivos anula qualquer análise. ABORTE.

                [PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE RÍGIDA]
                - Avalie rigorosamente os riscos. Se o cenário for qualificado, defina a taxa de acerto estritamente dentro da faixa de **80% a 96%**. 
                - Sinais com menos de 80% de confluência real devem ser definidos obrigatoriamente como OPERAÇÃO ABORTADA e a porcentagem travada em "0% - FILTRO ATIVADO". Nenhuma taxa pode passar de 96%.

                [PASSO 6: CRONOMETRAGEM DE EXECUÇÃO]
                - Verifique o relógio oficial da plataforma no print. Calcule e projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **1 a 5 minutos**, buscando o ponto exato do toque ou confirmação estrutural. Expiração fixa de 1 minuto (mesma vela do clique).

                [PASSO 7: SUGESTÃO DE GERENCIAMENTO DE MÃO DE ENTRADA]
                Defina matematicamente a recomendação de capital baseada estritamente na taxa de acerto calculada:
                - Taxa entre 93% e 96%: MÃO DE SOROS (Cenário de altíssima confluência e extremo respeito).
                - Taxa entre 87% e 92%: ENTRADA FIXA padronizada (Cenário bom, mas exige proteção).
                - Taxa entre 80% e 86%: MÃO LEVE / REDUZIDA (Cenário aceitável, mas com volatilidade parcial).
                - Operação Abortada: PARADA OBRIGATÓRIA (Stop Loss/Preservação de capital).

                Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 86% ou 94% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 1 a 5 minutos para o futuro]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
                🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
                💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

                🧠 ESTRATÉGIA COMBINADA ATIVADA: [Ex: REVERSÃO EM LATERALIDADE (SUPORTE HORIZONTAL RESPEITADO) ou FLUXO EM TENDÊNCIA DE BAIXA (ROMPIMENTO DE S/R)]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / CONSOLIDAÇÃO LATERAL RESPEITADA / MERCADO PICOTADO LATERAL]
                📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato para atingir e confirmar sua zona de entrada]

                🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (FILTROS APLICADOS):
                - Ambiente Identificado: [MERCADO ABERTO ou OTC]
                - Mapeamento S/R, LTA/LTB e SMC: [Explique como o comportamento das velas provou o extremo respeito às regiões fixas ou inclinadas]
                - Filtro da Média Móvel (EMA 9): [Alinhamento e posicionamento do preço em relação à inclinação da EMA 9]
                - Diagnóstico do Fluxo de Cores e Volume Oculto: [Análise da sequência de cores e tamanho dos corpos/volume]
                - Justificativa de Frieza Analítica e Gestão de Lote: [Argumente por que essa operação se enquadra na taxa definida e defenda a escolha do lote sugerido para proteger a banca]

                Seja extremamente frio, preciso e direto. Velocidade e precisão salvam bancas.
                """
                
                try:
                    # Executa a chamada utilizando o modelo multimodal mais recente e performático para visão computacional
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Suprema Matricial Concluída!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao processar com a chave atual: {str(e)}")
                    st.warning("Verifique sua chave de contingência na barra lateral.")
else:
    st.warning("Insira pelo menos uma Gemini API Key válida na barra lateral para ativar o Agente.")
