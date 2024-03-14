import os
import json
import requests
from tabulate import tabulate

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
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postClientes(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")



def postClientes():
    cliente = {
        "codigo_cliente": int(input("Ingrese el codigo: ")),
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
    res["Mensaje"] = "Producto Guardado"
    return [res]