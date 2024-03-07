import storage.pedido as pe
from datetime import datetime 

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
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
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
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregados

def getAllPedidoRechazados2009():
    allRechazados = list()
    for val in pe.pedido:
        if val.get("estado") == "Rechazado" and "2009" in val.get("fecha_pedido"):
            allRechazados.append(val)
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
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregadosEnero





