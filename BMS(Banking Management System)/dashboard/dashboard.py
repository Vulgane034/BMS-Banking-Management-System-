import streamlit as st
import pandas as pd
import os

st.title('Tableau de bord macroéconomique BEAC')

# Charger les données simulées
DATA_PATH = os.path.join('..', 'data', 'macro_data.csv')
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    st.line_chart(df.set_index('date'))
else:
    st.warning('Aucune donnée disponible. Veuillez générer les données via main.py.')

# Placeholder pour les résultats de modèles
st.header('Comparaison des modèles')
st.write('Les résultats des modèles seront affichés ici.')

# Placeholder pour recommandations
st.header('Recommandations')
st.write('Les recommandations seront générées après l’évaluation des modèles.')