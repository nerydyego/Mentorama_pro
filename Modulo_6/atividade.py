
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OperacaoRequest(BaseModel):
    valor1: int
    valor2: int
    operacao: str

@app.get("/calcular/")
async def calcular():
    return {"messagem": "Conexão com sucesso"}

@app.post("/calcular/")
async def calcular_post(operacao_req: OperacaoRequest):
    valor1 = operacao_req.valor1
    valor2 = operacao_req.valor2
    operacao = operacao_req.operacao

    if operacao == "+":
        resultado = valor1 + valor2
    elif operacao == "-":
        resultado = valor1 - valor2
    elif operacao == "*":
        resultado = valor1 * valor2
    elif operacao == "/":
        if valor2 == 0:
            return {"error": "Divisão por zero não é permitida."}
        resultado = valor1 / valor2
    else:
        return {"error": "Operação não suportada. Use +, -, *, /"}

    return {"resultado": resultado}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
