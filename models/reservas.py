from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Reservas(db.Model):
    def to_dict(self):
        return{
            'id_reserva': self.id_reserva,
            'fk_livro': self.fk_livro,
            'fk_membro': self.fk_membro,
            'data_reserva': self.data_reserva,
            'fk_status': self.fk_status
        }
    
    id_reserva = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    fk_livro = db.Column(ForeignKey('livros.id'), nullable=False)
    fk_membro = db.Column(ForeignKey('membros.id'), nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)
    fk_status = db.Column(ForeignKey('status_reservas.id'), nullable=False)

    livro = relationship('Livros', backref='reservas')
    membro = relationship('Membros', backref='reservas')
    status_reserva = relationship('Status_reservas', backref='reservas')


    def __init__(self, fk_livro, fk_membro, data_reserva, fk_status):
        self.fk_livro = fk_livro
        self.fk_membro = fk_membro
        self.data_reserva = data_reserva
        self.fk_status = fk_status




