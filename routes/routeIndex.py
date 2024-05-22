from routes.autoresRoutes import autoresRoutes
from routes.categoriasRoutes import categoriasRoutes
from routes.livrosRoutes import livrosRoutes
from routes.autores_livrosRoutes import autores_livrosRoutes
from routes.membrosRoutes import membrosRoutes
from routes.multasRoutes import multasRoutes
from routes.pagamentosRoutes import pagamentosRoutes
from routes.reservasRoutes import reservasRoutes
from routes.emprestimosRoutes import emprestimosRoutes
from routes.sttsEmprestimosRoutes import sttsEmprestimosRoutes

def routeIndex(app):
    autoresRoutes(app)
    categoriasRoutes(app)
    livrosRoutes(app)
    autores_livrosRoutes(app)
    sttsEmprestimosRoutes(app)
    membrosRoutes(app)
    pagamentosRoutes(app)
    reservasRoutes(app)
    multasRoutes(app)
