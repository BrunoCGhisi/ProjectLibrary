from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Livros(db.Model):
    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'fk_autor': self.fk_autor
        }
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    nome = db.Column(db.String(100), nullable=False)
    fk_autor = db.Column(ForeignKey('cargos.id'))

    autor = relationship('Autores', backref='livros')


    def __init__(self, nome, fk_autor):
        self.nome= nome
        self.fk_autor = fk_autor
