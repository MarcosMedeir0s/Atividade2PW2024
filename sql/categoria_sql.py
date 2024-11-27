SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL
    );
"""

SQL_INSERIR_CATEGORIA = """
    INSERT INTO categoria (nome) 
    VALUES (?);
"""

SQL_ALTERAR_CATEGORIA = """
    UPDATE categoria 
    SET nome = ? 
    WHERE id = ?;
"""

SQL_EXCLUIR_CATEGORIA = """
    DELETE FROM categoria 
    WHERE id = ?;
"""

SQL_OBTER_CATEGORIA_POR_ID = """
    SELECT id, nome 
    FROM categoria 
    WHERE id = ?;
"""

SQL_OBTER_TODAS_CATEGORIAS = """
    SELECT id, nome 
    FROM categoria 
    ORDER BY nome;
"""