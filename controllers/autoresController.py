from flask import request
from database.db import db
from models.autores import Autores

def autoresController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            autores = Autores(data['nome'])
            db.session.add(autores)
            db.session.commit()
            return 'Autores adicionados com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Autores.query.all()

            newData = {'autores': [autor.to_dict() for autor in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:
                data = request.get_json() #pega todos os dados
                put_autor_id = data['id'] #pega o id dos dados que o data trouxe
                autor = Autores.query.get(put_autor_id)
                if autor is None:
                    return{'error': 'Autor não encontrado'}, 405
                
                autor.nome = data.get('nome', autor.nome)

              #  autor.cargos_id = data.get('cargos_id', autor.cargos_id)
                
                db.session.commit()
                return "Autor atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o autor. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_autor_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            autor = Autores.query.get(delete_autor_id) # vai procurar usuarios NO BANCO com esse id

            if autor is None:
                return{'error': 'Autor não encontrado'}, 405
            
            db.session.delete(autor)
            db.session.commit()
            return "Autor deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o autor. Erro:{str(e)}", 405
        

