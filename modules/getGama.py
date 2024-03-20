import requests

def getAllGama():
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = list()
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre