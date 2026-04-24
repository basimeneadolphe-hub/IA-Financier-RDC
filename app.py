import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="IA Stratégique RDC", page_icon="🇨🇩")

# Connexion sécurisée
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# Utilisation du modèle le plus récent (1.5 Flash)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Stratégique RDC")

# Historique de discussion
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if prompt := st.chat_input("Posez votre question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Génération de la réponse
            response = model.generate_content(f"Tu es un expert en développement pour la RDC. Réponds en français à : {prompt}")
            text_response = response.text
            st.markdown(text_response)
            
            # Option Audio (Le texte s'affiche, et on peut l'écouter)
            # Note: Pour un vrai micro en temps réel, c'est très complexe, 
            # mais voici une astuce pour lire le texte :
            st.audio(f"https://translate.google.com/translate_tts?ie=UTF-8&tl=fr&client=tw-ob&q={text_response[:200]}")
            
            st.session_state.messages.append({"role": "assistant", "content": text_response})
        except Exception as e:
            st.error("Désolé, j'ai eu un petit problème technique. Réessayez !")
