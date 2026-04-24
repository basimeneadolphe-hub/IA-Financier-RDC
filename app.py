import streamlit as st
import google.generativeai as genai

# Configuration de l'app
st.set_page_config(page_title="Mon IA Perso", page_icon="🇨🇩")

# MÉTHODE DIRECTE : On branche ta clé ici (plus besoin des Secrets)
genai.configure(api_key="AIzaSyDP98nptCOu6NxOib1na6iNcZae1T2B9Ls")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Intelligent")

# Mémoire de la discussion
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if prompt := st.chat_input("Dis-moi n'importe quoi..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # L'IA répond maintenant à tout (Généraliste)
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Erreur de connexion. Vérifie que ton téléphone est bien connecté à internet.")
