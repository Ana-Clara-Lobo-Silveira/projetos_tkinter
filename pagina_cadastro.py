import ttkbootstrap as ttk

class Janela_cadastro:
    def __init__(self):
        self.janela_c = ttk.Window (title="Cadastro", themename="vapor")
        self.janela_c.geometry("1200x900")
        self.janela_c.resizable(0,0)
#-----------------------------------------------------------------------------------------------------------------------------
        titulo = ttk.Label(text= "Cadastro",
                           font=("Times New Roman",40),
                           foreground="#7300FF"
                           )
        titulo.pack(pady= (40,0))
#---------------------------------------------------------------------------------------------------------------------------
        texto_nome = ttk.Label(text= "Nome:",
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
        texto_usuario = ttk.Label(text= "Usuário:",
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
        texto_senha = ttk.Label(text= "Senha:",
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
        texto_confirmar_senha = ttk.Label(text= "Confirmar senha:",
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
    def run(self):
        self.janela_c.mainloop()

if __name__ == "__main__":
    janela_c = Janela_cadastro()
    janela_c.run() #janela_c.janela.mainloop()