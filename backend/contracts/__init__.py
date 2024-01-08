from typing import Union, Dict

GenericSchema = Dict[str,Union[str,float, int]]

VendaSeguro: GenericSchema = {
    "usuario": str,
    "produto_id": int
}