from modelos.pessoas import Pessoa

from .notificador import Notificador


class EmailNotificador(Notificador):
    def enviar(self, destinatario: Pessoa, mensagem: str) -> None:
        print(f"[E-mail para {destinatario.email}] {mensagem}")
