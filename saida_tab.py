#!/usr/bin/env python3
import itertools

with open('dadoware.txt', encoding='ascii') as fp:
    dadoware = fp.read().split('\n')

def colsplit(l, cols):
    rows = len(l) // cols
    if len(l) % cols:
        rows += 1
    m = []
    for i in range(rows):
        m.append(l[i::rows])
    return m


for lin, lin_str in zip(colsplit(dadoware, 36*6), itertools.product('123456', repeat=2)):
    for col, cel in enumerate(lin):
        chave = '{}{}{}'.format((col % 6) + 1, *lin_str)
        print(chave, cel, sep='\t', end='\t')
    print()
