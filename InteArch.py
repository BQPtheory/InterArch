#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Copyright (c) 2021-2030, Pequeño código en python3 para Pruebas de DDoS.
"""

import sys 
from inspect import getargspec 


def search(linea, criterio):
    if criterio in linea:
        print "Encontrado '%(criterio)s' en '%(linea)s'" % {'criterio': criterio, 'linea': linea.strip()}
    return linea

def replace(linea, original, reemplazo):
    if original in linea:
        print "reemplazando %s por %s en %s" % (original, reemplazo, linea)
        return linea.replace(original, reemplazo)
    return linea

def copy(linea):
    return linea

operaciones = {'copiar': copy,
               'reemplazar': replace,
               'buscar': search,
              }

def operar_en_archivo(nombre_de_archivo, operacion="copiar", *args):
    archivo = open(nombre_de_archivo)
    salida  = open("copy_"+nombre_de_archivo, 'w') 
    for linea in archivo:
        if operacion in operaciones:
            salida.write(operaciones[operacion](linea, *args))
        else:
            salida.write(linea)
def usage(script, operation, params):
    print "python %s archivo %s %s" % (script, operation, " ".join([e for e in params if e != "linea"]))

if __name__ == "__main__":
    print "bienvenido al operador de archivos %s" %sys.argv[0]
    if len(sys.argv) > 2:
        print "elegiste ejecutar la operación %s" % sys.argv[2] 
        operar_en_archivo(sys.argv[1], *sys.argv[2:]) 
    else:
        print "Uso:\n\t%s archivo [parámetros]" % sys.argv[0]
        print "por ejemplo:"
        for key,value in operaciones.items():
            usage(sys.argv[0], key, getargspec(value)[0])
