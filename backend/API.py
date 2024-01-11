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

SECRET_KEY = "MY_KEY"

def verify_key(api_key: str = Header(...)):
    print(api_key)
    
    
@app.post("/auto_grava") 
async def auto_grava(request: Request):
  data = await request.json()
  
  collector = APICollector(schema, azure, data).start(data)
  
  #print(api_key)
  return {"Sucesso": collector}


    # Adicione suporte para redirecionar HTTP para HTTPS
    #app.add_middleware(HTTPSRedirectMiddleware)

    # Certifique-se de ajustar o caminho dos certificados conforme necessário
    #uvicorn.run(app, host="127.0.0.1", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem", reload=True)
