from abc import ABC, abstractmethod

# --- ELEMENTOS (Os objetos que aceitam Visitors) ---

class OrderElement(ABC):
    """Interface Elemento: Declara um método accept."""
    @abstractmethod
    def accept(self, visitor):
        pass

class StandardOrder(OrderElement):
    """Elemento Concreto 1 (Pedido Padrão)"""
    def __init__(self, price: float):
        self.price = price
        
    def accept(self, visitor):
        # Chama o método visit específico no Visitor
        return visitor.visit_standard_order(self)
        
    def get_price(self):
        return self.price

class PremiumOrder(OrderElement):
    """Elemento Concreto 2 (Pedido Premium)"""
    def __init__(self, price: float):
        self.price = price
        
    def accept(self, visitor):
        # Chama o método visit específico no Visitor
        return visitor.visit_premium_order(self)

    def get_price(self):
        return self.price

# --- VISITORS (As novas operações) ---

class OrderVisitor(ABC):
    """Interface Visitor: Declara um método visit para cada tipo de Elemento."""
    @abstractmethod
    def visit_standard_order(self, element: StandardOrder):
        pass

    @abstractmethod
    def visit_premium_order(self, element: PremiumOrder):
        pass

class TaxCalculator(OrderVisitor):
    """Visitor Concreto 1: Calcula imposto de forma diferente para cada tipo de pedido."""
    def visit_standard_order(self, element: StandardOrder):
        tax = element.get_price() * 0.10
        print(f"Imposto Padrão (10%): R$ {tax:.2f}")
        return tax

    def visit_premium_order(self, element: PremiumOrder):
        tax = element.get_price() * 0.05  # Imposto menor para Premium
        print(f"Imposto Premium (5%): R$ {tax:.2f}")
        return tax

# --- Uso (Cálculo de Imposto Diferenciado) ---
orders = [
    StandardOrder(price=100.00),
    PremiumOrder(price=200.00),
]

tax_visitor = TaxCalculator()
total_tax = 0.0

print("--- Executando Visitor: TaxCalculator ---")
for order in orders:
    # O Elemento aceita o Visitor e o Visitor executa a lógica
    total_tax += order.accept(tax_visitor)

print(f"\nImposto Total a ser recolhido: R$ {total_tax:.2f}")