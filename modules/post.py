import json
import requests

def postProducto(producto):
    peticion = requests.post("http://localhost:5501", data=json.dumps(producto))
    res = peticion.json()
    return res

def postPedido(pedido):
    peticion = requests.post("http://localhost:5503", data=json.dumps(pedido))
    res = peticion.json()
    return res

def postPagos(pago):
    peticion = requests.post("http://localhost:5504", data=json.dumps(pago))
    res = peticion.json()
    return res

def postOficina(oficina):
    peticion = requests.post("http://localhost:5505", data=json.dumps(oficina))
    res = peticion.json()
    return res

def postEmpleados(empleado):
    peticion = requests.post("http://localhost:5506", data=json.dumps(empleado))
    res = peticion.json()
    return res

def postClientes(cliente):
    peticion = requests.post("http://localhost:5507", data=json.dumps(cliente))
    res = peticion.json()
    return res