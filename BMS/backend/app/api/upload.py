from fastapi import APIRouter, File, UploadFile, Depends
from app.services.report_parser import parse_report

router = APIRouter()

@router.post("")
async def upload_report(file: UploadFile = File(...)):
    data = await parse_report(file)
    return {"status": "ok", "data": data}