from .endereco import Endereco
from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(nome, telefone, email)
        self.endereco = endereco  

    @property
    def papel(self) -> str:
        return "Cliente"
