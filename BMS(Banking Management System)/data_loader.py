# data_loader.py
import wbdata
import pandas as pd

# Définition des pays de la CEMAC et de leurs codes ISO
CEMAC_COUNTRIES = {
    "CMR": "Cameroun",
    "COG": "Congo",
    "GAB": "Gabon",
    "TCD": "Tchad",
    "CAF": "République Centrafricaine",
    "GNQ": "Guinée Équatoriale"
}

# Définition des indicateurs de la Banque Mondiale que nous voulons utiliser
INDICATORS = {
    "FP.CPI.TOTL.ZG": "inflation",
    "NY.GDP.MKTP.KD.ZG": "croissance_gdp"
}

def fetch_world_bank_data(country_code):
    """
    Télécharge les données macroéconomiques pour un pays donné depuis l'API de la Banque Mondiale.
    """
    try:
        # Utiliser l'appel le plus simple et le plus compatible
        df = wbdata.get_dataframe(INDICATORS, country=country_code)

        # Renommer les colonnes
        df = df.rename(columns=INDICATORS)

        # L'index est 'country' et 'date', nous les réinitialisons
        df = df.reset_index()

        # Renommer la colonne 'date' en 'year' et convertir en numérique
        df = df.rename(columns={'date': 'year'})
        df['year'] = pd.to_numeric(df['year'])

        # Filtrer pour ne garder que les années après 2000
        start_year = 2000
        df = df[df['year'] >= start_year]

        # Trier par année
        df = df.sort_values('year', ascending=True)

        # Interpoler les valeurs manquantes
        df = df.interpolate(method='linear', limit_direction='forward')
        df = df.dropna()

        return df

    except Exception as e:
        print(f"Erreur lors du téléchargement des données pour {country_code}: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    cameroon_data = fetch_world_bank_data("CMR")
    if not cameroon_data.empty:
        print("Données pour le Cameroun :")
        print(cameroon_data.head())
