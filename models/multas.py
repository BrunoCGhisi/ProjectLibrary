from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Multas(db.Model):
    def to_dict(self):
        return{
            'id_multa': self.id_multas,
            'fk_emprestimo': self.fk_emprestimo,
            'fk_membro': self.fk_membro,
            'data_multa': self.data_multa,
            'data_prazo': self.data_prazo,
            'valor': self.valor,
            'status': self.status
        }
    
    id_multa = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    fk_emprestimo = db.Column(ForeignKey('emprestimos.id_emprestimo'), nullable=False)
    fk_membro = db.Column(ForeignKey('membros.id_membro'), nullable=False)
    data_multa = db.Column(db.Date, nullable=False)
    data_prazo = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    membro = relationship('Membros', backref='multas')
    emprestimo = relationship('Emprestimos', backref='multas')


    def __init__(self, fk_emprestimo, fk_membro, data_multa, data_prazo, valor, status):
        self.fk_emprestimo = fk_emprestimo
        self.fk_membro = fk_membro
        self.data_multa = data_multa
        self.data_prazo = data_prazo
        self.valor = valor
        self.status = int(status)




