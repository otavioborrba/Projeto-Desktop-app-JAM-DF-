from modelos.pessoas import Pessoa

from .notificador import Notificador


class WhatsAppNotificador(Notificador):
    def enviar(self, destinatario: Pessoa, mensagem: str) -> None:
        print(f"[WhatsApp para {destinatario.telefone}] {mensagem}")
