# main.py
"""
Point d'entrée principal du projet BEAC Macroéconomie Prédictive
"""
import os
import pandas as pd
from data.simulation_data import generate_macro_data
from evaluation.evaluation import evaluate_models
from recommendation.recommendation import generate_recommendations

# Charger ou générer les données
DATA_PATH = os.path.join('data', 'macro_data.csv')
if not os.path.exists(DATA_PATH):
    df = generate_macro_data()
    df.to_csv(DATA_PATH, index=False)
else:
    df = pd.read_csv(DATA_PATH)

# TODO: Charger et entraîner les modèles, évaluer, comparer, recommander
# Voir les modules dans hmm_model, lstm_model, stochastic_model, bvar_model

# Exemple d'appel d'évaluation (à compléter)
# results = evaluate_models(df)
# generate_recommendations(results)

print('Pipeline macroéconomique prêt. Voir dashboard pour visualisation.')