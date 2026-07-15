import streamlit as st
from google import genai
from PIL import Image
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Biblioteca nativa para fuso horário de Brasília
import json
import os

# 1. Configuração da Página e Inicialização de Arquivo
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

ARQUIVO_HISTORICO = "historico_trader.json"
FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")

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
st.write("Fusão Total: Estrutura Dinâmica do Preço, Projeção Temporal Avançada (3 a 10 Minutos) e Análise de Proximidade.")

# 2. Barra Lateral e Painel Estatístico Real
st.sidebar.markdown("### 🔑 Gerenciador de Chaves de Contingência")
chaves_input = st.sidebar.text_input("Cole suas Gemini API Keys aqui (separadas por ponto e vírgula):", type="password")
lista_de_chaves = [chave.strip() for chave in chaves_input.split(";") if chave.strip()]

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Painel Estatístico Real")
if historico:
    total_auditado = sum(1 for x in historico if x.get("resultado_manual") in ["WIN", "LOSS"])
    wins = sum(1 for x in historico if x.get("resultado_manual") == "WIN")
    
    if total_auditado > 0:
        taxa_acerto = (wins / total_auditado) * 100
        st.sidebar.metric("🏆 Taxa de Acerto Real", f"{taxa_acerto:.1f}%")
        st.sidebar.write(f"Operações avaliadas: {total_auditado}")
    else:
        st.sidebar.info("Aguardando auditoria das ordens no final da página.")
else:
    st.sidebar.info("Nenhuma operação registrada ainda.")

# 3. Definição Dinâmica do Prompt Mestre com Cálculo de Tempo Futuro Embutido
def gerar_prompt_mestre(horario_referencia):
    horario_formatado = horario_referencia.strftime('%H:%M:%S')
    return (
        "[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias e Price Action Avançado Estrutural. "
        "Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.\n\n"
        
        "[ANCORAGEM TEMPORAL E PROJEÇÃO FUTURA CRITICA OBRIGATÓRIA]\n"
        f"O horário exato em que este print foi capturado no fuso do Brasil é: {horario_formatado}.\n"
        "REGRAS CRUCIAL DE CÁLCULO DE TEMPO DE DESLOCAMENTO FUTURO:\n"
        "1. Você deve analisar graficamente quantos minutos o preço levará para atingir a zona ou concluir o movimento desejado. Projete e escolha obrigatoriamente um tempo futuro de expiração de 3 a 10 minutos à frente.\n"
        f"2. O 'HORÁRIO DO CLIQUE (ENTRADA)' NÃO pode ser igual ao horário do print ({horario_formatado}). Calcule e projete o clique alguns minutos à frente (ex: de 1 a 4 minutos à frente de {horario_formatado}) dependendo do gatilho gráfico estimado.\n"
        "3. O 'HORÁRIO DE FECHAMENTO DA ORDEM' deve ser rigorosamente igual à soma matemática: (HORÁRIO DO CLIQUE + TEMPO DE EXPIRAÇÃO DEFINIDO). Faça a soma dos minutos com precisão absoluta.\n\n"
        
        "[REGRA DE OURO: PROIBIDO PADRÕES DE VELAS]\n"
        "ATENÇÃO: Você está PROIBIDO de basear suas decisões em padrões isolados de velas (como Martelo, Engolfo, Doji, etc.). "
        "Sua análise deve ignorar nomes de velas e focar puramente na ESTRUTURA DINÂMICA DO PREÇO e na anatomia física dos candles.\n\n"
        
        "[REGRA OPERACIONAL DA ANATOMIA DO PREÇO: RETRAÇÃO VS PULLBACK]\n"
        "Sua tomada de decisão sobre zonas estruturais e zonas ocultas deve seguir estritamente duas regras:\n"
        "1. SE O GRÁFICO APRESENTAR BASTANTE PAVIO (Alta densidade de pavios e rejeição): Você deve operar focado em RETRAÇÃO INSTANTÂNEA nas zonas estruturais ou ocultas mapeadas.\n"
        "2. SE O GRÁFICO APRESENTAR VELAS DE FORÇA OU DE CONTINUAÇÃO (Corpos cheios, expressivos e sem pavio): Você está PROIBIDO de operar retração. Você deve, obrigatoriamente, ESPERAR O ROMPIMENTO E O PULLBACK da região (ou seguir o fluxo momentâneo) para projetar a sua entrada.\n\n"
        
        "[ANÁLISE ESTRUTURAL DO PREÇO E LIQUIDEZ]\n"
        "Mapeie topos e fundos majoritários, canais de preço, lines de tendência (LTA/LTB) e ZONAS OCULTAS de suporte/resistência (Order Blocks, Imbalances ou Acumulações antigas). "
        "Avalie a agressividade com que o mercado se move e calcule o espaço livre que o preço tem para correr antes de encontrar uma barreira real.\n\n"
        
        "[DIRETRIZ DE SEGURANÇA MÁXIMA: GATILHO DE REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]\n"
        "Mude seu comportamento dinamicamente com base na proximidade do preço em relação às zonas estruturais demarcadas:\n"
        "- Se você detectar que o preço JÁ ESTIVER NA REGIÃO de reversão forte (testando topos/fundos relevantes ou simetrias fortes), "
        "ative o [OPERACIONAL DE REVERSÃO EM REGIÃO], aplicando o filtro de anatomia (retração se houver pavio, ou aguardando o pullback se for vela de força).\n"
        "- CASO CONTRÁRIO (se o preço estiver distante da região de reversão), você está PROIBIDO de antecipar reversões. "
        "Nesse cenário, entre imediatamente a favor do [FLUXO MOMENTÂNEO DO GRÁFICO], surfando a continuidade do movimento atual até o próximo alvo estrutural de liquidez.\n\n"
        
        "[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]\n"
        "Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].\n\n"
        
        "[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]\n"
        "Identifique se há uma sequência de 4 velas ou mais consecutivas da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.\n\n"
        
        "[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]\n"
        "Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões estruturais de S/R ou LTA/LTB.\n\n"
        
        "[PASSO 4: LOGICA DE OPERAÇÃO DINÂMICA (REVERSÃO OU FLUXO MOMENTÂNEO)]\n"
        "Avalie a distância até a zona de respeito baseado na estrutura do preço. Se estiver nela, projete o clique de reversão de 3 à 10 minutos (ideal 5 a 6 min). "
        "Se estiver longe, configure a entrada para seguir o fluxo momentâneo da tendência atual.\n\n"
        
        "[PASSO 5: REGRA DO RSI]\n"
        "Proibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos. Aguarde a perda de angulação ou siga o fluxo estrutural.\n\n"
        
        "[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]\n"
        "Avalie com base em: 1. LEITURA DA ESTRUTURA DO PREÇO (ALTA ASSERTIVIDADE), 2. ANATOMIA DA VELA (PAVIO = RETRAÇÃO | FORÇA = PULLBACK), 3. OPERACIONAL DE REVERSÃO EM REGIÃO (SE JÁ NA REGIÃO), 4. FLUXO MOMENTÂNEO DO GRÁFICO (SE LONGE DA REGIÃO), 5. FLUXO DE CONTINUIDADE (4+ VELAS).\n\n"
        
        "[PASSO 7: PROTOCOLO DE BLOQUEIO]\n"
        "Bloqueie retrações contra velas de força cheias. Aborte operações que vão contra a estrutura vigente sem confirmação de rompimento ou sem alvo claro.\n\n"
        
        "[PASSO 8: CRONOMETRAGEM E GESTÃO DE ALTA ASSERTIVIDADE]\n"
        "Projete o clique entre 3 a 10 minutos à frente. Atribua taxas rigorosas de assertividade entre 75% a 98% baseando-se unicamente "
        "na confluência dos fatores estruturais filtrados. Se não houver clareza técnica total na estrutura, ordene a operação como Abortada (0%).\n\n"
        
        "Retorne o diagnóstico estruturado exatamente neste formato markdown (mantenha rigidamente os rótulos abaixo):\n\n"
        "🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]\n"
        "⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:SS - Calcule obrigatoriamente projetando minutos à frente no futuro]\n"
        "⏳ TEMPO DE EXPIRAÇÃO: [Ex: 5 Minutos]\n"
        "🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:SS - Deve ser exatamente o horário do clique + tempo de expiração]\n"
        "🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]\n"
        "💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Gerenciamento]\n"
        "🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:\n"
        "- Tipo de operacional isolado ativado (Exemplos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'FLUXO MOMENTÂNEO DO GRÁFICO', 'OPERACIONAL DE PULLBACK', ou 'OPERACIONAL DE RETRAÇÃO EM ZONA STRUCT').\n"
        "- Detalhes dos gatilhos, anatomia observada nos candles (força ou pavio) e a proximidade da região alvo estrutural.\n"
        "- Descrição minuciosa da combinação (Estrutura do preço + Retração por pavio em zona oculta, Vela de força + Espera de Pullback, Quebra de pivô + Fluxo momentâneo, etc).\n"
        "🌐 MODO DE MERCADO DETECTADO: [Mercado]\n"
        "📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência e Padrão Estrutural de Topos/Fundos]\n"
        "📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA/A FAVOR DO MOMENTUM: [RSI]\n"
        "📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa baseada no deslocamento estrutural, anatomia das velas e tempo]\n\n"
        "🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:\n"
        "- Ambiente Identificado\n"
        "- Trajetória pós-Print e Leitura de Estrutura do Preço (Topos, Fundos e Pivôs)\n"
        "- Análise de Reversão em Região vs Fluxo Momentâneo (Filtro de Posição Estrutural)\n"
        "- Decisão por Anatomia: Presença de pavios expressivos (Retração) ou corpo cheio (Pullback/Fluxo)\n"
        "- Padrão Sequencial de Cores e Força do Fluxo\n"
        "- Densidade dos Pavios e Regiões de Retração Estrutural\n"
        "- Comportamento do RSI e Angulação do Preço\n"
        "- Verificação de Bloqueios de Estrutura (Filtro de proteção contra velas cheias)\n"
