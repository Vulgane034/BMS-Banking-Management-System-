import requests
import pandas as pd

def fetch_macro_data_worldbank(indicator, country):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json"
    r = requests.get(url)
    data = r.json()[1]
    df = pd.DataFrame(data)
    return df