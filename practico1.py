import numpy as np


def ev_facturas(nfacturas=0):
    if nfacturas <= 12:
        print('Cantidad de facturas: {}'.format(nfacturas))
    else:
        print('Cantidad de facturas: muchas')


test = ev_facturas(-5)
