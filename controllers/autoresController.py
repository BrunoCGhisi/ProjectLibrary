from flask import request
from database.db import db
from models.autores import Autores

def autoresController():
    if request.method == 'POST':
        try:
            data = request.get_json() # converte em python
            autores = Autores(data['nome'])
            db.session.add(autores)
            db.session.commit()
            return 'Autores adicionados com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    elif request.method == 'GET':
        try:
            data = Autores.query.all()
            newData = {'autores': [autor.to_dict() for autor in data]} #pegando cada obj autor, e tranformando num dicionario
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:
                id_autor = request.args.to_dict().get('id')
                autor = Autores.query.get(id_autor)
                data = request.get_json() #pega todos os dados

                
                if autor is None:
                    return{'error': 'Autor não encontrado'}, 405
                
                autor.nome = data.get('nome', autor.nome)                
                db.session.commit()
                return "Autor atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o autor. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            id_autor = request.args.to_dict().get('id') #pega o id dos dados que o data trouxe do front
            autor = Autores.query.get(id_autor) # vai procurar usuarios NO BANCO com esse id

            if autor is None:
                return{'error': 'Autor não encontrado'}, 405
            
            db.session.delete(autor)
            db.session.commit()
            return "Autor deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o autor. Erro:{str(e)}", 405
        

