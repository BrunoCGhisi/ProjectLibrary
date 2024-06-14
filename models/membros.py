from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_restx import inputs


class Membros(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            'id_membro': self.id_membro,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'data_ingresso': self.data_ingresso,
            'is_adm': self.is_adm,
            'status': self.status
        }
    

    id_membro = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(9), nullable=False)
    data_ingresso = db.Column(db.Date, nullable=False)
    is_adm = db.Column(db.Boolean(), nullable=False)
    status = db.Column(db.Boolean(), nullable=False)


    def __init__(self, nome, email,senha, cpf, telefone, data_ingresso, is_adm, status):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.data_ingresso = data_ingresso
        self.is_adm = int(is_adm)
        self.status = int(status)


# MUDAR OS VALORES PRO BANCO ORIGINAL OBV