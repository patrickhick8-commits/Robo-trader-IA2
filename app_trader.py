import streamlit as st
from google import genai
from PIL import Image
import time

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1 Supremo", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Confluência Avançada M1")
st.write("Análise de Contexto, Médias (EMA 9, SMA 20), RSI, Suporte/Resistência, LTA/LTB e Padrões Gráficos/Candles.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole uma ou mais chaves (uma por linha) para ativar o rodízio automático antiqueda.")

# Campo para colar várias chaves (uma por linha) para rodízio grátis
chaves_input = st.sidebar.text_area("Cole suas Gemini API Keys aqui:", type="password", height=150)

# Transforma o texto em uma lista de chaves limpas e sem espaços vazios
lista_de_chaves = [chave.strip() for chave in chaves_input.split("\n") if chave.strip()]

if lista_de_chaves:
    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (Obrigatório conter o Relógio da Plataforma visível, Velas, RSI e Volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise de Confluência Suprema", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE SUPREMA DE CONFLUÊNCIA"):
            with st.spinner("IA calculando confluências de indicadores e padrões..."):
                
                # Prompt ultraconsistente focado em confluência geral e contexto macro de tempo real
                prompt = """
                [SYSTEM_ROLE] Você é um superalgoritmo HFT (High-Frequency Trading) e analista quantitativo sênior focado em trading de altíssima precisão e gerenciamento de risco institucional para Opções Binárias (M1). Sua missão é fornecer uma ENTRADA CIRÚRGICA cruzando múltiplos indicadores técnicos e padrões visuais. Se não houver confluência perfeita, você DEVE abortar a operação.

                [INDICADORES TÉCNICOS E PROJEÇÃO COGNITIVA]
                Escaneie o gráfico e rastreie a movimentação do preço projetando mentalmente/visualmente os seguintes indicadores:
                1. Média Móvel Exponencial de 9 Períodos (EMA 9): Rastreie a força do preço a curtíssimo prazo.
                2. Média Móvel Simples de 20 Períodos (SMA 20): Identifique a linha de tendência média do preço e zonas de pullback dinâmico.
                3. Índice de Força Relativa (RSI 14): Monitore exaustão em zonas de Sobrecompra (>70) ou Sobrevenda (<30).
                4. Suporte e Resistência Fixos: Identifique as zonas de fundos e topos horizontais importantes da tela.
                5. Linhas de Tendência (LTA / LTB): Identifique canais de alta, canais de baixa ou triângulos que afunilam o preço.

                [ANÁLISE DE PADRÕES VISUAIS EM M1]
                Combine os indicadores acima com a leitura de price action rigorosa:
                1. PADRÕES GRÁFICOS: Identifique figuras macro na tela como OCO (Ombro-Cabeça-Ombro), Topo/Fundo Duplo, Triângulos, Bandeiras ou Retângulos de acumulação.
                2. PADRÕES DE CANDLES (VELAS):
                   - Reversão: Identifique Martelo, Estrela da Manhã/Noite, Engolfo, Harami ou Doji em zonas de suporte, resistência, LTA ou LTB.
                   - Fluxo e Rompimento: Identifique Velas de Força (Marubozu), velas sem pavio superior/inferior confirmando rompimento legítimo de zonas fixas ou linhas de tendência, indicando continuação do movimento.

                [FILTRO DE SEGURANÇA E ASSERTIVIDADE EXTREMA]
                - Para dar um sinal de COMPRA ou VENDA, você precisa de no mínimo 3 fatores de confluência (Ex: Preço batendo em Suporte + Candle de Martelo + RSI sobrevendido).
                - Se houver falso rompimento sem volume, ou se as médias EMA 9 e SMA 20 estiverem horizontais e emboladas (mercado lateral sem força), ABORTE a operação.
                - Nível de assertividade mínimo exigido para emitir ordem: 88% a 99%.

                [CRONOMETRAGEM RÍGIDA DO RELÓGIO]
                1. Localize o relógio oficial da plataforma dentro do print.
                2. Projete o HORÁRIO DO CLIQUE com exatidão matemática cronometrada entre 2 a 4 minutos no futuro em relação ao horário exato visto na foto.
                3. A expiração deve ser calculada de forma rígida para o fechamento da mesma vela (1 Minuto de duração de operação).

                Retorne estritamente neste formato markdown limpo e direto:
                🌐 CONTEXTO GERAL DETECTADO: [Ex: Tendência Forte de Alta / Lateralização em Topo Histórico]
                🎯 NÍVEL DE ASSERTIVIDADE FILTRADA: [Ex: 95% - Confluência Tripla Confirmada]
                ⏰ HORÁRIO EXATO DO CLIQUE: [HH:MM:00 rigoroso com base no relógio do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Fechamento no Candle Alvo)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM+1:00]
                🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
                🧠 GATILHO DA ESTRATÉGIA: [Descreva de forma resumida a confluência. Ex: Rompimento de LTB com Vela de Força + Pullback na EMA 9]

                🔍 MAPA DE CONFLUÊNCIA GRÁFICA (O QUE FOI ANALISADO):
                - Posição das Médias (EMA 9 vs SMA 20): [O cruzamento ou alinhamento das duas médias]
                - Nível do RSI 14: [Status de força ou exaustão do indicador]
                - Zonas de Suporte / Resistência: [Proximidade com zonas de topos ou fundos horizontais]
                - Linhas de Tendência (LTA / LTB): [Interseção ou respeito às linhas de tendência inclinadas]
                - Padrão Gráfico Identificado: [Ex: Pivô de Alta, Canal de Baixa, Topo Duplo, etc.]
                - Padrão de Candle Validado: [Ex: Engolfo de Alta para Fluxo / Martelo para Reversão / Vela de Força rompendo taxa]
                - Filtro de Proteção Ativado: [Justificativa do porquê o sinal é extremamente seguro e não foi abortado por falso rompimento]
                """
                
                sucesso = False
                modelos_disponiveis = ['gemini-2.5-flash', 'gemini-1.5-flash']
                
                # Percorre cada chave colada pelo usuário na barra lateral
                for indice_chave, chave_atual in enumerate(lista_de_chaves):
                    if sucesso:
                        break
                        
                    try:
                        client = genai.Client(api_key=chave_atual)
                        
                        # Testa os modelos sequencialmente
                        for nome_modelo in modelos_disponiveis:
                            try:
                                st.toast(f"Disparando análise macro com Chave #{indice_chave + 1} no motor {nome_modelo}...")
                                
                                response = client.models.generate_content(
                                    model=nome_modelo,
                                    contents=[image, prompt]
                                )
                                
                                st.success(f"Análise Concluída! (Chave #{indice_chave + 1} | Motor: {nome_modelo})")
                                st.markdown(response.text)
                                
                                sucesso = True
                                break
                            except Exception as e:
                                st.warning(f"Falha no modelo {nome_modelo} com a Chave #{indice_chave + 1}: {e}")
                                continue
                                
                    except Exception as e:
                        st.error(f"Erro crítico com a Chave #{indice_chave + 1}: {e}")
                        continue
                
                if not sucesso:
                    st.error("❌ Todas as tentativas falharam. Verifique suas API Keys ou envie outro print.")
else:
    st.warning("⚠️ Insira pelo menos uma Gemini API Key na barra lateral para ativar o sistema.")


