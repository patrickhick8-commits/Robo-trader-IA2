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
    chave_ativa = lista_de_chaves
    
    # Inicializa o cliente oficial da nova SDK do Google GenAI
    client = genai.Client(api_key=chave_ativa)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (Obrigatório conter o Relógio da Plataforma visível, Velas, RSI e Volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise de Confluência Suprema", use_container_width=True)
        
        if st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL"):
            with st.spinner("IA escaneando padrões e buscando oportunidades de entrada com confluência máxima..."):
                
                # Prompt mestre recalibrado para fundir todas as estratégias com foco em Pullback e Retração por Pavio
                prompt = """
                [SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em encontrar oportunidades frequentes e de boa precisão para Opções Binárias (M1). Sua postura é moderadamente agressiva: seu objetivo é extrair o máximo de sinais válidos do gráfico, operando por confluência de fatores sem descartar operações por detalhes mínimos de ruído.

                [PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
                Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
                - Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

                [PASSO 2: FILTROS DE TENDÊNCIA E CONFLUÊNCIA COM EMA 9]
                - Rastreie visualmente o fluxo do preço em relação à Média Móvel Exponencial de 9 períodos (EMA 9).
                - COMPRA (CALL): Preço preferencialmente ACIMA da EMA 9 com inclinação ascendente.
                - VENDA (PUT): Preço preferencialmente ABAIXO da EMA 9 com inclinação descendente.
                - Permita operações se o preço estiver ligeiramente próximo à média, validando correções rápidas e continuidades.

                [PASSO 3: MATRIZ DE ESTRATÉGIA ADAPTATIVA MULTI-CONFLUENTE]
                Busque de forma ativa por confluências de Price Action em Suporte, Resistência (S/R) e Linhas de Tendência (LTA/LTB). Funda as estratégias para buscar a maior quantidade de confluências possíveis:

                1. SE O MERCADO ESTIVER EM TENDÊNCIA NÍTIDA:
                   - MODO FLUXO / ROMPIMENTO EM TENDÊNCIA: Se houver rompimento de zonas de S/R ou LTA/LTB por velas institucionais cheias (Marubozu) a favor da EMA 9, opere a continuidade imediata (Fluxo).
                   - MODO PULLBACK EM TENDÊNCIA: Monitore o preço testando a zona recém-rompida (antigo suporte que virou resistência ou vice-versa). O sinal deve ocorrer quando a vela de teste tocar a linha e demonstrar exaustão.
                   - MODO RETRAÇÃO EM TENDÊNCIA / LTA / LTB: Identifique toques em canais ou linhas de tendência inclinadas onde o preço deixa pavios longos de rejeição, operando a retração a favor do canal.

                2. SE O MERCADO ESTIVER EM LATERALIDADE / CONSOLIDAÇÃO:
                   - MODO REVERSÃO EM LATERALIDADE (SUPORTE / RESISTÊNCIA HORIZONTAL): Opere o extremo respeito de zonas horizontais nítidas de Suporte (Fundo) e Resistência (Topo). Quando o preço testar os limites com velas de perda de pressão, opere para a reversão.
                   - MODO RETRAÇÃO PELOS PAVIOS EM LATERALIDADE: Rastreie o histórico recente de pavios longos nas extremidades da consolidação. Se as velas atuais estiverem demonstrando forte rejeição visual através de pavios ao tocar a barreira horizontal, valide a entrada de retração para a mesma vela.
                   - MODO PULLBACK EM LATERALIDADE (ROMPIMENTO DA CAIXA): Se uma vela romper os limites horizontais da acumulação e a vela seguinte for testar a região rompida deixando pavio de rejeição, valide o pullback na consolidação.

                [PASSO 4: FILTROS ANTI-RUÍDO E MANIPULAÇÃO SUAVIZADOS]
                Não seja excessivamente rígido ao filtrar o gráfico. Só aborte a operação em casos extremos de mercado totalmente parado:
                - FILTRO ANTI-XADREZ: Aborte apenas se houver uma alternância perfeita e sem direção de cores por mais de 8 velas seguidas. Pequenas oscilações normais intercaladas devem ser operadas.
                - FILTRO DE MICRO-VELAS: Aborte apenas se houver uma sequência longa de Dojis legítimos (linhas horizontais finas). Velas pequenas com corpos mínimos e pavios curtos ainda são elegíveis para operação.
                - EM OTC: Permita operações de retração de pavios e pullbacks se as regiões estiverem bem marcadas, aproveitando o fluxo comprador/vendedor para preenchimento de zonas.

                [PASSO 5: SISTEMA DE CALIBRAGEM DE ASSERTIVIDADE REALISTA]
                - Avalie os riscos de forma equilibrada. Quanto mais fatores confluírem juntos (ex: Toque na EMA 9 + Pavio de Retração + Zona de Suporte), maior deve ser a taxa de acerto.
                - Classifique a taxa de acerto obrigatoriamente dentro da faixa de **80% a 95%**. 
                - Só emmitas "OPERAÇÃO ABORTADA" (e taxa 0%) se o gráfico estiver completamente plano, sem tendência alguma e sem zonas visíveis. Se o cenário for minimamente operável, determine uma direção dentro da faixa estipulada.

                [PASSO 6: CRONOMETRAGEM DE EXECUÇÃO PADRÃO]
                - Localize o relógio oficial da plataforma no print. 
                - Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente (ex: se o relógio marca 10:15:20, projete o clique para entre 10:17:00 e 10:20:00).
                - A expiração deve ser rígida de exatamente 1 minuto para fechar na mesma vela do clique projetado.

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

                🧠 ESTRATÉGIA COMBINADA ATIVADA: [Ex: REVERSÃO EM LATERALIDADE (SUPORTE HORIZONTAL RESPEITADO) ou FLUXO EM TENDÊNCIA DE BAIXA (ROMPIMENTO DE S/R) ou PULLBACK EM TENDÊNCIA COM RETRAÇÃO POR PAVIO]
                🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA / TENDÊNCIA DE BAIXA / CONSOLIDAÇÃO LATERAL / MERCADO PARADO]
                📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para atingir sua zona de entrada e confirmar a confluência]

                🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
                - Ambiente Identificado: [MERCADO ABERTO ou OTC]
                - Mapeamento das Regiões (S/R, LTA/LTB e Zonas de Pullback): [Descreva as microzonas, regiões principais ou testes de pullback que o preço tende a respeitar]
                - Comportamento e Retração pelos Pavios: [Explique o que a presença e tamanho dos pavios recentes revelam sobre a rejeição ou preenchimento das zonas]
                - Posicionamento da EMA 9: [Direção do preço em relação à média móvel para validar a força do sinal]
                - Avaliação de Ruído e Volatilidade: [Explique por que o cenário foi considerado aceitável para clique com filtros moderados]
                - Diagnóstico do Fluxo de Cores e Volume por Corpo: [Análise do tamanho das últimas velas para validar o movimento e a força do gatilho]
                - Justificativa da Gestão de Lote: [Explique por que o lote sugerido se adequa a esta oportunidade]

                Seja frio, preciso e direto. Velocidade e precisão salvam bancas.
                """
                
                try:
