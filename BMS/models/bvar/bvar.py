import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR

class BVARModel:
    def __init__(self, lags=2):
        self.lags = lags
        self.model = None
        self.results = None

    def fit(self, df):
        self.model = VAR(df)
        self.results = self.model.fit(self.lags)

    def predict(self, steps=1):
        return self.results.forecast(self.results.y, steps=steps)

# Exemple d'utilisation
if __name__ == "__main__":
    from data.simulation_data import generate_macro_data
    df = generate_macro_data()
    bvar = BVARModel()
    bvar.fit(df[['inflation', 'croissance', 'taux_change', 'masse_monetaire']])
    pred = bvar.predict(steps=5)
    print(pred)