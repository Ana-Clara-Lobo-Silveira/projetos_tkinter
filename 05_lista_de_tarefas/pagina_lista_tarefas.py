import ttkbootstrap as ttk
import tkinter as tk
from tkinter import Listbox

class Janela_pagina:
    def __init__(self):
        self.pagina = ttk.Window (title="Lista de tarefas", themename="vapor")
        self.pagina.geometry("1200x800")
        self.pagina.resizable(0,0)

        titulo = ttk.Label(text= "Lista de tarefas:",
                           font=("Times New Roman",35),
                           foreground="#7300FF"
                           )
        titulo.pack(pady= (40,0))

        frame_botao = ttk.Frame()
        frame_botao.pack()

        ttk.Button(frame_botao,text="Adicionar tarefa",width=30,padding = 9,command= self.adicionar_tarefa).pack(pady=(20,0), padx=20,side="right")
        self.caixa_adicionar = ttk.Entry(frame_botao, width=50,font=("Times New Roman",15))
        self.caixa_adicionar.pack(pady=(20,0), padx=20,side="left")

        self.lista = tk.Listbox (self.pagina,height = 20, width=70)
        self.lista.pack(pady=(30,0))

        frame_botao_d = ttk.Frame()
        frame_botao_d.pack()

        ttk.Button(frame_botao_d,text="Excluir",width=40,padding = 9).pack(pady=(30,0), padx=20,side="left")
        ttk.Button(frame_botao_d,text="Concluir",width=40,padding = 9).pack(pady=(30,0), padx=20,side="right")
        

    def adicionar_tarefa(self):
        caixa = self.caixa_adicionar.get
        self.lista.insert(tk.END,caixa)

    def run(self):
        self.pagina.mainloop()

if __name__ == "__main__":
    janela_p = Janela_pagina()
    janela_p.run() #janela_c.janela.mainloop()