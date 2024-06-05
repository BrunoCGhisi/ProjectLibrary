from database.db import db

class Categorias(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            
            'id_categoria': self.id_categoria,
            'categoria': self.categoria
        }
    id_categoria = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    categoria = db.Column(db.String(45), nullable=False)

    def __init__(self, categoria):
        self.categoria = categoria


# MUDAR OS VALORES PRO BANCO ORIGINAL OBV