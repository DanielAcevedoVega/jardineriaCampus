from tabulate import tabulate
import modules.getClients as cliente

#print(cliente.getAllClientName())
#print(cliente.getOneClientCodigo(1))
#print(cliente.getAllClientCreditCiudad(5000, "Humanes"))
#print(tabulate(cliente.getAllClientName(), tablefmt="grid"))
print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain", None, "Madrid"), tablefmt="grid"))
