"""Versão imperativa do Sistema de Análise de Triângulos."""

from math import acos, degrees, isclose, isfinite, sqrt

TOLERANCIA = 1e-9


def validar_entrada(a, b, c):
    """Retorna o motivo da rejeição ou None; não faz entrada/saída."""
    for lado in (a, b, c):
        if lado is None:
            return "medida ausente"
        if isinstance(lado, bool) or not isinstance(lado, (int, float)):
            return "valor não numérico"
        if not isfinite(lado):
            return "valor não finito"
    for lado in (a, b, c):
        if lado <= 0:
            return "lado não positivo"
    if not (a + b > c and a + c > b and b + c > a):
        return "as medidas não formam um triângulo"
    return None


def triangulo_valido(a, b, c):
    """Retorna True quando os três lados formam um triângulo."""
    return validar_entrada(a, b, c) is None


def classificar_lados(a, b, c):
    """Classifica o triângulo como equilátero, isósceles ou escaleno."""
    if (isclose(a, b, abs_tol=TOLERANCIA) and isclose(b, c, abs_tol=TOLERANCIA)
            and isclose(a, c, abs_tol=TOLERANCIA)):
        return "equilátero"
    if (isclose(a, b, abs_tol=TOLERANCIA) or isclose(a, c, abs_tol=TOLERANCIA)
            or isclose(b, c, abs_tol=TOLERANCIA)):
        return "isósceles"
    return "escaleno"


def classificar_angulos(a, b, c):
    """Classifica o triângulo pelo tipo de seus ângulos."""
    # Trocas explícitas de valores evidenciam a atualização de estado local.
    menor, medio, maior = a, b, c
    if menor > medio:
        menor, medio = medio, menor
    if medio > maior:
        medio, maior = maior, medio
    if menor > medio:
        menor, medio = medio, menor
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

    resultado = {}
    resultado["lados"] = classificar_lados(a, b, c)
    resultado["angulos"] = classificar_angulos(a, b, c)
    resultado["perimetro"] = a + b + c
    resultado["area"] = calcular_area(a, b, c)
    resultado["angulo_a"] = calcular_angulo(a, b, c)
    resultado["angulo_b"] = calcular_angulo(b, a, c)
    resultado["angulo_c"] = calcular_angulo(c, a, b)
    return resultado


def ler_lado(nome):
    """Converte a entrada textual; preserva valores inválidos para validação."""
    texto = input(f"Digite o lado {nome}: ").strip()
    if texto == "":
        return None
    try:
        return float(texto.replace(",", "."))
    except ValueError:
        return texto


def exibir_resultado(resultado):
    """Apresenta os cálculos; imprimir no terminal é um efeito colateral."""
    print("\nTriângulo válido.")
    print(f"Classificação pelos lados: {resultado['lados']}")
    print(f"Classificação pelos ângulos: {resultado['angulos']}")
    print(f"Perímetro: {resultado['perimetro']:.2f}")
    print(f"Área: {resultado['area']:.2f}")
    print(f"Ângulo A: {resultado['angulo_a']:.2f} graus")
    print(f"Ângulo B: {resultado['angulo_b']:.2f} graus")
    print(f"Ângulo C: {resultado['angulo_c']:.2f} graus")


def main():
    print("=== Sistema de Análise de Triângulos ===")
    continuar = True
    tentativas = 0
    validos = 0
    # Estado da sessão: contadores e controle de repetição mudam a cada rodada.
    while continuar:
        try:
            a = ler_lado("A")
            b = ler_lado("B")
            c = ler_lado("C")
        except (EOFError, KeyboardInterrupt):
            print("\nLeitura interrompida; trio incompleto não analisado.")
            break
        tentativas += 1
        erro = validar_entrada(a, b, c)
        if erro is not None:
            print(f"Entrada rejeitada: {erro}.")
        else:
            resultado = analisar_triangulo(a, b, c)
            validos += 1
            exibir_resultado(resultado)
        try:
            resposta = input("Analisar outro triângulo? (s/n): ").strip().lower()
            while resposta not in ("s", "n"):
                resposta = input("Digite s ou n: ").strip().lower()
            continuar = resposta == "s"
        except (EOFError, KeyboardInterrupt):
            continuar = False
    print(f"\nSessão encerrada: {tentativas} tentativa(s), {validos} válida(s).")


if __name__ == "__main__":
    main()
