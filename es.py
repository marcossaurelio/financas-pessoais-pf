import json
from transacoes import Transacao
import os

# Lambda functions
formatar_tipo = lambda tipo: "Receita" if tipo == "R" else "Despesa"
validar_valor = lambda valor: True if valor.replace('.', '').replace('.','').isdigit() else False
retornar_modulo_valor = lambda valor: abs(valor)

def carregar_transacoes(arquivo, categoria_padrao="Outros"):
    # Carrega as transações do arquivo JSON.
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
            return [Transacao(t['tipo'], t['valor'], t.get('categoria', categoria_padrao)) for t in dados] # List comprehension
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_transacoes(transacoes, arquivo):
    # Salva as transações no arquivo JSON.
    with open(arquivo, "w") as f:
        json.dump([t._asdict() for t in transacoes], f, indent=4)

def limpar_transacoes(arquivo):
    # Apaga o arquivo de transações
    if os.path.exists(arquivo):
        os.remove(arquivo)  # Exclui o arquivo
    print("Todas as transações foram removidas!")
    return []