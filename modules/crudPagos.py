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
    ____  ___   __________  _____                                                                      
   / __ \/   | / ____/ __ \/ ___/                                                                      
  / /_/ / /| |/ / __/ / / /\__ \                                                                       
 / ____/ ___ / /_/ / /_/ /___/ /                                                                       
/_/   /_/  |_\____/\____//____/                                                                        
                                                      
          
          1. Agregar un pago nuevo
          0. Atras

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postPagos(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")

def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504")
    data = peticion.json()
    return data 

def postPagos():
    pago = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese la id de la transaccion: "),
        "fecha_pago": input("Ingrese la fecha de pago: "),
        "total": int(input("Ingrese el total pagado: "))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5504", headers=headers, data=json.dumps(pago))
    res = peticion.json()
    return res
