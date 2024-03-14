import os
import json
import requests
import modules.getGama as gG
from tabulate import tabulate

def postProducto():
    
    producto = {
                "codigo_producto": input("Ingrese el codigo del producto: "),
                "nombre": input("Ingrese el nombre del producto: "),
                "gama": gG.getAllNombre()[int(input("Seleccione la gama\n: "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
                "dimensiones": input("Ingrese la dimension del producto: "),
                "proveedor": input("Ingrese el proveedor del producto: "),
                "descripcion": input("Ingrese la descipcion del producto: "),
                "cantidad_en_stock": int(input("Ingrese la cantidad de stock: ")),
                "precio_venta": int(input("Ingrese el precio de venta: ")),
                "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
            }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5501", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")  
        print("""


    ___       __          _       _      __                         __      __                    __        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/      
    ____  ____  ____  ____  __  __________________  _____                                                   
   / __ \/ __ \/ __ \/ __ \/ / / / ____/_  __/ __ \/ ___/                                                   
  / /_/ / /_/ / / / / / / / / / / /     / / / / / /\__ \                                                    
 / ____/ _, _/ /_/ / /_/ / /_/ / /___  / / / /_/ /___/ /                                                    
/_/   /_/ |_|\____/_____/\____/\____/ /_/  \____//____/                                                     
                                                                                                            

          
          1. Guardar un producto nuevo
          0. Regresar al menu principl

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postProducto(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")

def postPedido(pedido):
    peticion = requests.post("http://localhost:5503", data=json.dumps(pedido))
    res = peticion.json()
    return res

def postPagos(pago):
    peticion = requests.post("http://localhost:5504", data=json.dumps(pago))
    res = peticion.json()
    return res

def postOficina(oficina):
    peticion = requests.post("http://localhost:5505", data=json.dumps(oficina))
    res = peticion.json()
    return res

def postEmpleados(empleado):
    peticion = requests.post("http://localhost:5506", data=json.dumps(empleado))
    res = peticion.json()
    return res

def postClientes(cliente):
    peticion = requests.post("http://localhost:5507", data=json.dumps(cliente))
    res = peticion.json()
    return res