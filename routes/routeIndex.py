from routes.autoresRoutes import autoresRoutes
from routes.categoriasRoutes import categoriasRoutes
from routes.livrosRoutes import livrosRoutes
from routes.sttsMembrosRoutes import sttsMembrosRoutes
from routes.sttsMultasRoutes import sttsMultasRoutes
from routes.sttsEmprestimosRoutes import sttsEmprestimosRoutes
from routes.membrosRoutes import membrosRoutes
from routes.pagamentosRoutes import pagamentosRoutes
from routes.reservasRoutes import reservasRoutes

def routeIndex(app):
    autoresRoutes(app)
    categoriasRoutes(app)
    livrosRoutes(app)
    sttsMembrosRoutes(app)
    sttsMultasRoutes(app)
    sttsEmprestimosRoutes(app)
    membrosRoutes(app)
    pagamentosRoutes(app)
    reservasRoutes(app)
