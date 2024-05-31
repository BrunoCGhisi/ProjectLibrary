from flask import request, render_template
from database.db import db
from models.categorias import Categorias

def clientesHtmlController():
    if request.method == 'GET':
        return render_template('catHTML.html')

def categoriasController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            categorias = Categorias(data['categoria'])
            #perguntar sobre salvar a senha 
            db.session.add(categorias)
            db.session.commit()
            return 'Categorias adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    elif request.method == 'GET':
        try:
            data = Categorias.query.all()

            print([ categoria.to_dict() for categoria in data])
            # newdata peggando os dados e deixando eles cute
            newData={'categorias':[ categoria.to_dict() for categoria in data]}
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        

    elif request.method == 'PUT':
            try:
                
                data = request.get_json() #pega todos os dados
                put_categoria_id = data['id'] #pega o id dos dados que o data trouxe
                categoria = Categorias.query.get(put_categoria_id)

                if categoria is None:
                    return{'error': 'Categoria não encontrado'}, 405
                
                categoria.categoria = data.get('categoria', categoria.categoria)
               
                db.session.commit()
                return "Categoria atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar a categoria. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        try:
            data = request.get_json() #pega todos os dados do Bruno

            delete_categoria_id = data['id'] #pega o id dos dados que o data trouxe do Bruno
            categoria = Categorias.query.get(delete_categoria_id) # vai procurar usuarios NO BANCO com esse id

            if categoria is None:
                return{'error': 'Categoria não encontrado'}, 405
            
            db.session.delete(categoria)
            db.session.commit()
            return "Categoria deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o categoria. Erro:{str(e)}", 405
        


