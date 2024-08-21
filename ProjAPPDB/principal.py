import tkinter
from tkinter import *
import subprocess

class Principal:
    def __init__(self,master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", "10")#definindo uma variavel para usar quando chamada
        self.janela.pack()

        self.titulo = Label(self.janela, text="SISTEMA\n")
        self.titulo["font"] = ("Calibri", "25", "italic", "bold")
        self.titulo.pack()

        self.botao = Button(self.janela)
        self.botao["text"] = "Usuários"
        self.botao["font"] = ("Calibri", 13)
        self.botao["width"] = 14
        self.botao["command"] = self.abrir_usuarios
        self.botao.pack(side=LEFT)

        self.botao2 = Button(self.janela)
        self.botao2["text"] = "Cidades"
        self.botao2["font"] = ("Calibri", 13)
        self.botao2["width"] = 14
        self.botao2["command"] = self.abrir_cidades
        self.botao2.pack(side=LEFT)

        self.botao3 = Button(self.janela)
        self.botao3["text"] = "Clientes"
        self.botao3["font"] = ("Calibri", 13)
        self.botao3["width"] = 14
        self.botao3["command"] = self.abrir_clientes
        self.botao3.pack(side=LEFT)

        self.botao4 = Button(self.janela)
        self.botao4["text"] = "Fechar"
        self.botao4["font"] = ("Calibri", 13)
        self.botao4["width"] = 14
        self.botao4["command"] = self.janela.quit
        self.botao4.pack(side=LEFT)

    def abrir_usuarios(self):
        subprocess.run(["python", "cadusuarios.py"])

    def abrir_cidades(self):
        subprocess.run(["python", "cadcidades.py"])

    def abrir_clientes(self):
        subprocess.run(["python", "cadclientes.py"])

root = Tk()
Principal(root)
root.state("zoomed") #para a tela sempre aparecer maximizada
root.mainloop()
