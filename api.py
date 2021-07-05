from joblib import load
import pandas as pd
import uvicorn
from fastapi import FastAPI
from function import accent, lemma_enumerate

import nltk
from unidecode import unidecode
import spacy

model= load('model.pkl')

app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'Detecção operador cliente'}

@app.get('/teste/')
async def detect(message:str):
  text = pd.Series(message)
  previsao = model.predict(text)
  return int(previsao)

if __name__ == '__main__':
   uvicorn.run('api:app', host='0.0.0.0', port=8000)    