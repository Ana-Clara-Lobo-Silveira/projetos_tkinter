import tkinter as tk

#Criando janela
janela = tk.Tk()
janela.title("Janela_Personalizada_Ana")
#Mudando o tamanho da tela
janela.geometry("500x500+180+0")
#Permitindo a mudança da janela
janela.resizable(True,True)
#Mudando a cor da janela
janela.configure(bg="#1b22a7")
#Mudar o icone da janela
janela.iconbitmap("01_Hello_World/computador.ico")

#Widgets
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
                 height=2)
b_bd.pack(pady=20)

#Loop para manter a janela aberta
janela.mainloop()