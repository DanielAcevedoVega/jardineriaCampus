import json
import requests

def postProducto(producto):
    peticion = requests.post("http://172.16.100.140:5501", data=json.dumps(producto))
    res = peticion.json()
    return res
