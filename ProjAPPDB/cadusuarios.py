from tkinter import *
# import subprocess
from usuarios import Usuarios


class Usuario:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)
        self.janela.pack()

    #TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:")
        self.titulo["font"] = ("Calibri", "30", "italic", "bold")
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Usuários\n")
        self.titulo2["font"] = ("Calibri", "20", "italic")
        self.titulo2.pack()

    #IDUSUARIO
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="idUsuário:     \n", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 18
        self.id["font"] = self.fontepadrao
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2, font=self.fontebotao)
        self.buscar["text"] = "Buscar"
        self.buscar["width"] = 10
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.buscarUsuario  # BANCO DE DADOS

    #NOME
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome:     \n", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 30
        self.nome["font"] = self.fontepadrao
        self.nome.pack(side=LEFT)

    #TELEFONE
        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telLabel = Label(self.janela4, text="Telefone: \n", font=self.fontepadrao)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela4)
        self.tel["width"] = 30
        self.tel["font"] = self.fontepadrao
        self.tel.pack(side=LEFT)

    #EMAIL
        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.emailLabel = Label(self.janela5, text="E-mail:    \n", font=self.fontepadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 30
        self.email["font"] = self.fontepadrao
        self.email.pack(side=LEFT)

    #USUARIO
        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuLabel = Label(self.janela6, text="Usuário:  \n", font=self.fontepadrao)
        self.usuLabel.pack(side=LEFT)
        self.usu = Entry(self.janela6)
        self.usu["width"] = 30
        self.usu["font"] = self.fontepadrao
        self.usu.pack(side=LEFT)

    #SENHA
        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senhaLabel = Label(self.janela7, text="Senha:    \n", font=self.fontepadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7)
        self.senha["width"] = 30
        self.senha["font"] = self.fontepadrao
        self.senha["show"] = "*"  # pra não mostrar a senha
        self.senha.pack(side=LEFT)

    #BOTÕES
        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8, font=self.fontebotao)
        self.inserir["text"] = "Inserir"
        self.inserir["width"] = 10
        self.inserir.pack(side=LEFT)
        self.inserir["command"] = self.inserirUsuario  # BANCO DE DADOS

        self.alt = Button(self.janela8, font=self.fontebotao)
        self.alt["text"] = "Alterar"
        self.alt["width"] = 10
        self.alt.pack(side=LEFT)
        self.alt["command"] = self.alterarUsuario  # BANCO DE DADOS

        self.excluir = Button(self.janela8, font=self.fontebotao)
        self.excluir["text"] = "Excluir"
        self.excluir["width"] = 10  # largura
        self.excluir.pack(side=LEFT)
        self.excluir["command"] = self.excluirUsuario  # BANCO DE DADOS

        self.voltar = Button(self.janela8, font=self.fontebotao)
        self.voltar["text"] = "Voltar"
        self.voltar["width"] = 10  # largura
        self.voltar["command"] = self.janela.quit
    # ooouu self.voltar["command"] = self.abrir_principal
        self.voltar.pack(side=LEFT)

    # def abrir_principal(self):
        # subprocess.run(["python", "principal.py"])

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.id.get()
        self.idLabel["text"] = user.selectUser(idusuario)
        self.id.delete(0, END)
        self.id.insert(INSERT, user.idusuario)
        self.nome.delete(0, END)
        self.nome.insert(INSERT, user.nome)
        self.tel.delete(0, END)
        self.tel.insert(INSERT, user.telefone)
        self.email.delete(0, END)
        self.email.insert(INSERT, user.email)
        self.usu.delete(0, END)
        self.usu.insert(INSERT, user.usuario)
        self.senha.delete(0, END)
        self.senha.insert(INSERT, user.senha)

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.tel.get()
        user.email = self.email.get()
        user.usuario = self.usu.get()
        user.senha = self.senha.get()
        self.idLabel["text"] = user.insertUser()
        self.id.delete(0, END)
        self.nome.delete(0, END)
        self.tel.delete(0, END)
        self.email.delete(0, END)
        self.usu.delete(0, END)
        self.senha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.id.get()
        user.nome = self.nome.get()
        user.telefone = self.tel.get()
        user.email = self.email.get()
        user.usuario = self.usu.get()
        user.senha = self.senha.get()
        self.idLabel["text"] = user.updateUser()
        self.id.delete(0, END)
        self.nome.delete(0, END)
        self.tel.delete(0, END)
        self.email.delete(0, END)
        self.usu.delete(0, END)
        self.senha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.id.get()
        self.idLabel["text"] = user.deleteUser()
        self.id.delete(0, END)
        self.nome.delete(0, END)
        self.tel.delete(0, END)
        self.email.delete(0, END)
        self.usu.delete(0, END)
        self.senha.delete(0, END)


root = Tk()
Usuario(root)
root.state("zoomed")  # para a tela sempre aparecer maximizada
root.mainloop()
