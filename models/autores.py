from database.db import db

class Autores(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            'id_autor': self.id_autor,
            'nome': self.nome
        }
    
    id_autor = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)

    def __init__(self, nome):
        self.nome = nome


