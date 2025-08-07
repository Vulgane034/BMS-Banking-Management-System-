import pdfplumber
import pandas as pd

async def parse_report(file):
    if file.filename.endswith('.pdf'):
        with pdfplumber.open(file.file) as pdf:
            text = ''.join(page.extract_text() for page in pdf.pages)
            return {"text": text}
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file.file)
        return df.to_dict()
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(file.file)
        return df.to_dict()
    else:
        return {"error": "Format non supporté"}