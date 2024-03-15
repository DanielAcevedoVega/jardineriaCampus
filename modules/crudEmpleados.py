import os
import json
import requests
from tabulate import tabulate
import modules.crudOficina as oFi

def menu():
    while True:
        os.system("clear")  
        print("""


    ___       __          _       _      __                         __      __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \\
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/ 
    ________  _______  __    _________    ____  ____  _____                                            
   / ____/  |/  / __ \/ /   / ____/   |  / __ \/ __ \/ ___/                                            
  / __/ / /|_/ / /_/ / /   / __/ / /| | / / / / / / /\__ \                                             
 / /___/ /  / / ____/ /___/ /___/ ___ |/ /_/ / /_/ /___/ /                                             
/_____/_/  /_/_/   /_____/_____/_/  |_/_____/\____//____/                                              
                                                                            
          
          1. Agregar un nuevo empleado
          0. Atras

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postEmpleados(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")

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
    return [res]