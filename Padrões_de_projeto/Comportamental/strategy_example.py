from abc import ABC, abstractmethod

# 1. Strategy (Interface Comum)
class ExportStrategy(ABC):
    """
    Interface para todas as estratégias de exportação de dados.
    """
    @abstractmethod
    def export(self, data):
        pass

# 2. Concrete Strategies (Implementações específicas)
class ExportJSONStrategy(ExportStrategy):
    def export(self, data):
        # Em Django, isso seria a lógica para Serialização JSON
        print("Exportando dados para formato JSON...")
        return f"{{'dados': {data}}}"

class ExportCSVStrategy(ExportStrategy):
    def export(self, data):
        # Em Django, isso seria a lógica para Serialização CSV
        print("Exportando dados para formato CSV...")
        return f"col1,col2\n{data[0]}, {data[1]}" # Exemplo simples

# 3. Context
class DataExporter:
    """
    O Contexto mantém uma referência à estratégia e a executa.
    """
    def __init__(self, strategy: ExportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        self._strategy = strategy
        
    def export_data(self, data):
        print("\nContexto: Executando a exportação...")
        result = self._strategy.export(data)
        return result

# --- Uso no código Django ---
dataset = ["ValorA", "ValorB"]

# 1. Estratégia inicial: JSON
exporter = DataExporter(ExportJSONStrategy())
output = exporter.export_data(dataset)
print(f"Resultado:\n{output}")

# 2. Mudança de estratégia em tempo de execução: CSV
exporter.set_strategy(ExportCSVStrategy())
output = exporter.export_data(dataset)
print(f"Resultado:\n{output}")