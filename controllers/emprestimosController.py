from flask import request
from database.db import db
from models.emprestimos import Emprestimos
from models.multas import Multas
from datetime import date, timedelta



def emprestimosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            emprestimos = Emprestimos(data['fk_livro'], data['fk_membro'], data['data_emprestimo'], data['data_retorno'], data['fk_status'])
            db.session.add(emprestimos)
            db.session.commit()
            return 'emprestimos adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Emprestimos.query.all()
            newData = {'emprestimos': [emprestimo.to_dict() for emprestimo in data]} 

            # for emprestimo_dict in newData['emprestimos']:
            #     if 'data_retorno' in emprestimo_dict:  # Verifique se a chave existe
            #         data_retorno = emprestimo_dict['data_retorno']
            #         if data_retorno < date.today():
            #             exists = []
            #             exists.append(Multas.query.filter_by(fk_emprestimo=emprestimo_dict['id_emprestimo']))
            #             if len(exists) > 0:
            #                 for x in exists:
            #                     print("a")

            # def multas(newData):
            #     hoje = date.today()
            #     retorno = newData.data_retorno



            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        
        
        

    elif request.method == 'PUT':
            try:
                
                id_emprestimo = request.args.to_dict().get('id') #pega o id dos dados que o data trouxe
                emprestimo = Emprestimos.query.get(id_emprestimo)
                data = request.get_json() #pega todos os dados

                if emprestimo is None:
                    return{'error': 'emprestimo não encontrado'}, 405
                
                emprestimo.fk_livro = data.get('fk_livro', emprestimo.fk_livro)
                emprestimo.fk_membro = data.get('fk_membro', emprestimo.fk_membro)
                emprestimo.data_emprestimo = data.get('data_emprestimo', emprestimo.data_emprestimo)
                emprestimo.data_retorno = data.get('data_retorno', emprestimo.data_retorno)
                emprestimo.fk_status = data.get('fk_status', emprestimo.fk_status)

               
                db.session.commit()
                return "emprestimo atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar a emprestimo. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.args.to_dict().get('id')
            emprestimo = Emprestimos.query.get(data) # vai procurar usuarios NO BANCO com esse id

            if emprestimo is None:
                return{'error': 'emprestimo não encontrado'}, 405
            
            db.session.delete(emprestimo)
            db.session.commit()
            return "emprestimo deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o emprestimo. Erro:{str(e)}", 405




