from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Livros(db.Model):
    def to_dict(self):
        return{
            'id_livro': self.id_livro,
            'titulo': self.titulo,
            'ano': self.ano,
            'disponiveis': self.disponiveis, 
            'estoque': self.estoque, #contando os que estão emprestados
            'fk_categoria': self.fk_categoria,
            'fk_autor': self.fk_autor
        }
    
    id_livro = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    titulo = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    disponiveis = db.Column(db.Integer, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    fk_categoria = db.Column(ForeignKey('categorias.id_categoria'), nullable=False)
    fk_autor = db.Column(ForeignKey('autores.id_autor'), nullable=False)

    categoria = relationship('Categorias', backref='livros')
    autor = relationship('Autores', backref='livros')


    def __init__(self, titulo, ano, disponiveis, estoque, fk_categoria, fk_autor):
        self.titulo = titulo
        self.ano = ano
        self.disponiveis = disponiveis
        self.estoque = estoque
        self.fk_categoria = fk_categoria
        self.fk_autor = fk_autor
