# pipeline.py
"""
Ce module contient le pipeline principal pour le traitement des données,
l'entraînement du modèle, l'évaluation et la génération de recommandations.
"""

import pandas as pd
import numpy as np
from data_loader import fetch_world_bank_data, CEMAC_COUNTRIES
from models.lstm.lstm import train_lstm, predict_lstm
from models.evaluation.evaluation import evaluate_models
from recommendation.recommendation import generate_recommendations
from sklearn.preprocessing import MinMaxScaler

def run_macro_pipeline(country_code="CMR", look_back=3, epochs=5):
    """
    Exécute le pipeline macroéconomique complet pour un pays donné.
    """
    # Étape 1: Charger les données réelles depuis la Banque Mondiale
    df = fetch_world_bank_data(country_code)

    if df.empty or len(df) < 10: # S'assurer qu'il y a assez de données
        print(f"Pas assez de données pour le pays {CEMAC_COUNTRIES.get(country_code, country_code)}.")
        return pd.DataFrame(), {}, [], np.array([]), np.array([])

    # Étape 2: Préparer les données pour le LSTM (en utilisant l'inflation)
    data = df['inflation'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)

    def create_dataset(dataset, look_back=1):
        dataX, dataY = [], []
        for i in range(len(dataset) - look_back - 1):
            a = dataset[i:(i + look_back), 0]
            dataX.append(a)
            dataY.append(dataset[i + look_back, 0])
        return np.array(dataX), np.array(dataY)

    train_size = int(len(data_scaled) * 0.8)
    train, test = data_scaled[0:train_size, :], data_scaled[train_size:len(data_scaled), :]

    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)

    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

    # Étape 3: Entraîner le modèle LSTM
    lstm_model = train_lstm(trainX, trainY, testX, testY, epochs=epochs)

    # Étape 4: Faire des prédictions
    test_predict_scaled = predict_lstm(lstm_model, testX)
    test_predict = scaler.inverse_transform(test_predict_scaled.reshape(-1, 1))

    # Inverser la transformation pour les données de test originales
    original_testY = scaler.inverse_transform(testY.reshape(-1, 1))

    # Étape 5: Évaluer le modèle
    results = {'LSTM': (original_testY.flatten(), test_predict.flatten())}
    scores = evaluate_models(results)

    # Étape 6: Générer des recommandations
    recommendations = generate_recommendations(scores)

    return df, scores, recommendations, original_testY, test_predict
