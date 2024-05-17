from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Pagamentos(db.Model):
    def to_dict(self):
        return{
            'id_pagamento': self.id_pagamento,
            'fk_membro': self.fk_membro,
            'data_pagamento': self.data_pagamento,
            'valor': self.valor
        }
    
    id_pagamento = db.Column(db.Integer, primary_key=True, nullable=False, unique= True)
    fk_membro = db.Column(ForeignKey('membros.id_membro'), nullable=False)
    data_pagamento = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)

    membro = relationship('Membros', backref='pagamentos')


    def __init__(self, fk_membro, data_pagamento, valor):
        self.fk_membro = fk_membro
        self.data_pagamento = data_pagamento
        self.valor = valor




