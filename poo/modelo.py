"""Modelo de domínio independente da interface. [P4-ETAPA-04]"""

from dataclasses import dataclass
from math import acos, degrees, isclose, isfinite, sqrt


@dataclass(frozen=True)
class Triangulo:
    """Objeto de valor imutável: sua construção exige três lados válidos.

    Atributos iniciados por _ são internos por convenção em Python.
    Para mudar as medidas, construa outro objeto, passando pela validação.
    """

    _a: float
    _b: float
    _c: float

    def __post_init__(self):
        for lado in self.lados:
            if lado is None:
                raise ValueError("medida ausente")
            if isinstance(lado, bool) or not isinstance(lado, (int, float)):
                raise ValueError("valor não numérico")
            if not isfinite(lado):
                raise ValueError("valor não finito")
        for lado in self.lados:
            if lado <= 0:
                raise ValueError("lado não positivo")
        a, b, c = self.lados
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("as medidas não formam um triângulo")

    @property
    def lados(self):
        return (self._a, self._b, self._c)

    @property
    def perimetro(self):
        return sum(self.lados)

    @property
    def area(self):
        a, b, c = self.lados
        s = self.perimetro / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))

    @property
    def classificacao_lados(self):
        a, b, c = self.lados
        ab = isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
        ac = isclose(a, c, rel_tol=1e-9, abs_tol=1e-9)
        bc = isclose(b, c, rel_tol=1e-9, abs_tol=1e-9)
        if ab and ac and bc:
            return "equilátero"
        if ab or ac or bc:
            return "isósceles"
        return "escaleno"

    @property
    def classificacao_angulos(self):
        x, y, z = sorted(self.lados)
        soma = x * x + y * y
        if isclose(z * z, soma, rel_tol=1e-9, abs_tol=1e-9):
            return "retângulo"
        return "acutângulo" if z * z < soma else "obtusângulo"

    @staticmethod
    def _angulo(oposto, adjacente1, adjacente2):
        cosseno = (adjacente1 ** 2 + adjacente2 ** 2 - oposto ** 2) / (2 * adjacente1 * adjacente2)
        # Protege acos contra arredondamentos ligeiramente fora de [-1, 1].
        return degrees(acos(max(-1.0, min(1.0, cosseno))))

    @property
    def angulos(self):
        a, b, c = self.lados
        return (self._angulo(a, b, c), self._angulo(b, a, c), self._angulo(c, a, b))


class SessaoAnalise:
    """Agrega triângulos aceitos e controla o estado de uma sessão."""

    def __init__(self):
        self._tentativas = 0
        self._triangulos = []

    @property
    def tentativas(self):
        return self._tentativas

    @property
    def triangulos(self):
        # Uma tupla impede que o cliente modifique a lista interna.
        return tuple(self._triangulos)

    @property
    def validos(self):
        return len(self._triangulos)

    def analisar(self, a, b, c):
        self._tentativas += 1
        triangulo = Triangulo(a, b, c)
        self._triangulos.append(triangulo)
        return triangulo
