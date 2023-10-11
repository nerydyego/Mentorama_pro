# Atividade Mentorama - Modulo 6

* tarefa:

* crie um projeto em python:
 > crie uma api utlizando framework de sua preferência.
 > A api deverá receber uma quesição no método POST no seguinte formato:
`{ 
    "valor1": int, 
    "valor2": int,
    "operacao": string 
    }`
 > A api deverá responder com a operação matemática (operacao) realizada entre os as variaveis (valor1 e valor2) informados crie os teste e a documentação para API.

* Foi Criado arquivo da API (Interface de Programa de Aplicação), no arquivo ___atividade.py__. 
> Foram atulizado as Bibliotecas
 <details>
    ```    from fastapi import FastAPI
           from pydantic import BaseModel 
    ``` 
 </details> 

* Foi Criado arquivo da API de para teste a API, no arquivo ___testeAtividade.ipynb__.

* Teste da API com Biblioteca _pytest_, no arquivo __pyTesteAtividade__.