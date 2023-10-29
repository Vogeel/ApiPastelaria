from fastapi import APIRouter
from mod_produto.Produto import Produto
import db
from mod_produto.ProdutoModel import ProdutoDB
# import da segurança
from fastapi import Depends
import security

router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] )

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produtos"])
def get_produto():
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).all()
        return dados, 200
    
    except Exception as e:
        return {"erro:": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produtos"])
def get_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produtos"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()
        dados = ProdutoDB(None, corpo.nome, corpo.descricao, corpo.foto, corpo.valor_unitario)
        session.add(dados)
        session.commit()
        return{"id": dados.id_produto}, 200
    except Exception as e:
        return{"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produtos"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        dados.valor_unitario = corpo.valor_unitario
        session.add(dados)
        session.commit()
        return{"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()


@router.delete("/produto/{id}", tags=["Produtos"])
def delete_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()
        return{"id": dados.id_produto,
               "Produto deletado": dados.nome}, 200
    except Exception as e:
        session.rollback()
        return{"erro": str(e)}, 400
    finally:
        session.close()