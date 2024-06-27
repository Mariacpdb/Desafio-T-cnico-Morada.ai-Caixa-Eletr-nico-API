# tests.py

import unittest
from withdrawal_logic import calculate_notes
from app import app

class TestWithdrawalLogic(unittest.TestCase):
    """
    Testes para a lógica de cálculo de cédulas.
    """
    
    def test_valid_withdrawal(self):
        """
        Testa se a função calculate_notes retorna a quantidade correta de cédulas para valores válidos.
        """
        self.assertEqual(calculate_notes(380), {100: 3, 50: 1, 20: 1, 10: 1, 5: 0, 2: 0})
        self.assertEqual(calculate_notes(5), {100: 0, 50: 0, 20: 0, 10: 0, 5: 1, 2: 0})
    
    def test_invalid_withdrawal(self):
        """
        Testa se a função calculate_notes levanta uma exceção para valores inválidos (negativos ou não múltiplos de 2).
        """
        with self.assertRaises(ValueError):
            calculate_notes(-10)
        with self.assertRaises(ValueError):
            calculate_notes(3)
    
    def test_non_integer_withdrawal(self):
        """
        Testa se a função calculate_notes levanta uma exceção para valores não inteiros.
        """
        with self.assertRaises(ValueError):
            calculate_notes(7.5)
        with self.assertRaises(ValueError):
            calculate_notes("100")

class TestAPI(unittest.TestCase):
    """
    Testes para a API de saque.
    """
    
    def setUp(self):
        """
        Configura o cliente de teste do Flask.
        """
        self.app = app.test_client()
        self.app.testing = True
    
    def test_valid_request(self):
        """
        Testa se a API responde corretamente para um valor de saque válido.
        """
        response = self.app.post('/api/saque', json={"valor": 380})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {100: 3, 50: 1, 20: 1, 10: 1, 5: 0, 2: 0})
    
    def test_invalid_request(self):
        """
        Testa se a API responde com um erro para um valor de saque inválido.
        """
        response = self.app.post('/api/saque', json={"valor": -10})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == '__main__':
    # Executa os testes
    unittest.main()
