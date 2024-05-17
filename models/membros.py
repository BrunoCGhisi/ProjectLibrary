from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Membros(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            'id_membro': self.id_membro,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'data_ingresso': self.data_ingresso,
            'fk_status': self.fk_status
        }
    

    id_membro = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(9), nullable=False)
    data_ingresso = db.Column(db.Date, nullable=False)
    fk_status = db.Column(ForeignKey('status_membros.id_status'), nullable=False)

    status_membro = relationship('Status_membros', backref='membros')


    def __init__(self, nome, email, cpf, telefone, data_ingresso, fk_status):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_ingresso = data_ingresso
        self.fk_status = fk_status


# MUDAR OS VALORES PRO BANCO ORIGINAL OBV