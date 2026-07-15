import streamlit as st
from google import genai
from PIL import Image
from datetime import datetime
import json
import os

# 1. Configuração da Página e Inicialização de Arquivo
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

ARQUIVO_HISTORICO = "historico_trader.json"

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_historico(dados):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

historico = carregar_historico()

st.title("🤖 Agente IA Trader Pro: Matriz Suprema")
st.write("Fusão Total: Estrutura Dinâmica do Preço, Projeção Temporal Avançada e Análise de Proximidade com Filtro de Confiança Cruzada.")

# 2. Barra Lateral e Painel de Assertividade Real
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Painel Estatístico Real")
if historico:
    total_auditado = sum(1 for x in historico if x["resultado_manual"] in ["WIN", "LOSS"])
    wins = sum(1 for x in historico if x["resultado_manual"] == "WIN")
    
    if total_auditado > 0:
        taxa_acerto = (wins / total_auditado) * 100
        st.sidebar.metric("🏆 Taxa de Acerto Real", f"{taxa_acerto:.1f}%")
        st.sidebar.write(f"Operações avaliadas: {total_auditado}")
    else:
        st.sidebar.info("Aguardando auditoria das ordens no final da página.")
else:
    st.sidebar.info("Nenhuma operação registrada ainda.")

# 3. Interface Principal de Inputs
uploaded_file = st.file_uploader("📷 Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])
horario_atual_print = st.time_input("⏰ Que horas o print foi tirado no gráfico?", datetime.now().time())

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA")

# 4. Definição do Prompt Mestre Otimizado (Filtro de Confiança Cruzada Aplicado)
def gerar_prompt_mestre(horario_referencia):
    return (
        "[SYSTEM_ROLE] Você é um algoritmo analítico quantitativo sênior de visão computacional voltado para Opções Binárias e Price Action Estrutural Puro. "
        "Sua postura é de ceticismo extremo, frieza matemática e foco absoluto em proteção de capital.\n\n"
        
        f"[ANCORAGEM TEMPORAL OBRIGATÓRIA]\n"
        f"O horário exato em que este print foi capturado é: {horario_referencia.strftime('%H:%M:%S')}. "
        "Qualquer cálculo de projeção de tempo (expiração de 3 a 10 minutos) DEVE usar este horário exato como ponto de partida inicial zero.\n\n"
        
        "[REGRA DE OURO IMPRESCINDÍVEL: PROIBIDO PADRÕES DE VELAS]\n"
        "Você está TERMINANTEMENTE PROIBIDO de basear suas decisões em nomenclaturas de velas isoladas (como Martelo, Engolfo, Doji, etc.). "
        "Ignore nomes de velas. Concentre sua visão puramente na ESTRUTURA DINÂMICA DO PREÇO: deslocamento vetorial, velocidade visual de aproximação, "
        "topos/fundos majoritários, canais (LTA/LTB), zonas de simetria e o espaço vazio (vácuo de liquidez) que o preço tem para correr antes de bater em uma barreira.\n\n"
        
        "[DIRETRIZ DE SEGURANÇA: REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]\n"
        "Avalie a distância geométrica do preço atual até as zonas de suporte/resistência mais fortes visíveis no print:\n"
        "- Se o preço JÁ ESTIVER tocando ou dentro da zona cinza de rejeição (testando topos/fundos relevantes), ative o [OPERACIONAL DE REVERSÃO EM REGIÃO], projetando exaustão estrutural para uma contra-tendência.\n""- Se o preço ESTIVER DISTANTE e houver espaço livre até o próximo alvo, ative o [FLUXO MOMENTÂNEO DO GRÁFICO] para surfar a continuidade até o alvo estrutural. É proibido antecipar reversões no meio do caminho.\n\n"
        
        "[PROTOCOLO DE FILTRO DE CONFIANÇA CRUZADA - OBRIGATÓRIO]\n"
        "Antes de definir a direção, você deve confrontar rigidamente a sua própria análise. Mesmo que os indicadores ou o Price Action apontem uma probabilidade estatística teórica alta (como 90% a 98%), "
        "você deve procurar ativamente por motivos para NÃO entrar na operação. Procure por: aproximações aceleradas demais em direção à taxa, falta de pavios de retração nas velas anteriores, "
        "proximidade de horários cheios de virada de vela macro, ou RSI sem angulação clara. "
        "Se encontrar qualquer um desses sinais de risco estrutural, você deve obrigatoriamente rebaixar a recomendação ou ordenar o aborto da entrada, explicando o perigo oculto na linha de risco.\n\n"
        
        "Retorne o diagnóstico estruturado exatamente neste formato markdown (não mude uma linha sequer do layout):\n\n"
        "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]\n"
        "🚨 VEREDITO REAL DE CONFIANÇA: [ENTRAR COM CONFIANÇA / ENTRAR COM LOTE MÍNIMO POR RISCO OCULTO / ABORTAR OPERAÇÃO]\n"
        "⚠️ DETECTADO RISCO OCULTO NA ESTRUTURA? [Sim (especifique em uma frase curta qual é o risco) / Não, estrutura totalmente limpa]\n"
        "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:SS]\n"
        "⏳ TEMPO DE EXPIRAÇÃO: [Ex: 5 Minutos]\n"
        "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:SS]\n"
        "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
        "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Conservador / Moderado / Abortar]\n"
        "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
        "- Tipo de operacional ativo: ['REVERSÃO EM REGIÃO', 'FLUXO MOMENTÂNEO', ou 'RETRAÇÃO ESTRUTURAL']\n"
        "- Detalhes explicativos estruturais.\n\n"
        "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
        "- Resumo analítico do comportamento visual das massas do mercado na imagem."
    )

def executar_chamada_gemini(chave_api, imagem_objeto, prompt_comando):
    modelos_contingencia = ['gemini-2.5-flash', 'gemini-2.5-pro']
    for modelo in modelos_contingencia:
        try:
            client = genai.Client(api_key=chave_api)
            response = client.models.generate_content(model=modelo, contents=[imagem_objeto, prompt_comando])
            return response.text
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                continue
            return f"❌ Erro na API: {str(e)}"
    return "❌ Erro na API: Todos os modelos falharam por instabilidade."

# 5. Execução Lógica Controlada pós-Clique
if botao_analise:
    if not uploaded_file:
        st.error("⚠️ Por favor, faça o upload de uma imagem do gráfico antes de iniciar a análise.")
    elif not lista_de_chaves:
        st.error("⚠️ Insira pelo menos uma Gemini API Key válida na barra lateral antes de analisar.")
    else:
        imagem = Image.open(uploaded_file).convert("RGB")
        st.image(imagem, caption="Gráfico Carregado com Sucesso", use_container_width=True)
        
        with st.spinner("Analisando estrutura pura do preço, distância e tempo futuro..."):
            prompt_dinamico = gerar_prompt_mestre(horario_atual_print)
            resultado_analise = executar_chamada_gemini(lista_de_chaves, imagem, prompt_dinamico)
            
            st.markdown("### 📊 Resultado da Análise da IA")
            
            # Alertas Visuais Baseados no Veredito da IA para proteger o usuário
            if "ABORTAR" in resultado_analise or "Abortada" in resultado_analise:st.error("🚨 ALERTA MÁXIMO: A IA identificou risco extremo. OPERAÇÃO RECOMENDADA COMO ABORTADA!")
            elif "LOTE MÍNIMO" in resultado_analise or "RISCO OCULTO" in resultado_analise:
                st.warning("⚠️ ATENÇÃO: Embora haja sinal, existem riscos ocultos na estrutura. Use lote mínimo!")
            else:
                st.success("🟢 SINAL VALIDADO: Estrutura gráfica limpa e confluente para operação.")
                
            st.markdown(resultado_analise)
            
            # Salva no histórico local JSON
            nova_entrada = {
                "id": len(historico) + 1,
                "data_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "horario_print": horario_atual_print.strftime("%H:%M:%S"),
                "analise_texto": resultado_analise,
                "resultado_manual": "Pendente"
            }
            historico.append(nova_entrada)
            salvar_historico(historico)
            st.success("✅ Análise arquivada com sucesso! Verifique a auditoria no rodapé da página.")
            st.rerun()

# 6. Painel de Auditoria de Resultados (Fim da Página)
st.markdown("---")
st.markdown("### 🔍 Auditoria de Sinais Gerados")

if historico:
    for idx, item in enumerate(reversed(historico)):
        with st.container(border=True):
            st.write(f"Operação #{item['id']} | Registrada em: {item['data_registro']} (Horário do Print: {item['horario_print']})")
            
            with st.expander("Ver texto completo da análise gerada pela IA"):
                st.code(item['analise_texto'])
            
            st.write(f"Status Atual da Auditoria: {item['resultado_manual']}")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button(f"Definir como WIN 🟢", key=f"win_{item['id']}"):
                    historico[len(historico) - 1 - idx]["resultado_manual"] = "WIN"
                    salvar_historico(historico)
                    st.rerun()
            with col2:
                if st.button(f"Definir como LOSS 🔴", key=f"loss_{item['id']}"):
                    historico[len(historico) - 1 - idx]["resultado_manual"] = "LOSS"
                    salvar_historico(historico)
                    st.rerun()
            with col3:
