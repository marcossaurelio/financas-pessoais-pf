from processamento import calcular_saldo
from es import salvar_transacoes, carregar_transacoes, limpar_transacoes, formatar_tipo, retornar_modulo_valor, validar_valor
from categorizador import categorizador_de_transacoes

# Caminho do arquivo json onde serão salvas as transações
ARQUIVO_DADOS = "transacoes.json"

def menu():
    # Exibe o menu principal e captura a opção do usuário.
    print("\n=== Controle Financeiro ===")
    print("1. Adicionar transação")
    print("2. Ver saldo atual")
    print("3. Listar transações")
    print("4. Filtrar por categoria")
    print("5. Limpar transações")
    print("6. Sair")
    return input("Escolha uma opção: ")

def adicionar_transacao(transacoes, adicionar_transacao_categoria_default):
    # Adiciona uma nova transação à lista.
    tipo = input("Tipo (R - Receita / D - Despesa): ").strip().upper()
    if tipo not in ["R", "D"]:
        print("Tipo inválido!")
        return transacoes

    valor = input("Valor: ")
    
    if validar_valor(valor):
        valor = retornar_modulo_valor(float(valor))
        
    categoria = input("Categoria: ").strip()

    transacoes = adicionar_transacao_categoria_default(transacoes, tipo, valor, categoria if categoria else None)

    salvar_transacoes(transacoes, ARQUIVO_DADOS)
    print("Transação adicionada com sucesso!")
    return transacoes

def listar_transacoes(transacoes):
    # Exibe todas as transações registradas.
    if not transacoes:
        print("Nenhuma transação registrada.")
        return

    print("\n=== Transações ===")
    for t in transacoes:
        print(f"{formatar_tipo(t.tipo.capitalize())} | R$ {t.valor:.2f} | {t.categoria}")

def redefinir_transacoes():
    confirmacao = input("Tem certeza que deseja limpar todas as transações realizadas? (S/N) ").upper()
    if confirmacao == "S":
        limpar_transacoes(ARQUIVO_DADOS)
    elif(confirmacao != "N"):
        print("Opção inválida.")

def filtrar_transacoes(transacoes):
    # Filtra transações por categoria.
    categoria = input("Digite a categoria para filtrar: ").strip()
    filtradas = filter(lambda t: t.categoria == categoria, transacoes) # Função de alta ordem: Filter

    if not filtradas:
        print("Nenhuma transação encontrada nessa categoria.")
    else:
        print(f"\n=== Transações na categoria '{categoria}' ===")
        for t in filtradas:
            print(f"{formatar_tipo(t.tipo.capitalize())} | R$ {t.valor:.2f}")

def main():
    # Função principal do programa.
    transacoes = carregar_transacoes(ARQUIVO_DADOS)

    adicionar_transacao_categoria_default = categorizador_de_transacoes("Outros")

    while True:
        opcao = menu()

        if opcao == "1":
            transacoes = adicionar_transacao(transacoes, adicionar_transacao_categoria_default)
        elif opcao == "2":
            saldo = calcular_saldo(transacoes)
            print(f"Saldo atual: R$ {saldo:.2f}")
        elif opcao == "3":
            listar_transacoes(transacoes)
        elif opcao == "4":
            filtrar_transacoes(transacoes)
        elif opcao == "5":
            redefinir_transacoes()
            transacoes = carregar_transacoes(ARQUIVO_DADOS)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()