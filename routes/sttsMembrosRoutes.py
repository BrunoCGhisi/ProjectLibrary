from controllers.sttsMembrosController import sttsMembrosController


def sttsMembrosRoutes(app):
    app.route('/sttsMembro', methods=['GET', 'POST', 'PUT', 'DELETE'])(sttsMembrosController)