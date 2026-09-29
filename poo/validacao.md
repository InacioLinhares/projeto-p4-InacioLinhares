# Validação da implementação orientada a objetos

[P4-ETAPA-04]

Execução local em 29/09/2026, usando Python. Resultado: **18/18 casos da Etapa 02 aprovados**, mais **4/4 testes complementares aprovados**.

O arquivo `validar_etapa02.py` contém os mesmos dados e valores esperados de `testes/casos.md`, sem importar a implementação imperativa. Todos os campos numéricos são comparados com tolerância absoluta de 0,01; classificações e motivos de rejeição são comparados explicitamente. Também é verificada a soma dos ângulos. A execução mostra os valores obtidos e retorna status de erro se houver reprovação.

| Casos | Resultado | Verificações |
|---|---|---|
| N01, N02, N03, N04, N05 | Todos aprovados | Classificações, perímetro, área, três ângulos e soma. |
| N06, N07, N08, N09, N10 | Todos aprovados | Mesmos campos, incluindo decimais e permutação dos lados. |
| L01 | Aprovado | Zero rejeitado. |
| L02 | Aprovado | Igualdade triangular rejeitada. |
| L03 | Aprovado | Triângulo próximo da degeneração; medidas dentro da tolerância. |
| I01 | Aprovado | Valor negativo rejeitado. |
| I02 | Aprovado | Texto rejeitado. |
| I03 | Aprovado | Medida ausente rejeitada. |
| I04 | Aprovado | Infinito rejeitado. |
| I05 | Aprovado | NaN rejeitado. |

Os testes complementares verificam que não é possível alterar normalmente os lados de um objeto construído, que o histórico não expõe sua lista interna, que tentativas inválidas não são armazenadas, que os dois apresentadores funcionam com o mesmo objeto e que uma sessão de terminal processa uma análise válida seguida de uma inválida, terminando com 2 tentativas e 1 válida.

Comandos para reproduzir:

```text
python poo/validar_etapa02.py
python -m unittest discover -s poo -p test_modelo.py
```

Essa aprovação vale para os casos executados, não para todas as entradas possíveis.
