import requests
import pandas as pd
import datetime
from io import BytesIO
from contracts.schema import GenericSchema
from typing import List


class APICollector:
    def __init__(self, schema, azure):
        self._schema = schema
        self._azure = azure
        self._buffer = None
        return

    def start(self, param):
        response = self.getData(param)
        response = self.extractData(response)
        response = self.transformDf(response)
        response = self.convertToParquet(response)

        if self._buffer is not None:
            file_name = self.fileName()
    
            self._azure.upload_file(self._buffer.getvalue(), file_name)
            return True

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
        result: List[GenericSchema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
            result.append(index)
        return result

    def transformDf(self, response):
        result = pd.DataFrame(response)
        return result

    def convertToParquet(self, response):
        print(response)
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
        return f"Teleport/auto_grava{match[0]}.parquet"
