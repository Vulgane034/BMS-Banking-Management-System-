# dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Ajouter le chemin du projet au sys.path pour permettre les imports relatifs
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline import run_macro_pipeline
from data_loader import load_beac_data
from chatbot import SimpleChatbot

# --- Configuration de la Page ---
st.set_page_config(layout="wide")
st.title("BMS - Tableau de Bord de Supervision Macroéconomique")
st.write("Ce tableau de bord permet de lancer le pipeline d'analyse prédictive et de visualiser les résultats à partir des données de la BEAC.")

# --- Barre latérale pour les paramètres ---
st.sidebar.header("Paramètres de l'Analyse")

# Charger les données une seule fois
@st.cache_data
def cached_load_beac_data():
    """Charge les données de la BEAC et les met en cache."""
    return load_beac_data()

data_for_columns = cached_load_beac_data()

if data_for_columns is not None:
    # Obtenir les colonnes numériques pour le sélecteur
    numeric_columns = data_for_columns.select_dtypes(include=np.number).columns.tolist()
else:
    st.sidebar.error("Impossible de charger les données pour le sélecteur de colonnes.")
    numeric_columns = []

# Sélecteur de colonne cible pour l'analyse
target_column = st.sidebar.selectbox(
    "Choisissez la variable à prédire",
    options=numeric_columns,
    index=numeric_columns.index('Avoirs ext.') if 'Avoirs ext.' in numeric_columns else 0
)

# Sélecteur de caractéristiques pour l'analyse multivariée
feature_columns = st.sidebar.multiselect(
    "Choisissez les caractéristiques pour l'entraînement",
    options=[col for col in numeric_columns if col != target_column],
    default=[col for col in numeric_columns if col != target_column][:2] # Sélectionner les 2 premières par défaut
)


# Paramètres du modèle LSTM
st.sidebar.subheader("Paramètres du Modèle")
look_back = st.sidebar.slider("Période de Look-Back", 1, 10, 3)
epochs = st.sidebar.slider("Nombre d'Époques d'Entraînement", 5, 50, 10)

# Paramètres d'alerte basés sur la colonne cible
st.sidebar.subheader("Paramètres d'Alerte")
alert_threshold = st.sidebar.number_input(f"Seuil d'alerte pour {target_column}", value=500000.0)

# --- Contenu Principal ---
if st.button("Lancer l'Analyse"):
    with st.spinner(f"Analyse multivariée de '{target_column}' en cours..."):
        # Exécuter le pipeline complet
        df, scores, recommendations, y_true, y_pred = run_macro_pipeline(
            feature_columns=feature_columns,
            target_column=target_column,
            look_back=look_back,
            epochs=epochs
        )

    if df is not None and not df.empty:
        st.success("Analyse terminée !")

        # Vérification et affichage du seuil d'alerte
        last_value = df[target_column].iloc[-1]
        if last_value < alert_threshold:
            st.error(f"⚠️ ALERTE : La dernière valeur de {target_column} ({last_value:,.2f}) est en dessous du seuil de {alert_threshold:,.2f}.")

        # --- Affichage des Résultats en Colonnes ---
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Résultats de l'Évaluation du Modèle")
            st.json(scores)

            st.subheader("Recommandations de Politique Monétaire")
            for rec in recommendations:
                st.info(rec)

        with col2:
            st.subheader(f"Statistiques Descriptives pour {target_column}")
            st.write(df[target_column].describe())

            st.subheader(f"Distribution de {target_column}")
            st.bar_chart(df[target_column])

        # Afficher le graphique des prédictions
        st.subheader(f"Prédictions vs. Données Réelles ({target_column})")
        chart_data = pd.DataFrame({
            'Période': df['Period'].iloc[-len(y_true):],
            'Données Réelles': y_true.flatten(),
            'Prédictions': y_pred.flatten()
        }).set_index('Période')
        st.line_chart(chart_data)

        # Option pour afficher les données complètes
        if st.checkbox("Afficher les données complètes nettoyées"):
            st.subheader("Données Complètes de la BEAC")
            st.dataframe(df)

    else:
        st.error("Impossible de récupérer ou de traiter les données. Le pipeline ne peut pas continuer.")

else:
    st.info("Ajustez les paramètres dans la barre latérale et cliquez sur 'Lancer l'Analyse' pour commencer.")

# --- Section du Chatbot ---
st.subheader("Chatbot Expert")
st.write("Posez des questions sur les données chargées.")

if data_for_columns is not None:
    # Initialiser le chatbot avec les données chargées
    chatbot = SimpleChatbot(data_for_columns)

    # Initialiser l'historique de la conversation
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Afficher l'historique de la conversation
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Obtenir l'entrée de l'utilisateur et générer une réponse
    if prompt := st.chat_input("Votre question"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = chatbot.get_response(prompt)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
else:
    st.warning("Les données n'ont pas pu être chargées, le chatbot est donc désactivé.")
