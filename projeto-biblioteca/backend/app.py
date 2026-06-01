from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from routes.books import books_bp

app = Flask(__name__)
CORS(app)

# Configuração do Swagger
app.config['SWAGGER'] = {
    'title': 'Biblioteca API',
    'uiversion': 3
}
swagger = Swagger(app)

# Registro do Blueprint
app.register_blueprint(books_bp, url_prefix='/api/books')

if __name__ == '__main__':
    app.run(debug=True, port=5000)