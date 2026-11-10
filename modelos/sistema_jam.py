from modelos.pessoas import Cliente, Tecnico
from modelos.servicos import Servico
from modelos.solicitacoes import SolicitacaoServico


class SistemaJAM:
    """Fachada que a interface gráfica vai usar."""

    def __init__(self):
        
        self.clientes: list[Cliente] = []
        self.tecnicos: list[Tecnico] = []
        self.solicitacoes: list[SolicitacaoServico] = []

    def cadastrar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def cadastrar_tecnico(self, tecnico: Tecnico) -> None:
        self.tecnicos.append(tecnico)

    def abrir_solicitacao(self, cliente: Cliente, servico: Servico, obs: str = "") -> SolicitacaoServico:
        s = SolicitacaoServico(cliente, servico, obs)
        self.solicitacoes.append(s)
        return s

    def solicitacoes_do_cliente(self, cliente: Cliente) -> list[SolicitacaoServico]:
        return [s for s in self.solicitacoes if s.cliente is cliente]
