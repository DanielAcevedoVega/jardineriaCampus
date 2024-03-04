import storage.cliente as cli

def getAllClientName():
    clientName = list()
    for val in cli.clientes:
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clientName.append(codigoName)
    return clientName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }
            
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredit.append(val)
    return clienteCredit

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if (val.get('pais') == pais):
            if((region is None or val.get('region') == region)):
                if((ciudad is None or val.get('ciudad') == ciudad)):
                    clientZone.append(val)
    return clientZone
            
