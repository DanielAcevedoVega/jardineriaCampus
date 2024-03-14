import os
import requests
#from modules.post import postPagos as pay
from tabulate import tabulate

def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504")
    data = peticion.json()
    return data 

def getAllDataEmpleado():
    #json-server storage/empleado.json -b 5506
    peticion = requests.get("http://localhost:5506")
    data = peticion.json()
    return data 

def getAllDataCliente():
    #json-server storage/cliente.json -b 5507
    peticion = requests.get("http://localhost:5507")
    data = peticion.json()
    return data 



def getAllCodigoClientePago():
    codigoClientePago = list()
    for val in getAllDataPagos():
        if(val.get("fecha_pago")[0:4] == "2008"):
            codigoClientePago.append(val.get("codigo_cliente"))
        converted = set(str(item) for item in codigoClientePago)
    return converted

def getAllPagos2008Paypal():
    allPagosPaypal = list()
    for val in getAllDataPagos():
        if val.get("forma_pago") == "PayPal" and "2008" in val.get("fecha_pago"):
            allPagosPaypal.append(val)
    allPagosPaypal.sort(key=lambda x: x.get("total"), reverse=True) 
    return allPagosPaypal

def getAllFormasDePago():
    formaDePago = list()
    for val in getAllDataPagos():
        val.get("forma_pago")
        formaDePago.append(val.get("forma_pago"))
        conjuntoFormaDePago = set(str(item) for item in formaDePago)
    return conjuntoFormaDePago

def getAllNombreClientesRealizaronPagos():
    nombresClientesPagos = set()
    for val in getAllDataCliente():
        codigoCliente = val.get("codigo_cliente")
        nombreCliente = val.get("nombre_cliente")
        codigoEmpleado = val.get("codigo_empleado_rep_ventas")
        for val in getAllDataEmpleado():
            nombreRepresentanteVentas = f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'
            if codigoEmpleado == val.get("codigo_empleado") and val.get("puesto") == "Representante Ventas":
                for val in getAllDataPagos():
                    if codigoCliente == val.get("codigo_cliente"):
                        nombresClientesPagos.add(( 
                            nombreCliente,
                            nombreRepresentanteVentas
                        ))
    return [{"nombre cliente": nombre, "nombre de representante de ventas": representante} for nombre, representante in nombresClientesPagos] 

def getAllNombreClientesNoRealizaronPagos():
    nombresClientesNoPagos = list()
    for val in getAllDataCliente():
        codigoCliente = val.get("codigo_cliente")
        nombreCliente = val.get("nombre_cliente")
        codigoEmpleado = val.get("codigo_empleado_rep_ventas")
        cliente_con_pago = False
        for val in getAllDataEmpleado():
            nombreRepresentanteVentas = f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'
            if codigoEmpleado == val.get("codigo_empleado") and val.get("puesto") == "Representante Ventas":
                for val in getAllDataPagos():
                    if codigoCliente == val.get("codigo_cliente"):
                        cliente_con_pago = True
                        break
                if not cliente_con_pago:
                        nombresClientesNoPagos.append({
                            "nombre cliente": nombreCliente,
                            "nombre de representante de ventas": nombreRepresentanteVentas
                        })
    return nombresClientesNoPagos

def menu():
    while True:
        os.system("clear")
        print("""

______                      _             _       ______                     
| ___ \                    | |           | |      | ___ \                    
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |_/ /_ _  __ _  ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __/ _` |/ _` |/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | | | (_| | (_| | (_) \__ \\
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \_|  \__,_|\__, |\___/|___/
          | |                                                 __/ |          
          |_|                                                |___/           

          0. Regresar al menu principal
          1. Obtener codigo cliente de los que realizaron pagos en el 2008.
          2. Obtener la infromacion de los clientes que pagaron con Paypal y realizadas en el 2008.
          3. Obtener todas las formas de pago.
          4. Muestra el nombre de los clientes que hayan realizado pagos junto con el nombre de sus representantes de ventas.
          5. Obtener el nombre de los clientes que no hayan realizado pagos junto con el nombre de sus representantes de ventas.  
    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllCodigoClientePago()))
            input("Precione una tecla para continuar.........")
        elif (opcion == 2):
            print(tabulate(getAllPagos2008Paypal(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 3):
            print(tabulate(getAllFormasDePago()))
            input("Precione una tecla para continuar.........")
        elif (opcion == 4):
            print(tabulate(getAllNombreClientesRealizaronPagos(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 5):
            print(tabulate(getAllNombreClientesNoRealizaronPagos(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")