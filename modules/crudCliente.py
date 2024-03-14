import os
import json
import requests
from tabulate import tabulate


def postClientes(cliente):
    peticion = requests.post("http://localhost:5507", data=json.dumps(cliente))
    res = peticion.json()
    return res