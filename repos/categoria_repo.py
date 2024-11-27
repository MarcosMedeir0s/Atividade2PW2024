from typing import Optional, List
from models.produto_model import CategoriaModel
from sql.categoria_sql import *
from util.db import obter_conexao

class CategoriaRepo:
    @staticmethod
    def criar_tabela():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @staticmethod
    def inserir(categoria: CategoriaModel) -> Optional[CategoriaModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_INSERIR_CATEGORIA, (
                categoria.nome,))
            if cursor.rowcount == 0:
                return None
            else:
                categoria.id = cursor.lastrowid
                return categoria
            
    @staticmethod
    def alterar(categoria: CategoriaModel) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ALTERAR_CATEGORIA, (
                categoria.nome,
                categoria.id))
            if cursor.rowcount > 0:
                return True
            else:
                return False
            
    @staticmethod
    def excluir_categoria(id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR_CATEGORIA, (id))
            if cursor.rowcount > 0:
                return True
            else:
                return False
            
    @staticmethod
    def obter_categoria_por_id(id: int) -> Optional[CategoriaModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_CATEGORIA_POR_ID, (id))
            linha = cursor.fetchone()
            if linha:
                return CategoriaModel(
                    id=linha["id"],
                    nome=linha["nome"])
            else:
                return None
            
    @staticmethod
    def obter_todos() -> List[CategoriaModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_TODAS_CATEGORIAS)
            linhas = cursor.fetchall()
            return [
                CategoriaModel(
                    id=linha["id"],
                    nome=linha["nome"]
                ) for linha in linhas]