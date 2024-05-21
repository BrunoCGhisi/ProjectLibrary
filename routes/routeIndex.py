from routes.autoresRoutes import autoresRoutes
from routes.categoriasRoutes import categoriasRoutes
from routes.livrosRoutes import livrosRoutes
from routes.Autores_livrosRoutes import Autores_livrosRoutes
from routes.membrosRoutes import membrosRoutes
from routes.pagamentosRoutes import pagamentosRoutes
from routes.reservasRoutes import reservasRoutes
from routes.sttsEmprestimosRoutes import sttsEmprestimosRoutes

def routeIndex(app):
    autoresRoutes(app)
    categoriasRoutes(app)
    livrosRoutes(app)
    Autores_livrosRoutes(app)
    sttsEmprestimosRoutes(app)
    membrosRoutes(app)
    pagamentosRoutes(app)
    reservasRoutes(app)
