import os
import requests
from tabulate import tabulate

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

def getAllClientName():
    clientName = list()
    for val in getAllDataCliente():
        codigoName = dict({
            "codigo": val.get('codigo_cliente'),
            "nombre": val.get('nombre_cliente')
        })
        clientName.append(codigoName)
    return clientName

def getOneClientCodigo(codigo):
    for val in getAllDataCliente():
        if(val.get('codigo_cliente') == codigo):
            return[{
                "codigo": val.get('codigo_cliente'),
                "nombre": val.get('nombre_cliente')
            }]
            
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredit = list()
    for val in getAllDataCliente():
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
    for val in getAllDataCliente():
        if (val.get('pais') == pais):
            if((region is None or val.get('region') == region)):
                if((ciudad is None or val.get('ciudad') == ciudad)):
                    clientZone.append({
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
    return clientZone

def getOneClientContac(telefono):
    clientPhone = list()
    for val in getAllDataCliente():
        if(val.get('telefono') == telefono):
             clientPhone.append({
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
    return clientPhone

def getClientCodePostal(postal):
    clientPostal = list()
    for val in getAllDataCliente():
        if(val.get('codigo_postal') == postal):
             clientPostal.append({
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
    return clientPostal

def getAllNombreClientesEspañoles():
    nombreClienteEspañol = list()
    for val in getAllDataCliente():
        if(val.get("pais") == 'Spain'):
            nombreClienteEspañol.append(
                {
                    "nombre": val.get("nombre_cliente"),
                    "pais": val.get("pais")
                }
            )
    return nombreClienteEspañol

def getAllClientesMadridRepresentantesVentas():
    clientesMadrid = list()
    for val in getAllDataCliente():
        if(val.get("ciudad") == "Madrid"):
            if(val.get("codigo_empleado_rep_ventas") == 11 or val.get("codigo_empleado_rep_ventas") == 30):
                clientesMadrid.append({
                "nombre": val.get("nombre_cliente"),
                "ciudad": val.get("ciudad"),
                "Codigo del asesor": val.get("codigo_empleado_rep_ventas")
                })
    return clientesMadrid

def getAllNombreApellidosDeClientesRepresentanteVentas():
    nombreClienteRepresentanteVentas = list()
    for val in getAllDataCliente():
        codigoEmpleado = val.get("codigo_empleado_rep_ventas")
        nombreCliente = val.get("nombre_cliente")
        for val in getAllDataEmpleado():
            if codigoEmpleado == val.get("codigo_empleado") and val.get("puesto") == "Representante Ventas":
                nombreClienteRepresentanteVentas.append({
                    "nombre cliente": nombreCliente,
                    "nombre del representante de ventas": f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'
                })
    return nombreClienteRepresentanteVentas




def menu():
    while True:
        os.system("clear")
        print("""
   ____                       _                  _        _                  _ _            _            
  |  _ \ ___ _ __   ___  _ __| |_ ___  ___    __| | ___  | | ___  ___    ___| (_) ___ _ __ | |_ ___  ___ 
  | |_) / _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \ | |/ _ \/ __|  / __| | |/ _ \ '_ \| __/ _ \/ __|
  |  _ <  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | | (_) \__ \ | (__| | |  __/ | | | ||  __/\__ 
  |_| \_\___| .__/ \___/|_|   \__\___||___/  \__,_|\___| |_|\___/|___/  \___|_|_|\___|_| |_|\__\___||___/
            |_|                                                                                          
          
          0. Regresar al menu principal  
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el código (codigo y nombre)
          3. Obtener toda la informacion de los cliente segun su limite de creditos y ciudad que pertenece (ejem:3000.0, San Francisco).
          4. Obtener toda la informacion de los clientes segun su pais, region y ciudad (ejem: Spain, Madrid, Fuenlabrada).
          5. Obtener toda la informacion del cliente por el numero de contacto (telefono).
          6. Obtener toda la informacion del cliente por el codigo postal.
          7. Obtener todos los nombres de los clientes Españoles.
          8. Obtener un listado de los clientes de Madird y su representante de ventas tenga el codigo de empleado (11 o 30).
          9. Obtener un listado con los nombres del cliente y su representante de ventas.  
          
    """)            
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 2):
                codigo = int(input("Ingrese el codigo del cliente: "))
                print(tabulate(getOneClientCodigo(codigo), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar.........")
        elif (opcion == 3):
                limite = float(input("Ingrese el limite de credito de los clientes que desee visualizar: "))
                ciudad = input("Ingrese el nombre de la ciudad que desea filtrar a los clientes: ")
                print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar.........")
        elif (opcion == 4):
                pais = input("Ingrese el pais filtrar a los clientes: ")
                region = input("Ingrese la region que desea filtrar a los clientes(opcional): ") or None
                ciudad = input("Ingrese la ciudad que desea filtrar a los clientes(opcional): ") or None
                print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar.........")
        elif (opcion == 5):
                telefono = input("Ingrese el nuemro de contacto del cliente que deseas filtrar: ")
                print(tabulate(getOneClientContac(telefono), headers="keys", tablefmt="github"))   
                input("Precione una tecla para continuar.........")
        elif (opcion == 6):
                codigo_postal = input("Ingrese el codigo postal del cliente que deseas filtrar: ")
                print(tabulate(getClientCodePostal(codigo_postal), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar.........")
        elif (opcion == 7):
            print(tabulate(getAllNombreClientesEspañoles(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 8):
            print(tabulate(getAllClientesMadridRepresentantesVentas(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 9):
            print(tabulate(getAllNombreApellidosDeClientesRepresentanteVentas(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("opcion no validad")
