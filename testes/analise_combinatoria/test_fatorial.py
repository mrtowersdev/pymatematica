import unittest
from analise_combinatoria.fatorial import fatorial


class FatorialCasoDeTeste(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)


if __name__ == '__main__':
    unittest.main()
