from flask import request
from database.db import db
from models.status_membros import Status_membros

def sttsMembrosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            stts_membros = Status_membros(data['status_atual'])
            db.session.add(stts_membros)
            db.session.commit()
            return 'Status do membro adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Status_membros.query.all()

            newData = {'status_membros': [stts_membro.to_dict() for stts_membro in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:

                data = request.get_json() #pega todos os dados
                put_stts_membro_id = data['id'] #pega o id dos dados que o data trouxe
                stts_membro = Status_membros.query.get(put_stts_membro_id)

                if stts_membro is None:
                    return{'error': 'Status não encontrado'}, 405
                
                stts_membro.status_atual = data.get('status_atual', stts_membro.status_atual)
                 
                
                db.session.commit()
                return "Status atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o status. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_stts_membro_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            stts_membro = Status_membros.query.get(delete_stts_membro_id) # vai procurar usuarios NO BANCO com esse id

            if stts_membro is None:
                return{'error': 'Status não encontrado'}, 405
            
            db.session.delete(stts_membro)
            db.session.commit()
            return "Status deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o status . Erro:{str(e)}", 405
        

