import re

def validacionOpciones(opcion):
    val = re.match(r'[0-9]+$', opcion)
    return val

def validacionCodigo(codigo):
    val = re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)
    return val

def validacionNombre(nombre):
    val = re.match(r'^([A-Z][a-z]*\s*)+$', nombre)
    return val

def validacionDimension(dimensiones):
    val = re.match(r'^\s*[0-9]+\s*-\s*[0-9]+\s*$', dimensiones)
    return val

def validacionNumerica(numero):
    val = re.match(r'^\s*\d+(\.\d+)?\s*$', numero)
    return val