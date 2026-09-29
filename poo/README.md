# Implementação orientada a objetos

[P4-ETAPA-04]

Sistema de Análise de Triângulos em Python 3, sem pacotes externos. Execute os comandos abaixo na pasta principal do repositório.

```text
python poo/main.py
```

Digite os lados A, B e C, um por pergunta. Para o exemplo 3, 4 e 5, o resultado é escaleno, retângulo, perímetro 12 e área 6. Digite s para outra análise ou n para encerrar.

Para demonstrar o segundo apresentador:

```text
python poo/main.py --json
```

A opção troca a formatação de cada análise válida para JSON, mantendo perguntas, erros e resumo no terminal. Não é uma API nem um arquivo JSON completo.

Para validar:

```text
python poo/validar_etapa02.py
python -m unittest discover -s poo -p test_modelo.py
```

No Windows, se necessário, substitua `python` por `py`.

## Arquivos

- `modelo.py`: domínio e sessão de análise.
- `apresentacao.py`: interface abstrata e apresentações em texto e JSON.
- `main.py`: aplicação interativa.
- `validar_etapa02.py`: os 18 casos do contrato.
- `test_modelo.py`: testes de encapsulamento, histórico, polimorfismo e execução no terminal.
- `reflexão.md`: reflexão obrigatória e decisões de modelagem.
- `validacao.md`: registro de resultados.
