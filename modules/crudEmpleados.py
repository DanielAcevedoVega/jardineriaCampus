import os
import json
import requests
from tabulate import tabulate
import modules.crudOficina as oFi

def getAllDataEmpleado():
    #json-server storage/empleado.json -b 5506
    peticion = requests.get("http://localhost:5506")
    data = peticion.json()
    return data 

def nuevoCodigoEmpleado():
    codigodelCliente = list()
    for val in getAllDataEmpleado():
        codigodelCliente.append(val.get("codigo_empleado"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

def postEmpleados():
    empleado = {
        "codigo_empleado": nuevoCodigoEmpleado(),
        "nombre": input("Ingrese el nombre del empleado: "),
        "apellido1": input("Ingrese el apellido del empleado: "),
        "apellido2": input("Ingrese el segundo apellido del empleado(opcional): "),
        "extension": input("Ingrese la extension: "),
        "email": input("Ingrese el email del empleado: "),
        "codigo_oficina": oFi.getAllCodigoOficina()[int(input("Seleccione la oficina:\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(oFi.getAllCodigoOficina())])))],
        "codigo_jefe": int(input("Ingrese el codigo del jefe: ")),
        "puesto": input("Ingrese el nombre del puesto: ")
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5506", headers=headers, data=json.dumps(empleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Agregado"
    return res