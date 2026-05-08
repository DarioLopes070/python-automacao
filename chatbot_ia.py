# pip install streamlit
# pip install google-genai
import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

if not "historico_mensagens" in st.session_state:
    st.session_state.historico_mensagens = []

st.write("# Chatbot com IA")
texto_do_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagem in st.session_state.historico_mensagens:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)  # Exibe as mensagens do histórico

if texto_do_usuario:
    st.chat_message("user").write(texto_do_usuario)  # Exibe a mensagem do usuário
    mensagem_usuario = {"role": "user", "content": texto_do_usuario}
    st.session_state.historico_mensagens.append(
        mensagem_usuario
    )  # Adiciona a mensagem do usuário ao histórico

    # transforma em texto
    resposta_da_ia = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents="\n".join(
            [
                f"{msg['role']}: {msg['content']}"
                for msg in st.session_state.historico_mensagens
            ]
        ),
    )
    print(resposta_da_ia)  # Exibe a resposta da IA no console (para depuração)

    mensagem_da_ia = (
        "Resposta da IA: " + resposta_da_ia.text
    )  # Usa a resposta real da IA
    st.chat_message("assistant").write(mensagem_da_ia)  # Exibe a resposta da IA
    mensagem_ia = {"role": "assistant", "content": mensagem_da_ia}
    st.session_state.historico_mensagens.append(
        mensagem_ia
    )  # Adiciona a mensagem da IA ao histórico

print(
    st.session_state.historico_mensagens
)  # Exibe o histórico de mensagens no console (para depuração)
