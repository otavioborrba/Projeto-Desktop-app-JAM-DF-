from enum import Enum


class StatusSolicitacao(Enum):
    ABERTA = "Aberta"
    ORCADA = "Orçada"
    APROVADA = "Aprovada"
    RECUSADA = "Recusada"
    AGENDADA = "Agendada"
