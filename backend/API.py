from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.security import APIKeyHeader
import timber
import uvicorn

app = FastAPI()

# Configurações para Timber
timber.api_key = "MY_KEY"
timber.source_id = "NOME_DO_SEU_APLICATIVO"

# Configurações para API Key
API_KEY = "MY_KEY"
api_key_header = APIKeyHeader(name="X-Api-Key")

# Middleware para verificar a API Key
async def get_api_key(api_key: str = Depends(api_key_header)):
    print(api_key)
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(status_code=403, detail="API Key inválida")

# Rota para criar um novo cliente
@app.post("/auto_grava")
async def auto_grava(request: Request, client_info: dict, api_key: APIKeyHeader = Depends(get_api_key)):
    # Acesse o corpo da requisição através do objeto `request
    # 
    # `
    print(api_key)

    body = await request.json()
    print(body)

    # Faça o que precisar com as informações do cliente
    # Neste exemplo, retorna as informações do corpo da requisição
    return {"status": "success", "client_info": body}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8022,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem",
    )