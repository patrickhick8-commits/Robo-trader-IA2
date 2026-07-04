import streamlit as st
from google import genai
from PIL import Image
import re
from datetime import datetime, timedelta
import time

# 1. Configuração da Página do Site Separado
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

st.title("🤖 Agente IA Trader Pro: Matriz Suprema de Alta Assertividade")
st.write("Fusão Total: Projeção de Tempo (Mesma Vela M1), SMC, Volume Oculto, Fluxo de Cores, Médias, RSI e S/R / LTA / LTB.")

st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
st.sidebar.info("Cole suas chaves protegidas separando-as por ponto e vírgula (;). Exemplo: chave1; chave2; chave3")

chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui:", type="password")

# Transforma o texto em uma lista de chaves limpas
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

# PROMPT MESTRE RECONFIGURADO - ULTRA PRECISÃO ANTI-FALSO SINAL NO RSI
PROMPT_TRADER = """
[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias (M1). Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA. Sua missão principal é eliminar falsos sinais de reversão gerados por indicadores esticados.

[DIRETRIZ DE POSTURA: EVITAR LOSS POR CONTA DE RSI ESTICADO]
ATENÇÃO: Em gráficos M1, o preço frequentemente continua subindo ou caindo mesmo com o RSI acima de 70 ou abaixo de 30. NUNCA envie uma ordem de reversão (PUT no topo ou CALL no fundo) simplesmente porque o RSI tocou ou cruzou essas linhas. Isso é um erro fatal de momentum. Você deve esperar o gatilho correto de exaustão ou retorno.

[PASSO 1: IDENTIFICAÇÃO OBRIGATÓRIA DO AMBIENTE]
Escaneie textualmente a imagem em busca do nome do ativo (ex: EUR/USD, BTC/USD, EUR/GBP-OTC).
- Identifique se o ativo é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA MAJORITÁRIA (MACRO) E POSICIONAMENTO DA EMA 9]
- ANALISE DA TENDÊNCIA MAJORITÁRIA: Avalie o cenário macro do gráfico em segundo plano.
- COMPRA (CALL): A tendência majoritária deve ser de Alta e o preço operando ACIMA da EMA 9.
- VENDA (PUT): A tendência majoritária deve ser de Baixa e o preço operando ABAIXO da EMA 9.

[PASSO 3: REGRA DE PRECISÃO DO RSI (ANTI-FALSO SINAL - PROTEÇÃO DE BANCA)]
Examine a sub-janela do RSI (Padrão 14 períodos com zonas 70/30 ou 80/20) com os seguintes critérios rígidos:
1. BLOQUEIO DE OPERAÇÃO CONTRA MOMENTUM: Se o RSI cruzou 70 (para cima) ou 30 (para baixo) com uma inclinação reta e agressiva, PROIBIDO OPERAR REVERSÃO. O mercado está esticado e vai romper. Aborte a reversão ou opere o FLUXO do rompimento a favor do movimento.
2. GATILHO VÁLIDO DE REVERSÃO (RETORNO OU DIVERGÊNCIA): Para validar uma reversão em zona extrema, o RSI deve:
   - Demonstrar perda nítida de angulação (curvando para o lado).
   - Idealmente, mostrar o início do cruzamento de volta para dentro da zona neutra (cruzando o 70 de cima para baixo para PUT, ou cruzando o 30 de baixo para cima para CALL).
   - Ou apresentar divergência visível (preço fazendo topos mais altos e RSI fazendo topos mais baixos).

[PASSO 4: MAPEAMENTO GEO-ESPACIAL DO PREÇO]
- Analise milimetricamente a REGIÃO QUE O PREÇO ESTÁ OU IRÁ BUSCAR. Há espaço para o preço caminhar até o alvo real antes de reverter? Se o RSI estiver em 70 mas a verdadeira resistência do gráfico estiver mais acima, o preço irá buscar a resistência. Não entre antes do preço atingir a zona alvo mapeada!

[PASSO 5: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]
Avalie o gráfico com base estrita na fusão dos seguintes pilares operacionais confluentes:

1. REVERSÃO EM REGIÃO DE TENDÊNCIA E LATERALIDADE COM REVERSÃO E PAVIO:
   - Só opere se o preço atingiu a zona forte de S/R ou LTA/LTB E o RSI validou a exaustão conforme as regras do Passo 3. O candle deve deixar pavio longo de rejeição.

2. FLUXO DE VELA EM TENDÊNCIA DE BAIXA E ALTA (ROMPIMENTO DE S/R):
   - Se o preço rompeu uma barreira e o RSI continua inclinado para fora da zona (rompendo o extremo), pegue a continuidade do fluxo. O rompimento deve ter corpo expressivo e sem pavios longos de contração.

3. PULLBACK EM TENDÊNCIA DE ALTA, BAIXA E LATERAL COM RETRAÇÃO COM PAVIO:
   - Aguarde o preço retornar para testar a zona rompida. O teste deve deixar pavio nítido de retração e o RSI deve estar retornando de forma saudável, sem força contrária.

4. FLUXO DE CONTINUIDADE PÓS-REVERSÃO DO MERCADO:
   - Após a virada estrutural confirmada, pegue o fluxo a favor da nova direção em busca do próximo alvo do preço.

[PASSO 6: PROTOCOLO DE FILTRAGEM DE RUÍDO E REGRAS DE BLOQUEIO]
- BLOQUEIO DE RETRAÇÃO CURTA: Proibido operar retração em velas que deixem pavios minúsculos ou corpos excessivamente curtos. O pavio deve ser longo e impactante.
- FILTRO DE RSI EM CONSOLIDAÇÃO INDEFINIDA: Aborte se o RSI estiver travado em linha reta perto da linha 50.

[PASSO 7: CRONOMETRAGEM DE EXECUÇÃO E GESTÃO DE LOTE]
- Projete o HORÁRIO DO CLIQUE rigorosamente para uma janela futura de **2 a 5 minutos** à frente. Expiração fixa de 1 minuto para fechar na mesma vela do clique projetado.
- Classifique a taxa de acerto de forma realista de **80% a 95%**. Se houver risco do RSI continuar esticado, determine como OPERAÇÃO ABORTADA (taxa 0% - FILTRO ATIVADO).

Retorne o diagnóstico estruturado exatamente neste formato markdown limpo e destacado:

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Ex: 84% ou 93% - Dentro do padrão calibrado. Se for Abortada, escreva '0% - FILTRO ATIVADO'] (Escreva destacado e em tamanho grande)

⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:00 exato projetado entre 2 a 5 minutos para o futuro]
⏳ TEMPO DE EXPIRAÇÃO: 1 Minuto (Para fechar na mesma vela do clique)
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:00 do fechamento real da vela]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA / VENDA / OPERAÇÃO ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [SOROS / ENTRADA FIXA / MÃO LEVE / PARADA OBRIGATÓRIA]

🧠 ESTRATÉGIA COMBINADA ATIVADA: [Descreva minuciosamente qual combinação exata ocorreu na tela: se foi Reversão com bastante respeito + Pavio, se foi Rompimento + Fluxo, se foi Pullback + Retração Longa de Pavio ou se foi Fluxo Pós-Reversão analisando o alvo do preço]
🌐 MODO DE MERCADO DETECTADO: [MERCADO ABERTO ou MERCADO OTC]
📊 CONTEXTO DO MERCADO MACRO: [TENDÊNCIA MAJORITÁRIA DE ALTA / TENDÊNCIA MAJORITÁRIA DE BAIXA / CONSOLIDAÇÃO LATERAL SEVERA]
📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA MOMENTUM: [Descreva a posição do RSI, a INCLINAÇÃO ANGULAR e comprove se ele está curvando/retornando ou se está esticado gerando bloqueio]
📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Explique a região que o preço está ou irá buscar e por que levará esse tempo exato até o clique]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO (OPORTUNIDADES IDENTIFICADAS):
- Ambiente Identificado: [MERCADO ABERTO ou OTC]
- Avaliação da Tendência Majoritária e Região Synch: [Análise da macro e o alvo que o preço está buscando]
- Comportamento Gráfico do RSI (Filtro Anti-Loss): [Explique como o filtro de inclinação ou curva do RSI salvou a operação de tomar um loss por rompimento de momentum]
- Verificação de Bloqueios (Retração Curta e Ruídos): [Justifique se a retração foi longa e forte o suficiente para evitar o bloqueio de retração curta]
- Mapeamento das Regiões de Respeito (S/R, LTA/LTB): [Descreva as microzonas]
- Diagnóstico do Fluxo de Continuidade ou Pullback (Cor, Impulso e Corpo): [Análise anatômica das velas, pavios e rompimentos]
- Posicionamento da Média Móvel (EMA 9): [Relação do preço com a EMA 9]
- Justificativa da Gestão de Lote sob Frieza Máxima: [Por que o lote sugerido se adequa a esses fatores rígidos]

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
            resposta_sucesso = False
            resultado = ""
            
            # Loop de contingência para varrer as chaves fornecidas se houver erro
            for i, chave_atual in enumerate(lista_de_chaves):
                status_placeholder.status(f"⏳ Processando análise com a chave de contingência #{i+1}...")
                
                resultado = executar_chamada_gemini(chave_atual, imagem_aberta, PROMPT_TRADER)
                
                if "ERRO_GERADO:" not in resultado:
                    status_placeholder.empty()
                    st.success("✅ Análise gerada com sucesso!")
                    st.markdown(resultado)
                    resposta_sucesso = True
                    break
                else:
                    st.warning(f"⚠️ Chave #{i+1} falhou. Tentando próxima chave da lista...")
            
            if not resposta_sucesso:
                st.error("❌ Todas as chaves de contingência falharam. Verifique os limites ou a validade das chaves no console.")
            else:
                # Verificação explícita e isolada para impedir quebras de identação
                validar_aborto = "OPERAÇÃO ABORTADA" in resultado or "FILTRO ATIVADO" in resultado
                
