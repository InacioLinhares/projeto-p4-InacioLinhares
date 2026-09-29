[P4-ETAPA-01]

[P4-ETAPA-02] Contrato semântico e testes: [testes/casos.md](testes/casos.md).

[P4-ETAPA-03] Implementação imperativa em Python: [código](imperativo/triangulo.py), [decisões](imperativo/decisoes.md) e [validação](imperativo/validacao.md).

[P4-ETAPA-04] Implementação orientada a objetos em Python: [instruções](poo/README.md), [reflexão](poo/reflexão.md) e [validação](poo/validacao.md).

Este projeto resolve o mesmo problema usando os paradigmas imperativo, orientado a objetos, funcional e lógico. O problema escolhido é analisar um triângulo a partir dos seus três lados.

## Organização

- `docs/`: especificação e decisões do projeto.
- `testes/`: casos de teste e resultados esperados.
- `imperativo/`: primeira implementação em Python.
- `poo/`: implementação orientada a objetos e reflexão da Etapa 04.
- `funcional/` e `logico/`: implementações das etapas futuras.
- `integrado/`: comparação final entre os paradigmas.

## Como executar a versão atual

No terminal, entre na pasta `imperativo` e execute:

```powershell
python triangulo.py
```

## Como executar os testes

Na pasta principal do projeto, execute:

```powershell
python -m unittest testes/test_triangulo.py
```

Para validar os 18 casos da Etapa 02 na implementação imperativa:

```powershell
python imperativo/validar_etapa02.py
```

O programa permite repetir análises e mostra contadores ao encerrar. Digite `s` para continuar ou `n` para sair. Não há dependências externas.

## Versão orientada a objetos

Na pasta principal, execute:

```powershell
python poo/main.py
python poo/validar_etapa02.py
python -m unittest discover -s poo -p test_modelo.py
```

Use `python poo/main.py --json` para trocar o apresentador dos resultados válidos. O modelo matemático permanece o mesmo.

