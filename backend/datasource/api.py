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
            #response = self.transformarDF(response)
            #response = self.convertToParquet(response)
            file_name = self.fileName()

      
            if   self._azure.upload_file(response, file_name):
                print('Foi sucesso')
                return True
            
            else: False
                

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

    def extractData(self, response):
        result = []

        for key in response.keys():
            item_value = response.get(key)
            result.append({key: item_value})
       
        json_string = json.dumps(result)
        #print(json_string)
        return json_string
    

    def transformarDF(self, response):
        df = pd.read_json(response)
       # print(df)
        return df
        

    def transformDf(self, response):
        df = pd.json_normalize(response)
        itens_list = df['itens'].tolist()
        itens_df = pd.DataFrame()
        
        for i, item_dict in enumerate(itens_list):
            
            prefix = f'item_{i}_'
            item_df = pd.json_normalize(item_dict, sep='_')
            
            item_df.columns=[f'{prefix}{col}' for col in item_df.columns]
            itens_df = pd.concat([itens_df, item_df], axis=1)
        
        
        df = pd.concat([df, itens_df], axis=1)
        df = df.drop(columns=['itens'])
      
        return df

    def convertToParquet(self, response):
        self._buffer = BytesIO()
        
        try:
            response.to_parquet(self._buffer)
            return self._buffer
        except:
            print("Erro ao transformar o DF em parquet")
            self._buffer = None

    def fileName(self):
        data_atual = datetime.datetime.now().isoformat()
        match = data_atual.split(".")
        unique_id = str(uuid.uuid4().hex)  # Gera um UUID único como string hexadecimal
        return f"teleport/auto_grava/{match[0]}_{unique_id}.json"
