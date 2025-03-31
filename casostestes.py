import unittest
from processamento import calcular_saldo
from es import carregar_transacoes, salvar_transacoes, limpar_transacoes, formatar_tipo, validar_valor
from categorizador import categorizador_de_transacoes
from main import adicionar_transacao, filtrar_transacoes

ARQUIVO_TESTE = "test_transacoes.json"

class TestSistemaFinanceiro(unittest.TestCase):

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.transacoes = [
            {"tipo": "R", "valor": 1000.0, "categoria": "Salário"},
            {"tipo": "D", "valor": 200.0, "categoria": "Alimentação"},
            {"tipo": "D", "valor": 150.0, "categoria": "Transporte"}
        ]
        salvar_transacoes(self.transacoes, ARQUIVO_TESTE)

    def tearDown(self):
        """Limpa os dados após cada teste."""
        limpar_transacoes(ARQUIVO_TESTE)

    def test_calculo_saldo(self):
        """Testa se o saldo é calculado corretamente."""
        saldo = calcular_saldo(self.transacoes)
        self.assertEqual(saldo, 650.0)  # 1000 - (200 + 150) = 650

    def test_adicionar_transacao(self):
        """Testa se uma transação é adicionada corretamente."""
        transacoes_atualizadas = adicionar_transacao(self.transacoes, categorizador_de_transacoes("Outros"))
        self.assertGreater(len(transacoes_atualizadas), len(self.transacoes))  # Deve aumentar a lista

    def test_validar_valor(self):
        """Verifica se a validação de valores funciona corretamente."""
        self.assertTrue(validar_valor("50"))  # Valor válido
        self.assertFalse(validar_valor("abc"))  # Valor inválido

    def test_formatar_tipo(self):
        """Testa a formatação do tipo de transação."""
        self.assertEqual(formatar_tipo("R"), "Receita")
        self.assertEqual(formatar_tipo("D"), "Despesa")

    def test_filtro_transacoes(self):
        """Testa a filtragem por categoria."""
        resultado = list(filter(lambda t: t["categoria"] == "Alimentação", self.transacoes))
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["valor"], 200.0)

if __name__ == "__main__":
    unittest.main()