import os
import json
import requests
from tabulate import tabulate


def postPagos(pago):
    peticion = requests.post("http://localhost:5504", data=json.dumps(pago))
    res = peticion.json()
    return res
