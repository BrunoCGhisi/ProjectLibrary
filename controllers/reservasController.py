from flask import request
from database.db import db
from models.reservas import Reservas

def reservasController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            reservas = Reservas(data['fk_livro'], data['fk_membro'], data['data_reserva'], data['data_retirada'], data['status'])
                                
            # data['status_reserva'], data['status_retirada'
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
                reserva_id = request.args.to_dict().get('id')  #pega o id dos dados que o data trouxe
                reserva = Reservas.query.get(reserva_id)

                if reserva is None:
                    return{'error': 'reserva não encontrado'}, 405
                
                reserva.fk_livro = data.get('fk_livro', reserva.fk_livro)
                reserva.fk_membro = data.get('fk_membro', reserva.fk_membro)
                reserva.data_reserva = data.get('data_reserva', reserva.data_reserva)
                reserva.data_retirada = data.get('data_retirada', reserva.data_retirada)
                """ reserva.status_reserva = data.get('status_reserva', reserva.status_reserva)
                reserva.status_retirada = data.get('status_retirada', reserva.status_retirada) """
                reserva.status = data.get('status', reserva.status)

               
                db.session.commit()
                return "reserva atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar a reserva. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.args.to_dict().get('id') #pega todos os dados do Bruno
            reserva = Reservas.query.get(data) # vai procurar usuarios NO BANCO com esse id

            if reserva is None:
                return{'error': 'reserva não encontrado'}, 405
            
            db.session.delete(reserva)
            db.session.commit()
            return "reserva deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o reserva. Erro:{str(e)}", 405
        


