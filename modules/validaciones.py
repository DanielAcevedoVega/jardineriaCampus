import re

def validacionOpciones(opcion):
    val = re.match(r'[0-9]+$', opcion)
    return val