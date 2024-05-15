from controllers.livrosController import livrosController

def livrosRoutes(app):
    app.route('/livro', methods=['GET', 'POST', 'PUT', "DELETE"])(livrosController)