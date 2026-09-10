"""Versão imperativa do Sistema de Análise de Triângulos."""

from math import acos, degrees, isclose, sqrt

TOLERANCIA = 1e-9


def triangulo_valido(a, b, c):
    """Retorna True quando os três lados formam um triângulo."""
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a


def classificar_lados(a, b, c):
    """Classifica o triângulo como equilátero, isósceles ou escaleno."""
    if isclose(a, b, abs_tol=TOLERANCIA) and isclose(b, c, abs_tol=TOLERANCIA):
        return "equilátero"
    if (isclose(a, b, abs_tol=TOLERANCIA) or isclose(a, c, abs_tol=TOLERANCIA)
            or isclose(b, c, abs_tol=TOLERANCIA)):
        return "isósceles"
    return "escaleno"


def classificar_angulos(a, b, c):
    """Classifica o triângulo pelo tipo de seus ângulos."""
    menor, medio, maior = sorted((a, b, c))
    comparacao = menor ** 2 + medio ** 2
    quadrado_maior = maior ** 2

    if isclose(comparacao, quadrado_maior, abs_tol=TOLERANCIA):
        return "retângulo"
    if comparacao > quadrado_maior:
        return "acutângulo"
    return "obtusângulo"


def calcular_area(a, b, c):
    """Calcula a área com a fórmula de Heron."""
    semiperimetro = (a + b + c) / 2
    return sqrt(semiperimetro * (semiperimetro - a) *
                (semiperimetro - b) * (semiperimetro - c))


def calcular_angulo(lado_oposto, lado_1, lado_2):
    """Calcula um ângulo interno pela lei dos cossenos, em graus."""
    cosseno = (lado_1 ** 2 + lado_2 ** 2 - lado_oposto ** 2) / (2 * lado_1 * lado_2)
    cosseno = max(-1.0, min(1.0, cosseno))
    return degrees(acos(cosseno))


def analisar_triangulo(a, b, c):
    """Organiza todos os resultados da análise em um dicionário."""
    if not triangulo_valido(a, b, c):
        return None

    return {
        "lados": classificar_lados(a, b, c),
        "angulos": classificar_angulos(a, b, c),
        "perimetro": a + b + c,
        "area": calcular_area(a, b, c),
        "angulo_a": calcular_angulo(a, b, c),
        "angulo_b": calcular_angulo(b, a, c),
        "angulo_c": calcular_angulo(c, a, b),
    }


def ler_lado(nome):
    """Lê um número e repete a pergunta se a entrada não for numérica."""
    while True:
        try:
            return float(input(f"Digite o lado {nome}: ").replace(",", "."))
        except ValueError:
            print("Digite um número válido. Exemplo: 3 ou 3,5.")


def main():
    print("=== Sistema de Análise de Triângulos ===")
    a = ler_lado("A")
    b = ler_lado("B")
    c = ler_lado("C")

    resultado = analisar_triangulo(a, b, c)
    if resultado is None:
        print("\nAs medidas informadas não formam um triângulo válido.")
        return

    print("\nTriângulo válido.")
    print(f"Classificação pelos lados: {resultado['lados']}")
    print(f"Classificação pelos ângulos: {resultado['angulos']}")
    print(f"Perímetro: {resultado['perimetro']:.2f}")
    print(f"Área: {resultado['area']:.2f}")
    print(f"Ângulo A: {resultado['angulo_a']:.2f} graus")
    print(f"Ângulo B: {resultado['angulo_b']:.2f} graus")
    print(f"Ângulo C: {resultado['angulo_c']:.2f} graus")


if __name__ == "__main__":
    main()
