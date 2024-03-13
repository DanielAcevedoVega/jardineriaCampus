import requests

def getAllGama():
    peticion = requests.get("http://localhost:5502")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = list()
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre