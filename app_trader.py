import streamlit as st
from google import genai
from PIL import Image
import time

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - M1 Pro", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Volume por Comportamento das Velas")
st.write("Análise Avançada: Velas, Tendência, RSI, Volume Implícito, Milissegundos e Auto-Correção para M1.")

# 2. Configuração da Chave da IA
API_KEY = st.sidebar.text_input("Cole sua Gemini API Key aqui:", type="password")

if API_KEY:
    # Inicializa o cliente com a nova biblioteca oficial do Google
    client = genai.Client(api_key=API_KEY)

    # 3. Campo de Upload do Print
    uploaded_file = st.file_uploader("Arraste o print do gráfico M1 (Velas, RSI, EMA 10 e Relógio visíveis):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gráfico M1 Carregado para Análise", use_container_width=True)
        
        # Botão de disparo rápido para Opções Binárias Avançado
        if st.button("🚀 EXECUTAR ANÁLISE COMPLETA"):
            # Marca o início exato em nanossundos para calcular milissegundos reais de processamento
            start_time = time.perf_counter()
            
            with st.spinner("IA escaneando padrões de velas, volume e mercado..."):
                
                # Prompt unificado contendo todas as regras solicitadas com foco em precisão absoluta
                prompt = """
                [SYSTEM_ROLE]
                Você é um robô de trading institucional de alta performance, projetado para operar com frieza absoluta e precisão cirúrgica. Sua inteligência é calibrada para ignorar ruídos de mercado e rastrear estritamente a ENTRADA PERFEITA. 
                Sua missão é escanear a imagem enviada, cruzar os dados gráficos e calcular uma taxa de assertividade extrema, focada em vitórias consistentes (WIN) e ganhos excelentes.

                [OPERATIONAL_PARAMETERS]
                - CRITÉRIO DE FILTRO: Só execute o gatilho se houver alta probabilidade matemática de acerto. Se o cenário for duvidoso, reduza drasticamente a assertividade ou declare estado NEUTRO.
                - TEMPO GRÁFICO: M1 (Velas de 1 minuto).
                - INDICADORES: EMA de 10 períodos (Exponencial) e RSI (Configuração Padrão 14).
                - PRICE ACTION & MÉTRICAS: Rejeição por tamanho de pavio (retração), fluxo de velas pelas cores, força da tendência atual, volume do mercado implícito e tamanho real do corpo da vela.

                [TIME_LOGIC_RULES]
                Você deve ler o relógio atual presente na imagem enviada e calcular o momento do clique futuro e sua respectiva expiração seguindo rigorosamente esta lógica:
                - O momento do clique deve ser agendado para ocorrer entre o mínimo de 2 a 5 minutos DEPOIS do horário do print.
                - A expiração deve ser estritamente para a MESMA VELA do clique (M1 Tradicional).
                - Exemplo Prático: Se o Print for tirado às 15:30:00, você deve projetar uma entrada futura. O comando do clique deve ser para as 15:32:00, 15:33:00, 15:34:00 ou 15:35:00. Se o clique for às 15:34:00, a expiração DEVE ser às 15:35:00 (fechamento da mesma vela).

                [FEEDBACK_LOOP_ALGORITHM]
                Filtre os pesos da sua análise com base no histórico do chat:
                - Se o histórico recente indicar WIN, mantenha a calibração matemática e pesos atuais dos indicadores.
                - Se o histórico recente indicar LOSS, mude seu comportamento imediatamente através de um processo de Auto-Análise de Erro. Identifique qual indicador ou padrão de Price Action falhou anteriormente e crie uma restrição técnica temporária nesta resposta atual, ajustando os pesos matemáticos para calibrar a precisão e garantir o WIN nesta nova imagem.

                Retorne o diagnóstico estruturado estritamente neste formato markdown limpo e destacado:
🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 94%] 🔥 ENTRADA DE ALTA ASSERTIVIDADE (WIN) 🔥

                --------------------------------------------------------------------------------
                📊 RELATÓRIO DE GATILHO GERADO PELA IA (FRIEZAE PRECISÃO EXTREMA)
                --------------------------------------------------------------------------------
                • CONTEXTO ATUAL DO MERCADO: [Tendência de Alta / Tendência de Baixa / Mercado Lateral / Fluxo Forte]
                • OPERAÇÃO: [COMPRA (CALL) ou VENDA (PUT)]
                • ASSERTIVIDADE MATEMÁTICA: [X]% (Métrica calculada com rigor institucional)
                • ESTRATÉGIA IDENTIFICADA: [Fluxo / Reversão / Rompimento de Região com Pullback através do Pavio, Tamanho da Vela, Força da Tendência e Volume / Tendência]

                ⏱️ SINCRO-CRONOGRAMA (Tempo de espera de 2 a 5 minutos):
                  ├── Horário do Seu Print: [HH:MM:SS]
                  ├── Momento Exato do Clique Perfeito: [HH:MM:00] <-- (Aguarde com frieza e clique neste minuto exato)
                  └── Horário de Expiração: [HH:MM:00] <-- (Mesma vela de M1 / Fechamento de 1 minuto para Vitória)

                ⚡ DESEMPENHO DO SISTEMA:
                  └── Tempo de Execução do Algoritmo: {{LATENCY_PLACEHOLDER}} ms (Cálculo de processamento em milissegundos)

                💡 GATILHO TÉCNICO DETALHADO:
                - Anatomia das Velas e Volume Implícito: [Descreva a cor predominante, variação dos corpos, o nível de volume estimado e o que os pavios indicam]
                - Indicadores e Tendência: [Explique o posicionamento do preço em relação à EMA 10 e os níveis de saturação/exaustão do RSI 14]
                - Justificativa do Alvo Futuro: [Explique o motivo técnico de projetar a operação exatamente para o minuto escolhido no Sincro-Cronograma para garantir ganhos excelentes]
                --------------------------------------------------------------------------------
                
                Seja extremamente frio, preciso e direto na resposta. Velocidade e precisão salvam bancas e geram vitórias excelentes.
                """
                
                try:
                    # Executa o modelo flash com suporte a leitura avançada de imagem
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    # Calcula o tempo total em milissegundos após o retorno da API
                    end_time = time.perf_counter()
                    execution_time_ms = round((end_time - start_time) * 1000, 2)
                    
                    # Injeta dinamicamente a marcação exata de milissegundos no relatório gerado
                    final_text = response.text.replace("{{LATENCY_PLACEHOLDER}}", str(execution_time_ms))
                    
                    st.success("Análise de Alta Precisão Concluída com Sucesso!")
                    st.markdown(final_text)
                    
                except Exception as e:
                    st.error(f"Erro no processamento visual da IA: {e}")
else:
    st.info("👈 Insira sua Gemini API Key na barra lateral para ativar o modo de análise avançada.")
