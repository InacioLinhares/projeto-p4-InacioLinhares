# Reflexão sobre a modelagem orientada a objetos

[P4-ETAPA-04]

## Como meu modelo mudou ao passar do paradigma imperativo para o orientado a objetos

Na Etapa 03, a solução era organizada em torno de uma sequência de operações: ler medidas, validar, calcular, preencher um dicionário e imprimir. Na Etapa 04, organizei a solução em torno de objetos com responsabilidades próprias. O objeto `Triangulo` representa uma figura válida, a `SessaoAnalise` mantém as análises realizadas e a `AplicacaoConsole` coordena a interação. O resultado matemático permanece o mesmo, mas a responsabilidade por proteger os dados passa para o objeto de domínio.

A mudança principal não é colocar as funções anteriores dentro de uma classe. Antes, os três números circulavam entre subprogramas e a validade precisava ser verificada pelo fluxo. Agora, a construção de um `Triangulo` rejeita medidas incorretas. As propriedades geométricas pertencem ao objeto válido, e os componentes que o recebem não precisam repetir a validação. A implementação não importa nem chama o código imperativo.

## Representação do estado

`Triangulo` guarda somente os três lados, preservando a ordem A, B e C. Perímetro, área, classificações e ângulos são propriedades calculadas, evitando armazenar informações redundantes que poderiam ficar desatualizadas.

A classe é uma `dataclass` congelada: depois da construção, atribuições normais aos atributos são bloqueadas. Para analisar outras medidas, crio outro objeto. Isso mantém a condição de que um triângulo construído possui medidas válidas. A imutabilidade do objeto de domínio não impede que a solução seja orientada a objetos.

`SessaoAnalise` possui estado mutável: contador de tentativas e lista de triângulos aceitos. Cada trio completo incrementa o contador; somente uma construção bem-sucedida adiciona um triângulo à lista. Uma tentativa inválida não insere um objeto inconsistente. Esse histórico pertence à sessão, não à figura geométrica.

## Responsabilidades

| Componente | Responsabilidade |
|---|---|
| `Triangulo` | Proteger a validade dos lados e fornecer propriedades geométricas. |
| `SessaoAnalise` | Registrar tentativas e agregar os triângulos aceitos. |
| `Apresentador` | Definir o contrato de formatação de um triângulo. |
| `ApresentadorTexto` | Produzir texto legível com valores em duas casas decimais. |
| `ApresentadorJSON` | Produzir uma representação JSON dos mesmos resultados. |
| `AplicacaoConsole` | Ler entradas, tratar rejeições e interrupções, controlar a interação e exibir saídas. |

Os cálculos não usam `input` ou `print`. A formatação retorna uma string; é a aplicação que a imprime. Dessa forma, os efeitos de entrada e saída ficam concentrados na interface.

## Relacionamento entre componentes

A aplicação cria e possui uma sessão, caracterizando composição. Recebe um apresentador pelo construtor, caracterizando agregação e permitindo escolher a apresentação sem alterar os cálculos. A sessão agrega referências a objetos `Triangulo`; eles também podem ser consultados por outros componentes independentemente da sessão.

O fluxo é: a aplicação lê o trio, solicita a análise à sessão, a sessão constrói o triângulo e o registra se válido, e a aplicação entrega esse objeto ao apresentador. Em caso de `ValueError`, a aplicação exibe o motivo da rejeição e continua sem um resultado geométrico.

## Encapsulamento

Os atributos internos usam o prefixo `_`, uma convenção de Python, e o acesso público é feito por propriedades e métodos. Esse prefixo não é uma barreira de segurança. A classe congelada bloqueia alterações usuais nos lados, mas não pretende impedir manipulação deliberada dos mecanismos internos da linguagem.

O histórico é exposto como tupla, sem devolver a lista interna da sessão. O cliente pode consultar os objetos, mas não pode adicionar ou remover análises pela coleção retornada. Contadores são expostos por propriedades sem métodos públicos para atribuir valores arbitrários.

Exemplo: `Triangulo(3, 4, 5)` cria um objeto válido; `Triangulo(1, 2, 3)` lança uma exceção. Assim, a validade é uma condição da existência do objeto, não apenas uma decisão na tela.

## Reutilização e abstração

Uma interface diferente pode reutilizar `Triangulo` e `SessaoAnalise` sem o terminal. O chamador consulta `triangulo.area` sem conhecer a fórmula de Heron. O apresentador consulta propriedades do objeto sem acessar as regras de validação.

Os mesmos 18 casos da Etapa 02 foram usados, com referências fixas e tolerância de 0,01. Os testes da versão orientada a objetos instanciam o modelo diretamente. O contrato define os valores observáveis, sem exigir que a interface interna seja igual à da versão imperativa.

## Polimorfismo e decisão sobre herança

Não criei subclasses `Equilatero`, `Isosceles` e `Escaleno`: são classificações determinadas pelas medidas, e compartilham as mesmas operações. Uma hierarquia dessas figuras duplicaria regras e exigiria decidir a subclasse antes de construir o objeto. Um único `Triangulo` encapsula melhor esse domínio.

A herança aparece onde há uma variação real: apresentação. `ApresentadorTexto` e `ApresentadorJSON` implementam a classe abstrata `Apresentador`. A aplicação chama o mesmo método `formatar(triangulo)` sem verificar qual implementação recebeu. Isso demonstra polimorfismo e permite duas saídas utilizáveis, selecionadas por `--json`.

A classe abstrata foi escolhida para explicitar a interface comum; também seria possível usar um protocolo ou tipagem dinâmica de Python. A aplicação recebe o colaborador por composição/agregação, em vez de herdar comportamento de apresentação.

## Extensão do sistema

Para acrescentar outro formato, posso implementar outro apresentador e fornecê-lo à aplicação. Não é necessário modificar `Triangulo` ou `SessaoAnalise`. Uma interface gráfica poderá usar o mesmo modelo, substituindo a aplicação de terminal. Novas propriedades geométricas pertencem a `Triangulo`; persistência do histórico, se futuramente necessária, deve ficar em um componente próprio.

A versão atual não implementa interface gráfica, banco de dados ou figuras diferentes, mantendo o escopo das etapas anteriores.

## Precisão e limitações

São mantidas a desigualdade triangular estrita, a tolerância relativa e absoluta de 10⁻⁹ nas classificações e a ordem dos ângulos correspondente aos lados. As entradas não numéricas, ausentes, não finitas e não positivas são rejeitadas antes dos cálculos. A interface aceita ponto ou vírgula decimal.

Como na versão anterior, números de ponto flutuante possuem limites: magnitudes extremas podem causar transbordamento ou perda de precisão. Os testes aprovados representam os casos definidos, não uma prova de correção para todos os números reais.
