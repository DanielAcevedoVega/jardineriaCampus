import os
import json
import requests
from tabulate import tabulate


def postOficina(oficina):
    peticion = requests.post("http://localhost:5505", data=json.dumps(oficina))
    res = peticion.json()
    return res