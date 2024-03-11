import storage.pedido as pe
from datetime import datetime 
from tabulate import tabulate

def getAllEstadoPedido():
    estadoPedido = list()
    for val in pe.pedido:
        estadoPedido.append(
            {
                "codigo": val.get("codigo_pedido"),
                "estado": val.get("estado")
            }
        )
    return estadoPedido

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregados = list()
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if (diff.days < 0):
                pedidosEntregados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fecha_entrega")
                })
    return pedidosEntregados

def getAllPedidosEntregadosAlMenosDosDiasAnteDeEspera():
    pedidosEntregados = list()
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if (diff.days >= 2):
                pedidosEntregados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fecha_entrega")
                })
    return pedidosEntregados

def getAllPedidoRechazados2009():
    allRechazados = list()
    for val in pe.pedido:
        if val.get("estado") == "Rechazado" and "2009" in val.get("fecha_pedido"):
            allRechazados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha pedido": val.get("fecha_pedido"),
                    "Estado": val.get("estado")
                })
    return allRechazados

def getAllPedidosEntregadosEnero():
    pedidosEntregadosEnero = list()
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            fecha_entrega = datetime.strptime(date_1, "%d/%m/%Y")
            if fecha_entrega.month == 1:
                pedidosEntregadosEnero.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha de entrega": val.get("fecha_entrega")
                })
    return pedidosEntregadosEnero

def menu():
    while True:
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
        opcion = int(input("\nSeleccione una de las opciones: "))
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
        else:
            print("Opcion no valida")




