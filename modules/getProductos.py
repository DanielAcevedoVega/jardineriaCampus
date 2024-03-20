import os
from tabulate import tabulate
import modules.validaciones as vali
import requests



def getAllStockPriceGama(gama, stock):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock_gte={stock}&_sort=-precio_venta")
    condiciones = peticion.json()
    for i, val in enumerate(condiciones):
        condiciones[i] = {
            "codigo": val.get("codigo_producto"),
            "venta": val.get("precio_venta"),
            "nombre": val.get("nombre"),
            "gama": val.get("gama"),
            "dimensiones": val.get("dimensiones"),
            "proveedor": val.get("proveedor"),
            "descripcion": f'{val.get("descripcion")[:8]}...' if condiciones[i].get("descripcion") else None,
            "stock": val.get("cantidad_en_stock"),
            "base": val.get("precio_proveedor")
        }
    return condiciones

def menu():
    while True:
        os.system("clear")
        print("""

______                      _             _       ______              _            _            
| ___ \                    | |           | |      | ___ \            | |          | |           
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |_/ / __ ___   __| |_   _  ___| |_ ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __/ '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | |  | | | (_) | (_| | |_| | (__| || (_) \__ \\
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \_|  |_|  \___/ \__,_|\__,_|\___|\__\___/|___/
          | |                                                                                   
          |_|                                                                                   

          
          1. Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de stock sea mayor de 100.   (Ejem: Ornamentales, 100)
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    gama = input("Ingrese la gama que deseas filtrar: ")
                    stock = int(input("Ingrese las unidades de stock: "))
                    print(tabulate(getAllStockPriceGama(gama,stock), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")
