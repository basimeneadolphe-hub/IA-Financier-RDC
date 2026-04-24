import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mon IA", page_icon="🇨🇩")

# --- TA NOUVELLE CLÉ ICI ---
p1 = "AIzaSyANe8DsHypqgxyIrpQ4"
p2 = "zVCOLshPiGTZAvk"
cle_complete = p1 + p2

genai.configure(api_key=cle_complete)
model = genai.GenerativeModel('gemini-1.5-flash')
# ---------------------------

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
        except Exception as e:
            st.error(f"Erreur technique : {e}")
