from routes.autoresRoutes import autoresRoutes
from routes.categoriasRoutes import categoriasRoutes
from routes.livrosRoutes import livrosRoutes


def routeIndex(app):
    autoresRoutes(app)
    categoriasRoutes(app)
    livrosRoutes(app)
