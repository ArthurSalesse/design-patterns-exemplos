from abc import ABC, abstractmethod
from typing import List

# 1. Component (Interface Base)
class OrganizationalComponent(ABC):
    """Interface comum para funcionários (Folhas) e departamentos (Compostos)."""
    @abstractmethod
    def get_salary_cost(self) -> float:
        pass
    
    @abstractmethod
    def display_structure(self, indent: str = ""):
        pass

# 2. Leaf (Folha)
class Employee(OrganizationalComponent):
    """Representa um objeto Folha (elemento indivisível)."""
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        
    def get_salary_cost(self) -> float:
        return self.salary
        
    def display_structure(self, indent: str = ""):
        print(f"{indent}Funcionario: {self.name} (Salário: {self.salary})")

# 3. Composite (Composto)
class Department(OrganizationalComponent):
    """Representa um objeto Composto (contém outros componentes)."""
    def __init__(self, name: str):
        self.name = name
        self._children: List[OrganizationalComponent] = []
        
    def add(self, component: OrganizationalComponent):
        self._children.append(component)
        
    def get_salary_cost(self) -> float:
        """Soma o custo salarial de todos os filhos (recursivamente)."""
        total = sum(child.get_salary_cost() for child in self._children)
        return total
        
    def display_structure(self, indent: str = ""):
        print(f"{indent}Departamento: {self.name}")
        for child in self._children:
            child.display_structure(indent + "  ")

# --- Uso (Gerenciamento de Custos Salariais) ---
joao = Employee("João Silva", 5000)
maria = Employee("Maria Costa", 7000)
dev_team = Department("Time de Desenvolvimento")
dev_team.add(joao)
dev_team.add(maria)

company = Department("Tecnologia S/A - Total")
company.add(dev_team)

print(f"Custo Salarial do Time de Dev: {dev_team.get_salary_cost()}") 
print(f"Custo Salarial Total da Empresa: {company.get_salary_cost()}")