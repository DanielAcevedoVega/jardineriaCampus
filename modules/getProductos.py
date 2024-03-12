import storage.producto as pro
from tabulate import tabulate

def getAllStockPriceGama(gama, stock):
    condiciones = list()
    for val in pro.producto:
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
          1. Obtener todos los prodcutos de la gama Ornamentales

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            gama = input("Ingrese la gama que deseas filtrar (Ejem: Ornamentales, 100): ")
            stock = int(input("Ingrese las unidades de stock: "))
            print(tabulate(getAllStockPriceGama(gama,stock), headers="keys", tablefmt="github"))
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")
