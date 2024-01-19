import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends, Header,Request
from datasource.api import APICollector
from contracts.schema import SeguroSchema
from azurestore.client import AzureBlobStorage
import pandas as pd
from faker import Faker

fake = Faker()
app = FastAPI()

schema = SeguroSchema
azure = AzureBlobStorage()



def verify_key(request: Request):
   
    expected_headers = {
        "Content-Type": "application/json",
        "user-agent": os.environ.get('HEADER_USER'),
        "X-Teleport-Event": os.environ.get('HEADER_EVENT')
    }

    for header, expected_value in expected_headers.items():
        if header.lower() not in request.headers:
            raise HTTPException(status_code=400, detail=f"Header incorreto na requisição.")

        actual_value = request.headers[header.lower()]
        if actual_value != expected_value:
            raise HTTPException(status_code=401, detail=f"Autenticacao Invalida")


    
@app.post("/auto_grava") 
async def auto_grava(request: Request, _=Depends(verify_key)):

  data = await request.json()

  collector = APICollector(schema, azure, data).start(data)
  
  return {"Sucesso": collector}
