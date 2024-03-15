import os
import json
import requests
from tabulate import tabulate

def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = requests.get("http://localhost:5505")
    data = peticion.json()
    return data 

def getAllCodigoOficina():
    oficinaNombre = list()
    for val in getAllDataOficina():
        oficinaNombre.append(val.get("codigo_oficina"))
    return oficinaNombre

def postOficina(oficina):
    peticion = requests.post("http://localhost:5505", data=json.dumps(oficina))
    res = peticion.json()
    return res