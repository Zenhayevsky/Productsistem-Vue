from flask import Flask, jsonify, request
from flask_cors import CORS
import json

with open("./Objects/clientes.json", encoding='utf-8') as listaclientes:
    clientes = json.load(listaclientes)

with open("./Objects/produtos.json", encoding='utf-8') as listaprodutos:
    produtos = json.load(listaprodutos)

with open("./Objects/vendas.json", encoding='utf-8') as listavendas:
    vendas = json.load(listavendas)

app = Flask(__name__)
CORS(app)

# consultar medicos


@app.route('/clientes')
def obter_clientes():
    return jsonify(clientes)

@app.route('/produtos', methods=['GET'])
def obter_produtoss():
    return jsonify(produtos)

@app.route('/vendas', methods=['GET'])
def obter_vendass():
    return jsonify(vendas)

app.run(port=5000, host='localhost', debug=True)
