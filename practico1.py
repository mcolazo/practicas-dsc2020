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


def mezclar(a,b):
    '''
    Dados dos strings `a` y `b`, implementar la función `mezclar` que devuleve
    el string `a` y `b` separados por un espacio, excepto los primeros 
    caracteres de cada string que son intercambiados. Por ejemplo, 
    `mezclar('mix' , 'pod')` devuelve `pix mod`.
    '''
    c = b[0] + a[1:] + ' ' + a[0] + b[1:]
    return c




ev_facturas(-5)
print(ambos('primavera'))
fix('burbubuja','u')
print(mezclar('mix','pod'))


