from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado

#print(cliente.getAllClientName())
#print(cliente.getOneClientCodigo(1))
#print(cliente.getAllClientCreditCiudad(5000, "Humanes"))
#print(tabulate(cliente.getAllClientName(), tablefmt="grid"))
#print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain", None, "Madrid"), tablefmt="grid"))
#print(tabulate(cliente.getOneClientContac("(33)5120578961")))
#print(tabulate(cliente.getClientCodePostal("24006")))
#print(tabulate(oficina.getAllCodigoCiudad(), tablefmt="grid"))
#print(tabulate(oficina.getAllCiudadTelefono("España"), tablefmt="rounded_grid"))
#print(tabulate(empleado.getAllNombreApellidoEmailJefe(None), tablefmt="grid"))
#print(tabulate(empleado.getAllJefeNombreApellidoEmailPuesto(None), tablefmt="grid"))
#print(tabulate(empleado.getAllNombreApellidosPuestoNoRepresentantesDeVentas(), tablefmt="rounded_grid"))
