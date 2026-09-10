# Casos de Teste

| Caso | Entrada | Resultado esperado |
|---|---|---|
| 1 | 3, 4, 5 | Válido, escaleno, retângulo, perímetro 12, área 6 |
| 2 | 5, 5, 5 | Válido, equilátero, acutângulo, perímetro 15 |
| 3 | 5, 5, 8 | Válido, isósceles, obtusângulo |
| 4 | 2, 3, 4 | Válido, escaleno, obtusângulo |
| 5 | 6, 8, 10 | Válido, escaleno, retângulo, perímetro 24, área 24 |
| Limite 1 | 0, 4, 5 | Inválido: lado não positivo |
| Limite 2 | 1, 2, 3 | Inválido: não respeita a desigualdade triangular |
| Limite 3 | 2, 3, 4,999 | Válido |
