from abc import ABC, abstractmethod


class Pessoa(ABC):
    """Superclasse abstrata (HERANÇA)."""

    def __init__(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    @property
    @abstractmethod
    def papel(self) -> str:
        """Cada subclasse informa seu papel no sistema (POLIMORFISMO)."""

    def __str__(self) -> str:
        return f"{self.papel}: {self.nome}"
