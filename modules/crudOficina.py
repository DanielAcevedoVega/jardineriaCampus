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
   ____  _____________________   _____   _____                                                         
  / __ \/ ____/  _/ ____/  _/ | / /   | / ___/                                                         
 / / / / /_   / // /    / //  |/ / /| | \__ \                                                          
/ /_/ / __/ _/ // /____/ // /|  / ___ |___/ /                                                          
\____/_/   /___/\____/___/_/ |_/_/  |_/____/                                                           
                                                                                                       
          
          1. Guardar una oficina nueva 
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 0):
                    break



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

def postOficina():
    oficina = {
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese la ciudad: "),
        "pais": input("Ingrese el pais: "),
        "region": input("Ingrese la region: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "telefono": input("Ingrese el numero de telefono: "),
        "linea_direccion1": input("Ingrese una linea de direccion: "),
        "linea_direccion2": input("Ingrese otra linea de direccion(opcional): ")
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5505", headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]