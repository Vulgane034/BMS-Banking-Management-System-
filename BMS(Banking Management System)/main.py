# main.py
"""
Point d'entrée principal du projet BEAC Macroéconomie Prédictive
"""
from pipeline import run_macro_pipeline

if __name__ == "__main__":
    print("Lancement du pipeline macroéconomique...")

    # Exécuter le pipeline avec les paramètres par défaut
    df, scores, recommendations, _, _ = run_macro_pipeline(look_back=3, epochs=10)

    print("\n--- Aperçu des Données ---")
    print(df.head())

    print("\n--- Scores du Modèle ---")
    print(scores)

    print("\n--- Recommandations ---")
    for rec in recommendations:
        print(rec)

    print('\nPipeline terminé. Pour une visualisation interactive, lancez le dashboard.')
