from banco import Banco
# manutenção dos dados: inclusão, alteração, excluir, consulta


class Cidades(object):

    def __init__(self, idcidades=0, nome="", uf=""):
        self.info = {}
        self.idcidades = idcidades
        self.nome = nome
        self.uf = uf

    def insertCid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_cidades (nome, uf) values (?, ?)",
                      (self.nome, self.uf))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateCid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_cidades set nome = ?, uf = ?",
                      (self.nome, self.uf))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteCid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tbl_cidades where idcidades = ?", (self.idcidades,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectCid(self, idcidades):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from tbl_cidades where idcidades = ?", (idcidades,))
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.uf = linha[2]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
