from analise_combinatoria import permutacao
from analise_combinatoria import fatorial
from analise_combinatoria import arranjo
from analise_combinatoria import combinacao


if __name__ == '__main__':
    print(f'Exemplo de fatorial: {fatorial.fatorial(3)}')
    print(f'Exemplo de permutacao simples: {permutacao.calculo_permutacao_simples(5)}')
    print(f'Exemplo de permutacao com repeticao: {permutacao.calculo_permutacao_com_repeticao(5, [2])}')
    print(f'Exemplo de arranjo simples: {arranjo.simples(6, 3)}')
    print(f'Exemplo de arranjo com repeticao: {arranjo.com_repeticao(5, 2)}')
    print(f'Exemplo de combinacao simples: {combinacao.simples(5, 2)}')
    print(f'Exemplo de combinacao com repeticao: {combinacao.com_repeticao(10, 3)}')

    print(f'Permutacao simples: {permutacao.permutacao_simples([1, 2, 3, 4])}')
    print(f'Permutacao com repeticao: {permutacao.permutacao_com_repeticao([1, 2, 3, 4])}')

