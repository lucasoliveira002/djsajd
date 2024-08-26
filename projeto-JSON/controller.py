from flask import Flask, request, jsonify
from flask import app
from app import livros, livro, encontrar_livro


@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros), 200

@app.route('/livros/<int:livro_id>',methods=['GET'])
def get_livro(livro_id):
    livro= encontrar_livro(livro_id)
    if livro:
        return jsonify(livro), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.json
    novo_livro['id'] = livro[-1]["id"] + 1 if livros else 1
    livros.append(novo_livro)
    return jsonify(novo_livro),201