import os
import json
import requests
from tabulate import tabulate
import modules.validaciones as vali

def menu():
    while True:
        os.system("clear")  
        print("""


    ___       __          _       _      __                         __      __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \\
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/ 
   ____  _____________________   _____   _____                                                         
  / __ \/ ____/  _/ ____/  _/ | / /   | / ___/                                                         
 / / / / /_   / // /    / //  |/ / /| | \__ \                                                          
/ /_/ / __/ _/ // /____/ // /|  / ___ |___/ /                                                          
\____/_/   /___/\____/___/_/ |_/_/  |_/____/                                                           
                                                                                                       
          
          1. Guardar una oficina nueva 
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")



def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = requests.get("http://localhost:5505")
    data = peticion.json()
    return data 

def getAllCodigoOficina():
    oficinaNombre = list()
    for val in getAllDataOficina():
        oficinaNombre.append(val.get("codigo_oficina"))
    return oficinaNombre


def getOficinaCodigo(codigo):
    for val in getAllDataOficina():
        if(val.get("codigo_oficina") == codigo):
             return [val]

def postOficina():

    oficina = dict()
    while True:
        try:
            if(not oficina.get("codigo_oficina")):
                codigo = input("Ingrese el codigo de la oficina (Ej: BCN-ES): ")
                if(vali.validacionCoidgoOficina(codigo) is not None):
                    data = getOficinaCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo oficina ya existe")
                    else:
                        oficina["codigo_oficina"] = codigo
                else:
                    raise Exception("El codigo oficina no cumple con el estandar establecido")
                
            if(not oficina.get("ciudad")):
                ciudad = input("Ingrese la ciudad: ")
                if(vali.validacionNombre(ciudad) is not None):
                    oficina["ciudad"] = ciudad
                else:
                    raise Exception("El nombre de la ciudad no cumple con lo establecido")
                
            if(not oficina.get("pais")):
                pais = input("Ingrese el pais: ")
                if(vali.validacionNombre(pais) is not None):
                    oficina["pais"] = pais
                else:
                    raise Exception("El nombre del pais no cumple con lo establecido")
                
            if(not oficina.get("region")):
                region = input("Ingrese la region: ")
                if(vali.validacionNombre(region) is not None):
                    oficina["region"] = region
                else:
                    raise Exception("El nombre de la region no cumple con lo establecido")
                
            if(not oficina.get("codigo_postal")):
                codigoPostal = input("Ingrese el codigo postal: ")
                if(vali.validacionNumerica(codigoPostal) is not None):
                    oficina["codigo_postal"] = codigoPostal
                else:
                    raise Exception("El codigo postal no cumple con lo establecido")
                
            if(not oficina.get("telefono")):
                telefono = input("Ingrese el numero de telefono: ")
                if(vali.validacionNumero(telefono) is not None):
                    oficina["telefono"] = telefono
                else:
                    raise Exception("El telefono ingresado no cumple con lo establecido")
                
            if(not oficina.get("linea_direccion1")):
                direccion1 = input("Ingrese una linea de direccion: ")
                oficina["linea_direccion1"] = direccion1
                 
            if not oficina.get("linea_direccion2"):  
                direccion2 = input("Ingrese otra linea de direccion(opcional): ")
                if direccion2:
                    oficina["linea_direccion2"] = direccion2
                else:
                    break

        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5505", headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]