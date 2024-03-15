import os
import json
import requests
from tabulate import tabulate
import modules.validaciones as vali

def menu():
    while True:
        os.system("clear")  
        print("""


    ___       __          _       _      __                         __      __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \\
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/ 
   ________    ___________   ___________________                                                       
  / ____/ /   /  _/ ____/ | / /_  __/ ____/ ___/                                                       
 / /   / /    / // __/ /  |/ / / / / __/  \__ \                                                        
/ /___/ /____/ // /___/ /|  / / / / /___ ___/ /                                                        
\____/_____/___/_____/_/ |_/ /_/ /_____//____/                                                         
                                                                                                       

          
          1. Agregar un nuevo cliente
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postClientes(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 0):
                    break


def getAllCliente():
    #json-server storage/cliente.json -b 5507
    peticion = requests.get("http://localhost:5507")
    data = peticion.json()
    return data

def nuevoCodigoCliente():
    codigodelCliente = list()
    for val in getAllCliente():
        codigodelCliente.append(val.get("codigo_cliente"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

def postClientes():
    cliente = {
        "codigo_cliente": nuevoCodigoCliente(),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido de contacto: "),
        "telefono": input("Ingrese el numero de telefono: "),
        "fax": input("Ingrese el fax: "),
        "linea_direccion1": input("Ingrese una linea de direccion: "),
        "linea_direccion2": input("Ingrese otra linea de direccion(opcional): "),
        "ciudad": input("Ingrese la ciudad: "),
        "region": input("Ingrese la region(opcional): "),
        "pais": input("Ingrese el pais: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo de empelado: ")),
        "limite_credito": float(input("Ingrese el limite de credito: "))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5507", headers=headers, data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Agregado"
    return [res]