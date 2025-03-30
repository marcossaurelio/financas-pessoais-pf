from transacoes import Transacao

# Closure
def categorizador_de_transacoes(categoria_default="Outros"):

    def adicionar_transacao_categoria_default(transacoes, tipo, valor, categoria=None):
        # Se a categoria não for fornecida, usa a categoria padrão
        if categoria is None:
            categoria = categoria_default
        
        nova_transacao = Transacao(tipo, valor, categoria)
        transacoes.append(nova_transacao)
        return transacoes

    return adicionar_transacao_categoria_default
