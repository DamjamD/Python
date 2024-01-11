import requests
import pandas as pd
import datetime
import json
from io import BytesIO
from contracts.schema import GenericSchema
from typing import List


class APICollector:
    def __init__(self, schema, azure, data):
        self._schema = schema
        self._azure = azure
        self._buffer = None
        self._data = data
        return

    def start(self, data):
        #response = self.getData(param)
        response = data
        response = self.extractData(response)
        response = self.transformDf(response)
        print(type(response))
        response = self.convertToParquet(response)
    

        if self._buffer is not None:
            file_name = self.fileName()
       
            self._azure.upload_file(self._buffer.getvalue(), file_name)
            return response

        return response

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
        result: List[GenericSchema] = []

        index = {}
        for key, expected_type in self._schema.items():
            item_value = response.get(key)
            
            # Verificar se a chave está presente e o tipo é o esperado
            if item_value is not None and isinstance(item_value, expected_type):
                index[key] = item_value
            else:
                # Se a validação falhar, você pode optar por omitir a chave ou definir como None
                index[key] = None

        result.append(index)

        return result


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
        return f"teleport/auto_grava/{match[0]}.parquet"
