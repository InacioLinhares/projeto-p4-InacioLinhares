"""Executar: python poo/main.py [--json]. [P4-ETAPA-04]"""

import argparse
from modelo import SessaoAnalise
from apresentacao import ApresentadorJSON, ApresentadorTexto


class AplicacaoConsole:
    """Coordena uma sessão e usa um apresentador recebido por parâmetro."""

    def __init__(self, apresentador):
        self._sessao = SessaoAnalise()
        self._apresentador = apresentador

    @staticmethod
    def _ler_lado(nome):
        texto = input(f"Digite o lado {nome}: ").strip()
        if not texto:
            return None
        try:
            return float(texto.replace(",", "."))
        except ValueError:
            return texto

    def executar(self):
        print("=== Análise de Triângulos — Orientação a Objetos ===")
        try:
            while True:
                a = self._ler_lado("A")
                b = self._ler_lado("B")
                c = self._ler_lado("C")
                try:
                    triangulo = self._sessao.analisar(a, b, c)
                except ValueError as erro:
                    print(f"Entrada rejeitada: {erro}.")
                else:
                    print(self._apresentador.formatar(triangulo))
                resposta = input("Analisar outro triângulo? (s/n): ").strip().lower()
                while resposta not in ("s", "n"):
                    resposta = input("Digite s ou n: ").strip().lower()
                if resposta == "n":
                    break
        except (EOFError, KeyboardInterrupt):
            print("\nLeitura encerrada. Um trio incompleto não é analisado.")
        print(f"Sessão encerrada: {self._sessao.tentativas} tentativa(s), {self._sessao.validos} válida(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análise orientada a objetos de triângulos")
    parser.add_argument("--json", action="store_true", help="Apresenta cada resultado válido em JSON; mantém o diálogo no terminal.")
    argumentos = parser.parse_args()
    apresentador = ApresentadorJSON() if argumentos.json else ApresentadorTexto()
    AplicacaoConsole(apresentador).executar()
