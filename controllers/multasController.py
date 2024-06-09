from flask import request
from database.db import db
from models.multas import Multas

def multasController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            multas = Multas(data['fk_empestimo'], data['fk_membro'], data['data_multa'], data['data_prazo'], data['valor'], data['status'])
            db.session.add(multas)
            db.session.commit()
            return 'Multa adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Multas.query.all()

            newData = {'multas': [multa.to_dict() for multa in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:

                data = request.get_json() #pega todos os dados
                multa_id = request.args.to_dict().get('id') #pega o id dos dados que o data trouxe
                multa = Multas.query.get(multa_id)

                if multa is None:
                    return{'error': 'Status não encontrado'}, 405
                
                multa.fk_emprestimo = data.get('fk_emprestimo', multa.fk_emprestimo)
                multa.fk_membro = data.get('fk_membro', multa.fk_membro)
                multa.data_multa = data.get('data_multa', multa.data_multa)
                multa.data_prazo = data.get('data_prazo', multa.data_prazo)
                multa.valor = data.get('valor', multa.valor)
                multa.status = data.get('status', multa.status)

                
                 
                
                db.session.commit()
                return "Status atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o status. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.args.to_dict().get('id') #pega todos os dados do Bruno
            multa = Multas.query.get(data) # vai procurar usuarios NO BANCO com esse id

            if multa is None:
                return{'error': 'Status não encontrado'}, 405
            
            db.session.delete(multa)
            db.session.commit()
            return "Status deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o status . Erro:{str(e)}", 405
        

