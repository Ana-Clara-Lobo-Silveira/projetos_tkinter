import ttkbootstrap as ttk
from tkinter import Listbox

class Janela_pagina:
    def __init__(self):
        self.pagina = ttk.Window (title="Lista de tarefas", themename="vapor")
        self.pagina.geometry("1200x800")
        self.pagina.resizable(0,0)

        titulo = ttk.Label(text= "Minha lista de tarefas:",
                           font=("Times New Roman",35),
                           foreground="#7300FF")
        titulo.pack(pady= (40,0))

        frame_botao = ttk.Frame()
        frame_botao.pack()

        ttk.Button(frame_botao,text="Adicionar tarefa",width=30,padding = 9).pack(pady=(20,0), padx=20,side="left")

    def run(self):
        self.pagina.mainloop()

if __name__ == "__main__":
    janela_p = Janela_pagina()
    janela_p.run() #janela_c.janela.mainloop()