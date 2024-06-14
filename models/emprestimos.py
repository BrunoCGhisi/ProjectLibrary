from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Emprestimos(db.Model):
    def to_dict(self):
        return{
            'id_emprestimo': self.id_emprestimo,
            'fk_livro': self.fk_livro,
            'fk_membro': self.fk_membro,
            'data_emprestimo': self.data_emprestimo,
            'data_retorno': self.data_retorno,
            'fk_status': self.fk_status
        }
    
    id_emprestimo = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    fk_livro = db.Column(ForeignKey('livros.id_livro'), nullable=False)
    fk_membro = db.Column(ForeignKey('membros.id_membro'), nullable=False)
    data_emprestimo = db.Column(db.Date, nullable=False)
    data_retorno = db.Column(db.Date, nullable=False)
    fk_status = db.Column(ForeignKey('status_emprestimos.id_status'), nullable=False)

    livro = relationship('Livros', backref='emprestimos')
    membro = relationship('Membros', backref='emprestimos')
    status_emprestimo = relationship('Status_emprestimos', backref='emprestimo')


    def __init__(self, fk_livro, fk_membro, data_emprestimo, data_retorno, fk_status):
        self.fk_livro = fk_livro
        self.fk_membro = fk_membro
        self.data_emprestimo = data_emprestimo
        self.data_retorno = data_retorno
        self.fk_status = fk_status

