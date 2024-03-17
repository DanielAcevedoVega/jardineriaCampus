import re

def validacionOpciones(opcion):
    val = re.match(r'[0-9]+$', opcion)
    return val

def validacionCodigo(codigo):
    val = re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)
    return val

def validacionCoidgoOficina(codigo):
    val = re.M(r'^[A-Z]{3}-[A-Z]{3}$', codigo)
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

def validacionNumero(numero):
    val = re.match(r'^\s*(\(\d+\))?\s*\d+(?:[\s-]?\d+)*\s*$', numero)
    return val

def validacionFecha(fecha):
    val = re.match(r'^\d{4}-\d{2}-\d{2}$', fecha)
    return val