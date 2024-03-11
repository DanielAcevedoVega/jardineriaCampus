import storage.producto as pro
from tabulate import tabulate

def getAllProductosOrnamentales():
    productoOrnamentales = list()
    for val in pro.producto:
        if (val.get("gama") == "Ornamentales") and (val.get("cantidad_en_stock") > 100):
            productoOrnamentales.sort(key=lambda x: x.get("precio_venta"), reverse=True) 
            productoOrnamentales.append({
                "precio_venta": val.get("precio_venta"),
                "gama": val.get("gama"),
                "nombre": val.get("nombre")
            })
    return productoOrnamentales

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
            print(tabulate(getAllProductosOrnamentales(), headers="keys", tablefmt="github"))
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")
