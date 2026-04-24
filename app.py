import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Assistant RDC", page_icon="🇨🇩")

# Ta clé API
cle = "AIzaSyANe8DsHypqgxyIrpQ4zVCOLshPiGTZAvk"

# Configuration ultra-simple
genai.configure(api_key=cle)
# On change 'gemini-1.5-flash' par 'gemini-pro' qui est plus ancien et stable
model = genai.GenerativeModel('gemini-pro')

st.title("🇨🇩 Mon Assistant Intelligent")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pose ta question..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.chat_history.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erreur : {e}")
