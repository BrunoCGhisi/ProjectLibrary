from flask import request
from database.db import db
from models.status_multas import Status_multas

def sttsMultasController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            stts_multas = Status_multas(data['status_atual'])
            db.session.add(stts_multas)
            db.session.commit()
            return 'Status da multa adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Status_multas.query.all()

            newData = {'status_multas': [stts_multa.to_dict() for stts_multa in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:

                data = request.get_json() #pega todos os dados
                put_stts_multa_id = data['id'] #pega o id dos dados que o data trouxe
                stts_multa = Status_multas.query.get(put_stts_multa_id)

                if stts_multa is None:
                    return{'error': 'Status não encontrado'}, 405
                
                stts_multa.status_atual = data.get('status_atual', stts_multa.status_atual)
                 
                
                db.session.commit()
                return "Status atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o status. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_stts_multa_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            stts_multa = Status_multas.query.get(delete_stts_multa_id) # vai procurar usuarios NO BANCO com esse id

            if stts_multa is None:
                return{'error': 'Status não encontrado'}, 405
            
            db.session.delete(stts_multa)
            db.session.commit()
            return "Status deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o status . Erro:{str(e)}", 405
        

