from flask import request
from database.db import db
from models.membros import Membros

def membrosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            membros = Membros(data['nome'], data['email'], data['senha'], data['cpf'], data['telefone'], data['data_ingresso'], data['is_adm'], data['status'])
            db.session.add(membros)
            db.session.commit()
            return 'Membro add com sucesso', 200
        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
            

    elif request.method == "GET":
        try:
            data = Membros.query.all()

            newData = {'membros': [membro.to_dict() for membro in data]}
            return newData, 200
        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
        

    elif request.method == "PUT":
        try:
            data = request.get_json()
            put_membro_id = data['id']
            membro = Membros.query.get(put_membro_id)

            if membro is None:
                  return{'error': 'Membro não encontrado'}, 405
            
            membro.nome = data.get('nome', membro.nome)
            membro.email = data.get('email', membro.email)
            membro.senha = data.get('senha', membro.senha)            
            membro.cpf = data.get('cpf', membro.cpf)
            membro.telefone = data.get('telefone', membro.telefone)
            membro.data_ingresso = data.get('data_ingresso', membro.data_ingresso)
            membro.is_adm = data.get('is_adm', membro.is_adm)
            membro.status = data.get('status', membro.status)
            
            db.session.commit()
            return "Membro atualizado com sucesso", 202

        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
    
    elif request.method == "DELETE":
        try:
            data = request.get_json()
            delete_membro_id  = data["id"]
            membro = Membros.query.get(delete_membro_id)

            if membro is None:
                return{'error': 'membro não encontrado'}, 405
                
            db.session.delete(membro)
            db.session.commit()
            return "membro deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o membro. Erro:{str(e)}", 405
            

        

