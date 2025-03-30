from functools import reduce

def calcular_saldo(transacoes):
    # Calcula o saldo total com base na lista de transações.
    # Lambda function com reduce
    # Função de alta ordem: Reduce
    return reduce(lambda saldo, t: saldo + t.valor if t.tipo == "R" else saldo - t.valor, transacoes, 0)