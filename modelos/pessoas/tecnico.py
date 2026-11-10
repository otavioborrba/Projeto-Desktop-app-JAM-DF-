from datetime import datetime

from .pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, especialidade: str):
        super().__init__(nome, telefone, email)
        self.especialidade = especialidade
        self._agenda: list[datetime] = []

    @property
    def papel(self) -> str:
        return "Técnico"

    def disponivel_em(self, data: datetime) -> bool:
        return data not in self._agenda

    def reservar(self, data: datetime) -> None:
        if not self.disponivel_em(data):
            raise ValueError(f"{self.nome} já tem compromisso em {data:%d/%m/%Y %H:%M}")
        self._agenda.append(data)

    def liberar(self, data: datetime) -> None:
        if data in self._agenda:
            self._agenda.remove(data)
