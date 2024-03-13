from tabulate import tabulate
from modules.post import postProducto as psPro
import modules.getGama as gG
#import json
import requests

def getAllData():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://localhost:5503")
    data = peticion.json()
    return data 

def getAllStockPriceGama(gama, stock):
    condiciones = list()
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {
            "codigo": val.get("codigo_producto"),
            "venta": val.get("precio_venta"),
            "nombre": val.get("nombre_"),
            "gama": val.get("gama"),
            "dimensiones": val.get("dimensiones"),
            "proveedor": val.get("proveedor"),
            "descripcion": f'{val.get("descripcion")[:20]}...' if condiciones[i].get("descripcion") else None,
            "stock": val.get("cantidad_en_stock"),
            "base": val.get("precio_proveedor")
        }
    return condiciones

def menu():
    while True:
        print("""

______                      _             _       ______              _            _            
| ___ \                    | |           | |      | ___ \            | |          | |           
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |_/ / __ ___   __| |_   _  ___| |_ ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __/ '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | |  | | | (_) | (_| | |_| | (__| || (_) \__ \\
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \_|  |_|  \___/ \__,_|\__,_|\___|\__\___/|___/
          | |                                                                                   
          |_|                                                                                   

          0. Regresar al menu principal
          1. Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de stock sea mayor de 100.   (Ejem: Ornamentales, 100)
          2. Guardar  

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            gama = input("Ingrese la gama que deseas filtrar: ")
            stock = int(input("Ingrese las unidades de stock: "))
            print(tabulate(getAllStockPriceGama(gama,stock), headers="keys", tablefmt="github"))
        elif (opcion == 2):
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
           psPro(producto)
           print("Producto Guardado")
           
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")
