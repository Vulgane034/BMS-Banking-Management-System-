import numpy as np
from hmmlearn.hmm import GaussianHMM

class HMMModel:
    def __init__(self, n_components=3, n_iter=100):
        self.model = GaussianHMM(n_components=n_components, n_iter=n_iter)

    def fit(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)

    def predict_next(self, X):
        # Prédit la prochaine valeur comme la moyenne de l'état caché le plus probable
        hidden_states = self.model.predict(X)
        means = self.model.means_.flatten()
        return means[hidden_states[-1]]

# Exemple d'utilisation
if __name__ == "__main__":
    from data.simulation_data import generate_macro_data
    df = generate_macro_data()
    X = df[['inflation']].values
    hmm = HMMModel()
    hmm.fit(X)
    pred = hmm.predict(X)
    print(pred)