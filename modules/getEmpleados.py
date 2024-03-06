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

