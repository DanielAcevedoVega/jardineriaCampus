import storage.pago as pay

def getAllCodigoClientePago():
    codigoClientePago = list()
    for val in pay.pago:
        if(val.get("fecha_pago")[0:4] == "2008"):
            codigoClientePago.append(val.get("codigo_cliente"))
        converted = set(str(item) for item in codigoClientePago)
    return converted

