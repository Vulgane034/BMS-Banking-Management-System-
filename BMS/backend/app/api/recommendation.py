from fastapi import APIRouter, Depends
from app.services.gemini_service import get_gemini_recommendations
import os

router = APIRouter()

@router.get("")
def gemini_recommendation():
    prompt = "Donne-moi 3 recommandations macroéconomiques pour la BEAC en zone CEMAC."
    api_key = os.getenv("GEMINI_API_KEY")
    recs = get_gemini_recommendations(prompt, api_key)
    return {"recommendations": recs.split('\n')}