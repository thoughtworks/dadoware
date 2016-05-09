#!/usr/bin/env python3

"""Numerar 7776 palavras de 11111 a 66666"""

import sys
import itertools

PATH_PALAVRAS = '7776palavras.txt'

if len(sys.argv) == 2 and sys.argv[1] == '3':
    listar_3_dados = True
else:
    listar_3_dados = False

with open(PATH_PALAVRAS, encoding='utf8') as fp:
    palavras = [p.strip() for p in fp]

dados5 = list(''.join(dados) for dados in itertools.product('123456', repeat=5))

for indice, palavra in zip(dados5, palavras):
    if listar_3_dados:
        indice = '.{}'.format(indice[-3:])
    print(indice, palavra)
