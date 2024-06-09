from database.db import db

class Autores_livros(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            'id_autor_livro': self.id_autor_livro,
            'fk_autor': self.fk_autor,
            'fk_livro': self.fk_livro
        }
    
    # o id é só ID ou é como é no banco? se for AUTO IN precisa por também?
    id_autor_livro = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    fk_autor = db.Column(db.Integer, nullable=False)
    fk_livro = db.Column(db.Integer, nullable=False)

    def __init__(self, id_autor_livro, fk_autor, fk_livro):
        self.id_autor_livro = id_autor_livro
        self.fk_autor = fk_autor
        self.fk_livro = fk_livro


# MUDAR OS VALORES PRO BANCO ORIGINAL OBV