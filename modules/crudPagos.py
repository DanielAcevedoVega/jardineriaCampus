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
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postPagos(), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")

def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504")
    data = peticion.json()
    return data 

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
                    pago["forma_pagoado"] = formaPago
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
    peticion = requests.post("http://localhost:5504", headers=headers, data=json.dumps(pago))
    res = peticion.json()
    return [res]
