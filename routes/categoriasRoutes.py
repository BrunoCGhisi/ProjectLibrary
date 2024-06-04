from controllers.categoriasController import categoriasController


def categoriasRoutes(app):
    app.route('/categoria/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])(categoriasController)