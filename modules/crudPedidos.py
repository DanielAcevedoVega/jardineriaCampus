import os
import json
import requests
from tabulate import tabulate

def postPedido(pedido):
    peticion = requests.post("http://localhost:5503", data=json.dumps(pedido))
    res = peticion.json()
    return res