import sqlite3   # banco padrão do banco de dados do python
# gerencia o banco = banco.py


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuarios(
        idusuario integer primary key autoincrement,
        nome text,
        telefone text,
        email text,
        usuario text,
        senha text)""")
        self.conexao.commit()
        c.close()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_cidades(
        idcidades integer primary key autoincrement,
        nome text,
        uf text)""")
        self.conexao.commit()
        c.close()
