from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Multas(db.Model):
    def to_dict(self):
        return{
            'id_multa': self.id_multas,
            'fk_emprestimo': self.fk_emprestimo,
            'data_prazo': self.data_prazo,
            'valor': self.valor,
            'fk_status': self.fk_status,
        }
    
    id_multa = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    fk_emprestimo = db.Column(ForeignKey('membros.id'), nullable=False)
    data_prazo = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    fk_status = db.Column(ForeignKey('status_multas.id'), nullable=False)

    membro = relationship('Membros', backref='pagamentos')
    status_multa = relationship('Status_multas', backref='multas')


    def __init__(self, fk_emprestimo, data_prazo, valor, fk_status):
        self.fk_emprestimo = fk_emprestimo
        self.data_prazo = data_prazo
        self.valor = valor
        self.fk_status = fk_status




