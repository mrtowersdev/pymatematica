from analise_combinatoria.fatorial import fatorial


def calculo_permutacao_simples(n):
    pn = fatorial(n)
    return pn


def calculo_permutacao_com_repeticao(n, k):
    nk = 1
    for i in k:
        nk = nk * fatorial(i)
    pn = fatorial(n)/nk

    return pn


def permutacao_simples(lst):
    p = [0 for x in range(len(lst))]

    def imprime():
        result = []
        for i in range(len(p)):
            result.append(p[i])
        print(result)

    def permuta(lst, n):
        if n == len(lst):
            imprime()
        else:
            for i in range(len(lst)):
                achou = False
                for j in range(n):
                    if p[j] == lst[i]:
                        achou = True
                if not achou:
                    p[n] = lst[i]
                    permuta(lst, n+1)

    permuta(lst, 0)


def permutacao_com_repeticao(lst):
    p = [0 for x in range(len(lst))]

    def imprime():
        result = []
        for i in range(len(p)):
            result.append(p[i])
        print(result)

    def permuta(lst, n):
        if n == len(lst):
            imprime()
        else:
            for i in range(len(lst)):
                p[n] = lst[i]
                permuta(lst, n+1)

    permuta(lst, 0)