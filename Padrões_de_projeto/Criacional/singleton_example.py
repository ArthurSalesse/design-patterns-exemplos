# Exemplo de uso em Python para configurar as configurações de um aplicativo Django
class GlobalConfigurationManager:
    """
    O Singleton para gerenciar um conjunto de configurações globais.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalConfigurationManager, cls).__new__(cls)
            # Inicialização da instância (só ocorre uma vez)
            cls._instance.settings = {}
            print("Configuração Global inicializada.")
        return cls._instance

    def load_settings(self, new_settings):
        self.settings.update(new_settings)
        print("Configurações carregadas.")

    def get_setting(self, key):
        return self.settings.get(key, "Configuração não encontrada")

# --- Uso ---
# Acesso à primeira instância
config1 = GlobalConfigurationManager()
config1.load_settings({"THEME_COLOR": "blue", "DEBUG_MODE": True})

# Acesso à segunda 'instância' (na verdade, é o mesmo objeto)
config2 = GlobalConfigurationManager()

# As instâncias são as mesmas
print(f"São o mesmo objeto? {config1 is config2}") # Saída: True
print(f"Cor do Tema (Config 2): {config2.get_setting('THEME_COLOR')}") # Saída: blue

# Se config2 alterar algo, config1 verá a mudança
config2.load_settings({"THEME_COLOR": "red"})
print(f"Nova Cor do Tema (Config 1): {config1.get_setting('THEME_COLOR')}") # Saída: red