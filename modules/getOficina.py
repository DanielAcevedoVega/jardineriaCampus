import storage.oficina as of   
from tabulate import tabulate
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


def menu():
    print("""
 ____                       _                  _               __ _      _             
 |  _ \ ___ _ __   ___  _ __| |_ ___  ___    __| | ___    ___  / _(_) ___(_)_ __   __ _ 
 | |_) / _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \  / _ \| |_| |/ __| | '_ \ / _` |
 |  _ <  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | (_) |  _| | (__| | | | | (_| |
 |_| \_\___| .__/ \___/|_|   \__\___||___/  \__,_|\___|  \___/|_| |_|\___|_|_| |_|\__,_|
           |_|                                                                          
           |_|                                                                                          
            
          1. Obtener una lista de las oficinas que hay en una ciudad (codigo oficina y ciudad)
          2. Obtener los contactos de todas las oficinas del pais especifico 
          
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
    if (opcion == 2):
        pais = input("Ingrese el pais que deseas filtrar: ")
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))     