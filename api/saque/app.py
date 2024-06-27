# app.py

from flask import Flask, request, jsonify
from withdrawal_logic import calculate_notes

# Cria a aplicação Flask
app = Flask(__name__)

@app.route('/api/saque', methods=['POST'])
def saque():
    """
    Endpoint para realizar um saque. Recebe um valor em formato JSON e retorna a quantidade de cédulas necessárias.

    Returns:
        Response: Resposta em formato JSON com a quantidade de cédulas ou mensagem de erro.
    """
    # Obtém os dados da requisição
    data = request.get_json()

    # Verifica se o parâmetro 'valor' foi fornecido
    if not data or 'valor' not in data:
        return jsonify({"error": "Parâmetro 'valor' é obrigatório."}), 400

    try:
        # Converte o valor para inteiro
        valor = int(data['valor'])
        
        # Calcula a quantidade de cédulas necessárias
        result = calculate_notes(valor)
        
        # Retorna o resultado em formato JSON
        return jsonify(result), 200
    except ValueError as e:
        # Retorna a mensagem de erro em formato JSON
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Inicia a aplicação Flask no modo debug
    app.run(debug=True)
