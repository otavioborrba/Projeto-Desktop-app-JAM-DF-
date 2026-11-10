from datetime import datetime
from itertools import count

from modelos.notificacoes import Notificador
from modelos.pessoas import Cliente, Tecnico
from modelos.servicos import Servico

from .agendamento import Agendamento
from .orcamento import Orcamento
from .status_solicitacao import StatusSolicitacao


class SolicitacaoServico:
    """Núcleo do fluxo: pedido -> orçamento -> aprovação -> agendamento."""

    _ids = count(1)

    def __init__(self, cliente: Cliente, servico: Servico, observacao: str = ""):
        self.id = next(self._ids)
        self.cliente = cliente               # ASSOCIAÇÃO
        self.servico = servico               # ASSOCIAÇÃO
        self.tecnico: Tecnico | None = None  # ASSOCIAÇÃO
        self.observacao = observacao
        self.status = StatusSolicitacao.ABERTA
        self.criada_em = datetime.now()
        # COMPOSIÇÃO: só existem como parte da solicitação
        self.orcamento: Orcamento | None = None
        self.agendamento: Agendamento | None = None

    def enviar_orcamento(self, tecnico: Tecnico, quantidade: int, notificador: Notificador) -> None:
        self.tecnico = tecnico
        self.orcamento = Orcamento.gerar(self.servico, quantidade)
        self.status = StatusSolicitacao.ORCADA
        # DEPENDÊNCIA: o Notificador entra por parâmetro
        notificador.enviar(
            self.cliente,
            f"Orçamento #{self.id} ({self.servico}): R$ {self.orcamento.valor:.2f}. Aprova?",
        )

    def responder_orcamento(self, aprovado: bool) -> None:
        if self.orcamento is None:
            raise RuntimeError("Nenhum orçamento foi enviado.")
        if aprovado:
            self.orcamento.aprovar()
            self.status = StatusSolicitacao.APROVADA
        else:
            self.orcamento.recusar()
            self.status = StatusSolicitacao.RECUSADA

    def agendar(self, data: datetime, notificador: Notificador) -> None:
        if self.status is not StatusSolicitacao.APROVADA or self.tecnico is None:
            raise RuntimeError("Só é possível agendar após a aprovação do orçamento.")
        self.agendamento = Agendamento(data, self.tecnico)
        self.status = StatusSolicitacao.AGENDADA
        notificador.enviar(self.cliente, f"Serviço agendado para {data:%d/%m/%Y %H:%M}.")

    def editar_data(self, nova_data: datetime, notificador: Notificador) -> None:
        if self.agendamento is None:
            raise RuntimeError("Não há agendamento para editar.")
        self.agendamento.editar_data(nova_data)
        notificador.enviar(self.cliente, f"Nova data: {nova_data:%d/%m/%Y %H:%M}.")

    def contatar_tecnico(self, notificador: Notificador, mensagem: str) -> None:
        if self.tecnico is None:
            raise RuntimeError("Nenhum técnico responsável ainda.")
        notificador.enviar(self.tecnico, f"Cliente {self.cliente.nome}: {mensagem}")
