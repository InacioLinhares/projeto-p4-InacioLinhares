"""Valida os mesmos 18 casos da Etapa 02, sem importar a versão imperativa."""
from math import isfinite
from modelo import Triangulo

# Referências fixas transcritas dos mesmos casos da Etapa 02.
CASOS_VALIDOS = [
    ("N01", (3, 4, 5), "escaleno", "retângulo", (12, 6, 36.87, 53.13, 90)),
    ("N02", (5, 5, 5), "equilátero", "acutângulo", (15, 10.83, 60, 60, 60)),
    ("N03", (5, 5, 8), "isósceles", "obtusângulo", (18, 12, 36.87, 36.87, 106.26)),
    ("N04", (2, 3, 4), "escaleno", "obtusângulo", (9, 2.90, 28.96, 46.57, 104.48)),
    ("N05", (6, 8, 10), "escaleno", "retângulo", (24, 24, 36.87, 53.13, 90)),
    ("N06", (5, 5, 6), "isósceles", "acutângulo", (16, 12, 53.13, 53.13, 73.74)),
    ("N07", (4, 5, 6), "escaleno", "acutângulo", (15, 9.92, 41.41, 55.77, 82.82)),
    ("N08", (5, 12, 13), "escaleno", "retângulo", (30, 30, 22.62, 67.38, 90)),
    ("N09", (1.5, 2, 2.5), "escaleno", "retângulo", (6, 1.50, 36.87, 53.13, 90)),
    ("N10", (5, 3, 4), "escaleno", "retângulo", (12, 6, 90, 36.87, 53.13)),
    ("L03", (2, 3, 4.999), "escaleno", "obtusângulo", (10, 0.12, 0.94, 1.40, 177.66)),
]
CASOS_REJEITADOS = [
    ("L01", (0, 4, 5), "lado não positivo"),
    ("L02", (1, 2, 3), "as medidas não formam um triângulo"),
    ("I01", (-3, 4, 5), "lado não positivo"),
    ("I02", ("abc", 4, 5), "valor não numérico"),
    ("I03", (3, 4, None), "medida ausente"),
    ("I04", (float("inf"), 4, 5), "valor não finito"),
    ("I05", (float("nan"), 4, 5), "valor não finito"),
]


def main():
    aprovados = 0
    for identificador, entrada, lados, angulos, numeros in CASOS_VALIDOS:
        try:
            triangulo = Triangulo(*entrada)
            obtidos = (triangulo.perimetro, triangulo.area, *triangulo.angulos)
            correto = triangulo.classificacao_lados == lados and triangulo.classificacao_angulos == angulos
            for obtido, esperado in zip(obtidos, numeros):
                correto = correto and isfinite(obtido) and abs(obtido - esperado) <= 0.01
            correto = correto and abs(sum(triangulo.angulos) - 180) <= 0.01
            detalhe = str(obtidos)
        except Exception as erro:
            correto = False
            detalhe = str(erro)
        if correto:
            aprovados += 1
        print(identificador, "APROVADO" if correto else "REPROVADO", detalhe)
    for identificador, entrada, esperado in CASOS_REJEITADOS:
        try:
            Triangulo(*entrada)
            correto = False
            detalhe = "Objeto inválido foi construído!"
        except ValueError as erro:
            detalhe = str(erro)
            correto = detalhe == esperado
        except Exception as erro:
            correto = False
            detalhe = str(erro)
        if correto:
            aprovados += 1
        print(identificador, "APROVADO" if correto else "REPROVADO", detalhe)
    print(f"\n{aprovados}/18 casos aprovados.")
    return 0 if aprovados == 18 else 1


if __name__ == "__main__":
    raise SystemExit(main())

