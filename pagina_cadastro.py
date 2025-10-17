import ttkbootstrap as ttk
import sqlite3

class Janela_cadastro():
        def __init__(self, janela_principal):
                self.janela_c = ttk.Toplevel(janela_principal)
                self.janela_principal_d = janela_principal
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
                self.caixa_nome = ttk.Entry(self.janela_c,self.janela_c,
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
                texto_confirmar_senha = ttk.Label(self.janela_c,text= "Confirmar senha:",
                font=("Times New Roman",20),
                foreground="#7300FF")
                texto_confirmar_senha.pack(pady= (30,0))
#---------------------------------------------------------------------------------------------------------------------------
                self.caixa_confirmar_senha = ttk.Entry(self.janela_c,
                justify="center",
                font=("Times New Roman",20),
                foreground="#7300FF",
                show="*")
                self.caixa_confirmar_senha.pack(pady=(20,0))
#---------------------------------------------------------------------------------------------------------------------------
                ttk.Button(self.janela_c, text="Cadastrar-se").pack()
                self.criar_usuario()
#---------------------------------------------------------------------------------------------------------------------------
        def criar_usuario (self): 
                self.conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
                self.cursor = self.cursor.conexao()
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
                nome VARCHAR (80),
                usuario VARCHAR (20) PRIMARY KEY,
                senha VARCHAR (20)
                )""")
                self.conexao.commit()
                self.conexao.close()
                self.cursor.close()
        def inserir_usuario (self):
                self.conexao_d = sqlite3.connect("./bd_lista_tarefa.sqlite")
                self.cursor_d = self.cursor.conexao_d()
                self.cursor_d.execute("""INSERT INTO usuario
                                        (nome, usuario, senha)
                                        VALUES ("Frederico Ferdinando", "Fefe", "123")
                                        ;
                                        """)
                self.conexao_d.commit()
                self.conexao_d.close()
                self.cursor_d.close()
                
#---------------------------------------------------------------------------------------------------------------------------
        def run(self):
                self.janela_c.mainloop()

        if __name__ == "__main__":
                janela_c = Janela_cadastro()
                janela_c.run() #janela_c.janela.mainloop()