from flask import request
from database.db import db
from models.autores_livros import Autores_livros

def autores_livrosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            autores_livros = Autores_livros(data['id_autor_livro'], data['fk_autor'], data['fk_livro'])
            db.session.add(autores_livros)
            db.session.commit()
            return 'autores_livros adicionados com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    if request.method == 'GET':
        try:

            data = Autores_livros.query.all()
            newData = {'autores_livros': [autor_livro.to_dict() for autor_livro in data]} #pe gando os dados e deixando eles cute
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:
                id_autor_livro = request.args.to_dict().get('id')
                autor_livro = Autores_livros.query.get(id_autor_livro)
                data = request.get_json()

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
            data = request.args.to_dict().get('id') #pega todos os dados do Bruno
            autor_livro = Autores_livros.query.get(data) # vai procurar usuarios NO BANCO com esse id

            if autor_livro is None:
                return{'error': 'Autor não encontrado'}, 405
            
            db.session.delete(autor_livro)
            db.session.commit()
            return "Autor deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o autor. Erro:{str(e)}", 405
        

