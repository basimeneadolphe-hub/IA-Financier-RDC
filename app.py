import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mon IA", page_icon="🇨🇩")

# Ta clé API
p1 = "AIzaSyANe8DsHypqgxyIrpQ4"
p2 = "zVCOLshPiGTZAvk"
cle_complete = p1 + p2

# Configuration avec forçage de la version stable
genai.configure(api_key=cle_complete)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Intelligent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Pose ta question ici..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # On demande explicitement la version stable
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erreur technique : {e}")
