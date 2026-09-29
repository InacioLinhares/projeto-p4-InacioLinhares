"""Apresentadores intercambiáveis: polimorfismo por interface abstrata."""

from abc import ABC, abstractmethod
import json


class Apresentador(ABC):
    @abstractmethod
    def formatar(self, triangulo):
        """Retorna uma representação textual de um triângulo válido."""
        raise NotImplementedError


class ApresentadorTexto(Apresentador):
    def formatar(self, triangulo):
        a, b, c = triangulo.angulos
        return (
            f"Triângulo válido.\n"
            f"Classificação pelos lados: {triangulo.classificacao_lados}\n"
            f"Classificação pelos ângulos: {triangulo.classificacao_angulos}\n"
            f"Perímetro: {triangulo.perimetro:.2f}\n"
            f"Área: {triangulo.area:.2f}\n"
            f"Ângulo A: {a:.2f} graus\nÂngulo B: {b:.2f} graus\nÂngulo C: {c:.2f} graus"
        )


class ApresentadorJSON(Apresentador):
    def formatar(self, triangulo):
        return json.dumps({
            "valido": True,
            "lados": triangulo.classificacao_lados,
            "angulos": triangulo.classificacao_angulos,
            "perimetro": triangulo.perimetro,
            "area": triangulo.area,
            "angulos_graus": triangulo.angulos,
        }, ensure_ascii=False, allow_nan=False)
