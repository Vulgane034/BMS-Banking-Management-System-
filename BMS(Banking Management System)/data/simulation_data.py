import numpy as np
import pandas as pd

def generate_macro_data(n_periods=120, seed=42):
    """
    Génère un DataFrame simulant des séries temporelles macroéconomiques réalistes.
    """
    np.random.seed(seed)
    dates = pd.date_range(start='2013-01-01', periods=n_periods, freq='M')
    inflation = np.random.normal(3, 1, n_periods).cumsum() / 20 + 2
    croissance = np.random.normal(0.5, 0.2, n_periods).cumsum() / 10 + 1
    taux_change = 600 + np.random.normal(0, 5, n_periods).cumsum()
    masse_monet = 1000 + np.random.normal(0, 20, n_periods).cumsum()
    df = pd.DataFrame({
        'date': dates,
        'inflation': inflation,
        'croissance': croissance,
        'taux_change': taux_change,
        'masse_monetaire': masse_monet
    })
    return df

if __name__ == "__main__":
    df = generate_macro_data()
    print(df.head())