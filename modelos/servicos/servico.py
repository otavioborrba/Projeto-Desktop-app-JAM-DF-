from abc import ABC, abstractmethod


class Servico(ABC):
    """Superclasse abstrata dos serviços oferecidos pela empresa."""

    def __init__(self, descricao: str, valor_base: float):
        self.descricao = descricao
        self.valor_base = valor_base

    @property
    @abstractmethod
    def tipo(self) -> str: ...

    @abstractmethod
    def calcular_custo(self, quantidade: int = 1) -> float:
        """quantidade = pontos instalados, horas de manutenção ou horas de consultoria.
        Cada subclasse implementa sua regra (POLIMORFISMO)."""

    def __str__(self) -> str:
        return f"{self.tipo} - {self.descricao}"
