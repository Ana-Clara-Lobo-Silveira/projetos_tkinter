import tkinter as tk

#Criando janela
janela = tk.Tk()
janela.title("Janela_Personalizada_Ana")
#Mudando o tamanho da tela
janela.geometry("500x500+180+0")
#Mudando a cor da janela
janela.configure(bg="#1b22a7")
#Adicionando texto
tet = tk.Label(janela, text="Hello World")
tet.pack()
#Mudar o icone da janela
janela.iconbitmap("01_Hello_World/computador.ico")
#Loop para manter a janela aberta
janela.mainloop()