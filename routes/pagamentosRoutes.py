from controllers.pagamentosController import pagamentosController

def pagamentosRoutes(app):
    app.route('/pagamento', methods=['GET', 'POST', 'PUT', "DELETE"])(pagamentosController)