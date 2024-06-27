


# withdrawal_logic.py

def calculate_notes(amount):
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("O valor deve ser um número inteiro positivo.")
    
    notes = [100, 50, 20, 10, 5, 2]
    result = {note: 0 for note in notes}
    
    for note in notes:
        if amount >= note:
            result[note] = amount // note
            amount %= note
    
    if amount != 0:
        raise ValueError("O valor de saque não pode ser atendido com as cédulas disponíveis.")
    
    return result
