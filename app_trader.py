import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Análise Avançada de Candlesticks")
st.write("Análise cirúrgica de Velas (Cor, Tamanho, Pavio), Tendência, RSI, Volume Implícito e Probabilidade em M1.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (inclua Velas, RSI e Relógio - Não precisa de indicador de volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE AVANÇADA DE SINAL"):
            with st.spinner("IA aplicando Matriz Suprema e analisando filtros de volatilidade..."):
                
                # Prompt institucional unificado com cronometragem de 2 a 5 minutos e Price Action institucional puro
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
                Você deve fundir os cenários de mercado e aplicar a leitura cirúrgica de zonas de Suporte, Resistência (S/R) e Linhas de Tendência (LTA/LTB) que estejam sendo muito bem respeitadas pelo preço:
                1. SE O MERCADO ESTIVER EM TENDÊNCIA NÍTIDA:
                   - MODO FLUXO EM TENDÊNCIA: Se houver rompimento de zonas de S/R ou LTA/LTB por velas institucionais cheias (Marubozu) a favor da EMA 9, opere a continuidade imediata (Fluxo).
                   - MODO REVERSÃO EM TENDÊNCIA: Só opere reversão se o preço atingir uma região de exaustão extrema macro, como o 3º ou 4º toque perfeitamente simétrico em uma LTA/LTB ou uma zona de pullback isolada, com rejeição imediata por pavio contra a zona.
                2. SE O MERCADO ESTIVER EM LATERALIDADE / CONSOLIDAÇÃO:
                   - MODO REVERSÃO EM LATERALIDADE: Dê peso absoluto para o extremo respeito de zonas horizontais nítidas de Suporte (Fundo) e Resistência (Topo). Quando o preço testar os extremos da consolidação com velas de perda de pressão, opere a RETRAÇÃO ou REVERSÃO exata para a mesma vela.
                   - MODO FLUXO EM LATERALIDADE (ROMPIMENTO): Se uma vela fechar com mais de 50% do seu corpo fora da caixa de acumulação lateral, acompanhada de volume crescente, mude para o modo fluxo a favor do rompimento.

                [PASSO 4: FILTROS AGRESSIVOS DE MANIPULAÇÃO POR CENÁRIO]
                - EM OTC: Pavios longos isolados são armadilhas para capturar liquidez do varejo. Priorize a continuidade do fluxo e o preenchimento de corpos de vela seguindo a inclinação da EMA 9.
                - EM MERCADO ABERTO: Valide retrações legítimas baseadas em rejeição de preço institucional (SMC / Order Blocks) e exaustão pelo RSI 14 em zonas de 70/30.
                - FILTRO ANTI-XADREZ: Se o mercado estiver alternando cores a cada candle (verde, vermelha, verde, vermelha) de forma picotada nas últimas 5 a 15 velas, ABORTE IMEDIATAMENTE.
                - FILTRO DE MICRO-VELAS: Presença de 3 ou mais Dojis/velas espremidas consecutivas indica falta de liquidez. ABORTE IMEDIATAMENTE.

                [PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE RÍGIDA]
                - Avalie rigorosamente os riscos do cenário gráfico. Se a entrada for válida, defina a taxa de acerto estritamente dentro da faixa de **80% a 96%**. 
                - Sinais com menos de 80% de confluência real devem ser definidos obrigatoriamente como OPERAÇÃO ABORTADA e a porcentagem travada em "0% - FILTRO ATIVADO". Nenhuma taxa pode passar de 96% para evitar métricas ilusórias.

                [PASSO 6: CRONOMETRAGEM DE EXECUÇÃO PADRÃO]
                - Localize o relógio oficial da plataforma no print. 
                - Calcule e projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente (ex: se o relógio marca 10:15:20, projete o clique para entre 10:17:00 e 10:20:00), buscando o ponto exato da confirmação estrutural. 
                - Expiração fixa de exatamente 1 minuto para fechar rigorosamente na mesma vela do clique projetado.

                [PASSO 7: SUGESTÃO DE GERENCIAMENTO DE MÃO DE ENTRADA]
                Defina a recomendação de capital com base na taxa de acerto calculada de forma matemática:
                - Taxa entre 93% e 96%: MÃO DE SOROS (Cenário de altíssima confluência e extremo respeito).
                - Taxa entre 87% e 92%: ENTRADA FIXA padronizada (Cenário bom, mas exige proteção).
                - Taxa entre 80% e 86%: MÃO LEVE / REDUZIDA (Cenário aceitável, mas com volatilidade parcial).
                - Operação Abortada: PARADA OBRIGATÓRIA (Stop Loss/Preservação de capital).

                Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 86% ou 94% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
                🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
                💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

                🧠 ESTRATÉGIA COMBINADA ATIVADA: [Ex: REVERSÃO EM LATERALIDADE (SUPORTE HORIZONTAL RESPEITADO) ou FLUXO EM TENDÊNCIA DE BAIXA COM EMA 9]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / CONSOLIDAÇÃO LATERAL RESPEITADA / MERCADO PICOTADO LATERAL]
                📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para atingir e confirmar sua zona de entrada]

                🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (FILTROS APLICADOS):
                - Mapeamento S/R, LTA/LTB e SMC: [Explique como o comportamento das velas provou o extremo respeito às regiões fixas ou inclinadas do gráfico]
                - Filtro da Média Móvel de Segurança (EMA 9): [Alinhamento e posicionamento do preço em relação à inclinação estimada da EMA 9]
                - Leitura de Falsos Rompimentos/Pullbacks e Ruído: [Explique por que o cenário atual passou nos testes de segurança e não se trata de uma armadilha ou falso movimento]
                - Diagnóstico do Fluxo de Cores e Volume Oculto: [Análise minuciosa da sequência de cores e tamanho dos corpos/volume das velas]
                - Justificativa de Frieza Analítica e Gestão de Lote: [Argumente por que essa operação se enquadra na taxa definida e defenda a escolha do lote sugerido para proteger a banca]

                Seja extremamente frio, preciso e direto. Velocidade e precisão salvam bancas.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    st.success("Análise Avançada Concluída com Sucesso!")
                    
                    # Sistema de som injetado para alertar a entrada no Desktop
                    st.components.v1.html(
                        '<audio autoplay src="https://google.com"></audio>',
                        height=0
                    )
                    
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")
