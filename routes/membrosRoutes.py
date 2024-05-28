from controllers.membrosController import membrosController

def membrosRoutes(app):
    app.route('/membro', methods=['GET', 'POST', 'PUT', "DELETE"])(membrosController)