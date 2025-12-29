import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def mae(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)

def evaluate_models(results_dict):
    """
    Prend un dict {model: (y_true, y_pred)} et retourne un DataFrame de scores.
    """
    scores = {}
    for model, (y_true, y_pred) in results_dict.items():
        scores[model] = {
            'RMSE': rmse(y_true, y_pred),
            'MAE': mae(y_true, y_pred)
        }
    return scores