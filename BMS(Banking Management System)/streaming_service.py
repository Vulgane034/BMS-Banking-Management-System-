# streaming_service.py
import time
from bvmac_scraper import get_latest_boc_url, download_and_parse_boc
import os

# Le chemin est maintenant relatif au répertoire 'BMS(Banking Management System)'
LAST_URL_FILE = "data/last_boc_url.txt"

def check_for_new_data():
    """
    Vérifie s'il y a un nouveau BOC disponible, et si c'est le cas, le télécharge et l'analyse.
    """
    print("Vérification de nouvelles données de la BVMAC...")

    latest_url = get_latest_boc_url()

    if latest_url:
        # Lire la dernière URL traitée
        last_processed_url = ""
        if os.path.exists(LAST_URL_FILE):
            with open(LAST_URL_FILE, 'r') as f:
                last_processed_url = f.read().strip()

        if latest_url != last_processed_url:
            print(f"Nouvelles données trouvées : {latest_url}")
            print("Téléchargement et analyse...")

            download_and_parse_boc(latest_url)

            # Mettre à jour la dernière URL traitée
            with open(LAST_URL_FILE, 'w') as f:
                f.write(latest_url)

            print("Données mises à jour avec succès.")
        else:
            print("Aucune nouvelle donnée trouvée.")
    else:
        print("Impossible de trouver le dernier BOC.")

if __name__ == '__main__':
    # Exécuter le service de streaming en continu
    # Pour cet exemple, nous allons l'exécuter une fois.
    # Dans un environnement de production, cela serait dans une boucle avec une temporisation.
    check_for_new_data()
