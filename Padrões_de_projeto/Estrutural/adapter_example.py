from abc import ABC, abstractmethod

# 1. Target (Interface esperada pelo seu projeto Django)
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass

# 3. Adaptee (A classe com a interface incompatível/antiga)
class ServicoEmailAntigo:
    def deliver_message(self, recipient_address, content):
        """Método com nome incompatível."""
        print(f"Serviço Email Antigo: Entregando '{content}' para {recipient_address}")
        # Lógica de envio real aqui

# 4. Adapter
class NotificacaoEmailAdapter(Notificacao):
    """
    Adapta a interface ServicoEmailAntigo para a interface Notificacao esperada.
    """
    def __init__(self, servico_antigo):
        self._servico_antigo = servico_antigo

    def enviar(self, destinatario, mensagem):
        # A tradução acontece aqui!
        self._servico_antigo.deliver_message(destinatario, mensagem)

# --- Uso no código Django (Client) ---

# O código Cliente espera a interface Notificacao
def enviar_alerta(notificacao_service, user_email, alert_message):
    print("Cliente: Preparando para enviar alerta...")
    notificacao_service.enviar(user_email, alert_message)
    print("Cliente: Alerta enviado com sucesso.")

# Instanciando o Adaptado (Serviço Antigo)
servico_antigo = ServicoEmailAntigo()

# Criando o Adaptador para que o Serviço Antigo possa ser usado
adapter = NotificacaoEmailAdapter(servico_antigo)

# O código Cliente usa o Adapter (que implementa Notificacao)
enviar_alerta(adapter, "usuario@exemplo.com", "Sua fatura está pendente.")