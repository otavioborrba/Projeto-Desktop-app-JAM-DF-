from .servico import Servico


class Instalacao(Servico):
    @property
    def tipo(self) -> str:
        return "Instalação"

    def calcular_custo(self, quantidade: int = 1) -> float:
        return self.valor_base * quantidade  # valor por ponto (câmera, sensor...)
