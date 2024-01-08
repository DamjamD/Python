from datasource.api import APICollector
from contracts.schema import SeguroSchema
from azurestore.client import AzureBlobStorage

schema = SeguroSchema
azure = AzureBlobStorage()
my_class = APICollector(schema, azure).start(10)

print(my_class)