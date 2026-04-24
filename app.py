import streamlit as st
import google.generativeai as genai

# 1. Configuration de l'interface
st.set_page_config(page_title="Mon Assistant Intelligent", page_icon="🇨🇩")

# 2. Configuration de ta nouvelle clé API
# Nous la coupons en deux pour éviter les erreurs de lecture sur mobile
p1 = "AIzaSyANe8DsHypqgxyIrpQ4"
p2 = "zVCOLshPiGTZAvk"
cle_complete = p1 + p2

# 3. Initialisation du modèle Google
genai.configure(api_key=cle_complete)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Intelligent")

# 4. Gestion de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des anciens messages
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 5. Zone de saisie utilisateur
if prompt := st.chat_input("Pose ta question ici..."):
    # Ajouter le message de l'utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Génération de la réponse par l'IA
    with st.chat_message("assistant"):
        try:
            # Appel à l'IA de Google
            response = model.generate_content(prompt)
            reponse_texte = response.text
            
            st.markdown(reponse_texte)
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({"role": "assistant", "content": reponse_texte})
            
        except Exception as e:
            # Affiche l'erreur réelle pour nous aider à diagnostiquer si ça bloque
            st.error(f"Erreur technique : {e}")
