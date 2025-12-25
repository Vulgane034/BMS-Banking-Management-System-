# main.py
"""
Point d'entrée principal pour exécuter le pipeline d'analyse macroéconomique
en ligne de commande.
"""
from pipeline import run_macro_pipeline

if __name__ == "__main__":
    print("Lancement du pipeline macroéconomique avec les données de la BEAC...")

    # Définir les colonnes de caractéristiques et la colonne cible
    feature_columns = ['Créances sur l\'Etat', 'Créances sur les institutions financières']
    target_column = 'Avoirs ext.'

    # Exécuter le pipeline avec des paramètres par défaut
    df, scores, recommendations, _, _ = run_macro_pipeline(
        feature_columns=feature_columns,
        target_column=target_column,
        look_back=3,
        epochs=10
    )

    if df is not None and not df.empty:
        print("\n--- Aperçu des Données ---")
        print(df.head())

        print("\n--- Scores du Modèle ---")
        print(scores)

        print("\n--- Recommandations ---")
        for rec in recommendations:
            print(f"- {rec}")

    else:
        print("Le pipeline n'a pas pu s'exécuter en raison d'un problème de données.")

    print('\nPipeline terminé.')
