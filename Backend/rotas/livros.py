from flask import Blueprint, jsonify, request

from servicos.livros import LivroDatabase


livros_blueprint = Blueprint("livro", __name__)

@livros_blueprint.route("/livros", methods=["GET"])
def get_livros():
    IDAutor = request.args.get("IDAutor", "")
    return jsonify(LivroDatabase().get_livros(IDAutor)), 200