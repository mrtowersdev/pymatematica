import unittest
from calculos.analise_combinatoria.combinacao import simples, com_repeticao


class CombinacaoCasoDeTeste(unittest.TestCase):
    def test_combinacao_simples(self):
        self.assertEqual(simples(5, 2), 10)

    def test_combinacao_com_repeticao(self):
        self.assertEqual(com_repeticao(5, 2), 15)


if __name__ == '__main__':
    unittest.main()
