import storage.pago as pay

def getAllCodigoClientePago():
    codigoClientePago = list()
    for val in pay.pago:
        if(val.get("fecha_pago")[0:4] == "2008"):
            codigoClientePago.append(val.get("codigo_cliente"))
        converted = set(str(item) for item in codigoClientePago)
    return converted

def getAllPagos2008Paypal():
    allPagosPaypal = list()
    for val in pay.pago:
        if val.get("forma_pago") == "PayPal" and "2008" in val.get("fecha_pago"):
            allPagosPaypal.append(val)
    allPagosPaypal.sort(key=lambda x: x.get("total"), reverse=True) 
    return allPagosPaypal