# dashboard.py
import streamlit as st
import pandas as pd
import sys
import os

# Ajouter le chemin du projet au sys.path pour permettre les imports relatifs
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline import run_macro_pipeline
from data_loader import CEMAC_COUNTRIES

st.title("BMS - Tableau de Bord de Supervision Macroéconomique")
st.write("Ce tableau de bord permet de lancer le pipeline d'analyse prédictive et de visualiser les résultats.")

# Barre latérale pour les paramètres
st.sidebar.header("Paramètres de l'Analyse")

# Sélecteur de pays
country_name = st.sidebar.selectbox("Choisissez un pays de la CEMAC", list(CEMAC_COUNTRIES.values()))
country_code = [code for code, name in CEMAC_COUNTRIES.items() if name == country_name][0]

# Paramètres du modèle
st.sidebar.subheader("Paramètres du Modèle")
look_back = st.sidebar.slider("Période de Look-Back (années)", 1, 10, 3)
epochs = st.sidebar.slider("Nombre d'Époques d'Entraînement", 5, 50, 10)

# Paramètres d'alerte
st.sidebar.subheader("Paramètres d'Alerte")
inflation_threshold = st.sidebar.number_input("Seuil d'alerte pour l'inflation (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.5)


if st.button("Lancer l'Analyse"):
    with st.spinner(f"Téléchargement des données et entraînement du modèle pour {country_name}..."):
        df, scores, recommendations, y_true, y_pred = run_macro_pipeline(
            country_code=country_code,
            look_back=look_back,
            epochs=epochs
        )

    if not df.empty:
        st.success("Analyse terminée !")

        # Vérification du seuil d'alerte
        last_inflation = df['inflation'].iloc[-1]
        if last_inflation > inflation_threshold:
            st.error(f"⚠️ ALERTE : Le dernier taux d'inflation ({last_inflation:.2f}%) pour {country_name} dépasse le seuil de {inflation_threshold}%.")

        # Afficher les résultats
        st.subheader(f"Aperçu des Données pour {country_name}")
        st.write(df.tail()) # Afficher les dernières données

        st.subheader("Résultats de l'Évaluation du Modèle")
        st.json(scores)

        st.subheader("Recommandations de Politique Monétaire")
        for rec in recommendations:
            st.info(rec)

        st.subheader("Prédictions vs. Données Réelles (Inflation)")
        chart_data = pd.DataFrame({
            'Années': df['year'].iloc[-len(y_true):],
            'Données Réelles': y_true.flatten(),
            'Prédictions': y_pred.flatten()
        })
        st.line_chart(chart_data.set_index('Années'))
    else:
        st.error(f"Impossible de récupérer ou de traiter les données pour {country_name}. Le pipeline ne peut pas continuer.")
