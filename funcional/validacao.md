# Validação da Etapa 06

## Comando executado

Na raiz do projeto:

```bash
python -m unittest funcional.test_funcional -v
```

Resultado obtido: **6 testes aprovados**.

## Cobertura

1. Os 18 casos de referência da Etapa 02 registrados no código anteriormente analisado: 11 trios válidos e 7 rejeitados. Para os válidos, confere classificações, perímetro, área, ângulos e soma de 180°, com tolerância de 0,01 nos valores arredondados de referência.
2. Rejeição de booleanos, quantidade incorreta de lados e falhas numéricas para valores extremos.
3. Preservação da entrada, da sessão inicial e da sessão anterior; contagem de tentativas rejeitadas; resultados em tuplas; repetição determinística da análise.
4. Ordem da composição, conversão com vírgula decimal, entrada ausente, análise em lote e serialização JSON de sucesso e erro.
5. Console em subprocesso: repetição, resposta de continuação inválida, rejeição e resumo.
6. Console com trio incompleto e apresentação JSON.

Os testes utilizam referências fixas, não apenas resultados recalculados pelo próprio núcleo. Isso não equivale a uma prova para todas as entradas numéricas possíveis.

## Limite desta entrega

A manutenção do ambiente removeu o ZIP e os arquivos locais das etapas anteriores. Esta pasta foi implementada usando o código e os 18 casos registrados na análise anterior desta conversa. Os testes acima foram executados sobre a nova implementação; as versões imperativa e POO não foram executadas novamente nesta etapa. O ZIP entregue contém somente a pasta `funcional/`, para ser acrescentada ao repositório existente.
