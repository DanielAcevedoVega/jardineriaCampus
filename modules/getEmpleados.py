import storage.empleado as em

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = list()
    for val in em.empleados:
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
    for val in em.empleados:
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
    for val in em.empleados:
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
    print("""
______                      _             _        _____                _                _           
| ___ \                    | |           | |      |  ___|              | |              | |          
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | |__ _ __ ___  _ __ | | ___  __ _  __| | ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ |  __| '_ ` _ \| '_ \| |/ _ \/ _` |/ _` |/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | |__| | | | | | |_) | |  __/ (_| | (_| | (_) \__ 
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| \____/_| |_| |_| .__/|_|\___|\__,_|\__,_|\___/|___/
          | |                                                    | |                                 
          |_|                                                    |_|                                 

          
          1. Obtener el nombre, apellidos y email del jefe por su codigo.
          2. Obtener la informacion por el codigo de empleado.
          3. Obtener el listado con el nombre, apellidos y puesto de aquellos empleados que no sean representantes de ventas.
""")
