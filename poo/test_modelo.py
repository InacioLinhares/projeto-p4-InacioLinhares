"""Verificações de encapsulamento, agregação e polimorfismo."""
import json
import subprocess
import sys
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from modelo import SessaoAnalise, Triangulo
from apresentacao import Apresentador, ApresentadorJSON, ApresentadorTexto


class TestModelo(unittest.TestCase):
    def test_objeto_valido_nao_permite_alterar_lados(self):
        triangulo = Triangulo(3, 4, 5)
        with self.assertRaises(FrozenInstanceError):
            triangulo._a = -1
        self.assertEqual(triangulo.lados, (3, 4, 5))

    def test_sessao_preserva_historico_e_conta_rejeicoes(self):
        sessao = SessaoAnalise()
        triangulo = sessao.analisar(3, 4, 5)
        with self.assertRaises(ValueError):
            sessao.analisar(1, 2, 3)
        self.assertEqual(sessao.tentativas, 2)
        self.assertEqual(sessao.validos, 1)
        self.assertIs(sessao.triangulos[0], triangulo)
        copia = sessao.triangulos + (Triangulo(5, 5, 5),)
        self.assertEqual(len(copia), 2)
        self.assertEqual(sessao.validos, 1)

    def test_apresentadores_intercambiaveis_preservam_dominio(self):
        triangulo = Triangulo(3, 4, 5)
        for apresentador in (ApresentadorTexto(), ApresentadorJSON()):
            self.assertIsInstance(apresentador, Apresentador)
            self.assertIn("retângulo", apresentador.formatar(triangulo))
        dados = json.loads(ApresentadorJSON().formatar(triangulo))
        self.assertEqual(dados["area"], 6)
        self.assertAlmostEqual(dados["angulos_graus"][2], 90)
        self.assertEqual(triangulo.lados, (3, 4, 5))

    def test_console_repeticao_e_rejeicao(self):
        processo = subprocess.run(
            [sys.executable, "-X", "utf8", str(Path(__file__).with_name("main.py"))],
            input="3\n4\n5\ns\n1\n2\n3\nn\n",
            capture_output=True, text=True, encoding="utf-8", check=True,
        )
        self.assertIn("Área: 6.00", processo.stdout)
        self.assertIn("Entrada rejeitada", processo.stdout)
        self.assertIn("2 tentativa(s), 1 válida(s)", processo.stdout)


if __name__ == "__main__":
    unittest.main()
