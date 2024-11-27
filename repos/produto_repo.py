from typing import Optional, List
from models.produto_model import *
from sql.produto_sql import *
from util.db import obter_conexao


class ProdutoRepo:
    @staticmethod
    def criar_tabela():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @staticmethod
    def inserir(produto: ProdutoModel) -> Optional[ProdutoModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_INSERIR, (
                produto.nome,
                produto.categoria,
                produto.descricao,
                produto.preco,
                produto.estoque))
            if cursor.rowcount == 0:
                return None
            else:
                produto.id = cursor.lastrowid
                return produto

    @staticmethod
    def alterar(produto: ProdutoModel) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ALTERAR, (
                produto.nome,
                produto.categoria,
                produto.descricao,
                produto.preco,
                produto.estoque,
                produto.id))
            if cursor.rowcount > 0:
                return True
            else:
                return False

    @staticmethod
    def excluir(id_produto: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR, (id_produto,))
            if cursor.rowcount > 0:
                return True
            else:
                return False

    @staticmethod
    def obter_por_id(id_produto: int) -> Optional[ProdutoModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_POR_ID, (id_produto,))
            linha = cursor.fetchone()
            if linha:
                return ProdutoModel(
                    id=linha["id"],
                    nome=linha["nome"],
                    categoria=linha["categoria"],
                    descricao=linha["descricao"],
                    preco=linha["preco"],
                    estoque=linha["estoque"])
            else:
                return None

    @staticmethod
    def obter_todos() -> List[ProdutoModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_TODOS)
            linhas = cursor.fetchall()
            return [
                ProdutoModel(
                    id=linha["id"],
                    nome=linha["nome"],
                    categoria=linha["categoria"],
                    descricao=linha["descricao"],
                    preco=linha["preco"],
                    estoque=linha["estoque"]
                ) for linha in linhas]

    @staticmethod
    def inserir_produtos_iniciais():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) AS count FROM produto;")
            count = cursor.fetchone()["count"]
            if count > 0:
                return
            produtos_iniciais = [
                ("Banana", "Frutas", "Banana fresca, colhida na época certa, doce e ideal para vitaminas e lanches.", 1.99, 100),
                ("Abacaxi", "Frutas", "Abacaxi maduro, suculento e doce, perfeito para sobremesas ou sucos refrescantes.", 3.49, 50),
                ("Mamão", "Frutas", "Mamão papaia de polpa alaranjada e sabor delicado, ideal para um café saudável.", 2.89, 80),
                ("Maçã", "Frutas", "Maçã gala de textura crocante e sabor suave, excelente para lanches nutritivos.", 1.50, 200),
                ("Goiaba", "Frutas", "Goiaba vermelha fresca, rica em vitamina C, ótima para sucos e doces caseiros.", 2.00, 150),
                ("Laranja", "Frutas", "Laranja pera doce e suculenta, rica em vitaminas e ideal para suco natural.", 1.25, 300),
                ("Abacate", "Frutas", "Abacate manteiga com polpa cremosa, ideal para saladas e receitas saudáveis.", 4.50, 40),
                ("Abacate Especial", "Frutas", "Abacate premium, com textura suave e sabor intenso, perfeito para guacamole.", 5.99, 30),
                ("Abóbora", "Legumes e Vegetais", "Abóbora moranga de cor viva, perfeita para sopas, purês e receitas tradicionais.", 1.80, 90),
                ("Abobrinha", "Legumes e Vegetais", "Abobrinha italiana fresca e saborosa, ótima para refogados, grelhados e saladas.", 2.20, 60),
                ("Repolho", "Legumes e Vegetais", "Repolho verde crocante e versátil, ideal para saladas, cozidos ou refogados.", 1.10, 120),
                ("Alho", "Legumes e Vegetais", "Alho fresco e aromático, essencial para temperar e realçar o sabor dos pratos.", 10.00, 20)]
            for nome, categoria, descricao, preco, estoque in produtos_iniciais:
                cursor.execute(SQL_INSERIR, (nome, categoria, descricao, preco, estoque))
            db.commit()