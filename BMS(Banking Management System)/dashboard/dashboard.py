# dashboard.py
import streamlit as st
import pandas as pd
import sys
import os

# Ajouter le chemin du projet au sys.path pour permettre les imports relatifs
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline import run_macro_pipeline

st.title("BMS - Tableau de Bord de Supervision Macroéconomique")
st.write("Ce tableau de bord permet de lancer le pipeline d'analyse prédictive et de visualiser les résultats.")

# Barre latérale pour les paramètres du modèle
st.sidebar.header("Paramètres du Modèle")
look_back = st.sidebar.slider("Période de Look-Back (mois)", 1, 12, 3)
epochs = st.sidebar.slider("Nombre d'Époques d'Entraînement", 5, 50, 10)

if st.button("Lancer l'Analyse"):
    # Exécuter le pipeline avec les paramètres configurés
    st.write(f"Entraînement du modèle pour {epochs} époques...")
    df, scores, recommendations, y_true, y_pred = run_macro_pipeline(look_back=look_back, epochs=epochs)
    st.success("Analyse terminée !")

    # Afficher les résultats
    st.subheader("Aperçu des Données Macroéconomiques")
    st.write(df.head())

    st.subheader("Résultats de l'Évaluation du Modèle")
    st.json(scores)

    st.subheader("Recommandations de Politique Monétaire")
    for rec in recommendations:
        st.info(rec)

    st.subheader("Prédictions vs. Données Réelles (Inflation)")
    chart_data = pd.DataFrame({
        'Données Réelles': y_true.flatten(),
        'Prédictions': y_pred.flatten()
    })
    st.line_chart(chart_data)
