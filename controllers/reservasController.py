from flask import request
from database.db import db
from models.reservas import Reservas

def reservasController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            reservas = Reservas(data['fk_livro'], data['fk_membro'], data['data_reserva'], data['data_retirada'],  data['status'])
            db.session.add(reservas)
            db.session.commit()
            return 'reservas adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Reservas.query.all()

            newData = {'reservas': [reserva.to_dict() for reserva in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:
                
                data = request.get_json() #pega todos os dados
                put_reserva_id = data['id'] #pega o id dos dados que o data trouxe
                reserva = Reservas.query.get(put_reserva_id)

                if reserva is None:
                    return{'error': 'reserva não encontrado'}, 405
                
                reserva.fk_livro = data.get('fk_livro', reserva.fk_livro)
                reserva.fk_membro = data.get('fk_membro', reserva.fk_membro)
                reserva.data_reserva = data.get('data_reserva', reserva.data_reserva)
                reserva.data_retirada = data.get('data_retirada', reserva.data_retirada)
                reserva.status = data.get('status', reserva.status)

               
                db.session.commit()
                return "reserva atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar a reserva. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_reserva_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            reserva = Reservas.query.get(delete_reserva_id) # vai procurar usuarios NO BANCO com esse id

            if reserva is None:
                return{'error': 'reserva não encontrado'}, 405
            
            db.session.delete(reserva)
            db.session.commit()
            return "reserva deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o reserva. Erro:{str(e)}", 405
        


