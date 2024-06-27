# withdrawal_logic.py

def calculate_notes(amount):
    """
    Calcula a quantidade mínima de cédulas necessárias para um valor de saque dado.

    Args:
        amount (int): O valor do saque desejado.

    Returns:
        dict: Um dicionário com a quantidade de cédulas de cada denominação.

    Raises:
        ValueError: Se o valor não for um número inteiro positivo ou não for múltiplo de 2.
    """
    # Verifica se o valor é um número inteiro positivo
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("O valor deve ser um número inteiro positivo.")
    
    # Verifica se o valor é múltiplo de 2
    if amount % 2 != 0:
        raise ValueError("O valor deve ser múltiplo de 2, pois a cédula mínima é de 2 reais.")
    
    # Denominações das cédulas
    notes = [100, 50, 20, 10, 5, 2]
    
    # Inicializa o resultado com zero cédulas de cada denominação
    result = {note: 0 for note in notes}
    
    # Calcula a quantidade de cédulas necessárias para cada denominação
    for note in notes:
        if amount >= note:
            result[note] = amount // note
            amount %= note
    
    # Verifica se o valor foi totalmente atendido com as cédulas disponíveis
    if amount != 0:
        raise ValueError("O valor de saque não pode ser atendido com as cédulas disponíveis.")
    
    return result
