from datetime import datetime

from modelos.pessoas import Tecnico


class Agendamento:
    """Parte de SolicitacaoServico (COMPOSIÇÃO)."""

    def __init__(self, data: datetime, tecnico: Tecnico):
        if data < datetime.now():
            raise ValueError("A data do agendamento deve estar no futuro.")
        tecnico.reservar(data)
        self.data = data
        self.tecnico = tecnico  # ASSOCIAÇÃO com Tecnico

    def editar_data(self, nova_data: datetime) -> None:
        if nova_data < datetime.now():
            raise ValueError("A nova data deve estar no futuro.")
        self.tecnico.reservar(nova_data)  # falha antes de liberar a data antiga
        self.tecnico.liberar(self.data)
        self.data = nova_data
