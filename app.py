import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="Mon IA Perso", page_icon="🇨🇩")

# Connexion à Gemini avec ta clé
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Intelligent")

# Gestion de la mémoire de la discussion
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Zone de saisie pour l'utilisateur
if prompt := st.chat_input("Dis-moi n'importe quoi..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # L'IA répond maintenant à TOUT (généraliste)
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Petit souci : vérifie que ta clé API est bien enregistrée dans les Secrets Streamlit.")
