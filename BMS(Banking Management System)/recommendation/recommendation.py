def generate_recommendations(scores, threshold_risk=2.5):
    """
    Génère des recommandations de politique et identifie les risques selon les scores des modèles.
    """
    recs = []
    for model, metrics in scores.items():
        if metrics['RMSE'] > threshold_risk:
            recs.append(f"Alerte : Le modèle {model} présente un risque élevé d'erreur de prévision. Surveillez les chocs potentiels.")
        else:
            recs.append(f"Le modèle {model} est fiable. Politique recommandée : Maintenir ou ajuster selon les signaux du modèle.")
    return recs