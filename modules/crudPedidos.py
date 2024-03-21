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
    ____  __________  ________  ____  _____                                                            
   / __ \/ ____/ __ \/  _/ __ \/ __ \/ ___/                                                            
  / /_/ / __/ / / / // // / / / / / /\__ \                                                             
 / ____/ /___/ /_/ // // /_/ / /_/ /___/ /                                                             
/_/   /_____/_____/___/_____/\____//____/                        
          
          1. Agregar un nuevo pedido
          2. Eliminar nuevo pedido
          3. Actualizar un pedido
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if (opcion == 1):
                    print(tabulate(postPedido(), headers="keys", tablefmt="github"))
                elif (opcion == 2):
                    id = (input("Ingrese el codigo del pedido que deseas eliminar: "))
                    print(tabulate(deletePedido(id), tablefmt="github"))
                elif (opcion == 3):
                    id = (input("Ingrese el codigo del pedido que deseas actualizar: "))
                    print(tabulate(updatePedido(id), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")


def getAllDataPedido():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = peticion.json()
    return data 

def nuevoCodigoPedido():
    codigoDelPedido = list()
    for val in getAllDataPedido():
        codigoPedido = val.get("codigo_pedido")
        if codigoPedido is not None:
            codigoDelPedido.append(codigoPedido)
    if codigoDelPedido:
        return max(codigoDelPedido) + 1
    else:
        return 1
    
def getCodigoPedido(codigo):
    peticion = requests.get(f"http://154.38.171.54:5007/pedidos/{codigo}")
    return peticion.json() if peticion.ok else []

def postPedido():
    pedido = dict()
    while True:
        try:
            codigoPedido = nuevoCodigoPedido()
            pedido["codigo_pedido"] = codigoPedido

            if(not pedido.get("fecha_pedido")):
                fechaPeido = input("Ingrese la fecha del pedido: ")
                if(vali.validacionFecha(fechaPeido) is not None):
                    pedido["fecha_pedido"] = fechaPeido
                else:
                    raise Exception("La fecha no cumple con lo establecido")
                
            if(not pedido.get("fecha_esperada")):
                fechaEspera = input("Ingrese la fecha de espera: ")
                if(vali.validacionFecha(fechaEspera) is not None):
                    pedido["fecha_esperada"] = fechaEspera
                else:
                    raise Exception("La fecha no cumple con lo establecido")
                
            fechaEntregada = input("Ingrese la fehca entregada: ")
            if(vali.validacionFecha(fechaEntregada) is not None):
                pedido["fecha_entrega"] = fechaEntregada
            else:
                raise Exception("La fecha no cumple con lo establecido")
            
            if(not pedido.get("estado")):
                estado = input("Ingrese el estado del pedido: ")
                if(vali.validacionNombre(estado) is not None):
                    pedido["estado"] = estado
                else:
                    raise Exception("El estado del pedido no cumple con lo establecido")            

            comentario = input("Ingrese un comentario: ")
            if(not pedido.get("comentario")):
                pedido["comentario"] = comentario

            if(not pedido.get("codigo_cliente")):
                codigocliente = input("Ingrese el codigo del cliente: ")
                if(vali.validacionNumerica(codigocliente) is not None):
                    codigocliente = int(codigocliente)
                    pedido["codigo_cliente"] = codigocliente
                    break
                else:
                    raise Exception("El codigo del cliente no cumple con lo establecido")     

        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5007/pedidos", headers=headers, data=json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Agregado"
    return [res]

def deletePedido(id):
    data = getCodigoPedido(id)
    if(len(data)):
        print("Informacion del pedido encontrado: ")
        print(tabulate([data], headers="keys", tablefmt="github"))
        while True:
            try:
                confirmacion = input("Deseas eliminar este pedido?(s/n): ")
                if vali.validacionSiNo(confirmacion):
                    if confirmacion == "s":
                        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
                        if(peticion.ok):
                            return[["messege", "Pedido eliminado correctamente"]]
                        break
                    else:
                        return[
                            ["messege", "La eliminacion del pedido fue cancelada"],
                            ["status", 200]
                        ]
                else:
                    raise Exception("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
    else:
        return [
            ["Pedido no encontrado", id],
            ["status", 400]
        ]
    
def updatePedido(id):
    data = getCodigoPedido(id)
    if(len(data)):
        print("Empleado Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        data["codigo_pedido"] = data["codigo_pedido"]
        continuarActualizar = True     
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Fecha pedido 
                    2. Fecha espera
                    3. Fecha entrega
                    4. Estado
                    5. Comentario
                    6. Codigo del cliente
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 6):
                        if(opcion == 1):
                            while True:
                                try:
                                    fechaPedido = input("Ingrese la fecha del pedido: ")
                                    if(vali.validacionFecha(fechaPedido) is not None):
                                        data["fecha_pedido"] = fechaPedido
                                        break
                                    else:
                                        raise Exception("La fecha no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    fechaEspera = input("Ingrese la fecha de espera: ")
                                    if(vali.validacionFecha(fechaEspera) is not None):
                                        data["fecha_esperada"] = fechaEspera
                                        break
                                    else:
                                        raise Exception("La fecha no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    fechaEntregada = input("Ingrese la fehca entregada: ")
                                    if(vali.validacionFecha(fechaEntregada) is not None):
                                        data["fecha_entrega"] = fechaEntregada
                                        break
                                    else:
                                        raise Exception("La fecha no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    estado = input("Ingrese el estado del pedido: ")
                                    if(vali.validacionNombre(estado) is not None):
                                        data["estado"] = estado
                                        break
                                    else:
                                        raise Exception("El estado del pedido no cumple con lo establecido")            
                                except Exception as error:
                                    print(error)
                        if(opcion == 5):
                            while True:
                                try:
                                    comentario = input("Ingrese un comentario: ")
                                    data["comentario"] = comentario
                                    break
                                except Exception as error:
                                    print(error)
                        if(opcion == 6):
                            while True:
                                try:
                                    codigocliente = input("Ingrese el codigo del cliente: ")
                                    if(vali.validacionNumerica(codigocliente) is not None):
                                        codigocliente = int(codigocliente)
                                        data["codigo_cliente"] = codigocliente
                                        break
                                    else:
                                        raise Exception("El codigo del cliente no cumple con lo establecido")     
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
        peticion = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        res["Mensaje"] = "Pedido Actualizado"
        return [res]
    else:
        return[{
            "messege": "Pedido no encontrado",
            "id": id
        }]