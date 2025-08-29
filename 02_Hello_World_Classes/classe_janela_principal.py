import ttkbootstrap as tk

class Janela_principal:
    """Classe para a janela principal."""

    def __init__(self):
        
    #Criando janela
        self.janela = tk.Window(themename = "vapor")
        self.janela.title("Janela_Personalizada_Ana")
        #Mudando o tamanho da tela
        self.janela.geometry("500x500+180+0")
        #Permitindo a mudança da janela
        self.janela.resizable(True,True)

        #Mudar o icone da janela
        self.janela.iconbitmap("01_Hello_World/computador.ico")


        #Adicionando texto e modificando
        self.tet = tk.Label(self.janela, 
            text="Hello World", 
            background="#1b22a7", 
            foreground="#FFFFFF",
            font="Times-New-Roman")
        self.tet.pack(pady=30)

        #Vai indicar o que o usuario deve fazer
        self.l_nome = tk.Label(self.janela,
                    text="Digite o seu nome:",
                    background="#1b22a7", 
                    foreground="#FFFFFF",
                    font="Times-New-Roman",)
        self.l_nome.pack()

        #Criar uma caixa de texto
        self.c_n = tk.Entry(self.janela)
        self.c_n.pack()

        #
        self.b_bd = tk.Button(self.janela,
                    text="Desejar bom dia!!!",
                    command= self.mostrar)
        self.b_bd.pack(pady=20)

        #label que vai aparecer o bom dia
        self.res = tk.Label(self.janela,
                text="",
                background="#1b22a7",
                foreground="#FFFFFF")
        self.res.pack()

    def run(self):
        """Executa a janela, permitindo que ela fique aberta."""
#Loop para manter a janela aberta
        self.janela.mainloop()

#Widgets
    def mostrar(self):
        """ESta função coleta o noem colocado na caixa de texto e deseja um bom dia."""
        n = self.c_n.get()
        self.res.configure(text=f"Bom dia {n}!!!")