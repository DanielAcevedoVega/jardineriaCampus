import storage.oficina as of   
#Devuelve un listado con el codigo de oficina y la ciudad donde hay oficinas

def getAllCodigoCiudad():
    codigoCiudad = list()
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = list()
    for val in of.oficina:
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficina": val.get("codigo_oficina"),
                "pais": val.get("pais")
            })
    return ciudadTelefono
