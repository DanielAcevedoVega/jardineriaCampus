import os
import requests
#from modules.post import postPedido as posPe
from datetime import datetime 
from tabulate import tabulate
from modules.crudPedidos import getAllDataPedido as pe
import modules.validaciones as vali


def getAllEstadoPedido():
    estadoPedido = list()
    for val in pe():
        estadoPedido.append(
            {
                "codigo": val.get("codigo_pedido"),
                "estado": val.get("estado")
            }
        )
    return estadoPedido

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregados = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()
    
    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("fechaEntrega") is None:
            continue
        
        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end = datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if (diff.days < 0):
            pedidosEntregados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fechaEntrega"),
                    "Dias de retraso": -(diff.days)
                })
    return pedidosEntregados

def getAllPedidosEntregadosAlMenosDosDiasAnteDeEspera():
    pedidosEntregados = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()
    
    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("fechaEntrega") is None:
            continue
        
        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end = datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if (diff.days >= 2):
            pedidosEntregados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fechaEntrega"),
                    "Dias Anticipados": (diff.days)
                })
    return pedidosEntregados

def getAllPedidoRechazados2009():
    allRechazados = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Rechazado")
    data = peticion.json()
    for val in data:
        if "2009" in val.get("fecha_pedido"):
            allRechazados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha pedido": val.get("fecha_pedido"),
                    "Estado": val.get("estado")
                })
    return allRechazados

def getAllPedidosEntregadosEnero():
    pedidosEntregadosEnero = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()
    
    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("fechaEntrega") is None:
            continue
        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
        fechaEntrega = datetime.strptime(date_1, "%d/%m/%Y")
        if fechaEntrega.month == 1:
            pedidosEntregadosEnero.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha de entrega": val.get("fechaEntrega")
                })
    return pedidosEntregadosEnero

def menu():
    while True:
        os.system("clear")
        print("""

______                      _             _       ______        _ _     _           
| ___ \                    | |           | |      | ___ \      | (_)   | |          
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |_/ /__  __| |_  __| | ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __/ _ \/ _` | |/ _` |/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | | |  __/ (_| | | (_| | (_) \__ \\
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \_|  \___|\__,_|_|\__,_|\___/|___/
          | |                                                                       
          |_|                                                                       
         
          0. Regresar al menu principal
          1. Obtener todos los estados de los pedidos.
          2. Obtener la lista de los pedidos atrasados.
          3. Obtener todos los pedidos que fueron entregados al menos 2 dias antes de lo esperado.
          4. Mostrar todos los pedidos rechazados en el 2009.
          5. Mostrar los pedidos entregados en el mes de enero sin importar el año.

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 5):
                if (opcion == 1):
                    print(tabulate(getAllEstadoPedido(), headers="keys", tablefmt="github"))
                elif (opcion == 2):
                    print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))
                elif (opcion == 3):
                    print(tabulate(getAllPedidosEntregadosAlMenosDosDiasAnteDeEspera(), headers="keys", tablefmt="github"))
                elif (opcion == 4):
                    print(tabulate(getAllPedidoRechazados2009(), headers="keys", tablefmt="github"))
                elif (opcion == 5):
                    print(tabulate(getAllPedidosEntregadosEnero(), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")




