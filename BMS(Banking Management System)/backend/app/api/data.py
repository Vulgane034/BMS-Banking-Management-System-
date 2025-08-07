from fastapi import APIRouter, Depends
from app.services.data_collector import fetch_macro_data_worldbank

router = APIRouter()

@router.get("/worldbank")
def get_worldbank_data(indicator: str, country: str):
    df = fetch_macro_data_worldbank(indicator, country)
    return df.to_dict(orient="records")