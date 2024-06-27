# Desafio Técnico Morada.ai: Caixa Eletrônico API

# Caixa Eletrônico API

## Descrição
Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

## Requisitos
- Python 3.7+
- Flask

## Instalação
1. Clone o repositório:
https://github.com/Mariacpdb/Desafio-T-cnico-Morada.ai-Caixa-Eletr-nico-API.git
2. Instale as dependências:
pip install -r requirements.txt

## Execução
1. Inicie a aplicação:
python app.py

2. Faça uma requisição de saque:
curl -X POST -H "Content-Type: application/json" -d '{"valor": 380}' http://localhost:5000/api/saque

## Testes
Para rodar os testes:
python -m unittest tests.py

## Desafios
- Garantir que a lógica de cálculo de cédulas seja eficiente e retorne a menor quantidade possível.
- Tratar entradas inválidas e garantir que a API responda adequadamente a esses casos.

## Considerações Finais
Este projeto foi desenvolvido para simular um caixa eletrônico simples, com a lógica otimizada para garantir a menor quantidade de cédulas possíveis para qualquer valor de saque permitido.


