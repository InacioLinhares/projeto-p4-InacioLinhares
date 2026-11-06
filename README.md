# Projeto P4 — Sistema de Análise de Triângulos

[P4-ETAPA-01] Proposta e especificação do problema.

[P4-ETAPA-02] Contrato semântico e testes: [casos de teste](testes/casos.md).

[P4-ETAPA-03] Implementação imperativa em Python: [código](imperativo/triangulo.py), [decisões](imperativo/decisoes.md) e [validação](imperativo/validacao.md).

[P4-ETAPA-04] Implementação orientada a objetos em Python: [instruções](poo/README.md), [reflexão](poo/reflexão.md) e [validação](poo/validacao.md).

[P4-ETAPA-05] Comparação entre as implementações imperativa e orientada a objetos: [análise](docs/comparacao-final.md).

[P4-ETAPA-06] Implementação funcional em Python: [código](funcional/nucleo.py), [instruções](funcional/README.md), [reflexão](funcional/reflexao.md) e [validação](funcional/validacao.md).

Este projeto analisa um triângulo a partir dos seus três lados, utilizando diferentes paradigmas de programação. Estão implementadas as versões imperativa, orientada a objetos e funcional. A versão lógica será desenvolvida em uma etapa futura.

O sistema valida as medidas, classifica o triângulo pelos lados e pelos ângulos e calcula perímetro, área e ângulos internos.

## Organização

- `docs/`: especificação, decisões e comparação entre paradigmas.
- `testes/`: casos de teste e testes da implementação imperativa.
- `imperativo/`: implementação imperativa em Python.
- `poo/`: implementação orientada a objetos e documentação.
- `funcional/`: implementação funcional, testes e reflexão da Etapa 06.
- `logico/`: previsto para uma etapa futura.
- `integrado/`: previsto para a comparação final entre os paradigmas.

## Requisitos

Python 3. Não há dependências externas.

Execute os comandos abaixo na pasta principal do projeto.

## Versão imperativa

Executar:

```bash
python imperativo/triangulo.py
```

Executar os testes:

```bash
python -m unittest testes/test_triangulo.py
```

Validar os 18 casos da Etapa 02:

```bash
python imperativo/validar_etapa02.py
```

## Versão orientada a objetos

Executar:

```bash
python poo/main.py
```

Apresentar os resultados válidos em JSON:

```bash
python poo/main.py --json
```

Executar os testes:

```bash
python -m unittest discover -s poo -p "test_modelo.py"
```

Validar os 18 casos da Etapa 02:

```bash
python poo/validar_etapa02.py
```

## Versão funcional

A implementação prioriza funções puras, composição, funções de primeira classe, funções de alta ordem e dados imutáveis. O núcleo dos cálculos fica separado das operações de entrada e saída.

Executar:

```bash
python funcional/main.py
```

Apresentar cada análise em JSON:

```bash
python funcional/main.py --json
```

Executar os testes, incluindo os 18 casos de referência da Etapa 02:

```bash
python -m unittest funcional.test_funcional -v
```

A identificação dos conceitos funcionais e a reflexão sobre a mudança de perspectiva estão em [funcional/reflexao.md](funcional/reflexao.md).

## Utilização

Informe os três lados, um por vez. O programa aceita ponto ou vírgula como separador decimal.

Digite `s` para realizar outra análise ou `n` para encerrar. Ao final, o programa apresenta a quantidade de tentativas e de análises válidas.

