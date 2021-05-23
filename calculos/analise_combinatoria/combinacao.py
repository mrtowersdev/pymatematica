from calculos.analise_combinatoria.fatorial import fatorial


def simples(n, k):
    cnk = fatorial(n)/(fatorial(k) * fatorial(n - k))
    return cnk


def com_repeticao(n, k):
    cnk = fatorial(n + k - 1)/(fatorial(k) * fatorial(n - 1))
    return cnk
