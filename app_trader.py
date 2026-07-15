import streamlit as st
from google import genai
from PIL import Image
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os

# 1. Configuração da Página e Inicialização de Arquivo
st.set_page_config(page_title="Agente IA Advanced - Matriz Suprema", page_icon="🤖", layout="centered")

ARQUIVO_HISTORICO = "historico_trader.json"
FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")

def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_historico(dados):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

historico = carregar_historico()

# Títulos Principais
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
        st.sidebar.metric("🏆 Taxa de Acerto Real", f"{taxor_acerto:.1f}%")
        st.sidebar.write(f"Operações avaliadas: {total_auditado}")
    else:
        st.sidebar.info("Aguardando auditoria das ordens no final da página.")
    st.sidebar.markdown("---")
    if st.sidebar.button("🗑️ Limpar Histórico Local"):
        if os.path.exists(ARQUIVO_HISTORICO):
            os.remove(ARQUIVO_HISTORICO)
        st.rerun()
else:
    st.sidebar.info("Nenhuma operação registrada ainda.")

# 3. Interface Principal de Inputs
st.markdown("### 📷 Entrada de Dados do Gráfico")
uploaded_file = st.file_uploader("Faça o upload do Print do seu Gráfico (M1):", type=["png", "jpg", "jpeg"])

botao_analise = st.button("🧠 Iniciar Análise Avançada por IA", use_container_width=True)

# 4. Definição Dinâmica do Prompt Mestre
def gerar_prompt_mestre(horario_referencia):
    horario_formatado = horario_referencia.strftime('%H:%M:%S')
    return f"""[SYSTEM_ROLE] Você é um algoritmo de trading quantitativo focado em Opções Binárias e Price Action Avançado Estrutural. Sua postura é de FRIEZA MÁXIMA, RIGOR ABSOLUTO E PRECISÃO CIRÚRGICA.

[ANCORAGEM TEMPORAL E PROJEÇÃO FUTURA CRITICA OBRIGATÓRIA]
O horário exato em que este print foi capturado no fuso do Brasil é: {horario_formatado}.
REGRAS CRUCIAL DE CÁLCULO DE TEMPO DE DESLOCAMENTO FUTURO:
1. Você deve analisar graficamente quantos minutos o preço levará para atingir a zona ou concluir o movimento desejado. Projete e escolha obrigatoriamente um tempo futuro de expiração de 3 a 10 minutos à frente.
2. O 'HORÁRIO DO CLIQUE (ENTRADA)' NÃO pode ser igual ao horário do print ({horario_formatado}). Calcule e projete o clique alguns minutos à frente (ex: de 1 a 4 minutos à frente de {horario_formatado}) dependendo do gatilho gráfico estimado.
3. O 'HORÁRIO DE FECHAMENTO DA ORDEM' deve ser rigorosamente igual à soma matemática: (HORÁRIO DO CLIQUE + TEMPO DE EXPIRAÇÃO DEFINIDO). Faça a soma dos minutos com precisão absoluta.

[REGRA DE OURO: PROIBIDO PADRÕES DE VELAS]
ATENÇÃO: Você está PROIBIDO de basear suas decisões em padrões isolados de velas (como Martelo, Engolfo, Doji, etc.). Sua análise deve ignorar nomes de velas e focar puramente na ESTRUTURA DINÂMICA DO PREÇO e na anatomia física dos candles.

[REGRA OPERACIONAL DA ANATOMIA DO PREÇO: RETRAÇÃO VS PULLBACK]
Sua tomada de decisão sobre zonas estruturais e zonas ocultas deve seguir estritamente duas regras:
1. SE O GRÁFICO APRESENTAR BASTANTE PAVIO (Alta densidade de pavios e rejeição): Você deve operar focado em RETRAÇÃO INSTANTÂNEA nas zonas estruturais ou ocultas mapeadas.
2. SE O GRÁFICO APRESENTAR VELAS DE FORÇA OU DE CONTINUAÇÃO (Corpos cheios, expressivos e sem pavio): Você está PROIBIDO de operar retração. Você deve, obrigatoriamente, ESPERAR O ROMPIMENTO E O PULLBACK da região (ou seguir o fluxo momentâneo) para projetar a sua entrada.

[ANÁLISE ESTRUTURAL DO PREÇO E LIQUIDEZ]
Mapeie topos e fundos majoritários, canais de preço, linhas de tendência (LTA/LTB) e ZONAS OCULTAS de suporte/resistência (Order Blocks, Imbalances ou Acumulações antigas). Avalie a agressividade com que o mercado se move e calcule o espaço livre que o preço tem para correr antes de encontrar uma barreira real.

[DIRETRIZ DE SEGURANÇA MÁXIMA: GATILHO DE REVERSÃO EM REGIÃO VS FLUXO MOMENTÂNEO]
Mude seu comportamento dinamicamente com base na proximidade do preço em relação às zonas estruturais demarcadas:
- Se você detectar que o preço JÁ ESTIVER NA REGIÃO de reversão forte (testando topos/fundos relevantes ou simetrias fortes), ative o [OPERACIONAL DE REVERSÃO EM REGIÃO], aplicando o filtro de anatomia (retração se houver pavio, ou aguardando o pullback se for vela de força).
- CASO CONTRÁRIO (se o preço estiver distante da região de reversão), você está PROIBIDO de antecipar reversões. Nesse cenário, entre imediatamente a favor do [FLUXO MOMENTÂNEO DO GRÁFICO], surfando a continuidade do movimento atual até o próximo alvo estrutural de liquidez.

[PASSO 1: IDENTIFICAÇÃO DO AMBIENTE]
Identifique o ativo e se é [MERCADO ABERTO REAL] ou [ALGORITMO OTC].

[PASSO 2: FILTROS DE TENDÊNCIA E FLUXO DE CORES (MÍNIMO 4 VELAS)]
Identifique se há uma sequência de 4 velas ou mais consecutivas da mesma cor com corpos expressivos e poucos pavios para fluxo de continuidade.

[PASSO 3: FILTROS DE FLUXO PARA RETRAÇÃO]
Identifique se o preço se movimenta com candles médios que deixam bastante pavio buscando regiões estruturais de S/R ou LTA/LTB.

[PASSO 4: LOGICA DE OPERAÇÃO DINÂMICA (REVERSÃO OU FLUXO MOMENTÂNEO)]
Avalie a distância até a zona de respeito baseado na estrutura do preço. Se estiver nela, projete o clique de reversão de 3 à 10 minutos (ideal 5 a 6 min). Se estiver longe, configure a entrada para seguir o fluxo momentâneo da tendência atual.

[PASSO 5: REGRA DO RSI]
Proibido reverter se o RSI estiver cruzando de forma reta e agressiva os extremos. Aguarde a perda de angulação ou siga o fluxo estrutural.

[PASSO 6: MATRIZ DE ESTRATÉGIA COMBINADA ATIVADA]
Avalie com base em: 1. LEITURA DA ESTRUTURA DO PREÇO (ALTA ASSERTIVIDADE), 2. ANATOMIA DA VELA (PAVIO = RETRAÇÃO | FORÇA = PULLBACK), 3. OPERACIONAL DE REVERSÃO EM REGIÃO (SE JÁ NA REGIÃO), 4. FLUXO MOMENTÂNEO DO GRÁFICO (SE LONGE DA REGIÃO), 5. FLUXO DE CONTINUIDADE (4+ VELAS).

[PASSO 7: PROTOCOLO DE BLOQUEIO]
Bloqueie retrações contra velas de força cheias. Aborte operações que vão contra a estrutura vigente sem confirmação de rompimento ou sem alvo claro.

[PASSO 8: CRONOMETRAGEM E GESTÃO DE ALTA ASSERTIVIDADE]
Projete o clique entre 3 a 10 minutos à frente. Atribua taxas rigorosas de assertividade entre 75% a 98% baseando-se unicamente na confluência dos fatores estruturais filtrados. Se não houver clareza técnica total na estrutura, ordene a operação como Abortada (0%).

Retorne o diagnóstico estruturado exatamente neste formato markdown (mantenha rigidamente os rótulos abaixo):

🎯 PORCENTAGEM DE ACERTO DA ENTRADA: [Resultado de 75% a 98% ou Abortada 0%]
⏰ HORÁRIO DO CLIQUE (ENTRADA): [HH:MM:SS - Calcule obrigatoriamente projetando minutos à frente no futuro]
⏳ TEMPO DE EXPIRAÇÃO: [Ex: 5 Minutos]
🏁 HORÁRIO DE FECHAMENTO DA ORDEM: [HH:MM:SS - Deve ser exatamente o horário do clique + tempo de expiração]
🟥🟩 DIREÇÃO EXATA DA ORDEM: [COMPRA/VENDA/ABORTADA]
💰 GERENCIAMENTO DE LOTE RECOMENDADO: [Gerenciamento]
🧠 ESTRATÉGIA E OPERACIONAL COMBINADO ATIVADO:
- Tipo de operacional isolado ativado (Exemplos: 'OPERACIONAL DE REVERSÃO EM REGIÃO', 'FLUXO MOMENTÂNEO DO GRÁFICO', 'OPERACIONAL DE PULLBACK', ou 'OPERACIONAL DE RETRAÇÃO EM ZONA STRUCT').
- Detalhes dos gatilhos, anatomia observada nos candles (força ou pavio) e a proximidade da região alvo estrutural.
- Descrição minuciosa da combinação (Estrutura do preço + Retração por pavio em zona oculta, Vela de força + Espera de Pullback, Quebra de pivô + Fluxo momentâneo, etc).
🌐 MODO DE MERCADO DETECTADO: [Mercado]
📊 CONTEXTO DO MERCADO MACRO E MICRO (ALINHAMENTO): [Tendência e Padrão Estrutural de Topos/Fundos]
📈 LEITURA DO RSI PADRÃO E GATILHO CONTRA/A FAVOR DO MOMENTUM: [RSI]
📊 JUSTIFICATIVA DA REGIÃO E PROJEÇÃO TEMPORAL: [Justificativa baseada no deslocamento estrutural, anatomia das velas e tempo]

🔍 DETALHAMENTO ANATÔMICO, ESTRUTURAL E TÉCNICO:
- Ambiente Identificado
- Trajetória pós-Print e Leitura de Estrutura do Preço (Topos, Fundos e Pivôs)
- Análise de Reversão em Região vs Fluxo Momentâneo (Filtro de Posição Estrutural)
- Decisão por Anatomia: Presença de pavios expressivos (Retração) ou corpo cheio (Pullback/Fluxo)
- Padrão Sequencial de Cores e Força do Fluxo
- Densidade dos Pavios e Regiões de Retração Estrutural
- Comportamento do RSI e Angulação do Preço
- Verificação de Bloqueios de Estrutura (Filtro de proteção contra velas cheias)
- Regiões de Respeito e Alvos Disponíveis na Estrutura (Incluindo Zonas Ocultas)
- Gestão de Lote
"""

def executar_chamada_gemini(chaves, imagem_objeto, prompt_comando):
    modelos = ['gemini-2.5-flash', 'gemini-2.5-pro']
    conteudo = [imagem_objeto, prompt_comando]
    for k in chaves:
        for m in modelos:
            try:
                cli = genai.Client(api_key=k)
                res = cli.models.generate_content(model=m, contents=conteudo)
                return res.text
            except Exception as e:
