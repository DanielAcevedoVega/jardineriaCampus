#from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getPagos as pago
import modules.getProductos as producto

#import sys 
#def menu():
#    contador = 1
#    print("Menu Principal")
#    for nombre, objeto in sys.modules.items():
#        if nombre.startswith("modules"):
#            modulo = getattr(objeto, "name", None)
#            if(modulo != "modules"):
#                contador += 1
#
#menu()

if(__name__ == "__main__"):
    print("""
          
  _ __ ___   ___ _ __  _   _   _ __  _ __(_)_ __   ___(_)_ __   __ _| |
 | '_ ` _ \ / _ \ '_ \| | | | | '_ \| '__| | '_ \ / __| | '_ \ / _` | |
 | | | | | |  __/ | | | |_| | | |_) | |  | | | | | (__| | |_) | (_| | |
 |_| |_| |_|\___|_| |_|\__,_| | .__/|_|  |_|_| |_|\___|_| .__/ \__,_|_|
                              |_|                       |_|
          
          
            1. Cliente
            2. Oficina 
            3. Empleado
            4. Pedidos
          
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        cliente.menu()
    elif (opcion == 2):
        oficina.menu()
    elif (opcion == 3):
        empleado.menu()
    elif (opcion == 4):
        pedidos.menu()
    else:
        print("opcion no validad")


      
       
