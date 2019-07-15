"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla: Edson Kropniczki + Cristina Oliveira
    Descrição: algoritmo recursivo para calcular combinações sem usar fatorial
"""


def comb(n, k):
    # caso base
    if k == 0:
        return 1
    return ((n-k+1)*comb(n, k-1))//k





