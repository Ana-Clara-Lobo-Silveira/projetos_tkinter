import ttkbootstrap as ttk
import tkinter.messagebox

class Janela_login:
    def __init__(self):
        self.janela = ttk.Window(title="Login",themename="vapor")
        self.janela.geometry("1200x800")
        self.janela.resizable(0,0)
#---------------------------------------------------------------------------------------------------------------------------
        titulo = ttk.Label(text= "Bem-vindo! Realize seu login logo abaixo:",
                           font=("Times New Roman",35),
                           foreground="#7300FF")
        titulo.pack(pady= (40,0))
#---------------------------------------------------------------------------------------------------------------------------

        texto_usuario = ttk.Label(text= "Usuário",
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

        texto_senha = ttk.Label(text= "Senha",
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
        frame_botao = ttk.Frame()
        frame_botao.pack()
#---------------------------------------------------------------------------------------------------------------------------
        ttk.Button(frame_botao,text="Entrar",width=30,padding = 9,command=self.enviado).pack(pady=(20,0),side="left",padx=20)
        ttk.Button(frame_botao,text="Sair",width=30,padding=9,command=self.janela.destroy).pack(pady=(20,0),side="right",padx=20)
#---------------------------------------------------------------------------------------------------------------------------

        self.mostrar = ttk.Label(self.janela,
                                 text=" ",
                                font=("Times New Roman",20),
                                foreground="#7300FF")
        self.mostrar.pack(pady=(20,0))
#---------------------------------------------------------------------------------------------------------------------------
    def enviado(self):

        self.c_u = self.caixa_usuario.get()
        self.c_s = self.caixa_senha.get()
#---------------------------------------------------------------------------------------------------------------------------
        if self.c_u == "" or self.c_s == "":
            tkinter.messagebox.showerror(title="Erro", message="Confira se todos os dados foram preenchidos corretamente")
        else:
            if self.c_u == "Godofredo" and self.c_s == "amogirassol":
                self.mostrar.configure(text="Login efetuado")
                tkinter.messagebox.showinfo(title="Login", message="Login efetuado!")
            else:
                self.mostrar.configure(text="Login incorreto")
                tkinter.messagebox.showerror(title="Login", message="Login incorreto, confira se todos os dados foram preenchidos corretamente")

    def run(self):
        self.janela.mainloop()  


if __name__ == "__main__":
    janela_c = Janela_login()
    janela_c.run() #janela_c.janela.mainloop()