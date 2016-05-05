#!/usr/bin/env python3

import random

rnd = random.SystemRandom()

D1 = '⚀'
dado_cars = dict(zip('123456',
                     (chr(i) for i in range(ord(D1), ord(D1)+6))))

dadoware = {}
with open('../dadoware.txt', encoding='utf8') as fp:
    dadoware.update(lin.strip().split() for lin in fp)

for i in range(6):
    dados = ''.join(str(rnd.randint(1, 6)) for i in range(5))
    for d in dados:
        print(dado_cars[d], end=' ')
    print(end='\t')
    print(dados[0], dados[1], sep=',', end='\t')
    print(dados[2:], dadoware[dados], sep='\t')
