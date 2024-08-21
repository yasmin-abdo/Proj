import tkinter
from tkinter import *
import subprocess

class Usuario:
    def __init__(self,master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)
        self.janela.pack()

    #TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:")
        self.titulo["font"] = ("Calibri", "30", "italic", "bold")
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Cadastro de Clientes\n")
        self.titulo2["font"] = ("Calibri", "20", "italic")
        self.titulo2.pack()


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


    #CPF
        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuLabel = Label(self.janela6, text="CPF:       \n", font=self.fontepadrao)
        self.usuLabel.pack(side=LEFT)
        self.usu = Entry(self.janela6)
        self.usu["width"] = 30
        self.usu["font"] = self.fontepadrao
        self.usu.pack(side=LEFT)


    #CIDADE
        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senhaLabel = Label(self.janela7, text="Cidade:    \n", font=self.fontepadrao)
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

        self.alt = Button(self.janela8, font=self.fontebotao)
        self.alt["text"] = "Alterar"
        self.alt["width"] = 10
        self.alt.pack(side=LEFT)

        self.voltar = Button(self.janela8, font=self.fontebotao)
        self.voltar["text"] = "Voltar"
        self.voltar["width"] = 10  # largura
        self.voltar["command"] = self.abrir_principal
        self.voltar.pack(side=LEFT)

        self.sair = Button(self.janela8, font=self.fontebotao)
        self.sair["text"] = "Fechar"
        self.sair["width"] = 10  # largura
        self.sair["command"] = self.janela.quit
        self.sair.pack(side=LEFT)

    def abrir_principal (self):
        subprocess.run(["python", "principal.py"])


root = Tk()
Usuario(root)
root.state("zoomed") #para a tela sempre aparecer maximizada
root.mainloop()



