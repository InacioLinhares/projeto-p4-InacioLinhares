"""Testes de contrato, imutabilidade, composição e interação real."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from funcional.nucleo import (analisar_triangulo, analisar_textos, analisar_lote,
                              registrar_resultado, SESSAO_INICIAL, compor)
from funcional.apresentacao import formatar_json


# Referências das 18 entradas da Etapa 02 anteriormente analisadas.
VALIDOS = (
    ((3, 4, 5), 'escaleno', 'retângulo', (12, 6, 36.87, 53.13, 90)),
    ((5, 5, 5), 'equilátero', 'acutângulo', (15, 10.83, 60, 60, 60)),
    ((5, 5, 8), 'isósceles', 'obtusângulo', (18, 12, 36.87, 36.87, 106.26)),
    ((2, 3, 4), 'escaleno', 'obtusângulo', (9, 2.90, 28.96, 46.57, 104.48)),
    ((6, 8, 10), 'escaleno', 'retângulo', (24, 24, 36.87, 53.13, 90)),
    ((5, 5, 6), 'isósceles', 'acutângulo', (16, 12, 53.13, 53.13, 73.74)),
    ((4, 5, 6), 'escaleno', 'acutângulo', (15, 9.92, 41.41, 55.77, 82.82)),
    ((5, 12, 13), 'escaleno', 'retângulo', (30, 30, 22.62, 67.38, 90)),
    ((1.5, 2, 2.5), 'escaleno', 'retângulo', (6, 1.50, 36.87, 53.13, 90)),
    ((5, 3, 4), 'escaleno', 'retângulo', (12, 6, 90, 36.87, 53.13)),
    ((2, 3, 4.999), 'escaleno', 'obtusângulo', (10, 0.12, 0.94, 1.40, 177.66)),
)
INVALIDOS = (
    ((0, 4, 5), 'lado não positivo'),
    ((1, 2, 3), 'as medidas não formam um triângulo'),
    ((-3, 4, 5), 'lado não positivo'),
    (('abc', 4, 5), 'valor não numérico'),
    ((3, 4, None), 'medida ausente'),
    ((float('inf'), 4, 5), 'valor não finito'),
    ((float('nan'), 4, 5), 'valor não finito'),
)


class TestFuncional(unittest.TestCase):
    def test_18_casos_de_referencia(self):
        for lados, classe_lados, classe_angulos, numeros in VALIDOS:
            with self.subTest(lados=lados):
                erro, resultado = analisar_triangulo(lados)
                self.assertIsNone(erro)
                dados = dict(resultado)
                self.assertEqual(dados['lados'], classe_lados)
                self.assertEqual(dados['angulos'], classe_angulos)
                obtidos = (dados['perimetro'], dados['area']) + dados['angulos_graus']
                for obtido, esperado in zip(obtidos, numeros):
                    self.assertAlmostEqual(obtido, esperado, delta=0.01)
                self.assertAlmostEqual(sum(dados['angulos_graus']), 180, delta=0.01)
        for lados, motivo in INVALIDOS:
            with self.subTest(lados=lados):
                self.assertEqual(analisar_triangulo(lados), (motivo, None))

    def test_contratos_adicionais(self):
        self.assertEqual(analisar_triangulo((True, 4, 5))[0], 'valor não numérico')
        self.assertEqual(analisar_triangulo((3, 4))[0], 'informe exatamente três lados')
        for lados in ((1e308,) * 3, (1e-300,) * 3):
            erro, resultado = analisar_triangulo(lados)
            self.assertIsNotNone(erro)
            self.assertIsNone(resultado)

    def test_sessao_e_entrada_preservadas(self):
        lados = (3, 4, 5)
        analise = analisar_triangulo(lados)
        nova = registrar_resultado(SESSAO_INICIAL, analise)
        rejeitada = registrar_resultado(nova, analisar_triangulo((1, 2, 3)))
        self.assertEqual(lados, (3, 4, 5))
        self.assertEqual(SESSAO_INICIAL, (0, ()))
        self.assertEqual(nova, (1, (analise[1],)))
        self.assertEqual(rejeitada, (2, (analise[1],)))
        self.assertIsInstance(analise[1], tuple)
        self.assertIsInstance(dict(analise[1])['angulos_graus'], tuple)
        self.assertEqual(analisar_triangulo(lados), analise)

    def test_composicao_conversao_lote_e_formatacao(self):
        self.assertEqual(compor(lambda x: x + 1, lambda x: x * 2)(3), 8)
        self.assertEqual(compor()(3), 3)
        analise = analisar_textos(('1,5', '2', '2,5'))
        self.assertEqual(dict(analise[1])['area'], 1.5)
        self.assertEqual(analisar_textos(('', '4', '5'))[0], 'medida ausente')
        lote = analisar_lote(((3, 4, 5), (1, 2, 3)))
        self.assertEqual(json.loads(formatar_json(lote[0]))['area'], 6)
        self.assertFalse(json.loads(formatar_json(lote[1]))['valido'])

    def rodar_console(self, entrada, *opcoes):
        return subprocess.run([sys.executable, str(Path(__file__).with_name('main.py')),
                               *opcoes], input=entrada, text=True, capture_output=True,
                              check=True).stdout

    def test_console_repeticao_rejeicao_e_resposta_invalida(self):
        saida = self.rodar_console('3\n4\n5\nx\ns\n1\n2\n3\nn\n')
        self.assertIn('Área: 6.00', saida)
        self.assertIn('Entrada rejeitada', saida)
        self.assertIn('2 tentativa(s), 1 válida(s)', saida)

    def test_console_trio_incompleto_e_json(self):
        self.assertIn('0 tentativa(s), 0 válida(s)', self.rodar_console('3\n'))
        self.assertIn('"area": 6.0', self.rodar_console('3\n4\n5\nn\n', '--json'))


if __name__ == '__main__':
    unittest.main()
