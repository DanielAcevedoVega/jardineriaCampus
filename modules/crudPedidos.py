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
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postPedido(), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")


def getAllDataPedido():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://localhost:5503/pedidos")
    data = peticion.json()
    return data 

def nuevoCodigoPedido():
    codigodelCliente = list()
    for val in getAllDataPedido():
        codigodelCliente.append(val.get("codigo_pedido"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

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
                    raise Exception("La fehca no cumple con lo establecido")
                
            if(not pedido.get("fecha_esperada")):
                fechaEntrega = input("Ingrese la fecha de espera: ")
                if(vali.validacionFecha(fechaEntrega) is not None):
                    pedido["fecha_esperada"] = fechaEntrega
                else:
                    raise Exception("La fehca no cumple con lo establecido")
                
            fechaEntregada = input("Ingrese la fehca entregada: ")
            if(not pedido.get("fecha_entrega")):
                pedido["fecha_entrega"] = fechaEntregada

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
    peticion = requests.post("http://localhost:5503/pedidos", headers=headers, data=json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Agregado"
    return [res]