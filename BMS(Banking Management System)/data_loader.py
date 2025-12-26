import pandas as pd
import os

# Construire un chemin absolu vers le répertoire de données
# Cela garantit que le fichier de données peut être trouvé quel que soit le répertoire de travail actuel
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
DEFAULT_FILE_PATH = os.path.join(DATA_DIR, 'CEMAC_2025.xls')

def load_beac_data(file_path=DEFAULT_FILE_PATH):
    """
    Charge et analyse les statistiques monétaires de la BEAC à partir d'un fichier Excel.

    Args:
        file_path (str): Le chemin vers le fichier Excel.

    Returns:
        pandas.DataFrame: Un DataFrame contenant les données analysées.
    """
    try:
        # Lire la feuille 'BEAC', en utilisant la ligne 3 comme en-tête
        df = pd.read_excel(file_path, sheet_name='BEAC', header=3)

        # Nettoyer les noms de colonnes
        df.columns = df.columns.str.strip()

        # Supprimer la première ligne qui est vide
        df = df.drop(0)

        # Renommer la première colonne pour plus de clarté
        df = df.rename(columns={'Fin de périodes                ACTIF': 'Period'})

        # Supprimer les colonnes qui sont entièrement NaN
        df = df.dropna(axis=1, how='all')

        # Remplir les NaN dans la colonne 'Period'
        df['Period'] = df['Period'].ffill()

        # Supprimer les lignes où toutes les colonnes de données (sauf 'Period') sont NaN
        data_columns = [col for col in df.columns if col != 'Period']
        df = df.dropna(subset=data_columns, how='all')

        return df

    except FileNotFoundError:
        print(f"Fichier non trouvé : {file_path}")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

if __name__ == '__main__':
    data = load_beac_data()
    if data is not None:
        print("Données de la BEAC chargées et nettoyées avec succès :")
        print(data.head())
        print("\nInformations sur le DataFrame :")
        data.info()
