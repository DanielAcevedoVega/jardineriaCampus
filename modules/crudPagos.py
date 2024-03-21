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
    ____  ___   __________  _____                                                                      
   / __ \/   | / ____/ __ \/ ___/                                                                      
  / /_/ / /| |/ / __/ / / /\__ \                                                                       
 / ____/ ___ / /_/ / /_/ /___/ /                                                                       
/_/   /_/  |_\____/\____//____/                                                                        
                                                      
          
          1. Agregar un pago nuevo
          2. Eliminar un pago 
          3. Actualizar un pago 
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if (opcion == 1):
                    print(tabulate(postPagos(), headers="keys", tablefmt="github"))
                elif (opcion == 2):
                    id = (input("Ingrese el codigo del pago que deseas eliminar: "))
                    print(tabulate(deletePago(id), tablefmt="github"))
                elif (opcion == 3):
                    id = (input("Ingrese el codigo del pago que deseas actualizar: "))
                    print(tabulate(updatePago(id), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")

def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data 

def getPagoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo}")
    return peticion.json() if peticion.ok else []

def postPagos():
    pago = dict()
    while True:
        try:
            if(not pago.get("codigo_cliente")):
                codigocliente = input("Ingrese el codigo del cliente: ")
                if(vali.validacionNumerica(codigocliente) is not None):
                    codigocliente = int(codigocliente)
                    pago["codigo_cliente"] = codigocliente
                else:
                    raise Exception("El codigo del cliente no cumple con lo establecido")  

            if(not pago.get("forma_pago")):
                formaPago = input("Ingrese la forma de pago: ")
                if(vali.validacionNombre(formaPago) is not None):
                    pago["forma_pago"] = formaPago
                else:
                    raise Exception("La forma de pago no cumple con lo establecido")  
                
            if(not pago.get("id_transaccion")):
                idTransaccion = input("Ingrese la id de la transaccion: ")
                if(vali.validaiconTransccion(idTransaccion) is not None):
                    pago["id_transaccion"] = idTransaccion
                else:
                    raise Exception("La id de la transaccion no cumple con lo establecido")
                
            if(not pago.get("fecha_pago")):
                fechaPago = input("Ingrese la fecha de pago: ")
                if(vali.validacionFecha(fechaPago) is not None):
                    pago["fecha_pago"] = fechaPago
                else:
                    raise Exception("La fehca no cumple con lo establecido") 

            if(not pago.get("total")):
                total = input("Ingrese el total del pago: ")
                if(vali.validacionNumerica(total) is not None):
                    total = int(total)
                    pago["total"] = total
                    break
                else:
                    raise Exception("El pago no cumple con lo establecido")   
                
        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5006/pagos", headers=headers, data=json.dumps(pago))
    res = peticion.json()
    return [res]

def deletePago(id):
    data = getPagoCodigo(id)
    if(len(data)):
        print("Informacion del pago encontrado: ")
        print(tabulate([data], headers="keys", tablefmt="github"))
        while True:
            try:
                confirmacion = input("Deseas eliminar este pago?(s/n): ")
                if vali.validacionSiNo(confirmacion):
                    if confirmacion == "s":
                        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
                        if(peticion.ok):
                            return[["messege", "Pago eliminado correctamente"]]
                        break
                    else:
                        return[
                            ["messege", "La eliminacion del pago fue cancelada"],
                            ["status", 200]
                        ]
                else:
                    raise Exception("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
    else:
        return [
            ["Pago no encontrado", id],
            ["status", 400]
        ]
    
def updatePago(id):
    data = getPagoCodigo(id)
    if(len(data)):
        print("Pago Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        data["codigo_cliente"] = data["codigo_cliente"]
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Forma de pago 
                    2. Id transaccion
                    3. Fecha pago
                    4. Total
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 4):
                        if(opcion == 1):
                            while True:
                                try:
                                    formaPago = input("Ingrese la forma de pago: ")
                                    if(vali.validacionNombre(formaPago) is not None):
                                        data["forma_pago"] = formaPago
                                        break
                                    else:
                                        raise Exception("La forma de pago no cumple con lo establecido")  
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    idTransaccion = input("Ingrese la id de la transaccion: ")
                                    if(vali.validaiconTransccion(idTransaccion) is not None):
                                        data["id_transaccion"] = idTransaccion
                                        break
                                    else:
                                        raise Exception("La id de la transaccion no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    fechaPago = input("Ingrese la fecha de pago: ")
                                    if(vali.validacionFecha(fechaPago) is not None):
                                        data["fecha_pago"] = fechaPago
                                        break
                                    else:
                                        raise Exception("La fehca no cumple con lo establecido") 
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    total = input("Ingrese el total del pago: ")
                                    if(vali.validacionNumerica(total) is not None):
                                        total = int(total)
                                        data["total"] = total
                                        break
                                    else:
                                        raise Exception("El pago no cumple con lo establecido")   
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
        peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        return [res]
    else:
        return[{
            "messege": "Pago no encontrado",
            "id": id
        }]


