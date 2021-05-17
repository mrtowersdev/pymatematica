from analise_combinatoria.fatorial import fatorial


def simples(n, k):
    ank = fatorial(n)/fatorial(n - k)
    return ank


def com_repeticao(n, k):
    ank = n ** k
    return ank