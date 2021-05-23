from calculos.analise_combinatoria.fatorial import fatorial


def simples(n):
    pn = fatorial(n)
    return pn


def com_repeticao(n, k):
    nk = 1
    for i in k:
        nk = nk * fatorial(i)
    pn = fatorial(n)/nk

    return pn
