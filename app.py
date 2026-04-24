import streamlit as st
import google.generativeai as genai

# 1. Configuration de la page
st.set_page_config(page_title="Mon IA", page_icon="🇨🇩")

# 2. Ta nouvelle clé API (déjà intégrée)
p1 = "AIzaSyANe8DsHypqgxyIrpQ4"
p2 = "zVCOLshPiGTZAvk"
cle_complete = p1 + p2

# 3. Configuration du modèle (Utilisation de gemini-pro pour éviter l'erreur 404)
genai.configure(api_key=cle_complete)
model = genai.GenerativeModel('gemini-pro')

st.title("🇨🇩 Mon Assistant Intelligent")

# 4. Gestion de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 5. Zone de saisie et réponse
if p := st.chat_input("Pose ta question..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    with st.chat_message("assistant"):
        try:
            # Appel à l'IA
            r = model.generate_content(p)
            st.markdown(r.text)
            st.session_state.messages.append({"role": "assistant", "content": r.text})
        except Exception as e:
            # Affiche l'erreur précise si ça bloque encore
            st.error(f"Erreur technique : {e}")
