# Design Patterns em Python/Django 

Este repositório documenta a implementação de três padrões de projeto essenciais, escolhidos um de cada categoria (Criacional, Estrutural e Comportamental), com foco na aplicabilidade em projetos **Python** e no *framework* **Django**.

Os códigos de exemplo e a implementação funcional inspirada em cenários reais estão na pasta `Padroões_de_projeto/`.

---

## Padrões de Projeto Documentados

| Categoria | Padrão | Propósito | Referência (Refactoring Guru) |
| :---: | :---: | :--- | :--- |
| **Criacional** | **Prototype** | Cria objetos por meio da cópia de um objeto existente, evitando acoplamento. | [Prototype](https://refactoring.guru/pt-br/design-patterns/prototype) |
| **Estrutural** | **Composite** | Compõe objetos em estruturas de árvore e permite que os clientes tratem objetos individuais e composições de objetos de forma uniforme. | [Composite](https://refactoring.guru/pt-br/design-patterns/composite) |
| **Comportamental** | **Visitor** | Permite adicionar **novas operações** a hierarquias de objetos existentes sem modificar as classes desses objetos. | [Visitor](https://refactoring.guru/pt-br/design-patterns/visitor) |

---

## I. Padrão Criacional: Prototype 

O **Prototype** (Protótipo) é um padrão criacional que permite que você crie novos objetos copiando um objeto existente, chamado de protótipo.

* **Referência:** [Prototype - Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/prototype)

### Problema Resolvido
O problema de ter que re-inicializar objetos complexos com a mesma configuração várias vezes ou quando a criação de um novo objeto é custosa em termos de recursos. Evita o acoplamento ao cliente, pois ele não precisa saber a classe exata do objeto que está clonando.

### Solução
A classe que se deseja clonar (o Protótipo) implementa um método de clonagem. Em Python, isso é frequentemente feito através do protocolo `copy.deepcopy()`. O cliente solicita uma cópia ao objeto protótipo em vez de usar o construtor da classe. O objeto clonado é um novo objeto com os mesmos estados do original.

### Diagrama UML Conceitual


[Image of the Prototype design pattern UML diagram]


### Exemplo de Código (no `Padroões_de_projeto/criacional/prototype_example.py`)

**Exemplo Funcional:** Clonagem de Objetos de Tarefa (*Tasks*) em um Sistema de Gerenciamento de Projetos, onde a clonagem é usada para criar tarefas baseadas em um modelo pré-configurado.



## II. Padrão Estrutural:  Composite

O **Composite** é um padrão de projeto estrutural que permite que você componha objetos em estruturas de árvores e então trabalhe com essas estruturas como se elas fossem objetos individuais.

* **Referência:** [Composite - Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/composite)

### Problema Resolvido
Usar o padrão Composite faz sentido apenas quando o modelo central de sua aplicação pode ser representada como uma árvore.

A dificuldade em gerenciar estruturas hierárquicas (como árvores, menus, ou organogramas) onde você tem objetos simples (Folhas) e contêineres de objetos (Compostos). O código cliente deve ser capaz de interagir com qualquer um deles sem saber se está lidando com um grupo ou um item único.

### Solução

Define-se uma interface comum (Componente) implementada tanto por objetos simples (que não têm filhos, Folhas) quanto por objetos compostos (que podem ter filhos, Compostos). Os Compostos delegam o trabalho aos seus filhos e agregam os resultados, permitindo que o cliente trate toda a estrutura de forma uniforme usando a interface Componente.

### Diagrama UML Conceitual


[Image of the Prototype design pattern UML diagram]


### Exemplo de Código (no `Padroões_de_projeto/Estrutural/composite_example.py`)

**Exemplo Funcional:** Clonagem de Objetos de Tarefa (*Tasks*) em um Sistema de Gerenciamento de Projetos, onde a clonagem é usada para criar tarefas baseadas em um modelo pré-configurado.



## III. Padrão Comportamental:  Visitor

O Visitor (Visitante) é um padrão comportamental que permite que você separe algoritmos da estrutura de objetos em que eles operam.

* **Referência:** [Composite - Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/visitor)

### Problema Resolvido

A necessidade de adicionar novas operações (comportamentos) a classes de objetos existentes (Elementos) sem ter que modificar o código-fonte dessas classes. Isso evita a poluição das classes Elemento com operações que mudam frequentemente.

### Solução

Cria-se uma interface Visitor com métodos visit para cada tipo de Elemento concreto. As classes de Elemento, por sua vez, implementam um método accept que aceita o Visitor e o direciona para o método visit correto. O comportamento do sistema é estendido adicionando-se novos Visitors, e não alterando os Elementos.usando a interface Componente.

### Diagrama UML Conceitual


[Image of the Prototype design pattern UML diagram]


### Exemplo de Código (no `Padroões_de_projeto/Comportamental/visitor_example.py`)

**Exemplo Funcional:** Adicionar Operações de Relatório (Cálculo de Imposto) a diferentes tipos de Pedidos (Orders).

