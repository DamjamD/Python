from datasource.api import APICollector
from contracts.schema import SeguroSchema

from azurestore.client import AzureBlobStorage

schema = SeguroSchema
azure = AzureBlobStorage()
API
my_class = APICollector(schema, azure).start(3)

print(my_class)