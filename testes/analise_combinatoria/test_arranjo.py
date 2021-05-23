import unittest
from calculos.analise_combinatoria.arranjo import simples, com_repeticao


class ArranjoCasoDeTeste(unittest.TestCase):
    def test_arranjo_simples(self):
        self.assertEqual(simples(5, 2), 20)

    def test_arranjo_com_repeticao(self):
        self.assertEqual(com_repeticao(5, 2), 25)


if __name__ == '__main__':
    unittest.main()
