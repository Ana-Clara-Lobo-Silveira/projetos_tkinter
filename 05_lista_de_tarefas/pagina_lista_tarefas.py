import ttkbootstrap as ttk
import tkinter as tk
from tkinter import Listbox
import tkinter.messagebox
import sqlite3
from pagina_login import Janela_login

class Janela_pagina:
    def __init__(self):
        self.pagina = ttk.Window (title="Lista de tarefas", themename="vapor")
        self.pagina.geometry("1200x900")
        self.pagina.resizable(0,0)
#-----------------------------------------------------------------------------------------------------------------------------
        titulo = ttk.Label(text= "Lista de tarefas:",
                           font=("Times New Roman",35),
                           foreground="#7300FF"
                           )
        titulo.pack(pady= (40,0))
#-----------------------------------------------------------------------------------------------------------------------------
        frame_botao = ttk.Frame()
        frame_botao.pack()

        ttk.Button(frame_botao,text="Adicionar tarefa",width=30,padding = 9,command= self.adicionar_tarefa).pack(pady=(20,0), padx=20,side="right")
        self.caixa_adicionar = ttk.Entry(frame_botao, width=50,font=("Times New Roman",15))
        self.caixa_adicionar.pack(pady=(20,0), padx=20,side="left")
#-----------------------------------------------------------------------------------------------------------------------------
        self.lista = tk.Listbox (self.pagina,height = 20, width=70)
        self.lista.pack(pady=(30,0))
#-----------------------------------------------------------------------------------------------------------------------------
        frame_botao_d = ttk.Frame(style="Vapor")
        frame_botao_d.pack()

        ttk.Button(frame_botao_d,text="Excluir",width=40,padding = 9, style = "danger", command= self.excluir).pack(pady=(30,0), padx=20,side="left")

        ttk.Button(frame_botao_d,text="Feito",width=40,padding = 9, command= self.marcar).pack(pady=(30,0), padx=20,side="right")
#-1----------------------------------------------------------------------------------------------------------------------------
        self.conexao = sqlite3.connect("05_lista_de_tarefas/bd_lista_tarefa.sqlite")
        self.cursor = self.conexao.cursor()

        self.sql_para_criar_tabela = """
                                    CREATE TABLE IF NOT EXISTS tarefas (
                                    codigo integer primary key autoincrement,
                                    tarefa varchar(200)
                                    );
                                """
        
        self.cursor.execute(self.sql_para_criar_tabela) #criar tabela
        self.conexao.commit() #comitar as alterações
        self.cursor.close() #desligar o cursor e a conexão
        self.conexao.close()

        self.atualizar()

        janela_login = Janela_login(self.pagina)
        self.pagina.withdraw()

#-3----------------------------------------------------------------------------------------------------------------------------
    def atualizar (self):
        self.conexaot = sqlite3.connect("05_lista_de_tarefas/bd_lista_tarefa.sqlite")
        self.cursort = self.conexaot.cursor()
        self.sql_atualizar_tarefas = """
                                        SELECT codigo,tarefa FROM tarefas;
                                    """
        self.cursort.execute(self.sql_atualizar_tarefas)
        self.lista_tarefas = self.cursort.fetchall()
        self.cursort.close()
        self.conexaot.close()

        for linha in self.lista_tarefas:
            self.lista.insert("end", linha[1])
#-2----------------------------------------------------------------------------------------------------------------------------
    def adicionar_tarefa(self):
        self.caixa = self.caixa_adicionar.get()
        if self.caixa == "":
            tkinter.messagebox.showerror(title="Erro", message="É necessário inserir uma tarefa")
        else:
            self.lista.insert(tk.END,self.caixa)

            self.conexaod = sqlite3.connect("05_lista_de_tarefas/bd_lista_tarefa.sqlite")
            self.cursord = self.conexaod.cursor()

            self.sql_insert = ('''
                            INSERT INTO tarefas (tarefa)
                            VALUES (?)
                            ''')
            
            self.cursord.execute(self.sql_insert,[self.caixa])
            self.conexaod.commit()
            self.cursord.close() #desligar o cursor e a conexão
            self.conexaod.close()
#---------------------------------------------------------------------------------------------------------------------------

#-4----------------------------------------------------------------------------------------------------------------------------
    def excluir(self):
        self.tarefaq = self.lista.curselection()
        if self.tarefaq:
            self.tarefaqq = self.lista.get(self.tarefaq)
            self.lista.delete(self.tarefaq)

        else:
            tk.messagebox.showerror(message = "Selecione um item para excluir")

        self.conexaoq = sqlite3.connect("05_lista_de_tarefas/bd_lista_tarefa.sqlite")
        self.cursorq = self.conexaoq.cursor()
        self.sql_delete = """
                            DELETE FROM tarefas WHERE tarefa = (?)
                            """
        self.cursorq.execute(self.sql_delete, [self.tarefaqq])
        self.conexaoq.commit()
        self.cursorq.close()
        self.conexaoq.close()
#-5----------------------------------------------------------------------------------------------------------------------------
    def marcar(self):
        self.marcado = self.lista.curselection()
        if self.marcado:
            self.tarefa = self.lista.get(self.marcado)
            self.lista.delete(self.marcado)
            self.lista.insert(self.marcado, self.tarefa + "           ★ CONCLUÍDO")
        else:
            tk.messagebox.showerror(message = "Selecione um item para destacar como feito")

        ###############################################################################
        self.conexaoc = sqlite3.connect("05_lista_de_tarefas/bd_lista_tarefa.sqlite")
        self.cursorc = self.conexaoc.cursor()
        
        self.sql_update =   """
                                UPDATE tarefas SET tarefa = (?) WHERE tarefa = (?)
                            """

        self.cursorc.execute(self.sql_update,[self.tarefa + "- ★ CONCLUÍDO",self.tarefa])
        self.conexaoc.commit()
        self.cursorc.close() #desligar o cursor e a conexão
        self.conexaoc.close()



#-----------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------
    def run(self):
        self.pagina.mainloop()

if __name__ == "__main__":
    janela_p = Janela_pagina()
    janela_p.run() #janela_c.janela.mainloop()