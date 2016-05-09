#!/usr/bin/env python3

"""Numerar 7776 palavras de 11111 a 66666"""

PATH_PALAVRAS = '7776palavras.txt'

import itertools

with open(PATH_PALAVRAS, encoding='utf8') as fp:
    palavras = [p.strip() for p in fp]

dados5 = list(''.join(dados) for dados in itertools.product('123456', repeat=5))

for indice, palavra in zip(dados5, palavras):
    print(indice, palavra)
