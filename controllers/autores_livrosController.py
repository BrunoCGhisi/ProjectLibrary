from flask import request
from database.db import db
from models.autores_livros import Autores_livros

def Autores_livrosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            Autores_livros = Autores_livros(data['nome'])
            db.session.add(Autores_livros)
            db.session.commit()
            return 'Autores adicionados com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Autores_livros.query.all()

            newData = {'autores': [autor_livro.to_dict() for autor_livro in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:
                data = request.get_json() #pega todos os dados
                put_autor_id = data['id'] #pega o id dos dados que o data trouxe
                autor_livro = Autores_livros.query.get(put_autor_id)
                if autor_livro is None:
                    return{'error': 'Autor não encontrado'}, 405
                
                autor_livro.nome = data.get('nome', autor_livro.nome)

              #  autor.cargos_id = data.get('cargos_id', autor.cargos_id)
                
                db.session.commit()
                return "Autor atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o autor. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_autor_livro_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            autor_livro = Autores_livros.query.get(delete_autor_livro_id) # vai procurar usuarios NO BANCO com esse id

            if autor_livro is None:
                return{'error': 'Autor não encontrado'}, 405
            
            db.session.delete(autor_livro)
            db.session.commit()
            return "Autor deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o autor. Erro:{str(e)}", 405
        

