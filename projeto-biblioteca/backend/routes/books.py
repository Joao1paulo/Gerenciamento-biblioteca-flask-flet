from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from schemas.book_schema import BookCreateSchema

books_bp = Blueprint('books', __name__)

books_db = [
    {"id": 1, "title": "O Design do Dia a Dia", "author": "Donald Norman", "year": 2002},
    {"id": 2, "title": "Não Me Faça Pensar", "author": "Steve Krug", "year": 2000}
]

@books_bp.route('/', methods=['GET'])
def get_books():
    """
    Lista todos os livros

    """
    return jsonify(books_db), 200

@books_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Busca um livro pelo ID

    """
    book = next((b for b in books_db if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Livro não encontrado"}), 404

@books_bp.route('/', methods=['POST'])
def add_book():
    """
    Adiciona um novo livro ao acervo

    """
    try:
        data = request.get_json()
        validated_data = BookCreateSchema(**data)
        
        new_book = {
            "id": len(books_db) + 1 if books_db else 1,
            "title": validated_data.title,
            "author": validated_data.author,
            "year": validated_data.year
        }
        books_db.append(new_book)
        return jsonify(new_book), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

@books_bp.route('/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    """
    Edita um livro existente
    """
    book = next((b for b in books_db if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Livro não encontrado"}), 404
        
    try:
        data = request.get_json()
        validated_data = BookCreateSchema(**data)
        
        book["title"] = validated_data.title
        book["author"] = validated_data.author
        book["year"] = validated_data.year
        
        return jsonify(book), 200
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

@books_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Apaga um livro do acervo

    """
    global books_db
    book = next((b for b in books_db if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Livro não encontrado"}), 404
        
    books_db = [b for b in books_db if b["id"] != book_id]
    return jsonify({"message": "Livro apagado com sucesso"}), 200