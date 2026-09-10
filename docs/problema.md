# P4 ETAPA 01 Sistema de Análise de Triângulos

## 1. Descrição do problema

O projeto propõe um sistema que analisa um triângulo a partir das medidas dos seus três lados. O sistema verifica se as medidas realmente formam um triângulo e apresenta propriedades geométricas importantes.

## 2. Objetivo

O sistema deve validar três medidas, classificar o triângulo e calcular informações matemáticas sobre ele.

## 3. Entradas

Três números reais positivos que representam os lados A, B e C.

## 4. Saídas

Para um triângulo válido, o sistema informa a classificação pelos lados e pelos ângulos, o perímetro, a área e os três ângulos internos. Para medidas inválidas, informa que não formam um triângulo.

## 5. Regras do problema

1. Todos os lados devem ser maiores que zero.
2. Um triângulo é válido quando cada lado é menor que a soma dos outros dois.
3. O perímetro é a soma dos três lados.
4. A área é calculada pela fórmula de Heron.
5. O triângulo é equilátero quando possui três lados iguais, isósceles quando possui dois lados iguais e escaleno quando todos os lados são diferentes.
6. Considerando o maior lado: se o seu quadrado for igual à soma dos quadrados dos outros dois, o triângulo é retângulo; se for menor, é acutângulo; se for maior, é obtusângulo.
7. Os ângulos internos são calculados pela lei dos cossenos.

## 6. Casos de exemplo

| Entrada | Saída esperada |
|---|---|
| 3, 4, 5 | Válido, escaleno, retângulo, perímetro 12, área 6 |
| 5, 5, 5 | Válido, equilátero, acutângulo, perímetro 15 |
| 5, 5, 8 | Válido, isósceles, obtusângulo |
| 2, 3, 4 | Válido, escaleno, obtusângulo |
| 6, 8, 10 | Válido, escaleno, retângulo, perímetro 24, área 24 |

## 7. Casos limite

1. Lados iguais a zero ou negativos.
2. Medidas que não obedecem à desigualdade triangular, como 1, 2 e 3.
3. Valores decimais próximos do limite de validade, como 2, 3 e 4,999.

## 8. Restrições

O projeto não inclui desenho do triângulo, figuras tridimensionais, conversão de unidades, armazenamento em banco de dados ou interface gráfica.

## 9. Principais conceitos do domínio

Lado, triângulo, validade, perímetro, semiperímetro, área, ângulo e classificação geométrica.

## 10. Adequação aos quatro paradigmas

Na programação imperativa, as etapas são executadas em sequência usando variáveis e condicionais. Na orientação a objetos, o triângulo será uma entidade com propriedades e comportamentos. Na programação funcional, os cálculos serão organizados como funções puras. Na programação lógica, as condições de validade e as classificações serão expressas como regras e relações.

## 11. Linguagens inicialmente consideradas

- Imperativo: Python, usando variáveis, leitura de dados e estruturas condicionais.
- Orientado a objetos: Python, usando uma classe `Triangulo`.
- Funcional: Python, usando funções sem alterar os dados recebidos.
- Lógico: Prolog, usando regras para validade e classificação.
