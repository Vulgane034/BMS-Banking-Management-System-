# chatbot.py
import pandas as pd
import re

class SimpleChatbot:
    def __init__(self, data):
        self.data = data.select_dtypes(include=['number']) # Utiliser uniquement les colonnes numériques

    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        # Regex pour les demandes de corrélation
        corr_match = re.search(r"corrélation entre (.+) et (.+)", user_input)
        if corr_match:
            col1_name = self._find_column(corr_match.group(1).strip())
            col2_name = self._find_column(corr_match.group(2).strip())
            if col1_name and col2_name:
                return self._calculate_correlation(col1_name, col2_name)
            else:
                return f"Désolé, je n'ai pas pu trouver une ou les deux colonnes. Les colonnes disponibles sont : {', '.join(self.data.columns)}"

        # Regex pour les demandes de moyenne
        mean_match = re.search(r"moyenne de (.+)", user_input)
        if mean_match:
            column_name = self._find_column(mean_match.group(1).strip())
            if column_name:
                return self._calculate_mean(column_name)
            else:
                return f"Désolé, je n'ai pas pu trouver cette colonne. Les colonnes disponibles sont : {', '.join(self.data.columns)}"

        # Regex pour les demandes de valeur maximale
        max_match = re.search(r"valeur maximale de (.+)", user_input)
        if max_match:
            column_name = self._find_column(max_match.group(1).strip())
            if column_name:
                return self._get_max_value(column_name)
            else:
                return f"Désolé, je n'ai pas pu trouver cette colonne. Les colonnes disponibles sont : {', '.join(self.data.columns)}"

        # Regex pour les demandes de valeur minimale
        min_match = re.search(r"valeur minimale de (.+)", user_input)
        if min_match:
            column_name = self._find_column(min_match.group(1).strip())
            if column_name:
                return self._get_min_value(column_name)
            else:
                return f"Désolé, je n'ai pas pu trouver cette colonne. Les colonnes disponibles sont : {', '.join(self.data.columns)}"

        return "Désolé, je ne comprends pas. Essayez 'moyenne de [colonne]' ou 'corrélation entre [colonne1] et [colonne2]'."

    def _find_column(self, partial_name):
        # Essayer de trouver une colonne qui correspond au nom partiel
        for col in self.data.columns:
            if partial_name in col.lower():
                return col
        return None

    def _calculate_mean(self, column_name):
        try:
            mean_value = self.data[column_name].mean()
            return f"La moyenne de {column_name} est de {mean_value:,.2f}."
        except Exception as e:
            return f"Erreur lors du calcul de la moyenne : {e}"

    def _get_max_value(self, column_name):
        try:
            max_value = self.data[column_name].max()
            return f"La valeur maximale de {column_name} est de {max_value:,.2f}."
        except Exception as e:
            return f"Erreur lors de l'obtention de la valeur maximale : {e}"

    def _get_min_value(self, column_name):
        try:
            min_value = self.data[column_name].min()
            return f"La valeur minimale de {column_name} est de {min_value:,.2f}."
        except Exception as e:
            return f"Erreur lors de l'obtention de la valeur minimale : {e}"

    def _calculate_correlation(self, col1, col2):
        try:
            correlation = self.data[col1].corr(self.data[col2])
            return f"La corrélation entre {col1} et {col2} est de {correlation:.2f}."
        except Exception as e:
            return f"Erreur lors du calcul de la corrélation : {e}"
