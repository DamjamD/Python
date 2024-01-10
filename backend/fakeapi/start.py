from fastapi import FastAPI, HTTPException, Depends, Header,Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd
from faker import Faker

fake = Faker()
app = FastAPI()

SECRET_KEY = "MY_KEY"

def verify_key(api_key: str = Header(...)):
    print(api_key)
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Acesso não autorizado: Informe a Secret Key")


@app.post("/auto_grava") 
async def auto_grava(request: Request, api_key: str = Depends(verify_key)):
  data = await request.json()

  #print(data)
  print(api_key)
  return {"received_data": data}

@app.get("/auto_grava")
async def auto_grava():
    return [{
  "extra_doc": None,
  "empresa_id": 965,
  "calculo": 252700,
  "usuario_id": 50209,
  "usuario": "Gilson Batista Junior",
  "usuario_cpf": "360.689.628-06",
  "produtor_id": 2718,
  "produtor": "Gilson Batista Junior",
  "produtor_cpf": "360.689.628-06",
  "sub_produtor_id": None,
  "sub_produtor": None,
  "sub_produtor_cpf": None,
  "co_corretor_ev": None,
  "vendedor_corretora": None,
  "unidade_id": 724,
  "unidade": "Renovação",
  "unidade_sigla": "REN",
  "unidade_de_para": "0",
  "cliente_id": 56489,
  "cliente_vip": 0,
  "cliente_nome": fake.name(),
  "sexo": "M",
  "data_nascimento": "1982-10-26T03:00:00.000Z",
  "email": "relintvaz@gmail.com",
  "email_comercial": None,
  "telefone": None,
  "telefone_comercial": None,
  "celular": "(61) 983246278",
  "tipo_pessoa": "PF",
  "cpf": "727.423.801-91",
  "cnpj": None,
  "inicio_vigencia": "2023-12-28T03:00:00.000Z",
  "fim_vigencia": "2024-12-28T03:00:00.000Z",
  "renovacao": 2,
  "certificado_renovacao": 251418,
  "campanha": None,
  "id_lead": "56489",
  "origem": 99,
  "origem_descricao": "Outros",
  "origem_cliente": None,
  "origem_sistema": None,
  "itens": [
    {
      "empresa_id": 965,
      "calculo": 252700,
      "item": 1,
      "zero_km": 0,
      "fipe": "004522-5",
      "fipe_valor": 112952,
      "marca": "CHEVROLET",
      "modelo": "TRACKER LT 1.0 TURBO 12V FLEX AUT.",
      "ano_fabricacao": 2022,
      "ano_modelo": 2023,
      "combustivel": "Gasolina e Álcool (Flex)",
      "placa": "SGQ8A79",
      "chassi": "8AGEB76H0PR114942",
      "cor": "Outros",
      "blindado": 0,
      "antifurto": 0,
      "utilizacao": "Particular",
      "portas": 4,
      "eixo": 2,
      "categoria_id": 1,
      "categoria_descricao": "Automóvel",
      "carroceria_id": 25,
      "carga": 3,
      "cep_pernoite": "70730776",
      "cep_circulacao": "70730776",
      "proprietario_nome": "Francisco Erico de Castro Vaz",
      "proprietario_cpf": "727.423.801-91",
      "proprietario_cnpj": None,
      "anterior_seguradora": 5355,
      "anterior_seguradora_nome": "Azul",
      "anterior_quantidade_sinistro": 0,
      "anterior_apolice_inicio_vigencia": "2022-12-28T03:00:00.000Z",
      "anterior_apolice_fim_vigencia": "2023-12-28T03:00:00.000Z",
      "anterior_bonus": "04",
      "anterior_apolice": "033527",
      "anterior_sucursal": "0",
      "anterior_item": 1,
      "anterior_ci": "",
      "anterior_susep": "41104J",
      "anterior_codigo_renovacao": "",
      "cobertura_casco_tipo": "Compreensiva",
      "cobertura_casco_acessorio_nome": "     ",
      "cobertura_casco_acessorio_nome2": "     ",
      "cobertura_casco_acessorio_valor": 0,
      "cobertura_casco_acessorio_valor2": 0,
      "cobertura_casco_equipamento_nome": "Sem Equipamento",
      "cobertura_casco_equipamento_valor": 0,
      "cobertura_casco_fipe_tipo": "valor de mercado",
      "cobertura_casco_fipe_valor": 100,
      "cobertura_casco_vidro": 2,
      "cobertura_casco_despesas_extras": 0,
      "cobertura_casco_blindagem": 0,
      "cobertura_casco_blindagem_valor": 0,
      "cobertura_rcf_danos_materiais": 150000,
      "cobertura_rcf_danos_corporais": 150000,
      "cobertura_rcf_danos_morais": 5000,
      "cobertura_rcf_diarias_paralisacao": 0,
      "cobertura_app_passageiros": 5,
      "cobertura_app_morte": 5000,
      "cobertura_app_invalidez": 5000,
      "cobertura_app_despesa_hospital": 0,
      "tem_condutor": 1,
      "cp_nome": "Francisco Erico de Castro Vaz",
      "cp_cpf": "727.423.801-91",
      "cp_sexo": "M",
      "cp_nascimento": "1982-10-26T03:00:00.000Z",
      "cp_profissao": None
    }
  ]

         }]

@app.get("/autos_grava/{numero_registro}")
async def auto_grava(numero_registro: int):
    if numero_registro < 1:
        return {"Error": "Valor nao pode ser menor que 1 "}
    result = []
    
    for _ in range(numero_registro):
            data =  {
                "extra_doc": None,
                "empresa_id": 965,
                "calculo": 252700,
                "usuario_id": 50209,
                "usuario":  fake.name(),
                "usuario_cpf": "360.689.628-06",
                "produtor_id": 2718,
                "produtor":  fake.name(),
                "produtor_cpf": "360.689.628-06",
                "sub_produtor_id": None,
                "sub_produtor": None,
                "sub_produtor_cpf": None,
                "co_corretor_ev": None,
                "vendedor_corretora": None,
                "unidade_id": 724,
                "unidade": "Renovação",
                "unidade_sigla": "REN",
                "unidade_de_para": "0",
                "cliente_id": 56489,
                "cliente_vip": 0,
                "cliente_nome": fake.name(),
                "sexo": "M",
                "data_nascimento": "1982-10-26T03:00:00.000Z",
                "email": "relintvaz@gmail.com",
                "email_comercial": None,
                "telefone": None,
                "telefone_comercial": None,
                "celular": "(61) 983246278",
                "tipo_pessoa": "PF",
                "cpf": "727.423.801-91",
                "cnpj": None,
                "inicio_vigencia": "2023-12-28T03:00:00.000Z",
                "fim_vigencia": "2024-12-28T03:00:00.000Z",
                "renovacao": 2,
                "certificado_renovacao": 251418,
                "campanha": None,
                "id_lead": "56489",
                "origem": 99,
                "origem_descricao": "Outros",
                "origem_cliente": None,
                "origem_sistema": None,
                "itens": [
                    {
                    "empresa_id": 965,
                    "calculo": 252700,
                    "item": 1,
                    "zero_km": 0,
                    "fipe": "004522-5",
                    "fipe_valor": 112952,
                    "marca": "CHEVROLET",
                    "modelo": "TRACKER LT 1.0 TURBO 12V FLEX AUT.",
                    "ano_fabricacao": 2022,
                    "ano_modelo": 2023,
                    "combustivel": "Gasolina e Álcool (Flex)",
                    "placa": "SGQ8A79",
                    "chassi": "8AGEB76H0PR114942",
                    "cor": "Outros",
                    "blindado": 0,
                    "antifurto": 0,
                    "utilizacao": "Particular",
                    "portas": 4,
                    "eixo": 2,
                    "categoria_id": 1,
                    "categoria_descricao": "Automóvel",
                    "carroceria_id": 25,
                    "carga": 3,
                    "cep_pernoite": "70730776",
                    "cep_circulacao": "70730776",
                    "proprietario_nome": "Francisco Erico de Castro Vaz",
                    "proprietario_cpf": "727.423.801-91",
                    "proprietario_cnpj": None,
                    "anterior_seguradora": 5355,
                    "anterior_seguradora_nome": "Azul",
                    "anterior_quantidade_sinistro": 0,
                    "anterior_apolice_inicio_vigencia": "2022-12-28T03:00:00.000Z",
                    "anterior_apolice_fim_vigencia": "2023-12-28T03:00:00.000Z",
                    "anterior_bonus": "04",
                    "anterior_apolice": "033527",
                    "anterior_sucursal": "0",
                    "anterior_item": 1,
                    "anterior_ci": "",
                    "anterior_susep": "41104J",
                    "anterior_codigo_renovacao": "",
                    "cobertura_casco_tipo": "Compreensiva",
                    "cobertura_casco_acessorio_nome": "     ",
                    "cobertura_casco_acessorio_nome2": "     ",
                    "cobertura_casco_acessorio_valor": 0,
                    "cobertura_casco_acessorio_valor2": 0,
                    "cobertura_casco_equipamento_nome": "Sem Equipamento",
                    "cobertura_casco_equipamento_valor": 0,
                    "cobertura_casco_fipe_tipo": "valor de mercado",
                    "cobertura_casco_fipe_valor": 100,
                    "cobertura_casco_vidro": 2,
                    "cobertura_casco_despesas_extras": 0,
                    "cobertura_casco_blindagem": 0,
                    "cobertura_casco_blindagem_valor": 0,
                    "cobertura_rcf_danos_materiais": 150000,
                    "cobertura_rcf_danos_corporais": 150000,
                    "cobertura_rcf_danos_morais": 5000,
                    "cobertura_rcf_diarias_paralisacao": 0,
                    "cobertura_app_passageiros": 5,
                    "cobertura_app_morte": 5000,
                    "cobertura_app_invalidez": 5000,
                    "cobertura_app_despesa_hospital": 0,
                    "tem_condutor": 1,
                    "cp_nome": "Francisco Erico de Castro Vaz",
                    "cp_cpf": "727.423.801-91",
                    "cp_sexo": "M",
                    "cp_nascimento": "1982-10-26T03:00:00.000Z",
                    "cp_profissao": None
                    }
                ]
                }
            
            result.append(data)
    print(result)
    return result

if __name__ == "__main__":
    # Adicione suporte CORS se necessário
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Adicione suporte para redirecionar HTTP para HTTPS
    app.add_middleware(HTTPSRedirectMiddleware)

    # Certifique-se de ajustar o caminho dos certificados conforme necessário
    #uvicorn.run(app, host="127.0.0.1", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem", reload=True)
