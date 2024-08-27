import tkinter
from tkinter import *

class Cidades:
    def __init__(self,master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)
        self.janela.pack()

    #TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:")
        self.titulo["font"] = ("Calibri", "30", "italic", "bold")
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Cadastro de Cidades\n")
        self.titulo2["font"] = ("Calibri", "20", "italic")
        self.titulo2.pack()

        # IDUSUARIO
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="Buscar ID:     \n", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 18
        self.id["font"] = self.fontepadrao
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2, font=self.fontebotao)
        self.buscar["text"] = "Buscar"
        self.buscar["width"] = 10
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.buscarCidades  # BANCO DE DADOS


    #NOME CIDADE
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome Cidade:     \n", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 24
        self.nome["font"] = self.fontepadrao
        self.nome.pack(side=LEFT)

    #ESTADO
        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.ufLabel = Label(self.janela4, text="UF:     \n", font=self.fontepadrao)
        self.ufLabel.pack(side=LEFT)
        self.uf = Entry(self.janela4)
        self.uf["width"] = 32
        self.uf["font"] = self.fontepadrao
        self.uf.pack(side=LEFT)



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

        self.excluir = Button(self.janela8, font=self.fontebotao)
        self.excluir["text"] = "Fechar"
        self.excluir["width"] = 10  # largura
        self.excluir.pack(side=LEFT)

        self.voltar = Button(self.janela8, font=self.fontebotao)
        self.voltar["text"] = "Voltar"
        self.voltar["width"] = 10  # largura
        self.voltar["command"] = self.janela.quit
        self.voltar.pack(side=LEFT)

        def buscarCidades(self):
            user = Cidades()
            idcidades = self.id.get()
            self.idLabel["text"] = user.selectUser(idcidades)
            self.id.delete(0, END)
            self.id.insert(INSERT, user.idcidades)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, user.nome)
            self.uf.delete(0, END)
            self.uf.insert(INSERT, user.uf)

root = Tk()
Cidades(root)
root.state("zoomed") #para a tela sempre aparecer maximizada
root.mainloop()



