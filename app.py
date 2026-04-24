import streamlit as st

st.set_page_config(page_title="IA Financière RDC", page_icon="🇨🇩")

st.title("🇨🇩 IA Financière Stratégique")
st.write("Bienvenue Adolphe. Ton application est officiellement sur GitHub !")

# Simulation simple
capital = st.number_input("Capital initial ($)", value=1000)
taux = st.slider("Taux de croissance annuel (%)", 1, 100, 15)

resultat = capital * (1 + taux/100)

st.subheader("Projection à 1 an :")
st.success(f"Votre capital estimé : {round(resultat, 2)} $")
