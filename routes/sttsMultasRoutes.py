from controllers.sttsMultasController import sttsMultasController


def sttsMultasRoutes(app):
    app.route('/sttsMulta', methods=['GET', 'POST', 'PUT', 'DELETE'])(sttsMultasController)