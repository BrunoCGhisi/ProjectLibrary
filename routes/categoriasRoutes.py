from controllers.categoriasController import categoriasController


def categoriasRoutes(app):
    app.route('/categoria', methods=['GET', 'POST', 'PUT', 'DELETE'])(categoriasController)