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
          2. Eliminar una oficina
          3. Actualizar una oficina
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if (opcion == 1):
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                elif (opcion == 2):
                    id = int(input("Ingresel el id de la oficina que deseas eliminar: "))
                    print(tabulate(deleteOficina(id), tablefmt="github"))
                elif (opcion == 3):
                    id = int(input("Ingrese el id de la oficina que deseas actualizar: "))
                    print(tabulate(updateOficina(id), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")



def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data 

def getAllCodigoOficina():
    oficinaNombre = list()
    for val in getAllDataOficina():
        oficinaNombre.append(val.get("codigo_oficina"))
    return oficinaNombre

def getOficinaCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{codigo}")
    return peticion.json() if peticion.ok else []

def getCodigo(codigo):
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
                    data = getCodigo(codigo)
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
                
            direccion2 = input("Ingrese otra linea de direccion(opcional): ")
            if direccion2:
                oficina["linea_direccion2"] = direccion2
                
        except Exception as error:
            print(error)
            continue
        break
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5005/oficinas", headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]

def deleteOficina(id):
    data = getOficinaCodigo(id)
    if(len(data)):
        print("Informacion de la oficina encontrado: ")
        print(tabulate([data], headers="keys", tablefmt="github"))
        while True:
            try:
                confirmacion = input("Deseas eliminar este producto?(s/n): ")
                if vali.validacionSiNo(confirmacion):
                    if confirmacion == "s":
                        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
                        if(peticion.ok):
                            return[["messege", "Oficina eliminado correctamente"]]
                        break
                    else:
                        return [
                        ["messege", "La eliminacion de la oficina fue cancelada"],
                        ["status", 200]
                    ]
                else:
                    raise Exception("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
    else:
        return [["Oficina no encontrado", id], 
                ["status", 400 ]
            ]

def updateOficina(id):
    data = getOficinaCodigo(id)
    if (len(data)):
        print("Oficina Encontrada")
        print(tabulate([data], headers="keys", tablefmt="github"))
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Codigo oficina 
                    2. Ciudad
                    3. Pais
                    4. Region
                    5. Codigo postal
                    6. Telefono
                    7. Linea direccion 1
                    8. Linea direccion 2
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 8):
                        if(opcion == 1):
                            while True:
                                try:
                                    codigo = input("Ingrese el codigo de la oficina (Ej: BCN-ES): ")
                                    if(vali.validacionCoidgoOficina(codigo) is not None):
                                        data2 = getCodigo(codigo)
                                        if(data2):
                                            print(tabulate(data2, headers="keys", tablefmt="github"))
                                            raise Exception("El codigo oficina ya existe")
                                        else:
                                            data["codigo_oficina"] = codigo
                                            break
                                    else:
                                        raise Exception("El codigo oficina no cumple con el estandar establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    ciudad = input("Ingrese la ciudad: ")
                                    if(vali.validacionNombre(ciudad) is not None):
                                        data["ciudad"] = ciudad
                                        break
                                    else:
                                        raise Exception("El nombre de la ciudad no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    pais = input("Ingrese el pais: ")
                                    if(vali.validacionNombre(pais) is not None):
                                        data["pais"] = pais
                                        break
                                    else:
                                        raise Exception("El nombre del pais no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    region = input("Ingrese la region: ")
                                    if(vali.validacionNombre(region) is not None):
                                        data["region"] = region
                                        break
                                    else:
                                        raise Exception("El nombre de la region no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 5):
                            while True:
                                try:
                                    codigoPostal = input("Ingrese el codigo postal: ")
                                    if(vali.validacionNumerica(codigoPostal) is not None):
                                        data["codigo_postal"] = codigoPostal
                                        break
                                    else:
                                        raise Exception("El codigo postal no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 6):
                            while True:
                                try:
                                    telefono = input("Ingrese el numero de telefono: ")
                                    if(vali.validacionNumero(telefono) is not None):
                                        data["telefono"] = telefono
                                        break
                                    else:
                                        raise Exception("El telefono ingresado no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 7):
                            while True:
                                try:
                                    direccion1 = input("Ingrese una linea de direccion: ")
                                    data["linea_direccion1"] = direccion1
                                    break
                                except Exception as error:
                                    print(error)
                        if(opcion == 8):
                            while True:
                                try:
                                    direccion2 = input("Ingrese otra linea de direccion: ")
                                    data["linea_direccion2"] = direccion2
                                    break
                                except Exception as error:
                                    print(error)
                        

                        confirmacion = ""            
                        while (confirmacion !=  "s" and confirmacion != "n"):
                            confirmacion = input("Deseas cambiar mas datos?(s/n): ")
                            if vali.validacionSiNo(confirmacion):
                                if confirmacion == "n":
                                    continuarActualizar = False
                                    break
                                else:
                                    confirmacion == "s"
                                    break
                            else:
                                print("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
                

        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        res["Mensaje"] = "Oficina Actualizada"
        return [res]
    
    else:
        return [{
                    "message": "Oficina no encontrada",
                    "id": id
            }]   
