"""Borda impura: interação com terminal e argumentos de execução."""
import argparse

if __package__:
    from .nucleo import SESSAO_INICIAL, analisar_textos, registrar_resultado, compor
    from .apresentacao import formatar_texto, formatar_json, formatar_resumo
else:
    from nucleo import SESSAO_INICIAL, analisar_textos, registrar_resultado, compor
    from apresentacao import formatar_texto, formatar_json, formatar_resumo


def ler_lados():
    """Impura: depende do teclado; trio interrompido não vira tentativa."""
    return tuple(map(lambda nome: input(f'Digite o lado {nome}: '), ('A', 'B', 'C')))


def deseja_continuar():
    """Impura: consulta o usuário e repete até receber s ou n."""
    resposta = input('Analisar outro triângulo? (s/n): ').strip().lower()
    while resposta not in ('s', 'n'):
        resposta = input('Digite s ou n: ').strip().lower()
    return resposta == 's'


def executar(formatador):
    """Recebe função de primeira classe; concentra leitura e impressão.

    O laço da interface evita acumular chamadas na pilha do Python.
    A sessão é reatribuída a novos valores, nunca modificada internamente.
    """
    sessao = SESSAO_INICIAL
    apresentar = compor(formatador, print)
    print('=== Análise de Triângulos — Funcional ===')
    try:
        while True:
            analise = analisar_textos(ler_lados())
            sessao = registrar_resultado(sessao, analise)
            apresentar(analise)
            if not deseja_continuar():
                break
    except (EOFError, KeyboardInterrupt):
        print('\nInteração encerrada. Um trio incompleto não conta como tentativa.')
    print(formatar_resumo(sessao))


def main():
    parser = argparse.ArgumentParser(description='Análise funcional de triângulos')
    parser.add_argument('--json', action='store_true',
                        help='Formata cada análise em JSON; mantém o diálogo no terminal.')
    argumentos = parser.parse_args()
    executar(formatar_json if argumentos.json else formatar_texto)


if __name__ == '__main__':
    main()
