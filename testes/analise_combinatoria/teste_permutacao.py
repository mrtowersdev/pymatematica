import unittest
from analise_combinatoria.permutacao import simples, com_repeticao


class PermutacaoCasoDeTeste(unittest.TestCase):
    def test_permutacao_simples(self):
        self.assertEqual(simples(5), 120)

    def test_permutacao_com_repeticao(self):
        self.assertEqual(com_repeticao(5, [2]), 60)


if __name__ == '__main__':
    unittest.main()
