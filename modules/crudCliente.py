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
          2. Eliminar un cliente
          3. Actualizar un cliente
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if (opcion == 1):
                    print(tabulate(postClientes(), headers="keys", tablefmt="github"))
                elif (opcion == 2):
                    id = (input("Ingrese el codigo del cliente que deseas eliminar: "))
                    print(tabulate(deleteCliente(id), tablefmt="github"))
                elif (opcion == 3):
                    id = (input("Ingrese el codigo del cliente que deseas actualizar: "))
                    print(tabulate(updateCliente(id), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")


def getAllCliente():
    #json-server storage/cliente.json -b 5507
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

def nuevoCodigoCliente():
    codigoDelCliente = list()
    for val in getAllCliente():
        codigoCliente = val.get("codigo_cliente")
        if codigoCliente is not None:
            codigoDelCliente.append(codigoCliente)
    if codigoDelCliente:
        return max(codigoDelCliente) + 1
    else:
        return 1
    
def getClienteCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente/{codigo}")
    return peticion.json() if peticion.ok else []

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
                    limiteCredito = int(limiteCredito)
                    cliente["limite_credito"] = limiteCredito
                    break
                else:
                    raise Exception("El codigo de empleado no cumple con lo establecido")
                
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5001/cliente", headers=headers, data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Agregado"
    return [res]

    
def deleteCliente(id):
    data = getClienteCodigo(id)
    if(len(data)):
        print("Informacion del cliente encontrado: ")
        print(tabulate([data], headers="keys", tablefmt="github"))
        while True:
            try:
                confirmacion = input("Deseas eliminar este cliente(s/n): ")
                if vali.validacionSiNo(confirmacion):
                    if confirmacion == "s":
                        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
                        if(peticion.ok):
                            return[["messege", "Cliente eliminado correctamente"]]
                        break
                    else:
                        return[
                            ["messege", "La eliminacion del clienete fue cancelada"],
                            ["status", 200]
                        ]
                else:
                    raise Exception("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
    else:
        return [
            ["Cliente no encontrado", id],
            ["status", 400]
        ]

def updateCliente(id):
    data = getClienteCodigo(id)
    if(len(data)):
        print("Cliente Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        data["codigo_cliente"] = data["codigo_cliente"]
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Nombre cliente
                    2. Nombre contacto
                    3. Apellido contacto 
                    4. Telefono
                    5. Fax
                    6. Linea dirrecion 1 
                    7. Linea dirrecion 2
                    8. Ciudad
                    9. Region
                   10. Pais
                   11. Codigo postal
                   12. Codigo empleado
                   13. Limite credito
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 13):
                        if(opcion == 1):
                            while True:
                                try:
                                    nombreCliente = input("Ingrese el nombre del cliente: ")
                                    if(vali.validacionNombre(nombreCliente) is not None):
                                        data["nombre_cliente"] = nombreCliente
                                        break
                                    else:
                                        raise Exception("El nombre del cliente no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    nombreContacto = input("Ingrese el nombre del contacto: ")
                                    if(vali.validacionNombre(nombreContacto) is not None):
                                        data["nombre_contacto"] = nombreContacto
                                        break
                                    else:
                                        raise Exception("El nombre del contacto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    apellidoContacto = input("Ingrese el apellido de contacto: ")
                                    if(vali.validacionNombre(apellidoContacto) is not None):
                                        data["apellido_contacto"] = apellidoContacto
                                        break
                                    else:
                                        raise Exception("El apellido del contacto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
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
                        if(opcion == 5):
                            while True:
                                try:
                                    fax = input("Ingrese el fax: ")
                                    if(vali.validacionNumero(fax) is not None):
                                        data["fax"] = fax
                                        break
                                    else:
                                        raise Exception("El fax ingresado no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 6):
                            while True:
                                try:
                                    direccion1 = input("Ingrese una linea de direccion: ")
                                    if direccion1:
                                        data["linea_direccion1"] = direccion1
                                        break
                                except Exception as error:
                                    print(error)
                        if(opcion == 7):
                            while True:
                                try:
                                    direccion2 = input("Ingrese otra linea de direccion(opcional): ")
                                    if direccion2:
                                        data["linea_direccion2"] = direccion2
                                        break
                                except Exception as error:
                                    print(error)
                        if(opcion == 8):
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
                        if(opcion == 9):
                            while True:
                                try:
                                    region = input("Ingrese la region (opcional): ")
                                    if vali.validacionNombre(region) is not None:
                                        data["region"] = region
                                        break
                                    else:
                                        raise Exception("El nombre de la region no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 10):
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
                        if(opcion == 11):
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
                        if(opcion == 12):
                            while True:
                                try:
                                    codigoEmpleado = input("Ingrese el codigo de empleado: ")
                                    if(vali.validacionNumerica(codigoEmpleado) is not None):
                                        codigoEmpleado = int(codigoEmpleado)
                                        data["codigo_empleado_rep_ventas"] = codigoEmpleado
                                        break
                                    else:
                                        raise Exception("El codigo de empleado no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 13):
                            while True:
                                try:
                                    limiteCredito = input("Ingrese el limite de credito: ")
                                    if(vali.validacionNumerica(limiteCredito) is not None):
                                        limiteCredito = int(limiteCredito)
                                        data["limite_credito"] = limiteCredito
                                        break
                                    else:
                                        raise Exception("El limite de credito no cumple con lo establecido")
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
        peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        res["Mensaje"] = "Cliente Actualizado"
        return [res]
    
    else:
        return[{
            "messege": "Producto no encontrado",
            "id": id
        }]