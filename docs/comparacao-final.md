# ETAPA 05 — Comparação entre Imperativo e POO

**Autor:** Inácio Linhares  
**Projeto:** Sistema de Análise de Triângulos  
**Identificação da etapa:** `[P4-ETAPA-05]`

## 1. Base da comparação

Esta análise utiliza o código efetivamente produzido: `imperativo/triangulo.py`, `poo/modelo.py`, `poo/apresentacao.py`, `poo/main.py` e os testes existentes. O sistema recebe três lados, verifica se formam um triângulo e calcula classificações, perímetro, área e ângulos internos.

A versão imperativa organiza o trabalho em funções e controla a sessão em `main()`. A versão orientada a objetos utiliza `Triangulo`, `SessaoAnalise`, `AplicacaoConsole` e a hierarquia de apresentadores. As duas versões usam Python. A POO também contém instruções imperativas, como atribuições, condicionais e laços; a principal diferença está na organização dos dados e das responsabilidades.

## 2. Comparação dos aspectos solicitados

### 2.1. Representação do estado

Na versão imperativa, os lados são valores passados como parâmetros `a`, `b` e `c`. `analisar_triangulo()` monta um dicionário com os resultados. O estado da sessão fica nas variáveis locais `continuar`, `tentativas` e `validos`, dentro de `main()`.

Na POO, `Triangulo` reúne os lados nos atributos `_a`, `_b` e `_c`. Os resultados são calculados por propriedades, como `area` e `perimetro`, em vez de armazenados em um dicionário. `SessaoAnalise` mantém `_tentativas` e `_triangulos`; `validos` é obtido pelo tamanho da lista. Essa versão também armazena o histórico dos triângulos aceitos, recurso que a imperativa não possui.

### 2.2. Mutabilidade

Na imperativa, números são imutáveis em Python, mas as variáveis podem receber novos valores. Os contadores são reatribuídos e o dicionário de resultados é mutável. Em `classificar_angulos()`, as trocas entre `menor`, `medio` e `maior` alteram apenas as variáveis locais, sem modificar os argumentos do chamador.

Na POO, `Triangulo` usa `@dataclass(frozen=True)`, que impede a atribuição comum aos seus atributos após a construção. Para representar outras medidas, cria-se outro objeto. Isso não torna toda a implementação imutável: `SessaoAnalise.analisar()` incrementa `_tentativas` e acrescenta objetos a `_triangulos`. A propriedade `triangulos` devolve uma tupla, evitando que o cliente altere a lista interna pela coleção retornada. O prefixo `_` indica uso interno por convenção, sem constituir uma barreira absoluta de acesso em Python.

### 2.3. Fluxo de controle

Na imperativa, `main()` conduz diretamente a sequência de leitura, validação, análise, exibição e repetição. `while continuar` controla a sessão e os retornos das funções orientam as decisões.

Na POO, `AplicacaoConsole.executar()` mantém uma sequência semelhante com `while True`, mas delega a análise à sessão e a formatação ao apresentador. `ValueError` determina o caminho de rejeição. A orientação a objetos não eliminou o fluxo sequencial: distribuiu responsabilidades entre colaboradores.

### 2.4. Decomposição do problema

A imperativa divide o problema por operações: `validar_entrada()`, `classificar_lados()`, `classificar_angulos()`, `calcular_area()` e `calcular_angulo()`.

A POO divide o sistema por responsabilidades: `Triangulo` representa e valida a entidade matemática; `SessaoAnalise` registra tentativas e histórico; `AplicacaoConsole` coordena a interação; os apresentadores formatam resultados. As fórmulas passaram a integrar o comportamento de `Triangulo`.

### 2.5. Reutilização

As funções imperativas de cálculo já podem ser importadas e chamadas sem utilizar o terminal. Portanto, reutilização não é exclusiva da POO.

Na versão orientada a objetos, `Triangulo` e `SessaoAnalise` podem ser usados por outra interface porque `modelo.py` não utiliza `input()` nem `print()`. Os apresentadores também retornam texto sem imprimi-lo. Um mesmo objeto pode ser apresentado como texto ou JSON, reutilizando o modelo e a lógica da sessão.

### 2.6. Manutenção

A imperativa concentra a implementação em um arquivo, facilitando a localização do código em um programa pequeno. Entretanto, `main()` reúne interação, contadores e coordenação, enquanto consumidores do resultado dependem das chaves do dicionário.

Na POO, a separação entre modelo, apresentação e aplicação facilita localizar alterações por responsabilidade. Uma mudança na apresentação JSON fica em `ApresentadorJSON`; uma regra matemática fica em `Triangulo`. Em contrapartida, compreender o fluxo completo exige acompanhar chamadas entre arquivos e classes. A versão imperativa também poderia ser dividida em módulos: essa vantagem decorre da arquitetura implementada, e não apenas do uso de classes.

### 2.7. Facilidade de extensão

A POO já demonstra uma extensão concreta: `ApresentadorTexto` e `ApresentadorJSON` implementam `formatar()`. A aplicação recebe o apresentador no construtor e a opção `--json` seleciona qual usar. Um novo formato poderia implementar essa interface e ser conectado na inicialização sem mudar os cálculos.

Na imperativa, seria possível criar uma função de formatação JSON e selecionar qual função chamar. Para extensões simples, isso exigiria menos estrutura. Para várias apresentações e histórico reutilizável, a organização atual da POO oferece pontos de extensão mais explícitos. Não foi implementada uma hierarquia de tipos de triângulo nem uma interface gráfica.

### 2.8. Tratamento de erros

Na imperativa, `validar_entrada()` retorna uma mensagem de erro ou `None`. Já `analisar_triangulo()` retorna `None` quando as medidas são inválidas. O chamador deve interpretar esses retornos. As funções individuais de cálculo não validam os lados por conta própria, podendo ser chamadas com valores inadequados.

Na POO, `Triangulo.__post_init__()` lança `ValueError` para medidas ausentes, não numéricas, não finitas, não positivas ou que violem a desigualdade triangular. Assim, a construção normal de um objeto exige lados válidos. `AplicacaoConsole.executar()` captura essa exceção e apresenta a mensagem.

Em `SessaoAnalise.analisar()`, a tentativa é contada antes da construção do objeto; se a validação falhar, o histórico não recebe um triângulo, mas a tentativa permanece registrada. Ambas as interfaces tratam `EOFError` e `KeyboardInterrupt`. Na POO, a mensagem de interrupção é genérica e também pode aparecer quando a interrupção ocorre na pergunta de continuação, após um trio já analisado.

### 2.9. Efeitos colaterais

As funções matemáticas da imperativa não realizam entrada e saída nem alteram dados externos. Montar um novo dicionário local não modifica o estado do chamador. Os efeitos observáveis concentram-se em `input()` e `print()` durante a interação.

Na POO, as propriedades matemáticas e `formatar()` também não alteram o estado do domínio. Porém, `SessaoAnalise.analisar()` modifica o estado de um objeto já existente: atualiza tentativas e histórico, inclusive contando uma tentativa rejeitada. `AplicacaoConsole` realiza a entrada e saída. Objetos, portanto, não eliminam efeitos colaterais; permitem localizar e encapsular algumas mudanças de estado.

### 2.10. Facilidade para testar

Na imperativa, é simples chamar `analisar_triangulo(3, 4, 5)` e conferir o dicionário. `testes/test_triangulo.py` contém quatro testes que verificam classificações, perímetro, área e entradas inválidas.

Na POO, os testes de `poo/test_modelo.py` verificam imutabilidade, histórico e contagem de rejeições, apresentadores intercambiáveis e execução do console em um subprocesso. O modelo independente da interface permite testar regras sem simular teclado. Também há mais contratos a verificar, pois a versão acrescentou histórico e apresentação JSON.

Cada implementação possui ainda um `validar_etapa02.py` que verifica os mesmos 18 casos de referência. Ambas são testáveis; as diferenças observadas estão nas interfaces e funcionalidades cobertas pelos testes existentes.

### 2.11. Organização do código

A imperativa tem um módulo principal com funções de validação, cálculo, leitura e exibição. A estrutura é compacta e adequada ao tamanho do problema.

A POO distribui a implementação em `modelo.py`, `apresentacao.py` e `main.py`. Usa composição na aplicação, agregação de triângulos na sessão e herança na hierarquia dos apresentadores. Essa organização explicita responsabilidades, mas adiciona classes, propriedades, construtores e dependências entre módulos.

### 2.12. Complexidade

Para uma análise com três lados, as operações matemáticas e de validação têm quantidade fixa de trabalho: a complexidade é O(1), considerando operações numéricas de custo constante. A POO ordena três lados com `sorted()`, enquanto a imperativa usa até três trocas; como a quantidade de lados é sempre três, isso não muda a complexidade assintótica.

Para n tentativas, o trabalho de análise das duas versões é O(n), desconsiderando o tempo de espera do usuário. A imperativa não guarda o histórico e mantém memória auxiliar O(1). A POO armazena k triângulos válidos, usando O(k) de memória. A propriedade `triangulos` cria uma tupla com esse histórico e custa O(k) quando acessada.

A POO acrescenta custo de construção dos objetos, chamadas de métodos, validação e armazenamento do histórico. Suas propriedades recalculam resultados a cada acesso, sem cache; a imperativa calcula os resultados ao montar o dicionário. Isso pode produzir diferenças de tempo, mas não foi realizado um benchmark. Não é correto concluir que uma versão é mais rápida apenas por ser imperativa ou orientada a objetos, especialmente porque elas têm funcionalidades diferentes.

## 3. Respostas às seis perguntas

### 1. Qual problema ficou mais fácil de expressar de forma imperativa?

O procedimento de realizar uma análise isolada ficou mais direto: receber três números, validar, calcular e retornar um dicionário. As fórmulas de área e ângulos também são naturalmente expressas como funções que recebem valores e retornam resultados. Para apenas calcular a área de um triângulo já validado, `calcular_area(a, b, c)` exige menos estrutura que construir um objeto e acessar uma propriedade.

### 2. Qual problema ficou mais fácil de expressar utilizando orientação a objetos?

Representar um triângulo válido com comportamentos associados, manter uma sessão com histórico e permitir diferentes formatos de apresentação. `Triangulo` reúne medidas e operações, `SessaoAnalise` concentra o histórico e os contadores, e os apresentadores oferecem a mesma operação `formatar()` para duas saídas diferentes.

### 3. Onde a orientação a objetos realmente trouxe vantagem?

A vantagem mais concreta está na preservação das regras de construção e da estabilidade dos lados: `__post_init__()` valida o objeto e `frozen=True` impede sua alteração por atribuição comum. Outra vantagem implementada é trocar a apresentação de texto por JSON usando o apresentador recebido pela aplicação. A sessão também concentra o histórico e deriva a quantidade de válidos da própria coleção, evitando manter um contador separado para esse total.

### 4. Em quais situações a utilização de objetos acrescentou complexidade desnecessária?

Para analisar um único trio e mostrar uma única saída, a estrutura de sessão, aplicação e apresentadores seria maior do que o necessário. Uma função pode realizar essa tarefa diretamente. Se existisse apenas uma apresentação, a classe abstrata `Apresentador` poderia ser dispensada; neste código, ela tem utilidade porque existem dois formatos. `_angulo()` é um método estático sem acesso ao estado do objeto e poderia continuar sendo uma função auxiliar. A organização em classes ajuda o sistema completo, mas não simplifica cada fórmula individual.

### 5. Que partes do problema praticamente não mudaram entre as duas implementações?

Permaneceram as regras de entrada, a desigualdade triangular, a classificação pelos lados, a comparação dos quadrados dos lados, a fórmula de Heron, o perímetro e a lei dos cossenos. Ambas usam `isclose()` e limitam o cosseno ao intervalo [-1, 1] antes de chamar `acos()`. A leitura aceita vírgula como separador decimal e a interação permite repetir análises.

Há mudanças de implementação sem remodelação matemática: as trocas explícitas foram substituídas por `sorted()`, e o retorno dos três ângulos passou de campos separados no dicionário para uma tupla. Na imperativa, `isclose()` usa `abs_tol=TOLERANCIA` e o `rel_tol` padrão do Python, que é 1e-9; a POO explicita ambos como 1e-9. Portanto, as tolerâncias utilizadas nessas comparações são equivalentes.

### 6. Que partes precisaram ser completamente remodeladas?

A representação dos dados e a distribuição das responsabilidades foram remodeladas. Os parâmetros e o dicionário deram lugar ao objeto `Triangulo` e suas propriedades. A validação passou de uma função que retorna um indicador de erro para uma verificação obrigatória na construção, com exceções. Os contadores locais passaram para `SessaoAnalise`, que acrescentou histórico. A exibição direta foi reorganizada em apresentadores que retornam texto, e a coordenação passou de `main()` para `AplicacaoConsole.executar()`.

Essas mudanças remodelaram a estrutura e os contratos de uso; as fórmulas e as regras matemáticas não precisaram ser completamente reescritas.

## 4. Validação realizada

Os comandos abaixo foram executados na raiz do projeto durante a preparação desta etapa:

```bash
python -m unittest discover -s testes -p 'test_*.py'
python -m unittest discover -s poo -p 'test_*.py'
python imperativo/validar_etapa02.py
python poo/validar_etapa02.py
```

Resultado: 4 testes unitários aprovados na imperativa, 4 na POO e 18/18 casos de referência aprovados em cada implementação. Essa verificação sustenta a concordância para os casos testados, sem provar correção para toda entrada numérica possível. As duas versões ainda usam aritmética de ponto flutuante e podem exigir tratamento adicional para medidas extremas; validar lados finitos não garante que todos os cálculos intermediários permaneçam finitos.

## 5. Conclusão

A implementação imperativa oferece uma solução compacta e direta para os cálculos e o procedimento de análise. A POO organiza melhor as responsabilidades que foram acrescentadas: objeto válido e imutável, histórico da sessão e formatos de apresentação intercambiáveis. O benefício principal está na estrutura do sistema e nos contratos de uso, enquanto o núcleo matemático permanece equivalente. A escolha depende da necessidade de evolução do projeto, e não de uma superioridade universal de um paradigma.

## 6. Entrega e tag

Este documento identifica a Etapa 05, mas escrever `[P4-ETAPA-05]` no Markdown não cria uma tag Git. O ZIP fornecido não contém o histórico `.git`; a tag deve ser criada e enviada no repositório original após registrar a análise. Os comandos abaixo usam a alternativa sem colchetes, sujeita ao esclarecimento com o professor:

```bash
git add docs/comparacao-final.md README.md
git commit -m "Etapa 05: compara implementações imperativa e POO"
git tag "P4-ETAPA-05"
git push origin HEAD
git push origin "P4-ETAPA-05"
```

**Atenção:** Git não permite `[` em nomes de tags. Assim, o identificador literal pedido no enunciado não é um nome de tag Git válido. É necessário esclarecer esse detalhe com o professor. Se os colchetes forem apenas a notação da etapa, os comandos acima utilizam a tag `P4-ETAPA-05`. Não foi criada nem publicada uma tag nesta entrega.

