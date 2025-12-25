# pipeline.py
"""
Ce module contient le pipeline principal pour le traitement des données,
l'entraînement du modèle, l'évaluation et la génération de recommandations.
"""

import pandas as pd
import numpy as np
from data_loader import load_beac_data
from models.lstm.lstm import train_lstm, predict_lstm
from models.evaluation.evaluation import evaluate_models
from recommendation.recommendation import generate_recommendations
from sklearn.preprocessing import MinMaxScaler

def run_macro_pipeline(feature_columns, target_column='Avoirs ext.', look_back=3, epochs=5):
    """
    Exécute le pipeline macroéconomique complet pour une colonne cible et des caractéristiques données.
    """
    df = load_beac_data()

    if df is None or df.empty or len(df) < 10:
        print("Pas assez de données.")
        return pd.DataFrame(), {}, [], np.array([]), np.array([])

    all_columns = feature_columns + [target_column]
    for col in all_columns:
        if col not in df.columns:
            print(f"La colonne '{col}' n'a pas été trouvée dans les données.")
            return pd.DataFrame(), {}, [], np.array([]), np.array([])
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(subset=all_columns, inplace=True)

    data = df[all_columns].values
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)

    def create_dataset(dataset, look_back=1):
        dataX, dataY = [], []
        for i in range(len(dataset) - look_back):
            dataX.append(dataset[i:(i + look_back), :])
            dataY.append(dataset[i + look_back, -1]) # La dernière colonne est la cible
        return np.array(dataX), np.array(dataY)

    train_size = int(len(data_scaled) * 0.8)
    train, test = data_scaled[0:train_size, :], data_scaled[train_size:len(data_scaled), :]

    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)

    # Le LSTM s'attend à [échantillons, pas de temps, caractéristiques]
    # trainX est déjà dans le bon format de pas de temps

    lstm_model = train_lstm(trainX, trainY, testX, testY, epochs=epochs, input_shape=(look_back, len(all_columns)))

    test_predict_scaled = predict_lstm(lstm_model, testX)

    # Nous devons inverser l'échelle en utilisant un hack car le scaler s'attend à la même forme
    # que les données originales
    dummy_array = np.zeros((len(test_predict_scaled), len(all_columns)))
    dummy_array[:, -1] = test_predict_scaled.flatten()
    test_predict = scaler.inverse_transform(dummy_array)[:, -1]

    dummy_array_true = np.zeros((len(testY), len(all_columns)))
    dummy_array_true[:, -1] = testY.flatten()
    original_testY = scaler.inverse_transform(dummy_array_true)[:, -1]

    results = {'LSTM': (original_testY, test_predict)}
    scores = evaluate_models(results)
    recommendations = generate_recommendations(scores)

    return df, scores, recommendations, original_testY, test_predict
