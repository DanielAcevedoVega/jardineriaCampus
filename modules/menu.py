import os
import modules.getClients as REcliente
import modules.getOficina as REoficina
import modules.getEmpleados as REempleado
import modules.getPedido as REpedidos
import modules.getPagos as REpago
import modules.getProductos as REproducto
import modules.crudProductos as CRUDproducto
import modules.crudCliente as CRUDcliente


def menuCliente():
    while True:
        os.system("clear")
        print("""  
                  


    ____  _                            _     __               __                                     __        
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__      
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \\        
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/      
  / ____/ (_)__  ____  / /____                                                                                 
 / /   / / / _ \/ __ \/ __/ _ \                                                                                
/ /___/ / /  __/ / / / /_/  __/                                                                                
\____/_/_/\___/_/ /_/\__/\___/                                                                                 
                                                                                                               


                  1. Reportes de los clientes
                  2. Agregar, Actualizar y Eliminar clientes
                  0. Regresar al menu principal
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            REcliente.menu()
        elif (opcion == 2):
            CRUDcliente.menu()
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")

def menuOficina():
    while True:
        os.system("clear")
        print("""  
                  
    ____  _                            _     __               __                                     __        
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__      
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \\      
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/      
  / __ \/ __(_)____(_)___  ____ _                                                                              
 / / / / /_/ / ___/ / __ \/ __ `/                                                                              
/ /_/ / __/ / /__/ / / / / /_/ /                                                                               
\____/_/ /_/\___/_/_/ /_/\__,_/                                                                                
                                                                                                               
                                                                            

                  1. Reportes de las oficinas
                  2. Agregar, Actualizar y Eliminar oficinas
                  0. Regresar al menu principal
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            REoficina.menu()
        elif (opcion == 2):
            print("")
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")

def menuEmpleado():
    while True:
        os.system("clear")
        print("""  
                  
    ____  _                            _     __               __                                     __        
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__      
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \\     
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/      
   / ____/___ ___  ____  / /__  ____ _____/ /___  _____                                                        
  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/                                                        
 / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )                                                         
/_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/                                                          
               /_/                                                                                             

                                                                            
                  1. Reportes de empleados
                  2. Agregar, Actualizar y Eliminar oficinas
                  0. Regresar al menu principal
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            REempleado.menu()
        elif (opcion == 2):
            print("")
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")

def menuPedido():
    while True:
        os.system("clear")
        print("""  
                  
    ____  _                            _     __               __                                     __        
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__      
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \\     
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/      
   / __ \___  ____/ (_)___/ /___  _____                                                                        
  / /_/ / _ \/ __  / / __  / __ \/ ___/                                                                        
 / ____/  __/ /_/ / / /_/ / /_/ (__  )                                                                         
/_/    \___/\__,_/_/\__,_/\____/____/                                                                          
                                                                                                               

                                                                            
                  1. Reportes de pedidos
                  2. Guardar, Actualizar y Eliminar oficinas
                  0. Regresar al menu principal
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            REpedidos.menu()
        elif (opcion == 2):
            print("")
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")


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
                  0. Regresar al menu principal
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            REproducto.menu()
        elif (opcion == 2):
            CRUDproducto.menu()
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")

def menuPago():
    while True:
        os.system("clear")
        print("""  
                  
    ____  _                            _     __               __                                     __        
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__      
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \\     
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/      
   / __ \____ _____ _____  _____                                                                               
  / /_/ / __ `/ __ `/ __ \/ ___/                                                                               
 / ____/ /_/ / /_/ / /_/ (__  )                                                                                
/_/    \__,_/\__, /\____/____/                                                                                 
            /____/                                                                                             
                                               

                  1. Reportes de los pagos
                  2. Guardar, Actualizar y Eliminar productos
                  0. Regresar al menu principal
                  
                  """)
        opcion = int(input("\nSeleccione una de las opciones: ")) 
        if (opcion == 1):
            REpago.menu()
        elif (opcion == 2):
            print("")
        elif (opcion == 0):
            break
        else:
            print("opcion no valida")