Contrato semântico e testes

[P4-ETAPA-02]

Projeto: Sistema de Análise de Triângulos, mantendo o problema da Etapa 01.

## Contrato de comportamento

O sistema recebe exatamente três medidas numéricas finitas A, B e C, na mesma unidade. Todas devem ser positivas. As entradas abaixo usam a ordem (A; B; C), com ponto como separador decimal.

1. Texto não numérico, medida ausente ou valor não finito deve gerar indicação de entrada inválida, sem resultados geométricos. A interface pode solicitar correção, mas não deve analisar o trio incorreto.
2. Zero ou valor negativo deve gerar rejeição por lado não positivo, sem resultados geométricos.
3. As medidas positivas formam um triângulo somente quando A+B>C, A+C>B e B+C>A. A igualdade não é permitida. Se a condição falhar, informar que não formam um triângulo, sem resultados geométricos.
4. Para um triângulo válido, informar validade, classificação pelos lados, classificação pelos ângulos, perímetro, área e os três ângulos internos.
5. Cada ângulo corresponde ao lado oposto de mesmo nome: ângulo A oposto ao lado A, e assim por diante. A ordem deve ser preservada na saída.
6. Mensagens e apresentação podem variar entre linguagens, mas devem preservar o significado e todos os resultados. Nenhuma classe, função ou estrutura de dados específica é exigida.

### Regras matemáticas

- Perímetro P = A+B+C; semiperímetro s = P/2.
- Área S = raiz quadrada de s(s−A)(s−B)(s−C), pela fórmula de Heron.
- Equilátero: três lados iguais; isósceles: exatamente dois iguais; escaleno: todos diferentes.
- Sendo z o maior lado e x e y os demais: retângulo se z²=x²+y², acutângulo se z²<x²+y² e obtusângulo se z²>x²+y².
- Ângulo A = arccos((B²+C²−A²)/(2BC)), convertido para graus. Os demais seguem a mesma regra, trocando o lado oposto.
- Para igualdade numérica nas classificações, considerar u e v iguais quando |u−v| ≤ máximo(10⁻⁹ × máximo(|u|,|v|), 10⁻⁹). Verificar igualdade antes de maior ou menor. A desigualdade triangular permanece estrita.

### Precisão e aprovação

Os resultados tabelados estão arredondados para duas casas decimais. Aceitar diferença absoluta de até 0,01 para cada valor numérico. Validade e classificações devem coincidir em significado. Perímetro está em unidades de comprimento, área em unidades quadradas e ângulos em graus.

A soma dos ângulos deve ser aproximadamente 180 graus. Depois do arredondamento, a soma pode ser 179,99 ou 180,01 graus.

## Dez casos normais

P representa perímetro, S representa área e os ângulos aparecem na ordem (A; B; C).

| Identificador | Entrada (A; B; C) | Saída esperada | Descrição |
|---|---|---|---|
| N01 | (3; 4; 5) | Válido; escaleno; retângulo; P=12,00; S=6,00; ângulos=(36,87; 53,13; 90,00) | Exemplo retângulo original da Etapa 01. |
| N02 | (5; 5; 5) | Válido; equilátero; acutângulo; P=15,00; S=10,83; ângulos=(60,00; 60,00; 60,00) | Três lados e ângulos iguais. |
| N03 | (5; 5; 8) | Válido; isósceles; obtusângulo; P=18,00; S=12,00; ângulos=(36,87; 36,87; 106,26) | Dois lados iguais e um ângulo obtuso. |
| N04 | (2; 3; 4) | Válido; escaleno; obtusângulo; P=9,00; S=2,90; ângulos=(28,96; 46,57; 104,48) | Lados diferentes e área não inteira. |
| N05 | (6; 8; 10) | Válido; escaleno; retângulo; P=24,00; S=24,00; ângulos=(36,87; 53,13; 90,00) | Dobrar os lados de N01 dobra P e quadruplica S. |
| N06 | (5; 5; 6) | Válido; isósceles; acutângulo; P=16,00; S=12,00; ângulos=(53,13; 53,13; 73,74) | Dois lados iguais e todos os ângulos agudos. |
| N07 | (4; 5; 6) | Válido; escaleno; acutângulo; P=15,00; S=9,92; ângulos=(41,41; 55,77; 82,82) | Lados diferentes e todos os ângulos agudos. |
| N08 | (5; 12; 13) | Válido; escaleno; retângulo; P=30,00; S=30,00; ângulos=(22,62; 67,38; 90,00) | Outra combinação de triângulo retângulo. |
| N09 | (1.5; 2; 2.5) | Válido; escaleno; retângulo; P=6,00; S=1,50; ângulos=(36,87; 53,13; 90,00) | Lados decimais; metade das medidas de N01. |
| N10 | (5; 3; 4) | Válido; escaleno; retângulo; P=12,00; S=6,00; ângulos=(90,00; 36,87; 53,13) | Permutação de N01: o ângulo reto agora corresponde a A. |

## Três casos-limite

| Identificador | Entrada (A; B; C) | Saída esperada | Descrição |
|---|---|---|---|
| L01 | (0; 4; 5) | Rejeição por lado não positivo; sem classificações, perímetro, área ou ângulos. | Zero é a fronteira inferior dos valores permitidos. |
| L02 | (1; 2; 3) | Não forma triângulo; sem classificações, perímetro, área ou ângulos. | Soma dos dois menores lados exatamente igual ao maior. |
| L03 | (2; 3; 4.999) | Válido; escaleno; obtusângulo; P=10,00; S=0,12; ângulos=(0,94; 1,40; 177,66) | Próximo da degeneração, ainda com área positiva. P exato é 9,999. |

## Cinco casos de entrada inválida

| Identificador | Entrada (A; B; C) | Saída esperada | Descrição |
|---|---|---|---|
| I01 | (-3; 4; 5) | Rejeição por lado não positivo; sem resultados geométricos. | Comprimento negativo. |
| I02 | ("abc"; 4; 5) | Entrada inválida por valor não numérico; sem resultados geométricos. | Texto no lugar de um comprimento. |
| I03 | (3; 4; ausente) | Entrada inválida por medida ausente; sem resultados geométricos. | São necessárias as três medidas. |
| I04 | (infinito; 4; 5) | Entrada inválida por valor não finito; sem resultados geométricos. | Infinito não é um comprimento aceito. |
| I05 | (indefinido/NaN; 4; 5) | Entrada inválida por valor não finito; sem resultados geométricos. | Valor indefinido não pode participar dos cálculos. |

## Aplicação nas quatro versões

Executar os mesmos 18 casos nas versões imperativa, orientada a objetos, funcional e lógica. Comparar todos os campos e registrar resultado obtido e situação (aprovado ou reprovado). A forma de fornecer a entrada pode variar conforme a implementação.

Este documento define resultados esperados, sem declarar que as quatro versões já foram implementadas ou aprovadas. O teste automático Python existente é parcial e não substitui estes casos. As versões posteriores deverão ser verificadas contra o contrato completo.
