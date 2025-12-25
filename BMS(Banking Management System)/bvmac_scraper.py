# bvmac_scraper.py
import requests
import tabula
from datetime import datetime, timedelta
import pandas as pd
import os

BASE_URL = "https://www.bvm-ac.org/wp-content/uploads/"
DATA_DIR = "BMS(Banking Management System)/data"

def get_latest_boc_url():
    """
    Construit l'URL du dernier fichier PDF du BOC.
    """
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        date_str = date.strftime("%Y%m%d")
        year = date.strftime("%Y")
        month = date.strftime("%m")
        url = f"{BASE_URL}{year}/{month}/BOC-{date_str}.pdf"
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                return url
        except requests.RequestException:
            continue
    return None

def find_and_clean_stock_table(tables):
    """
    Trouve et nettoie la table des cours des actions parmi une liste de DataFrames.
    """
    for i, df in enumerate(tables):
        # Rechercher des mots-clés dans les en-têtes ou le contenu pour identifier la bonne table
        flat_list = [item for sublist in df.values.tolist() for item in sublist]
        if any("Code ISIN" in str(s) for s in flat_list) or any("Cours du jour" in str(s) for s in flat_list):
            # C'est probablement la bonne table, essayons de la nettoyer

            # La structure est complexe, nous allons essayer une approche de nettoyage plus robuste
            # 1. Trouver la ligne d'en-tête
            header_row_index = -1
            for j, row in df.iterrows():
                if "Code ISIN" in row.to_string():
                    header_row_index = j
                    break

            if header_row_index != -1:
                df.columns = df.iloc[header_row_index]
                df = df.drop(range(header_row_index + 1))

                # Nettoyer les noms de colonnes
                df.columns = df.columns.str.strip()

                # Sélectionner et renommer les colonnes pertinentes
                # Cela nécessitera un débogage itératif
                # Pour l'instant, nous allons retourner le DataFrame nettoyé tel quel
                return df
    return None


def download_and_parse_boc(url, output_pdf_path=os.path.join(DATA_DIR, "latest_boc.pdf")):
    """
    Télécharge un fichier PDF du BOC et en extrait la table des cours des actions.
    """
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        response = requests.get(url)
        with open(output_pdf_path, 'wb') as f:
            f.write(response.content)

        tables = tabula.read_pdf(output_pdf_path, pages=1, multiple_tables=True)

        if tables:
            return find_and_clean_stock_table(tables)
        return None

    except Exception as e:
        print(f"Erreur lors du téléchargement ou de l'analyse du PDF : {e}")
        return None

if __name__ == '__main__':
    print("Recherche du dernier BOC...")
    latest_url = get_latest_boc_url()

    if latest_url:
        print(f"Dernier BOC trouvé à : {latest_url}")
        print("Téléchargement et analyse...")

        stock_data = download_and_parse_boc(latest_url)

        if stock_data is not None and not stock_data.empty:
            print("Extraction et nettoyage des données sur les actions réussis.")
            print("\nAperçu des données sur les actions :")
            print(stock_data.head())

            output_csv_path = os.path.join(DATA_DIR, "boc_stock_data.csv")
            stock_data.to_csv(output_csv_path, index=False)
            print(f"Données enregistrées dans {output_csv_path}")
        else:
            print("Échec de l'extraction ou du nettoyage des données sur les actions du PDF.")
    else:
        print("Impossible de trouver le dernier BOC au cours des 7 derniers jours.")
