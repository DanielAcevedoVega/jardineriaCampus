import storage.pago as pay

def getAllCodigoClientePago():
    codigoClientePago = list()
    for val in pay.pago:
        if(val.get("fecha_pago") == "2008"):
            codigoClientePago.append(
                {
                    "codigo": val.get("codigo_cliente")
                }
            )
    return codigoClientePago