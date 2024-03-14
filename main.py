import os
#from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getPagos as pago
import modules.getProductos as Reproducto
import modules.post as CRUDproducto

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

def menuProducto():
    while True:
        os.system("clear")
        print("""  
                  
    ____  _                            _     __               __                                     __   
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__ 
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \\
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/ 
    ____  _________  ____/ /_  _______/ /_____  _____                                                     
   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                                     
  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                                      
 / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                                                       
/_/                                                                                                       

                  1. Reportes de los productos
                  2. Guardar, Actualizar y Eliminar productos
                  0. Atras
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            Reproducto.menu()
        elif (opcion == 2):
            CRUDproducto.menu()
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")

if(__name__ == "__main__"):
    
    while True:
        os.system("clear")
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
            5. Productos
            6. Pagos
            0. Salir
          
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
        elif (opcion == 5):
            menuProducto()
        elif (opcion == 6):
            pago.menu()
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")


      
       
