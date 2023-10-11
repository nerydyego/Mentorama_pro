import pytest
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000/calcular/"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Conexão com sucesso"

    def test_POSTmethod(self):
        resp = post(self.url, json= {"valor1" : 10, "valor2": 6, "operacao": '*'})
        message = loads(resp.text)
        resposta_esperada = {
            "resultado":60
        }
        assert message == resposta_esperada
