# Design Patterns em Python/Django

Este repositório documenta a implementação de três padrões de projeto essenciais, escolhidos um de cada categoria (Criacional, Estrutural e Comportamental), com foco na aplicabilidade em projetos **Python** e no *framework* **Django**.

Os códigos de exemplo estão na pasta `design_patterns/`.

---

## Padrões de Projeto Documentados

| Categoria | Padrão | Descrição Breve |
| :---: | :---: | :--- |
| **Criacional** | **Singleton** | Garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a ela. |
| **Estrutural** | **Adapter** | Permite que objetos com interfaces incompatíveis trabalhem juntos, atuando como um tradutor. |
| **Comportamental** | **Strategy** | Define uma família de algoritmos e os torna intercambiáveis, delegando a lógica para classes específicas. |

---

## I. Padrão Criacional: Singleton

O **Singleton** é usado para garantir que uma classe tenha apenas uma instância e fornecer um ponto de acesso global a ela. É ideal para gerenciar recursos compartilhados como configurações globais ou conexões de log.

* **Referência:** [Singleton - Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/singleton)

### Problema Resolvido
O problema de ter múltiplas instâncias de uma classe que gerencia um recurso centralizado (como um Objeto de Configuração ou um Pool de Conexões), o que pode levar a inconsistências de dados e uso ineficiente de recursos.

### Solução
A própria classe se encarrega de controlar a criação de instâncias. Ela oculta o construtor e expõe um método de acesso estático (`__new__` em Python) que sempre retorna a mesma instância armazenada em cache.

### Diagrama UML Conceitual



### Exemplo de Código (no `design_patterns/creational/singleton_example.py`)

A implementação em Python utiliza o método mágico `__new__` para controlar a criação da instância e garantir que apenas uma seja criada.

```python
# O código de exemplo em Python/Django se encontra no arquivo:
# design_patterns/creational/singleton_example.py

class GlobalConfigurationManager:
    """O Singleton para gerenciar um conjunto de configurações globais."""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            # Garante que a inicialização (init) ocorra apenas na primeira vez
            cls._instance = super(GlobalConfigurationManager, cls).__new__(cls)
            cls._instance.settings = {}
            print("Configuração Global inicializada.")
        return cls._instance

    # ... (Métodos de negócio como load_settings, get_setting)

# Demonstração: config1 e config2 são o mesmo objeto
config1 = GlobalConfigurationManager()
config2 = GlobalConfigurationManager()
# Saída: São o mesmo objeto? True
print(f"São o mesmo objeto? {config1 is config2}")