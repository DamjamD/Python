import requests
import pandas as pd
import datetime
import json
from io import BytesIO
from contracts.schema import GenericSchema
from typing import List
import uuid


class APICollector:
    def __init__(self, schema, azure, data):
        self._schema = schema
        self._azure = azure
        self._buffer = None
        self._data = data
        return

    def start(self, data):
        try:
            response = data
            response = self.extractData(response)
            response = self.transformDf(response)
            response = self.convertToJson(response)
            
            if self._buffer is not None:
                file_name = self.fileName()
                try:
                    self._azure.upload_file(self._buffer.getvalue(),file_name)
                    return True
                except Exception as e:
                    print(f"Erro ao Fazer Upload de Arquivo: {e}")
                    return False

        except Exception as error:
            print(f"Erro geral: {error}")
            return False

        return False
    

    def getData(self, param):
        response = None
        if param > 1:
            response = requests.get(
                f"http://127.0.0.1:8000/autos_grava/{param}"
            ).json()
        else:
            response = requests.get("http://127.0.0.1:8000/auto_grava").json()
        return response
    

    def extractData(self, response, separator='_'):
        result = {}
        
       
        def recursive_extract(obj, prefix=''):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_key = f"{prefix}{key}" if prefix else key
                   
                    recursive_extract(value, new_key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    recursive_extract(item, f"{prefix}{i}{separator}")
            else:
                result[prefix] = obj

        recursive_extract(response)
        return result
        

    def transformDf(self, response):
        try:
            df = pd.json_normalize(response, record_path=None)
            json_result = df.to_json()
            return df
            
        except Exception as e:
            print(f"Erro durante a normalização do JSON: {e}")
            return e
        

    def convertToParquet(self, response):
        self._buffer = BytesIO()
        
        try:
            response.to_parquet(self._buffer)
            return self._buffer
        except:
            print("Erro ao transformar o DF em parquet")
            self._buffer = None
    
    def convertToJson(self, response):
        try:
            self._buffer = BytesIO()
            response.to_json(self._buffer, orient='records', lines=True, force_ascii=False)
            return self._buffer
        except Exception as e:
            print(f"Erro ao transformar o DF em JSON: {e}")
            self._buffer = None
            return None


    def fileName(self):
        data_atual = datetime.datetime.now().isoformat()
        match = data_atual.split(".")
        unique_id = str(uuid.uuid4().hex)  # Gera um UUID único como string hexadecimal
        return f"teleport/auto_grava/{match[0]}_{unique_id}.json"
