Projeto P4 - Sistema de Análise de Triângulos

[P4-ETAPA-01]

[P4-ETAPA-02] Contrato semântico e testes: [testes/casos.md](testes/casos.md).

Este projeto resolve o mesmo problema usando os paradigmas imperativo, orientado a objetos, funcional e lógico. O problema escolhido é analisar um triângulo a partir dos seus três lados.

## Organização

- `docs/`: especificação e decisões do projeto.
- `testes/`: casos de teste e resultados esperados.
- `imperativo/`: primeira implementação em Python.
- `poo/`, `funcional/` e `logico/`: implementações das etapas futuras.
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
