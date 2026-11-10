from .servico import Servico


class Consultoria(Servico):
    @property
    def tipo(self) -> str:
        return "Consultoria"

    def calcular_custo(self, quantidade: int = 1) -> float:
        total = self.valor_base * quantidade
        return total * 0.9 if quantidade > 5 else total  # 10% de desconto acima de 5h
