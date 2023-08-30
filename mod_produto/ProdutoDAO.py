from fastapi import APIRouter
from mod_produto.Produto import Produto
router = APIRouter()
# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produtos"])
def get_produto(p: Produto):
    return {"msg": "get todos executado", "nome": p.nome, "descrição": p.descricao, "valor unitario": p.valor_unitario}, 200

@router.get("/produto/{id}", tags=["Produtos"])
def get_produto(id: int, p: Produto):
    return {"msg": "get um executado", "id": id, "nome": p.nome, "descrição": p.descricao, "valor unitario": p.valor_unitario}, 200

@router.post("/produto/", tags=["Produtos"])
def post_produto(p: Produto):
    return {"msg": "post executado", "nome": p.nome, "descrição": p.descricao, "valor unitario": p.valor_unitario}, 200

@router.put("/produto/{id}", tags=["Produtos"])
def put_produto(id: int, p: Produto):
    return {"msg": "put executado" , "id": id, "nome": p.nome, "descrição": p.descricao, "valor unitario": p.valor_unitario}, 201

@router.delete("/produto/{id}", tags=["Produtos"])
def delete_produto(id: int, p: Produto):
    return {"msg": "delete executado", "id": id, "nome": p.nome, "descrição": p.descricao, "valor unitario": p.valor_unitario}, 201