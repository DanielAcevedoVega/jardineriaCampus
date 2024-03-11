import storage.producto as pro

def getAllProductosGamaAromaticas():
    productoAromatica = list()
    for val in pro.producto:
        if (val.get("gama") == "Aromáticas") and (val.get("cantidad_en_stock") > 100):
            productoAromatica.sort(key=lambda x: x.get("precio_venta"), reverse=True) 
            productoAromatica.append({
                "Precio de venta": val.get("precio_venta"),
                "Gama": val.get("gama"),
                "Nombre": val.get("nombre")
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
