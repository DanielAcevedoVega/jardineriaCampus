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
   ________    ___________   ___________________                                                       
  / ____/ /   /  _/ ____/ | / /_  __/ ____/ ___/                                                       
 / /   / /    / // __/ /  |/ / / / / __/  \__ \                                                        
/ /___/ /____/ // /___/ /|  / / / / /___ ___/ /                                                        
\____/_____/___/_____/_/ |_/ /_/ /_____//____/                                                         
                                                                                                       

          
          1. Agregar un nuevo cliente
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postClientes(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 0):
                    break


def getAllCliente():
    #json-server storage/cliente.json -b 5507
    peticion = requests.get("http://localhost:5507")
    data = peticion.json()
    return data

def nuevoCodigoCliente():
    codigodelCliente = list()
    for val in getAllCliente():
        codigodelCliente.append(val.get("codigo_cliente"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

def postClientes():

    cliente = dict()
    while True:
        try:
            codigoCliente = nuevoCodigoCliente()
            cliente["codigo_cliente"] = codigoCliente

            if(not cliente.get("nombre_cliente")):
                nombreCliente = input("Ingrese el nombre del cliente: ")
                if(vali.validacionNombre(nombreCliente) is not None):
                    cliente["nombre_cliente"] = nombreCliente
                else:
                    raise Exception("El nombre del cliente no cumple con lo establecido")
                
            if(not cliente.get("nombre_contacto")):
                nombreContacto = input("Ingrese el nombre del contacto: ")
                if(vali.validacionNombre(nombreContacto) is not None):
                    cliente["nombre_contacto"] = nombreContacto
                else:
                    raise Exception("El nombre del contacto no cumple con lo establecido")
                
            if(not cliente.get("apellido_contacto")):
                apellidoContacto = input("Ingrese el apellido de contacto: ")
                if(vali.validacionNombre(apellidoContacto) is not None):
                    cliente["apellido_contacto"] = apellidoContacto
                else:
                    raise Exception("El apellido del contacto no cumple con lo establecido")
                
            if(not cliente.get("telefono")):
                telefono = input("Ingrese el numero de telefono: ")
                if(vali.validacionNumero(telefono) is not None):
                    cliente["telefono"] = telefono
                else:
                    raise Exception("El telefono ingresado no cumple con lo establecido")
                
            if(not cliente.get("fax")):
                fax = input("Ingrese el fax: ")
                if(vali.validacionNumero(fax) is not None):
                    cliente["fax"] = fax
                else:
                    raise Exception("El fax ingresado no cumple con lo establecido")
                
            if(not cliente.get("linea_direccion1")):
                direccion1 = input("Ingrese una linea de direccion: ")
                cliente["linea_direccion1"] = direccion1
                 
            direccion2 = input("Ingrese otra linea de direccion(opcional): ")
            if direccion2:
                cliente["linea_direccion2"] = direccion2

            if(not cliente.get("ciudad")):
                ciudad = input("Ingrese la ciudad: ")
                if(vali.validacionNombre(ciudad) is not None):
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception("El nombre de la ciudad no cumple con lo establecido")

            region = input("Ingrese la region (opcional): ")
            if region:
                if vali.validacionNombre(region) is not None:
                    cliente["region"] = region

            if(not cliente.get("pais")):
                pais = input("Ingrese el pais: ")
                if(vali.validacionNombre(pais) is not None):
                    cliente["pais"] = pais
                else:
                    raise Exception("El nombre del pais no cumple con lo establecido")
                
            if(not cliente.get("codigo_postal")):
                codigoPostal = input("Ingrese el codigo postal: ")
                if(vali.validacionNumerica(codigoPostal) is not None):
                    cliente["codigo_postal"] = codigoPostal
                else:
                    raise Exception("El codigo postal no cumple con lo establecido")
                
            if(not cliente.get("codigo_empleado_rep_ventas")):
                codigoEmpleado = input("Ingrese el codigo de empleado: ")
                if(vali.validacionNumerica(codigoEmpleado) is not None):
                    codigoEmpleado = int(codigoEmpleado)
                    cliente["codigo_empleado_rep_ventas"] = codigoEmpleado
                else:
                    raise Exception("El codigo de empleado no cumple con lo establecido")
                
            if(not cliente.get("limite_credito")):
                limiteCredito = input("Ingrese el limite de credito: ")
                if(vali.validacionNumerica(limiteCredito) is not None):
                    limiteCredito = float(limiteCredito)
                    cliente["limite_credito"] = limiteCredito
                    break
                else:
                    raise Exception("El codigo de empleado no cumple con lo establecido")
                
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5507", headers=headers, data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Agregado"
    return [res]