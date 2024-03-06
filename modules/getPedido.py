import storage.pedido as pe

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