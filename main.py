import os
#from tabulate import tabulate
import modules.menu as me
import modules.validaciones as vali
import json



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
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 6):
                if (opcion == 1):  
                    me.menuCliente()
                elif (opcion == 2):
                    me.menuOficina()
                elif (opcion == 3):
                    me.menuEmpleado()
                elif (opcion == 4):
                    me.menuPedido()
                elif (opcion == 5):
                    me.menuProducto()
                elif (opcion == 6):
                    me.menuPago()
                elif (opcion == 0):
                    break




      
       
