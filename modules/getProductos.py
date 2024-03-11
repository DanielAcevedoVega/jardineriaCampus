import storage.producto as pro
from tabulate import tabulate

def getAllProductosGamaAromaticas():
    productoAromatica = list()
    for val in pro.producto:
        if (val.get("gama") == "Aromáticas") and (val.get("cantidad_en_stock") > 100):
            productoAromatica.sort(key=lambda x: x.get("precio_venta"), reverse=True) 
            productoAromatica.append({
                "precio_venta": val.get("precio_venta"),
                "gama": val.get("gama"),
                "nombre": val.get("nombre")
            })
    return productoAromatica

def menu():
    print("""

______                      _             _       ______              _            _            
| ___ \                    | |           | |      | ___ \            | |          | |           
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |_/ / __ ___   __| |_   _  ___| |_ ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __/ '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | |  | | | (_) | (_| | |_| | (__| || (_) \__ \\
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \_|  |_|  \___/ \__,_|\__,_|\___|\__\___/|___/
          | |                                                                                   
          |_|                                                                                   

          1. Obtener todos los prodcutos de la gama Aromaticas

""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        print(tabulate(getAllProductosGamaAromaticas(), headers="keys", tablefmt="github"))
    else:
        print("Opcion no valida")
