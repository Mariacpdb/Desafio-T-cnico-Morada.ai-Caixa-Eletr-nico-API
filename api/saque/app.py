# app.py

from flask import Flask, request, jsonify
from withdrawal_logic import calculate_notes

app = Flask(__name__)


@app.route('/api/saque', methods=['POST'])
def saque():
    data = request.get_json()
    if not data or 'valor' not in data:
        return jsonify({"error": "Parâmetro 'valor' é obrigatório."}), 400

    try:
        valor = int(data['valor'])
        result = calculate_notes(valor)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
