# ETAPA 06 — Implementação funcional

**Projeto:** Sistema de Análise de Triângulos  
**Autor:** Inácio Linhares  
**Identificação:** [P4-ETAPA-06]

## Execução

Copie a pasta `funcional/` deste ZIP para a raiz do repositório, ao lado de `imperativo/` e `poo/`. Não é necessário instalar dependências. Utilize Python 3.

Na raiz do projeto:

```bash
python funcional/main.py
```

Alternativa como módulo:

```bash
python -m funcional.main
```

Para formatar cada análise em JSON:

```bash
python funcional/main.py --json
```

A opção mantém as perguntas e o resumo no terminal; não transforma toda a saída em um documento JSON. Digite três lados, um por vez. O programa aceita ponto ou vírgula decimal. Responda `s` para continuar ou `n` para encerrar.

## Arquivos

- `nucleo.py`: validação, cálculos, composição e transformação imutável da sessão.
- `apresentacao.py`: funções puras de formatação em texto e JSON.
- `main.py`: leitura, impressão e coordenação da interação.
- `test_funcional.py`: testes de contrato, propriedades funcionais e console.
- `reflexao.md`: identificação dos conceitos e reflexão obrigatória.
- `validacao.md`: comandos e resultados da verificação.
- `__init__.py`: permite importar a pasta como pacote.

## Contrato e uso sem terminal

```python
from funcional.nucleo import analisar_triangulo, analisar_textos

analise = analisar_triangulo((3, 4, 5))
erro, resultado = analise
# erro: None
# resultado: tupla de pares (nome, valor)
# dict(resultado)['area']: 6.0

rejeicao = analisar_triangulo((1, 2, 3))
# ('as medidas não formam um triângulo', None)

analise_decimal = analisar_textos(('1,5', '2', '2,5'))
```

A API do núcleo recebe uma tupla de três valores. Rejeita medidas ausentes, booleanos, valores não numéricos, não finitos, não positivos e trios que não atendam à desigualdade triangular. Falhas de alcance numérico dos cálculos também são devolvidas como rejeições. As funções matemáticas auxiliares pressupõem medidas válidas; use `analisar_triangulo()` como ponto de entrada validado.

As classificações, perímetro, fórmula de Heron, lei dos cossenos, tolerâncias e limitação do cosseno a [-1, 1] seguem as implementações analisadas nas etapas anteriores. O resultado passa a ser imutável e os ângulos são agrupados na tupla `angulos_graus`. O estado da sessão também passa a ser uma tupla nova a cada tentativa. O histórico conserva somente análises válidas, como na versão POO.

Os cálculos usam ponto flutuante: resultados próximos de fronteiras têm tolerância, e entradas extremas podem ser rejeitadas por limitações numéricas. Os testes não demonstram correção para todos os números possíveis.

## Testes

Na raiz do projeto:

```bash
python -m unittest funcional.test_funcional -v
```

## Tag de entrega

Depois de copiar a pasta para seu repositório:

```bash
git add funcional
git commit -m "Etapa 06: implementa análise funcional de triângulos"
git tag P4-ETAPA-06
git push origin HEAD
git push origin P4-ETAPA-06
```

O enunciado identifica a etapa como `[P4-ETAPA-06]`, mas Git não permite `[` em nomes de tags. Os comandos usam `P4-ETAPA-06`, sem colchetes. Confirme com o professor se os colchetes são somente a notação do enunciado. Nenhuma tag foi criada ou publicada neste pacote, que não contém o histórico Git.
