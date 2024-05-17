from controllers.reservasController import reservasController

def reservasRoutes(app):
    app.route('/reserva', methods=['GET', 'POST', 'PUT', "DELETE"])(reservasController)