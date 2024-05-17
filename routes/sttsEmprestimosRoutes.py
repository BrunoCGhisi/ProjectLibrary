from controllers.sttsEmprestimosController import sttsEmprestimosController

def sttsEmprestimosRoutes(app):
    app.route('/sttsEmprestimo', methods=['GET', 'POST', 'PUT', 'DELETE'])(sttsEmprestimosController)