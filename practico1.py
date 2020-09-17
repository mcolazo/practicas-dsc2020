import numpy as np


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
        res = s[0] + s[1] + s[-2] + s[-1]
    return res


ev_facturas(-5)
print(ambos('primavera'))



