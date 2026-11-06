"""Núcleo funcional puro: não lê, imprime ou modifica dados recebidos.

Os resultados são tuplas de pares, e não dicionários mutáveis.
Funções matemáticas internas pressupõem lados previamente validados.
"""
from functools import reduce
from math import acos, degrees, isclose, isfinite, sqrt

TOLERANCIA = 1e-9


def compor(*funcoes):
    """Alta ordem: recebe funções e cria uma composição da esquerda à direita."""
    return lambda valor: reduce(lambda dado, funcao: funcao(dado), funcoes, valor)


def aplicar_calculos(calculos, lados):
    """Alta ordem: aplica cada função recebida ao mesmo trio imutável."""
    return tuple(map(lambda item: (item[0], item[1](lados)), calculos))


def converter_lado(texto):
    """Transformação pura; a leitura do texto ocorre na interface."""
    texto = texto.strip()
    if not texto:
        return None
    try:
        return float(texto.replace(',', '.'))
    except ValueError:
        return texto


def validar_entrada(lados):
    """Retorna um motivo de rejeição ou None, sem lançar erros de domínio."""
    if len(lados) != 3:
        return 'informe exatamente três lados'
    verificacoes = (
        (lambda x: x is None, 'medida ausente'),
        (lambda x: isinstance(x, bool) or not isinstance(x, (int, float)),
         'valor não numérico'),
        (lambda x: not isfinite(x), 'valor não finito'),
    )
    # Preserva a prioridade por lado usada nas implementações anteriores.
    erro = next((mensagem for lado in lados for predicado, mensagem in verificacoes
                 if predicado(lado)), None)
    if erro is not None:
        return erro
    if any(map(lambda lado: lado <= 0, lados)):
        return 'lado não positivo'
    a, b, c = lados
    if not (a + b > c and a + c > b and b + c > a):
        return 'as medidas não formam um triângulo'
    return None


def classificar_lados(lados):
    a, b, c = lados
    iguais = tuple(map(lambda par: isclose(*par, rel_tol=TOLERANCIA,
                                          abs_tol=TOLERANCIA),
                       ((a, b), (a, c), (b, c))))
    return 'equilátero' if all(iguais) else ('isósceles' if any(iguais) else 'escaleno')


def classificar_angulos(lados):
    x, y, z = sorted(lados)
    soma = x ** 2 + y ** 2
    maior = z ** 2
    if isclose(soma, maior, rel_tol=TOLERANCIA, abs_tol=TOLERANCIA):
        return 'retângulo'
    return 'acutângulo' if soma > maior else 'obtusângulo'


def calcular_perimetro(lados):
    return sum(lados)


def calcular_area(lados):
    s = calcular_perimetro(lados) / 2
    return sqrt(s * (s - lados[0]) * (s - lados[1]) * (s - lados[2]))


def calcular_angulo(oposto, adjacente1, adjacente2):
    cosseno = ((adjacente1 ** 2 + adjacente2 ** 2 - oposto ** 2)
               / (2 * adjacente1 * adjacente2))
    return degrees(acos(max(-1.0, min(1.0, cosseno))))


def calcular_angulos(lados):
    a, b, c = lados
    return tuple(map(lambda trio: calcular_angulo(*trio),
                     ((a, b, c), (b, a, c), (c, a, b))))


# Funções são valores: ficam em uma tupla e são passadas a aplicar_calculos.
CALCULOS = (
    ('lados', classificar_lados),
    ('angulos', classificar_angulos),
    ('perimetro', calcular_perimetro),
    ('area', calcular_area),
    ('angulos_graus', calcular_angulos),
)


def analisar_triangulo(lados):
    """Retorna (erro, resultado); exatamente um dos dois é None.

    A API recebe uma tupla de três valores. Também captura falhas numéricas
    para que o console apresente uma rejeição, sem encerrar a sessão.
    """
    try:
        erro = validar_entrada(lados)
        if erro is not None:
            return (erro, None)
        resultado = aplicar_calculos(CALCULOS, lados)
        numeros = (resultado[2][1], resultado[3][1]) + resultado[4][1]
        if not all(map(isfinite, numeros)):
            return ('medidas fora do alcance numérico dos cálculos', None)
        return (None, resultado)
    except (OverflowError, ValueError, ZeroDivisionError):
        return ('medidas fora do alcance numérico dos cálculos', None)


# Tupla (tentativas, histórico). O histórico contém apenas resultados válidos.
SESSAO_INICIAL = (0, ())


def registrar_resultado(sessao, analise):
    """Cria uma nova sessão; preserva a versão anterior integralmente."""
    tentativas, historico = sessao
    erro, resultado = analise
    return (tentativas + 1,
            historico + (resultado,) if erro is None else historico)


def analisar_lote(trios):
    """Alta ordem com map: produz resultados independentes, sem entrada/saída."""
    return tuple(map(analisar_triangulo, trios))


analisar_textos = compor(
    lambda textos: tuple(map(converter_lado, textos)),
    analisar_triangulo,
)
