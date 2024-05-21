from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Autores_livros(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            'fk_autor': self.fk_autor,
            'fk_livro': self.fk_livro
        }
    
    # o id é só ID ou é como é no banco? se for AUTO IN precisa por também?
    fk_autor = db.Column(ForeignKey('autores.id_autor'), primary_key = True, nullable=False)
    fk_livro = db.Column(ForeignKey('livros.id_livro'), nullable=False)

    autor = relationship('Autores', backref='autores_livros')
    livro = relationship('Livros', backref='autores_livros')


    def __init__(self, fk_autor, fk_livro):
        self.fk_autor = fk_autor,
        self.fk_livro = fk_livro



# MUDAR OS VALORES PRO BANCO ORIGINAL OBV