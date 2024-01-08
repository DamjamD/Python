from typing import Union, Dict


GenericSchema = Dict[str, Union[str, float, int]]


SeguroSchema: GenericSchema = {
     
  "empresa_id": int,  
  "produtor": str,
  "cliente_nome": str,
  "sexo": str,
  "data_nascimento": str,
  "email": str, 
  "inicio_vigencia": str,
  "fim_vigencia": str,
  "renovacao": int,

  
}
