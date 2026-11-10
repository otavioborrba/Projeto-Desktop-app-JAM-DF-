from .servico import Servico


class Manutencao(Servico):
    TAXA_VISITA = 80.0

    @property
    def tipo(self) -> str:
        return "Manutenção"

    def calcular_custo(self, quantidade: int = 1) -> float:
        return self.TAXA_VISITA + self.valor_base * quantidade  # taxa + horas
