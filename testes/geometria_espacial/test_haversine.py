import unittest
from calculos.geometria_espacial.haversine import distance_kilometers, distance_meters


class CalculoDistanciaTeste(unittest.TestCase):
    def test_distancia_kilometros(self):
        self.assertEqual(distance_kilometers(-23.542987, -46.344314, -23.544095, -46.343032), 0.11163634749890428)

    def test_distancia_metros(self):
        self.assertEqual(distance_meters(-23.542987, -46.344314, -23.544095, -46.343032), 111.63634749890427)


if __name__ == '__main__':
    unittest.main()
