from controllers.emprestimosController import emprestimosController


def emprestimosRoutes(app):
    app.route('/emprestimo', methods=['GET', 'POST', 'PUT', 'DELETE'])(emprestimosController)