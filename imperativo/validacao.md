# Registro de validação da versão imperativa

[P4-ETAPA-03]

Data: 25/09/2026. Execução local em Python, utilizando `python imperativo/validar_etapa02.py`.

Resultado: **18 de 18 casos da Etapa 02 aprovados**. Foram conferidos os dois tipos de classificação, perímetro, área e cada ângulo com tolerância absoluta de 0,01. Para entradas rejeitadas, foram conferidos o motivo e a ausência de resultados geométricos.

| Caso | Resultado | Evidência resumida |
|---|---|---|
| N01 | Aprovado | Escaleno retângulo; P=12,00; área=6,00. |
| N02 | Aprovado | Equilátero acutângulo; P=15,00; área=10,83. |
| N03 | Aprovado | Isósceles obtusângulo; P=18,00; área=12,00. |
| N04 | Aprovado | Escaleno obtusângulo; P=9,00; área=2,90. |
| N05 | Aprovado | Escaleno retângulo; P=24,00; área=24,00. |
| N06 | Aprovado | Isósceles acutângulo; P=16,00; área=12,00. |
| N07 | Aprovado | Escaleno acutângulo; P=15,00; área=9,92. |
| N08 | Aprovado | Escaleno retângulo; P=30,00; área=30,00. |
| N09 | Aprovado | Escaleno retângulo; P=6,00; área=1,50. |
| N10 | Aprovado | Ângulo A=90,00; B=36,87; C=53,13. |
| L01 | Aprovado | Lado zero rejeitado por não ser positivo. |
| L02 | Aprovado | Igualdade triangular rejeitada. |
| L03 | Aprovado | Escaleno obtusângulo; área=0,12; C=177,66 graus. |
| I01 | Aprovado | Lado negativo rejeitado. |
| I02 | Aprovado | Texto não numérico rejeitado. |
| I03 | Aprovado | Medida ausente rejeitada. |
| I04 | Aprovado | Infinito rejeitado. |
| I05 | Aprovado | NaN rejeitado. |

Os quatro testes anteriores de `testes/test_triangulo.py` também passaram. As aprovações registradas referem-se somente à versão imperativa atual; não às implementações futuras nem a todas as entradas possíveis.
