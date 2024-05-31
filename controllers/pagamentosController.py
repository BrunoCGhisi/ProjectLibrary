from flask import request
from database.db import db
from models.pagamentos import Pagamentos

def pagamentosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            pagamentos = Pagamentos(data['fk_membro'], ['fk_multa'], data['data_pagamento'])
            db.session.add(pagamentos)
            db.session.commit()
            return 'Pagamento add com sucesso', 200
        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
            

    elif request.method == "GET":
        try:
            data = Pagamentos.query.all()

            newData = {'pagamentos': [pagamento.to_dict() for pagamento in data]}
            return newData, 200
        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
        

    elif request.method == "PUT":
        try:
            data = request.get_json()
            put_pagamento_id = data['id']
            pagamento = Pagamentos.query.get(put_pagamento_id)

            if pagamento is None:
                  return{'error': 'pagamento não encontrado'}, 405
            
            pagamento.fk_membro = data.get('fk_membro', pagamento.fk_membro)
            pagamento.fk_multa = data.get('fk_multa', pagamento.fk_multa)
            pagamento.data_pagamento = data.get('data_pagamento', pagamento.data_pagamento)

            db.session.commit()
            return "pagamento atualizado com sucesso", 202

        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
    
    elif request.method == "DELETE":
        try:
            data = request.get_json()
            delete_pagamento_id  = data["id"]
            pagamento = Pagamentos.query.get(delete_pagamento_id)

            if pagamento is None:
                return{'error': 'pagamento não encontrado'}, 405
                
            db.session.delete(pagamento)
            db.session.commit()
            return "pagamento deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o pagamento. Erro:{str(e)}", 405
            

        
