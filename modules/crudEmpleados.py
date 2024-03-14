import os
import json
import requests
from tabulate import tabulate

def postEmpleados(empleado):
    peticion = requests.post("http://localhost:5506", data=json.dumps(empleado))
    res = peticion.json()
    return res