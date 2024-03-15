import os
import requests
from tabulate import tabulate
from modules.crudOficina import getAllDataOficina as ofi


def getAllCodigoCiudad():
    codigoCiudad = list()
    for val in ofi():
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = list()
    for val in ofi():
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficina": val.get("codigo_oficina"),
                "pais": val.get("pais")
            })
    return ciudadTelefono


def menu():
    while True:
        os.system("clear")
        print("""
 ____                       _                  _               __ _      _             
 |  _ \ ___ _ __   ___  _ __| |_ ___  ___    __| | ___    ___  / _(_) ___(_)_ __   __ _ 
 | |_) / _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \  / _ \| |_| |/ __| | '_ \ / _` |
 |  _ <  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | (_) |  _| | (__| | | | | (_| |
 |_| \_\___| .__/ \___/|_|   \__\___||___/  \__,_|\___|  \___/|_| |_|\___|_|_| |_|\__,_|
           |_|                                                                          
           |_|                                                                                          
          
          0. Regresar al menu principal
          1. Obtener una lista de las oficinas que hay en una ciudad (codigo oficina y ciudad).
          2. Obtener los contactos de todas las oficinas del pais especifico. 
          
    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 2):
            pais = input("Ingrese el pais que deseas filtrar: ")
            print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github")) 
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")    