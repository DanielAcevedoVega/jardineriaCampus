import storage.producto as pro

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

