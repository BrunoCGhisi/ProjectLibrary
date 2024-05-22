from controllers.multasController import multasController

def multasRoutes(app):
    app.route('/multa', methods=['GET', 'POST', 'PUT', "DELETE"])(multasController)