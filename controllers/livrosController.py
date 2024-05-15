from flask import request
from database.db import db
from models.livros import Livros

def livrosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            livros = Livros(data['titulo'], data['ano'], data['disponiveis'], data['estoque'],data['fk_categoria'], data['fk_autor'])
            db.session.add(livros)
            db.session.commit()
            return 'Livro adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:
            data = Livros.query.all()

            newData = {'livros': [livro.to_dict() for livro in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:

                data = request.get_json() #pega todos os dados
                put_livro_id = data['id'] #pega o id dos dados que o data trouxe
                livro = Livros.query.get(put_livro_id)

                if livro is None:
                    return{'error': 'Livro não encontrado'}, 405
                
                livro.titulo = data.get('titulo', livro.titulo)
                livro.ano = data.get('ano', livro.ano)
                livro.disponiveis = data.get('disponiveis', livro.disponiveis)
                livro.estoque = data.get('estoque', livro.estoque)
                livro.fk_categoria = data.get('fk_categoria', livro.fk_categoria)
                livro.fk_autor = data.get('fk_autor', livro.fk_autor)           

                
                db.session.commit()
                return "Livro atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o livro. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_livro_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            livro = Livros.query.get(delete_livro_id) # vai procurar usuarios NO BANCO com esse id

            if livro is None:
                return{'error': 'Livro não encontrado'}, 405
            
            db.session.delete(livro)
            db.session.commit()
            return "Livro deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o livro. Erro:{str(e)}", 405
        

