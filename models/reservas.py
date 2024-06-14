from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Reservas(db.Model):
    def to_dict(self):
        return{
            'id_reserva': self.id_reserva,
            'fk_livro': self.fk_livro,
            'fk_membro': self.fk_membro,
            'data_reserva': self.data_reserva.strftime('%d/%m/%Y'),
            'data_retirada': self.data_retirada.strftime('%d/%m/%Y'),
            'status_reserva': self.status_reserva,
            'status_retirada': self.status_retirada,
        }
    
    id_reserva = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    fk_livro = db.Column(ForeignKey('livros.id_livro'), nullable=False)
    fk_membro = db.Column(ForeignKey('membros.id_membro'), nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)
    data_retirada = db.Column(db.Date, nullable=False)
    status_reserva = db.Column(db.Integer, nullable=False)
    status_retirada = db.Column(db.Integer, nullable=False)

    livro = relationship('Livros', backref='reservas')
    membro = relationship('Membros', backref='reservas')


    def __init__(self, fk_livro, fk_membro, data_reserva, data_retirada, status_reserva, status_retirada):
        self.fk_livro = fk_livro
        self.fk_membro = fk_membro
        self.data_reserva = data_reserva
        self.data_retirada = data_retirada
        self.status_reserva = status_reserva
        self.status_retirada =  status_retirada




