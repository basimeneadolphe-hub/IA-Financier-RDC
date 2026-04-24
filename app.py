import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mon IA", page_icon="🇨🇩")

# --- LA CLÉ DOIT RESTER SUR UNE SEULE LIGNE ---
cle ="AIzaSyDP98nptCOu6NxOib1na6iNcZae1T2B9Ls"
genai.configure(api_key=cle)
# ----------------------------------------------

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇨🇩 Mon Assistant Intelligent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("Pose ta question..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    with st.chat_message("assistant"):
        try:
            r = model.generate_content(p)
            st.markdown(r.text)
            st.session_state.messages.append({"role": "assistant", "content": r.text})
        except:
            st.error("Erreur. Vérifie que la clé API n'est pas coupée en deux dans ton code.")
