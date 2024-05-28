from controllers.autoresController import autoresController


def autoresRoutes(app):
    app.route('/autor', methods=['GET', 'POST', 'PUT', 'DELETE'])(autoresController)