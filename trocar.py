#!/usr/bin/env python3

"""
Tira uma palavra de dadoware.txt, adicionando outra no lugar.

Se a palavra a ser adicionada não é especificada, coloca uma sorteada
do arquivo fontes/excluidas_por_sorteio.txt.
"""

import unicodedata
import sys
import random

PATH_PALAVRAS = '7776palavras.txt'
QT_PALAVRAS = 6 ** 5
PATH_DADOWARE = 'dadoware.txt'
PATH_CANDIDATAS = 'fontes/canditatas.txt'

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

def normalizar(txt):
    return shave_marks(txt).lower()

def duplicatas():
    with open(PATH_PALAVRAS, encoding='utf8') as fp:
        palavras = [p.strip() for p in fp]
    assert len(palavras) == QT_PALAVRAS
    normals = [normalizar(p) for p in sorted(palavras)]
    for p in palavras:
        if normals.count(normalizar(p)) > 1:
            print(p)


def trocar(retirar, adicionar=None):
    with open(PATH_PALAVRAS, encoding='utf8') as fp:
        palavras = [p.strip() for p in fp]
        palavras_set = {normalizar(p) for p in palavras}
    try:
        with open(PATH_CANDIDATAS, encoding='utf8') as fp:
            candidatas = [p.strip() for p in fp]
    except FileNotFoundError:
        candidatas = []
    try:
        palavras.remove(retirar)
    except ValueError:
        print('*** Erro: palavra {!r} não encontrada.'.format(retirar))
        sys.exit(-1)
    if adicionar is None:
        if len(candidatas) == 0:
            print('*** Erro: não há mais palavras para adicionar.'.format(retirar))
            sys.exit(-2)
        adicionar = random.choice(candidatas)
        ex_candidata = adicionar
    else:
        if adicionar in canditatas:
            ex_candidata = adicionar
        else:
            ex_canditata = None
    if normalizar(adicionar) in palavras_set:
        ad_norm = normalizar(adicionar)
        print('*** Erro: palavra {!r} já existe.'.format(ad_norm))
        sys.exit(-3)
    palavras.append(adicionar)
    assert len(palavras) == QT_PALAVRAS
    palavras.sort(key=normalizar)
    print('- {} | + {}'.format(retirar, adicionar))
    with open(PATH_PALAVRAS, 'wt', encoding='utf8') as fp:
        fp.write('\n'.join(palavras) + '\n')
    if ex_candidata is not None:
        candidatas.remove(ex_candidata)
        candidatas.sort(key=normalizar)
        with open(PATH_CANDIDATAS, 'wt', encoding='utf8') as fp:
            fp.write('\n'.join(canditatas) + '\n')





if __name__ == '__main__':

    #duplicatas()
    #raise SystemExit

    import argparse

    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('retirar', metavar='palavra-sai',
        help='a palavra a ser retirada')
    parser.add_argument('-a', dest='adicionar', metavar='palavra-entra',
        help='a palavra a ser adicionada')

    args = parser.parse_args()
    #print(args._get_kwargs())
    trocar(**dict(args._get_kwargs()))
