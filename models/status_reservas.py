from database.db import db

class Status_reservas(db.Model): #criando representações das tabelas do bancp (db.Model) 
    def to_dict(self): #to_dict transforma database rows em dicioinarios
        return{
            'id_status': self.id_status,
            'status_atual': self.status_atual
        }
    id_status = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    status_atual = db.Column(db.String(45), nullable=False)

    def __init__(self, status_atual):
        self.status_atual = status_atual


# MUDAR OS VALORES PRO BANCO ORIGINAL OBV