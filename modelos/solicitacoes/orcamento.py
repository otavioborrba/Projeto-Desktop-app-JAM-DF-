from __future__ import annotations

from datetime import datetime

from modelos.servicos import Servico


class Orcamento:
    """Parte de SolicitacaoServico (COMPOSIÇÃO)."""

    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
        self.aprovado: bool | None = None  # None = aguardando resposta do cliente
        self.emitido_em = datetime.now()

    @classmethod
    def gerar(cls, servico: Servico, quantidade: int) -> Orcamento:
        # DEPENDÊNCIA: usa Servico só durante a execução, sem guardá-lo
        return cls(servico.calcular_custo(quantidade), str(servico))

    def aprovar(self) -> None:
        self.aprovado = True

    def recusar(self) -> None:
        self.aprovado = False
