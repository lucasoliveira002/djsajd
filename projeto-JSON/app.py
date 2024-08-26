from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {id: 1, "titulo": "Sapiens", "autor": "Yuval"},
    {id: 2, "titulo": "Monica", "autor": "Mauricio"}
]

def encontrar_livro (livro_id):
    return next((livro for livro in livros if livro["id"] == livro_id), None)

if __name__ == "__main__":
    app.run()