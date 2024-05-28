from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Livros(db.Model):
    def to_dict(self):
        return{
            'id_livro': self.id_livro,
            # 'fk_autor_livro': self.fk_autor_livro,
            'fk_categoria': self.fk_categoria,
            'titulo': self.titulo,
            'ano': self.ano,
            'disponiveis': self.disponiveis, 
            'estoque': self.estoque, #contando os que estão emprestados
            'capa': self.capa
        }
    
    id_livro = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    #fk_autor_livro = db.Column(ForeignKey('autores_livros.fk_autor'), nullable=False)    
    fk_categoria = db.Column(ForeignKey('categorias.id_categoria'), nullable=False)
    titulo = db.Column(db.String(45), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    disponiveis = db.Column(db.Integer, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    capa = db.Column(db.String(100), nullable=False)



    categoria = relationship('Categorias', backref='livros')
    #autores_livros = relationship('Autores_livros', backref='livros')


    def __init__(self, fk_categoria,titulo, ano, disponiveis, estoque, capa):
        #self.fk_autor_livro = fk_autor_livro
        self.fk_categoria = fk_categoria
        self.titulo = titulo
        self.ano = ano
        self.disponiveis = disponiveis
        self.estoque = estoque
        self.capa = capa
        
        
