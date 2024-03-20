import os
import json
import requests
from tabulate import tabulate
import modules.crudOficina as oFi
import modules.validaciones as vali

def menu():
    while True:
        os.system("clear")  
        print("""


    ___       __          _       _      __                         __      __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \\
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/ 
    ________  _______  __    _________    ____  ____  _____                                            
   / ____/  |/  / __ \/ /   / ____/   |  / __ \/ __ \/ ___/                                            
  / __/ / /|_/ / /_/ / /   / __/ / /| | / / / / / / /\__ \                                             
 / /___/ /  / / ____/ /___/ /___/ ___ |/ /_/ / /_/ /___/ /                                             
/_____/_/  /_/_/   /_____/_____/_/  |_/_____/\____//____/                                              
                                                                            
          
          1. Agregar un nuevo empleado
          2. Eliminar un empleado
          3. Actualizar un empleado
          0. Atras

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if (opcion == 1):
                    print(tabulate(postEmpleados(), headers="keys", tablefmt="github"))
                elif (opcion == 2):
                    id = int(input("Ingrese el codigo del empleado que deseas eliminar: "))
                    print(tabulate(deleteEmpleado(id), tablefmt="github"))
                elif (opcion == 3):
                    id = int(input("Ingrese el codigo del empleado que deseas actualizar: "))
                    print(tabulate(updateEmpleado(id), headers="keys", tablefmt="github"))
                elif (opcion == 0):
                    break
            input("Precione una tecla para continuar.........")

def getAllDataEmpleado():
    #json-server storage/empleado.json -b 5506
    peticion = requests.get("http://localhost:5506/empleados")
    data = peticion.json()
    return data 

def nuevoCodigoEmpleado():
    codigoDelEmpleado = list()
    for val in getAllDataEmpleado():
        codigoEmpleado = val.get("codigo_empleado")
        if codigoEmpleado is not None:
            codigoDelEmpleado.append(codigoEmpleado)
    if codigoDelEmpleado:
        return max(codigoDelEmpleado) + 1
    else:
        return 1
    
def getCodigoEmpleado(codigo):
    peticion = requests.get(f"http://localhost:5506/empleados/{codigo}")
    return peticion.json() if peticion.ok else []

def postEmpleados():
    empleado = dict()
    while True:
        try:
            codigoEmpleado = nuevoCodigoEmpleado()
            empleado["codigo_empleado"] = codigoEmpleado

            if(not empleado.get("nombre")):
                nombreEmpleado = input("Ingrese el nombre del empleado: ")
                if(vali.validacionNombre(nombreEmpleado) is not None):
                    empleado["nombre"] = nombreEmpleado
                else:
                    raise Exception("El nombre del cliente no cumple con lo establecido")
                
            if(not empleado.get("apellido1")):
                apellido1 = input("Ingrese el apellido del empleado: ")
                if(vali.validacionNombre(apellido1) is not None):
                    empleado["apellido1"] = apellido1
                else:
                    raise Exception("El apellido del empleado no cumple con lo establecido") 

            apellido2 = input("Ingrese el otro apellido del empleado(opcional): ")
            if(vali.validacionNombre(apellido1) is not None):
                empleado["apellido2"] = apellido2   
            
            if(not empleado.get("extension")):
                extension = input("Ingrese la extension: ")
                if(vali.validacionNumerica(extension) is not None):
                    empleado["extension"] = extension
                else:
                    raise Exception("La extension ingresada no cumple con lo establecido")
                
            if(not empleado.get("email")):
                email = input("Ingrese el email del empleado: ")
                empleado["email"] = email

            if(not empleado.get("codigo_oficina")):
                opcion = input("Seleccione la oficina:\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(oFi.getAllCodigoOficina())]))
                if vali.validacionOpciones(opcion):
                    gama = oFi.getAllCodigoOficina()[int(opcion)]
                    empleado["codigo_oficina"] = gama
                else:
                    raise Exception("La opcion de la oficina no cumple con lo establecido")
                
            if(not empleado.get("codigo_jefe")):
                codigoJefe = input("Ingrese el codigo jefe: ")
                if(vali.validacionNumerica(codigoJefe) is not None):
                    codigoJefe = int(codigoJefe)
                    empleado["codigo_jefe"] = codigoJefe
                else:
                    raise Exception("El codigo jefe no cumple con lo establecido")            

            if(not empleado.get("puesto")):
                puesto = input("Ingrese el puesto del empleado: ")
                if(vali.validacionNombre(puesto) is not None):
                    empleado["puesto"] = puesto
                    break
                else:
                    raise Exception("El puesto del empleado no cumple con lo establecido")

        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5506/empleados", headers=headers, data=json.dumps(empleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Agregado"
    return [res]

def deleteEmpleado(id):
    data = getCodigoEmpleado(id)
    if(len(data)):
        print("Informacion del empleado encontrado: ")
        print(tabulate([data], headers="keys", tablefmt="github"))
        while True:
            try:
                confirmacion = input("Deseas eliminar este empleado?(s/n): ")
                if vali.validacionSiNo(confirmacion):
                    if confirmacion == "s":
                        peticion = requests.delete(f"http://localhost:5506/empleados/{id}")
                        if(peticion.status_code == 204):
                            return[["messege", "Empleado eliminado correctamente"]]
                        break
                    else:
                        return[
                            ["messege", "La eliminacion del empleado fue cancelada"],
                            ["status", 200]
                        ]
                else:
                    raise Exception("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
    else:
        return [
            ["Empleado no encontrado", id],
            ["status", 400]
        ]
    
def updateEmpleado(id):
    data = getCodigoEmpleado(id)
    if(len(data)):
        empleado = dict()
        empleado["codigo_empleado"] = data["codigo_empleado"]
        while True:
            try:
                if(not empleado.get("nombre")):
                    nombreEmpleado = input("Ingrese el nombre del empleado: ")
                    if(vali.validacionNombre(nombreEmpleado) is not None):
                        empleado["nombre"] = nombreEmpleado
                    else:
                        raise Exception("El nombre del cliente no cumple con lo establecido")
                    
                if(not empleado.get("apellido1")):
                    apellido1 = input("Ingrese el apellido del empleado: ")
                    if(vali.validacionNombre(apellido1) is not None):
                        empleado["apellido1"] = apellido1
                    else:
                        raise Exception("El apellido del empleado no cumple con lo establecido") 

                apellido2 = input("Ingrese el otro apellido del empleado(opcional): ")
                if(vali.validacionNombre(apellido1) is not None):
                    empleado["apellido2"] = apellido2   
                
                if(not empleado.get("extension")):
                    extension = input("Ingrese la extension: ")
                    if(vali.validacionNumerica(extension) is not None):
                        empleado["extension"] = extension
                    else:
                        raise Exception("La extension ingresada no cumple con lo establecido")
                    
                if(not empleado.get("email")):
                    email = input("Ingrese el email del empleado: ")
                    empleado["email"] = email

                if(not empleado.get("codigo_oficina")):
                    opcion = input("Seleccione la oficina:\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(oFi.getAllCodigoOficina())]))
                    if vali.validacionOpciones(opcion):
                        gama = oFi.getAllCodigoOficina()[int(opcion)]
                        empleado["codigo_oficina"] = gama
                    else:
                        raise Exception("La opcion de la oficina no cumple con lo establecido")
                    
                if(not empleado.get("codigo_jefe")):
                    codigoJefe = input("Ingrese el codigo jefe: ")
                    if(vali.validacionNumerica(codigoJefe) is not None):
                        codigoJefe = int(codigoJefe)
                        empleado["codigo_jefe"] = codigoJefe
                    else:
                        raise Exception("El codigo jefe no cumple con lo establecido")            

                if(not empleado.get("puesto")):
                    puesto = input("Ingrese el puesto del empleado: ")
                    if(vali.validacionNombre(puesto) is not None):
                        empleado["puesto"] = puesto
                        break
                    else:
                        raise Exception("El puesto del empleado no cumple con lo establecido")

            except Exception as error:
                print(error)
        
        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://localhost:5506/empleados/{id}", headers=headers, data=json.dumps(empleado))
        res = peticion.json()
        res["Mensaje"] = "Empleado Actualizado"
        return [res]
    else:
        return[{
            "messege": "Empleado no encontrado",
            "id": id
        }]