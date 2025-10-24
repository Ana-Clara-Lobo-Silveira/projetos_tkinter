import ttkbootstrap as ttk
import tkinter.messagebox
import sqlite3

class Janela_cadastro():
        def __init__(self, janela_principal_d):
                self.janela_c = ttk.Toplevel(janela_principal_d)
                self.janela_principal_d = janela_principal_d
                self.janela_c.geometry("1200x900")
                self.janela_c.resizable(0,0)
#-----------------------------------------------------------------------------------------------------------------------------
                titulo = ttk.Label(self.janela_c,
                text= "Cadastre-se",
                font=("Times New Roman",40),
                foreground="#7300FF"
                )
                titulo.pack(pady= (40,0))
#---------------------------------------------------------------------------------------------------------------------------
                texto_nome = ttk.Label(self.janela_c,text= "Nome:",
                font=("Times New Roman",20),
                foreground="#7300FF")
                texto_nome.pack(pady= (30,0))
#---------------------------------------------------------------------------------------------------------------------------
                self.caixa_nome = ttk.Entry(self.janela_c,
                justify="center",
                font=("Times New Roman",20),
                foreground="#7300FF")
                self.caixa_nome.pack(pady=(20,0))
#---------------------------------------------------------------------------------------------------------------------------
                texto_usuario = ttk.Label(self.janela_c,text= "Usuário:",
                font=("Times New Roman",20),
                foreground="#7300FF")
                texto_usuario.pack(pady= (30,0))
#---------------------------------------------------------------------------------------------------------------------------
                self.caixa_usuario = ttk.Entry(self.janela_c,
                justify="center",
                font=("Times New Roman",20),
                foreground="#7300FF")
                self.caixa_usuario.pack(pady=(20,0))
#---------------------------------------------------------------------------------------------------------------------------
                texto_senha = ttk.Label(self.janela_c,text= "Senha:",
                font=("Times New Roman",20),
                foreground="#7300FF")
                texto_senha.pack(pady= (30,0))
#---------------------------------------------------------------------------------------------------------------------------
                self.caixa_senha = ttk.Entry(self.janela_c,
                justify="center",
                font=("Times New Roman",20),
                foreground="#7300FF",
                show="*")
                self.caixa_senha.pack(pady=(20,0))
#---------------------------------------------------------------------------------------------------------------------------
#                 texto_confirmar_senha = ttk.Label(self.janela_c,text= "Confirmar senha:",
#                 font=("Times New Roman",20),
#                 foreground="#7300FF")
#                 texto_confirmar_senha.pack(pady= (30,0))
# #---------------------------------------------------------------------------------------------------------------------------
#                 self.caixa_confirmar_senha = ttk.Entry(self.janela_c,
#                 justify="center",
#                 font=("Times New Roman",20),
#                 foreground="#7300FF",
#                 show="*")
#                 self.caixa_confirmar_senha.pack(pady=(20,0))
#---------------------------------------------------------------------------------------------------------------------------
                self.criar_usuario()
                ttk.Button(self.janela_c, text="Cadastrar-se", command= self.inserir_usuario).pack()
#---------------------------------------------------------------------------------------------------------------------------
        def criar_usuario (self): 
                self.conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
                self.cursor = self.conexao.cursor()
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
                nome VARCHAR (80),
                usuario VARCHAR (20) PRIMARY KEY,
                senha VARCHAR (20)
                )""")
                self.conexao.commit()
                self.conexao.close()

        def inserir_usuario (self):

                self.nome = self.caixa_nome.get()
                self.usuario = self.caixa_usuario.get()
                self.senha = self.caixa_senha.get()

                cad = tkinter.messagebox.askyesno(title="Cadastro", message="Você deseja cadastrar-se?")
                if cad == True:
                        self.conexao_d = sqlite3.connect("./bd_lista_tarefa.sqlite")
                        self.cursor_d = self.conexao_d.cursor()
                        self.cursor_d.execute("""INSERT INTO usuario
                                                (nome, usuario, senha)
                                                VALUES (?,?,?);
                                                """,[self.nome, self.usuario, self.senha])
                        self.conexao_d.commit()
                        self.conexao_d.close()


#---------------------------------------------------------------------------------------------------------------------------
        def run(self):
                self.janela_c.mainloop()

if __name__ == "__main__":
        janela_c = Janela_cadastro("kop")
        janela_c.run() #janela_c.janela.mainloop()