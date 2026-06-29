# Linha 112
prompt_especifico = """
Cole o seu texto do prompt aqui normalmente.
 Garanta que ele termine com as três aspas abaixo.
""" 

# ... (outras linhas de lógica do seu robô) ...

# Bloco dos botões atualizado (sem o botão de gerar sinal)
col1, col2 = st.columns(2)
with col1:
    if st.button("🟩 WIN", use_container_width=True):
        pass # substitua pelo seu código de win

with col2:
    if st.button("🟥 LOSS", use_container_width=True):
        pass # substitua pelo seu código de loss
