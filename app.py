import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="IA Financière RDC", page_icon="🇨🇩", layout="wide")

st.title("🇨🇩 Système d'Analyse Financière Stratégique")
st.markdown("---")

# Barre latérale pour les entrées
st.sidebar.header("Paramètres de Calcul")
capital = st.sidebar.number_input("Capital Initial ($)", value=1000, step=100)
taux = st.sidebar.slider("Taux de Croissance Annuel (%)", 1, 100, 15)
annees = st.sidebar.number_input("Durée de la projection (Années)", 1, 20, 5)

# Calculs de projection
annees_liste = list(range(0, annees + 1))
valeurs = [round(capital * (1 + taux/100)**t, 2) for t in annees_liste]
df = pd.DataFrame({"Année": annees_liste, "Projection ($)": valeurs})

# Affichage des indicateurs clés (Tableau de bord)
col1, col2, col3 = st.columns(3)
col1.metric("Capital Initial", f"{capital} $")
col2.metric("Taux appliqué", f"{taux} %")
col3.metric("Valeur Finale", f"{valeurs[-1]} $", f"+{round(valeurs[-1]-capital, 2)} $")

st.markdown("---")

# Graphique de croissance interactif
st.subheader("📈 Évolution de la Croissance Stratégique")
st.line_chart(df.set_index("Année"))

# Tableau de données détaillé
with st.expander("Voir le détail des calculs par année"):
    st.write("Ce tableau montre l'évolution annuelle de votre investissement.")
    st.table(df)

st.info("Adolphe, cette version pro permet une analyse plus fine pour tes futurs projets en RDC.")

