import streamlit as st
import google.generativeai as genai

# 1. Configuration de l'interface
st.set_page_config(page_title="Mon Assistant Intelligent", page_icon="🇨🇩")

# 2. Branchement direct de la clé API (sur une seule ligne)
genai.configure(api_key="AIzaSyDP98nptCOu6NxOib1na6iNcZae1T2B9Ls")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Intelligent")

# 3. Gestion de la mémoire du chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Zone de saisie
if prompt := st.chat_input("Pose-moi n'importe quelle question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # L'IA est maintenant généraliste
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("L'IA ne parvient pas à répondre. Vérifie que la clé API dans le code est bien sur une seule ligne sans coupure.")
