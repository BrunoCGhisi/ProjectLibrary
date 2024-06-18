from flask import request
from database.db import db
from models.status_emprestimos import Status_emprestimos

def sttsEmprestimosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            stts_emprestimos = Status_emprestimos(data['status_atual'])
            db.session.add(stts_emprestimos)
            db.session.commit()
            return 'Status do emprestimo adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    elif request.method == 'GET':
        try:
            data = Status_emprestimos.query.all()

            newData = {'status_emprestimos': [stts_membro.to_dict() for stts_membro in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:

                data = request.get_json() #pega todos os dados
                stts_emprestimo_id = request.args.to_dict().get('id')#pega o id dos dados que o data trouxe
                stts_emprestimo = Status_emprestimos.query.get(stts_emprestimo_id)

                if stts_emprestimo is None:
                    return{'error': 'Status não encontrado'}, 405
                
                stts_emprestimo.status_atual = data.get('status_atual', stts_emprestimo.status_atual)
                 
                
                db.session.commit()
                return "Status atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o status. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.args.to_dict().get('id') #pega todos os dados do Bruno

            stts_emprestimo = Status_emprestimos.query.get(data) # vai procurar usuarios NO BANCO com esse id

            if stts_emprestimo is None:
                return{'error': 'Status não encontrado'}, 405
            
            db.session.delete(stts_emprestimo)
            db.session.commit()
            return "Status deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o status . Erro:{str(e)}", 405
        

