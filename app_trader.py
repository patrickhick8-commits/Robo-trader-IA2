import streamlit as st
from google import genai
from PIL import Image

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema e Projeção Temporal")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

# Correção Crítica: Mudança para text_input que aceita type="password" nativamente
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas usando ponto e vírgula como separador
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

if lista_de_chaves:
    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print completo do gráfico M1 (Obrigatório conter o Relógio da Plataforma visível, Velas, RSI e Volume):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise de Confluência Suprema", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE SUPREMA MATRICIAL"):
            with st.spinner("IA aplicando Inteligência Quântica e aplicando filtros de volatilidade..."):
                
                # Prompt mestre unificando ABSOLUTAMENTE TODAS as estratégias, tempos e filtros de segurança
                prompt = """
                [SYSTEM_ROLE] Você é um superalgoritmo HFT (High-Frequency Trading) de fundos soberanos e analista quantitativo sênior focado em trading de altíssima precisão e mitigação rígida de risco para Opções Binárias (M1). Sua postura é extremamente fria, matemática, cética e profissional. Sua missão é extrair uma ENTRADA CIRÚRGICA de altíssima assertividade. Se o cenário for minimamente duvidoso, seu dever é ABORTAR.

                Analise rigorosamente as seguintes camadas visuais e macro-estratégias confluentes no print enviado:

                [1. CLASSIFICAÇÃO DE MERCADO E COMPORTAMENTO DE PAVIOS (ABERTO VS OTC)]
                Escaneie textualmente a imagem em busca de marcações (ex: 'EUR/USD-OTC') e analise o comportamento dos pavios junto com a movimentação:
                - MERCADO ABERTO REAL: Dê peso máximo para REJEIÇÃO E RETRAÇÃO nos pavios. Pavios longos em zonas de suporte, resistência ou extremidades do RSI indicam forte defesa institucional e entrada de volume contrário. Busque operações de Reversão e Retração na mesma vela.
                - ALGORÍTMO OTC (MERCADO FECHADO): Cuidado extremo com pavios longos. Em OTC, pavios longos frequentemente indicam manipulação de preço e o algoritmo tende a engolfar ou romper esses pavios nas velas seguintes para limpar as ordens dos traders de varejo. Foque 100% em FLUXO DE VELA DE CORPO CHEIO a favor do preenchimento desses pavios (alvos de liquidez).

                [2. REGRA DE TEMPO CRUCIAL - PROJEÇÃO DE VELA M1]
                - Localize visualmente o relógio oficial da plataforma dentro do print.
                - Você deve projetar matematicamente o momento exato em que a estrutura do gráfico se confirmará. Agende o HORÁRIO DO CLIQUE (ENTRADA) estritamente entre 2 a 5 minutos no futuro em relação ao horário do print.
                - A operação deve expirar na MESMA vela do clique. Ou seja, tempo de expiração fixo e rígido de exatamente 1 minuto.

                [3. MAPEAMENTO DE FLUXO POR CORES DE VELAS e VOLUME OCULTO]
                - FLUXO DE ALTA: Monitore blocos dominantes de velas verdes, corpos expandidos crescentes e redução de pavios superiores.
                - FLUXO DE BAIXA: Monitore blocos dominantes de velas vermelhas, corpos expandidos e redução de pavios inferiores.
                - VOLUME IMPLÍCITO: Deduza a urgência institucional pelo tamanho anatômico das velas (Marubozu = volume institucional; Dojis/corpos espremidos = ausência de liquidez e alto risco).

                [4. PROJEÇÃO DE INDICADORES INTERNOS]
                Mesmo que não estejam plotados na imagem, calcule mentalmente com base na sequência histórica de fechamento:
                - EMA 9 (Exponencial de 9): Força imediata e direção do preço a curtíssimo prazo.
                - SMA 20 (Simples de 20): Tendência média e zonas de Pullback dinâmico.
                - EMA 50 (Exponencial de 50): Tendência macro do ativo e suporte/resistência institucional de peso.
                - RSI 14 (Índice de Força Relativa): Rastreie exaustão em zonas de Sobrecompra (>70) ou Sobrevenda (<30).

                [5. ESTRUTURA SMC & ZONEAMENTO GEOMÉTRICO]
                - Identifique quebras de estrutura recentes (BOS - Break of Structure ou CHOCH - Change of Character).
                - Identifique as zonas horizontais de Suporte e Resistência, junto com linhas inclinadas de LTA e LTB.
                - Rastreie padrões gráficos macro na tela (Topos/Fundos Duplos, OCO, Canais, Triângulos ou Acumulações).

                [6. FILTROS DE SEGURANÇA E REGRAS EXTREMAS]
                - FILTRO MERCADO PICOTADO: Se o gráfico estiver alternando cores a cada candle (verde, vermelha, verde, vermelha), ABORTE imediatamente.
                - FILTRO FALSO ROMPIMENTO: Velas que rompem zonas sem volume implícito (com pavio de absorção longo contra o rompimento) devem ser descartadas.
                - REQUISITO MÍNIMO DE ENTRADA: Exija confluência tripla (Ex: Fluxo de Cor + Alinhamento de Médias + Rompimento de LTB por Vela de Força).
                - ASSERTIVIDADE RÍGIDA: Retorne um cálculo estatístico da operação. Sinais válidos apenas entre 88% e 99%. Abaixo disso, o veredito obrigatório é OPERAÇÃO ABORTADA.

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo e destacado:

                🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 97% - Matriz Suprema Cadenciada] (Escreva destacado e em tamanho grande)

                ⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro com base no relógio do print]
                ⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
                🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [Calcule o horário exato que a vela do clique termina, ex: HH:MM+1:00]
                🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]

                🧠 ESTRATÉGIA COMBINADA: [Ex: RETRAÇÃO EM SUPORTE HISTÓRICO DE MERCADO ABERTO ou PREENCHIMENTO DE PAVIO EM FLUXO OTC]
                📊 CONTEXTO DO MERCADO: [TENDÊNCIA DE ALTA, TENDÊNCIA DE BAIXA ou LATERALIZADO]
                📊 JUSTIFICATIVA DA PROJEÇÃO TEMPORAL: [Explique resumidamente o porquê o preço vai levar esse tempo exato (2 a 5 minutos) para atingir e confirmar sua zona de entrada]

                🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (O QUE A IA VIU):
                - Ambiente Identificado & Pavios: [Explique se identificou Mercado Aberto ou OTC e como os pavios das últimas velas confirmaram essa leitura]
                - Diagnóstico do Fluxo de Cores e Volume Oculto: [Análise minuciosa da sequência de cores e tamanho dos corpos/volume]
                - Projeção de Médias (EMA 9 / SMA 20 / EMA 50): [Alinhamento e posicionamento do preço em relação às médias estimadas]
                - Nível do RSI 14: [Status do oscilador e espaço livre para o Gain antes da exaustão]
                - Mapeamento S/R, LTA/LTB e SMC: [Comportamento do preço nas regiões estruturais, figuras gráficas ou quebras de estrutura]
                - Padrão de Candle Validado como Gatilho: [Qual foi o padrão de candle exato que acionou o sinal]
                - Justificativa de Frieza Analítica (Filtro Ativado): [Explique matematicamente por que esse sinal passou nos filtros anti-ruído]

                Seja extremamente frio, preciso e direto. Velocidade e precisão salvam bancas.
                """
                
                sucesso = False
                
                # Executa o loop simples por chave e motor
                for chave_atual in lista_de_chaves:
                    if sucesso:
                        break
                        
                    for nome_modelo in ['gemini-2.5-flash', 'gemini-1.5-flash']:
                        try:
                            st.toast(f"Analisando gráfico com o motor {nome_modelo}...")
                            client = genai.Client(api_key=chave_atual)
                            
                            response = client.models.generate_content(
                                model=nome_modelo,
                                contents=[image, prompt]
                            )
                            
                            st.success(f"Análise Concluída! Motor: {nome_modelo}")
                            
                            # Injeta áudio de alerta no Desktop
                            st.components.v1.html(
                                '<audio autoplay src="https://google.com"></audio>',
                                height=0
                            )
                            
                            st.markdown(response.text)
                            sucesso = True
                            break
                        except Exception:
                            continue
                
                if not sucesso:
                    st.error("❌ Todas as chaves ou motores de IA falharam. Verifique suas chaves e o print enviado.")
else:
    st.info("👈 Cole suas Gemini API Keys na barra lateral separadas por ponto e vírgula (;) para ativar a análise.")
