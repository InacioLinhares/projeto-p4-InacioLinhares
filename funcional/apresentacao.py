"""Formatação pura: retorna strings; a impressão fica em main.py."""
import json


def formatar_texto(analise):
    erro, resultado = analise
    if erro is not None:
        return f'Entrada rejeitada: {erro}.'
    # Dicionário temporário novo, não modificado nem compartilhado como estado.
    dados = dict(resultado)
    a, b, c = dados['angulos_graus']
    return (
        f"Triângulo válido.\n"
        f"Classificação pelos lados: {dados['lados']}\n"
        f"Classificação pelos ângulos: {dados['angulos']}\n"
        f"Perímetro: {dados['perimetro']:.2f}\n"
        f"Área: {dados['area']:.2f}\n"
        f"Ângulo A: {a:.2f} graus\n"
        f"Ângulo B: {b:.2f} graus\n"
        f"Ângulo C: {c:.2f} graus"
    )


def formatar_json(analise):
    erro, resultado = analise
    dados = {'valido': False, 'erro': erro} if erro else {'valido': True, **dict(resultado)}
    return json.dumps(dados, ensure_ascii=False, allow_nan=False)


def formatar_resumo(sessao):
    tentativas, historico = sessao
    return f'Sessão encerrada: {tentativas} tentativa(s), {len(historico)} válida(s).'
