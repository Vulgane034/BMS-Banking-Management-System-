# main.py
"""
Point d'entrée principal du projet BEAC Macroéconomie Prédictive
"""
from pipeline import run_macro_pipeline

if __name__ == "__main__":
    print("Lancement du pipeline macroéconomique pour le Cameroun (par défaut)...")

    # Exécuter le pipeline avec les paramètres par défaut
    df, scores, recommendations, _, _ = run_macro_pipeline(country_code="CMR", look_back=3, epochs=10)

    if not df.empty:
        print("\n--- Aperçu des Données ---")
        print(df.head())

        print("\n--- Scores du Modèle ---")
        print(scores)

        print("\n--- Recommandations ---")
        for rec in recommendations:
            print(rec)

    print('\nPipeline terminé.')
