class Endereco:
    """Parte de Cliente (COMPOSIÇÃO)."""

    def __init__(self, logradouro: str, cidade: str, uf: str = "DF"):
        self.logradouro = logradouro
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return f"{self.logradouro}, {self.cidade}-{self.uf}"
