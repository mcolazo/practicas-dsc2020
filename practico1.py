import numpy as np
from collections import Counter



def ev_facturas(nfacturas=0):
    '''
    Dado una número de facturas, implementar una función que devuelva el 
    string `Cantidad de facturas: <nro>` donde `nro` es el número que se 
    pasa como argumento.
    '''
    if nfacturas <= 12:
        print('Cantidad de facturas: {}'.format(nfacturas))
    else:
        print('Cantidad de facturas: muchas')


def ambos(s=''):
    '''
    Dado un string `s`, implementar la función `ambos` que devuelve un string
    construido con los dos primeros y dos últimos caracteres.
    '''
    if len(s)< 2:
        res = ''
    else:
        res = s[:2] + s[-2:]
    return res


def fix(s,car):
    '''
    Dado un string `s`, implementar una función `fix` que reemplaza todas las
    ocurrencias del primer caracter por `*` a excepción de la primera 
    ocurrencia.
    '''
    cuenta = Counter(s)
    nrep = cuenta[car]
    s = s[::-1]
    s1 = s.replace(car,'*',nrep - 1)
    s1 = s1[::-1]
    return s1


ev_facturas(-5)
print(ambos('primavera'))
fix('burbubuja','u')



