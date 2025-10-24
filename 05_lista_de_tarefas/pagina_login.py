import ttkbootstrap as ttk
import sqlite3
import tkinter.messagebox
from pagina_cadastro import Janela_cadastro

class Janela_login:
        def __init__(self,janela_principal):
                self.janela = ttk.Toplevel(janela_principal)
                self.janela_principal = janela_principal
                self.janela.geometry("1200x800")
                self.janela.resizable(0,0)

                self.janela.protocol("WM_DELETE_WINDOW",self.sair)
                #---------------------------------------------------------------------------------------------------------------------------
                titulo = ttk.Label(self.janela,
                text= "Bem-vindo! Realize seu login logo abaixo:",
                        font=("Times New Roman",35),
                        foreground="#7300FF")
                titulo.pack(pady= (40,0))
                #---------------------------------------------------------------------------------------------------------------------------
                texto_usuario = ttk.Label(self.janela,text= "Usuário",
                        font=("Times New Roman",30),
                        foreground="#7300FF")
                texto_usuario.pack(pady= (30,0))
                #---------------------------------------------------------------------------------------------------------------------------
                self.caixa_usuario = ttk.Entry(self.janela,
                                justify="center",
                        font=("Times New Roman",20),
                        foreground="#7300FF")
                self.caixa_usuario.pack(pady=(20,0))
                #---------------------------------------------------------------------------------------------------------------------------
                texto_senha = ttk.Label(self.janela,text= "Senha",
                        font=("Times New Roman",30),
                        foreground="#7300FF")
                texto_senha.pack(pady= (30,0))
                #---------------------------------------------------------------------------------------------------------------------------
                self.caixa_senha = ttk.Entry(self.janela,
                                justify="center",
                        font=("Times New Roman",20),
                        foreground="#7300FF",
                        show="*")
                self.caixa_senha.pack(pady=(20,0))
                #--------------------------------------------------------------------------------------------------------------------------
                frame_botao = ttk.Frame(self.janela)
                frame_botao.pack()
                #---------------------------------------------------------------------------------------------------------------------------
                ttk.Button(frame_botao,text="Entrar",width=20,padding = 9,command=self.enviado).pack(pady=(20,0),side="bottom",padx=20)
                ttk.Button(frame_botao,text="Sair",width=20,padding=9,command=self.sair).pack(pady=(20,0),side="right",padx=20)
                ttk.Button(frame_botao,text="Cadastre-se",width=20,padding=9,command= self.j_cadastro).pack(pady=(20,0),side="left",padx=20)
                #---------------------------------------------------------------------------------------------------------------------------
                self.mostrar = ttk.Label(self.janela,
                                text=" ",
                        font=("Times New Roman",20),
                        foreground="#7300FF")
                self.mostrar.pack(pady=(20,0))

        def j_cadastro(self):
                self.janela_cadastro = Janela_cadastro(self.janela)
              
        #---------------------------------------------------------------------------------------------------------------------------
        def sair(self):
                resposta = tkinter.messagebox.askyesno(title="Sair", message="Você realmente deseja sair?")
                if resposta == True:
                        exit()


        def enviado(self):

                self.c_u = self.caixa_usuario.get()
                self.c_s = self.caixa_senha.get()

                self.conexao_a = sqlite3.connect("./bd_lista_tarefa.sqlite")
                self.cursor_a = self.conexao_a.cursor()
                self.cursor_a.execute ("""SELECT usuario, nome from usuario
                                        WHERE usuario = ? and senha= ?;""",
                                    [self.c_u,self.c_s]
                                    )
                
                resultado_verificacao = self.cursor_a.fetchone()

                self.conexao_a.close()

                #---------------------------------------------------------------------------------------------------------------------------
                if resultado_verificacao:
                        self.mostrar.configure(text="Login efetuado")
                        self.janela.destroy()
                        self.janela_principal.deiconify()
                else:
                        self.mostrar.configure(text="Login incorreto")
                        tkinter.messagebox.showerror(title="Login", message="Login incorreto, confira se todos os dados foram preenchidos corretamente")


if __name__ == "__main__":
        janela_l = Janela_login("")
        janela_l.janela.mainloop()