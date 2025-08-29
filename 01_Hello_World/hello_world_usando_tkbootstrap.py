import ttkbootstrap as tk

#Criando janela
janela = tk.Window(themename = "vapor")
janela.title("Janela_Personalizada_Ana")
#Mudando o tamanho da tela
janela.geometry("500x500+180+0")
#Permitindo a mudança da janela
janela.resizable(True,True)

#Mudar o icone da janela
janela.iconbitmap("01_Hello_World/computador.ico")

#Widgets
def mostrar():
    """ESta função coleta o noem colocado na caixa de texto e deseja um bom dia."""
    n = c_n.get()
    res.configure(text=f"Bom dia {n}!!!")
#Adicionando texto e modificando
tet = tk.Label(janela, 
               text="Hello World", 
               background="#1b22a7", 
               foreground="#FFFFFF",
               font="Times-New-Roman")
tet.pack(pady=30)

#Vai indicar o que o usuario deve fazer
l_nome = tk.Label(janela,
                text="Digite o seu nome:",
                background="#1b22a7", 
                foreground="#FFFFFF",
                font="Times-New-Roman",)
l_nome.pack()

#Criar uma caixa de texto
c_n = tk.Entry(janela)
c_n.pack()

#
b_bd = tk.Button(janela,
                 text="Desejar bom dia!!!",
                 command= mostrar)
b_bd.pack(pady=20)

#label que vai aparecer o bom dia
res = tk.Label(janela,
               text="",
               background="#1b22a7",
               foreground="#FFFFFF")
res.pack()

#Loop para manter a janela aberta
janela.mainloop()
