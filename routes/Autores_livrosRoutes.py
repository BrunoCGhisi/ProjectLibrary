from controllers.autores_livrosController import Autores_livrosController


def autores_livrosRoutes(app):
    app.route('/autor_livro', methods=['GET', 'POST', 'PUT', 'DELETE'])(Autores_livrosController)