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
    ____  __________  ________  ____  _____                                                            
   / __ \/ ____/ __ \/  _/ __ \/ __ \/ ___/                                                            
  / /_/ / __/ / / / // // / / / / / /\__ \                                                             
 / ____/ /___/ /_/ // // /_/ / /_/ /___/ /                                                             
/_/   /_____/_____/___/_____/\____//____/                        
          
          1. Agregar un nuevo pedido
          0. Atras

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postPedido(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")

def getAllDataPedido():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://localhost:5503")
    data = peticion.json()
    return data 

def nuevoCodigoPedido():
    codigodelCliente = list()
    for val in getAllDataPedido():
        codigodelCliente.append(val.get("codigo_pedido"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

def postPedido():
    pedido = {
        "codigo_pedido": nuevoCodigoPedido(),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada: "),
        "fecha_entrega": input("Ingrese la fecha de entrega: "),
        "estado": input("Ingrese el estado del pedido: "),
        "comentario": input("Ingrese un comentario: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5503", headers=headers, data=json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Agregado"
    return res