import storage.pago as pay
from tabulate import tabulate

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

def getAllFormasDePago():
    formaDePago = list()
    for val in pay.pago:
        val.get("forma_pago")
        formaDePago.append(val.get("forma_pago"))
        conjuntoFormaDePago = set(str(item) for item in formaDePago)
    return conjuntoFormaDePago

def menu():
    print("""

______                      _             _       ______                     
| ___ \                    | |           | |      | ___ \                    
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |_/ /_ _  __ _  ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __/ _` |/ _` |/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | | | (_| | (_| | (_) \__ \\
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \_|  \__,_|\__, |\___/|___/
          | |                                                 __/ |          
          |_|                                                |___/           

          1. Obtener codigo cliente de los que realizaron pagos en el 2008.
          2. Obtener la infromacion de los clientes que pagaron con Paypal y realizadas en el 2008.
          3. Obtener todas las formas de pago.
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        print(tabulate(getAllCodigoClientePago()))
    elif (opcion == 2):
        print(tabulate(getAllPagos2008Paypal(), headers="keys", tablefmt="github"))
    elif (opcion == 3):
        print(tabulate(getAllFormasDePago()))
    else:
        print("Opcion no valida")