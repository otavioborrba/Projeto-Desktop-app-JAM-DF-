from abc import ABC, abstractmethod

from modelos.pessoas import Pessoa


class Notificador(ABC):
    @abstractmethod
    def enviar(self, destinatario: Pessoa, mensagem: str) -> None:
        """DEPENDÊNCIA de Pessoa: o destinatário só é usado no envio."""
