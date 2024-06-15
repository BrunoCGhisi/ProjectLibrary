from flask import request
from database.db import db
from models.pagamentos import Pagamentos
from models.multas import Multas
from models.emprestimos import Emprestimos

def pagamentosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            pagamentos = Pagamentos(data['fk_membro'], data['fk_multa'], data['data_pagamento'], data['valor'])

            data = Multas.query.all()
            
            multaData = {'multas': [multa.to_dict() for multa in data]}
            print("Multa data", multaData)
            print("Pagamentos fk multa", pagamentos.fk_multa)

            for multa_dict in multaData['multas']:
                print("Multa data", multa_dict['id_multa'])
                print("Pagamentos fk multa", pagamentos.fk_multa)

                if int(pagamentos.fk_multa) == int(multa_dict['id_multa']):
                    id_emprestimo = multa_dict['fk_emprestimo']
                    emprestimo = Emprestimos.query.get(id_emprestimo)
                    print(f"Primeiro print emprestimo.fkstatus {emprestimo.fk_status}")
                    emprestimo.fk_status = 2
                    print(f"Segundo print emprestimo.fkstatus {emprestimo.fk_status}")
                    id_multa = multa_dict['id_multa']
                    multa = Multas.query.get(id_multa)
                    multa.status = 0

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
            pagamento_id = request.args.to_dict().get('id') 
            pagamento = Pagamentos.query.get(pagamento_id)

            if pagamento is None:
                  return{'error': 'pagamento não encontrado'}, 405
            
            pagamento.fk_membro = data.get('fk_membro', pagamento.fk_membro)
            pagamento.fk_multa = data.get('fk_multa', pagamento.fk_multa)
            pagamento.data_pagamento = data.get('data_pagamento', pagamento.data_pagamento)
            pagamento.valor = data.get('valor', pagamento.valor)

            db.session.commit()
            return "pagamento atualizado com sucesso", 202

        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
    
    elif request.method == "DELETE":
        try:
            data = request.args.to_dict().get('id') 
            pagamento = Pagamentos.query.get(data)

            if pagamento is None:
                return{'error': 'pagamento não encontrado'}, 405
                
            db.session.delete(pagamento)
            db.session.commit()
            return "pagamento deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o pagamento. Erro:{str(e)}", 405
            

        

