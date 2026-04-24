import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. Configuration du design
st.set_page_config(page_title="IA Financière RDC", page_icon="🇨🇩", layout="wide")

# 2. Activation du cerveau (Gemini)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.title("🇨🇩 Mon Assistant Stratégique RDC")
st.markdown("---")

# 3. Menu latéral pour les chiffres
with st.sidebar:
    st.header("📊 Paramètres de calcul")
    capital = st.number_input("Capital Initial ($)", value=1000)
    taux = st.slider("Taux de croissance (%)", 1, 100, 15)
    annees = st.number_input("Durée (Années)", 1, 20, 5)

# 4. Zone de Discussion (Le Chat)
st.subheader("💬 Posez vos questions à l'IA")
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage de la discussion
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée de l'utilisateur
if prompt := st.chat_input("Ex: Comment développer l'industrie à Goma ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # L'IA génère sa réponse
        response = model.generate_content(f"Tu es un expert financier et conseiller stratégique en RDC. Réponds de façon concise à : {prompt}")
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})


