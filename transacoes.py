from typing import NamedTuple

class Transacao(NamedTuple):
    # Representa uma transação financeira.
    tipo: str  # "R" - Receita ou "D" - Despesa
    valor: float
    categoria: str
