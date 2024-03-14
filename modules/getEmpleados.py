import os
import requests
from tabulate import tabulate

def getAllDataEmpleado():
    #json-server storage/empleado.json -b 5506
    peticion = requests.get("http://localhost:5506")
    data = peticion.json()
    return data 

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = list()
    for val in getAllDataEmpleado():
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

def getAllJefeNombreApellidoEmailPuesto(codigo):
    jefeNombreApellidoEmailPuesto = list()
    for val in getAllDataEmpleado():
        if((val.get("codigo_empleado") == codigo)):
            jefeNombreApellidoEmailPuesto.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "puesto": val.get("puesto")
                }
            )
    return jefeNombreApellidoEmailPuesto

def getAllNombreApellidosPuestoNoRepresentantesDeVentas():
    nombreApellidosPuetos = list()
    for val in getAllDataEmpleado():
        if(val.get("puesto") != 'Representante Ventas'):
            nombreApellidosPuetos.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "puesto": val.get("puesto")
                }
            )
    return nombreApellidosPuetos

def menu():
    while True:
        os.system("clear")
        print("""
______                      _             _        _____                _                _           
| ___ \                    | |           | |      |  ___|              | |              | |          
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |__ _ __ ___  _ __ | | ___  __ _  __| | ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __| '_ ` _ \| '_ \| |/ _ \/ _` |/ _` |/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | |__| | | | | | |_) | |  __/ (_| | (_| | (_) \__ 
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \____/_| |_| |_| .__/|_|\___|\__,_|\__,_|\___/|___/
          | |                                                    | |                                 
          |_|                                                    |_|                                 

          0. Regresar al menu principal
          1. Obtener el nombre, apellidos y email de los empleados con el mismo codigo del jefe.
          2. Obtener la informacion de su jefe.
          3. Obtener el listado con el nombre, apellidos y puesto de aquellos empleados que no sean representantes de ventas.
    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
                cogido = int(input("Ingrese el codigo del jefe de los empleados: "))
                print(tabulate(getAllNombreApellidoEmailJefe(cogido), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar.........")
        elif (opcion == 2):
                cogido = int(input("Ingrese el codigo de su jefe para obtener su infromacion: "))
                print(tabulate(getAllJefeNombreApellidoEmailPuesto(cogido), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar.........")
        elif (opcion == 3):
            print(tabulate(getAllNombreApellidosPuestoNoRepresentantesDeVentas(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")
    
