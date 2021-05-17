from analise_combinatoria import permutacao
from analise_combinatoria import fatorial
from analise_combinatoria import arranjo
from analise_combinatoria import combinacao


if __name__ == '__main__':
    print(f'Exemplo de fatorial: {fatorial.fatorial(3)}')
    print(f'Exemplo de permutacao simples: {permutacao.simples(3)}')
    print(f'Exemplo de permutacao com repeticao: {permutacao.com_repeticao(5, [2])}')
    print(f'Exemplo de arranjo simples: {arranjo.simples(6, 3)}')
    print(f'Exemplo de arranjo com repeticao: {arranjo.com_repeticao(5, 2)}')
    print(f'Exemplo de combinacao simples: {combinacao.simples(12, 3)}')
    print(f'Exemplo de combinacao com repeticao: {combinacao.com_repeticao(10, 3)}')

