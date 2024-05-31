from controllers.autores_livrosController import autores_livrosController


def autores_livrosRoutes(app):
    app.route('/autor_livro', methods=['GET', 'POST', 'PUT', 'DELETE'])(autores_livrosController)   