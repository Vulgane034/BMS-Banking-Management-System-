# pipeline.py
"""
Ce module contient le pipeline principal pour le traitement des données,
l'entraînement du modèle, l'évaluation et la génération de recommandations.
"""

import pandas as pd
import numpy as np
import os
from data.simulation_data import generate_macro_data
from models.lstm.lstm import train_lstm, predict_lstm
from models.evaluation.evaluation import evaluate_models
from recommendation.recommendation import generate_recommendations
from sklearn.preprocessing import MinMaxScaler

def run_macro_pipeline(look_back=3, epochs=5):
    """
    Exécute le pipeline macroéconomique complet.
    """
    # Charger ou générer les données
    # Le chemin est maintenant relatif au répertoire racine du projet
    DATA_PATH = os.path.join('data', 'macro_data.csv')
    if not os.path.exists(DATA_PATH):
        df = generate_macro_data()
        # S'assurer que le répertoire data existe
        os.makedirs('data', exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
    else:
        df = pd.read_csv(DATA_PATH)

    # Préparer les données pour le LSTM
    def create_dataset(dataset, look_back=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-look_back-1):
            a = dataset[i:(i+look_back), 0]
            dataX.append(a)
            dataY.append(dataset[i + look_back, 0])
        return np.array(dataX), np.array(dataY)

    data = df['inflation'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)

    train_size = int(len(data) * 0.8)
    train, test = data[0:train_size,:], data[train_size:len(data),:]

    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)

    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

    # Entraîner le modèle LSTM
    lstm_model = train_lstm(trainX, trainY, testX, testY, epochs=epochs)

    # Faire des prédictions
    test_predict = predict_lstm(lstm_model, testX)

    # Inverser la normalisation
    test_predict = scaler.inverse_transform(test_predict.reshape(-1, 1))
    original_testY = scaler.inverse_transform(testY.reshape(-1, 1))

    # Évaluer le modèle
    results = {'LSTM': (original_testY.flatten(), test_predict.flatten())}
    scores = evaluate_models(results)

    # Générer des recommandations
    recommendations = generate_recommendations(scores)

    return df, scores, recommendations, original_testY, test_predict
