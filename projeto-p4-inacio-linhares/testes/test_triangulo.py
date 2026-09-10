import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "imperativo"))

from triangulo import analisar_triangulo, triangulo_valido


class TesteTriangulo(unittest.TestCase):
    def test_triangulo_retangulo_345(self):
        resultado = analisar_triangulo(3, 4, 5)
        self.assertEqual(resultado["lados"], "escaleno")
        self.assertEqual(resultado["angulos"], "retângulo")
        self.assertAlmostEqual(resultado["perimetro"], 12)
        self.assertAlmostEqual(resultado["area"], 6)

    def test_triangulo_equilatero(self):
        resultado = analisar_triangulo(5, 5, 5)
        self.assertEqual(resultado["lados"], "equilátero")
        self.assertEqual(resultado["angulos"], "acutângulo")

    def test_triangulo_isosceles_obtusangulo(self):
        resultado = analisar_triangulo(5, 5, 8)
        self.assertEqual(resultado["lados"], "isósceles")
        self.assertEqual(resultado["angulos"], "obtusângulo")

    def test_medidas_invalidas(self):
        self.assertFalse(triangulo_valido(0, 4, 5))
        self.assertFalse(triangulo_valido(1, 2, 3))
        self.assertIsNone(analisar_triangulo(1, 2, 3))


if __name__ == "__main__":
    unittest.main()
