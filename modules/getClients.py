import storage.cliente as cli
from tabulate import tabulate

def getAllClientName():
    clientName = list()
    for val in cli.clientes:
        codigoName = dict({
            "codigo": val.get('codigo_cliente'),
            "nombre": val.get('nombre_cliente')
        })
        clientName.append(codigoName)
    return clientName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return[{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }]
            
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredit.append({
                "codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Telefono": val.get('telefono'),
                "Fax": val.get('fax'),
                "Direcciones": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": val.get('limite_credito')
            })
    return clienteCredit

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if (val.get('pais') == pais):
            if((region is None or val.get('region') == region)):
                if((ciudad is None or val.get('ciudad') == ciudad)):
                    clientZone.append(val)
    return clientZone

def getOneClientContac(telefono):
    clientPhone = list()
    for val in cli.clientes:
        if(val.get('telefono') == telefono):
             clientPhone.append(val)
    return clientPhone

def getClientCodePostal(postal):
    clientPostal = list()
    for val in cli.clientes:
        if(val.get('codigo_postal') == postal):
             clientPostal.append(val)
    return clientPostal

def getAllNombreClientesEspañoles():
    nombreClienteEspañol = list()
    for val in cli.clientes:
        if(val.get("pais") == 'Spain'):
            nombreClienteEspañol.append(
                {
                    "nombre": val.get("nombre_cliente"),
                    "pais": val.get("pais")
                }
            )
    return nombreClienteEspañol

#def getAllClientesMadridRepresentantesVentas():
    clientesMadrid = list()
    for val in cli.clientes:
        if(val.get("ciudad") == "Madrid") and (val.get("codigo_empleado_rep_ventas") == 11 and val.get("codigo_empleado_rep_ventas") == 30):
            clientesMadrid.append({
                "nombre": val.get("nombre_cliente"),
                "ciudad": val.get("ciudad"),
                "codigo_empleado_rep_ventas": val.get("codigo_empleado_rep_ventas")
            })
    return clientesMadrid

def menu():
    print("""
   ____                       _                  _        _                  _ _            _            
  |  _ \ ___ _ __   ___  _ __| |_ ___  ___    __| | ___  | | ___  ___    ___| (_) ___ _ __ | |_ ___  ___ 
  | |_) / _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \ | |/ _ \/ __|  / __| | |/ _ \ '_ \| __/ _ \/ __|
  |  _ <  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | | (_) \__ \ | (__| | |  __/ | | | ||  __/\__ 
  |_| \_\___| .__/ \___/|_|   \__\___||___/  \__,_|\___| |_|\___/|___/  \___|_|_|\___|_| |_|\__\___||___/
            |_|                                                                                          
            
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el código (codigo y nombre)
          3. Obtener toda la informacion de los cliente segun su limite de creditos y ciudad que pertenece (ejem:3000.0, San Francisco)
          
""")            
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
    elif (opcion == 2):
        codigo = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getOneClientCodigo(codigo), headers="keys", tablefmt="github"))
    elif (opcion == 3):
        limite = float(input("Ingrese el limite de credito de los clientes que desee visualizar: "))
        ciudad = input("Ingrese el nombre de la ciudad que desea filtrar a los clientes: ")
        print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers="keys", tablefmt="github"))
    else:
        print("opcion no validad")
