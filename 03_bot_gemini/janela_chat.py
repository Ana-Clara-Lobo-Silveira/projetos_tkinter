import ttkbootstrap as ttk
from bot_gemini import Boot_gemini
#------------------------------------------------------------------------------------------------------------------------------
class Janela_chat():
    def __init__(self):
        self.janela = ttk.Window(title="Ms.Gothart Alternativa", themename= "vapor")
        self.janela.iconbitmap("03_bot_gemini/bat.ico")
        self.janela.geometry("1200x800")
        self.janela.resizable(0,0)
        ti = ttk.Label(self.janela,
                      text= "Ms. Gothart",
                      font= ('Times-New-Roman', 40))
        ti.pack(pady=(20,0))

        te = ttk.Label(self.janela,
                       text= "Qual a sua dúvida sobre arte gótica?",
                       font=('Times-New-Roman',30),
                       foreground= "#9D00FF")
        te.pack(pady=(20,0))

        #ttk.Label(self.janela,
        #        text= "Qual a sua dúvida sobre arte gótica?",
        #        font=('Times-New-Roman',30),
        #        foreground= "#9D00FF").pack(pady=(20,0))

        self.c_t = ttk.Entry(self.janela)
        self.c_t.pack(pady=(20,0))

        bo = ttk.Button(self.janela,
                        text="Enviar",
                        style='primary',
                        padding= 8,
                        command=self.resposta
                        )
        bo.pack(pady=(20,0))

        self.re = ttk.Label(self.janela,
                       text = " ",
                       foreground= "#9D00FF")
        self.re.pack(pady=(20,0))

        
        self.robo = Boot_gemini()
#------------------------------------------------------------------------------------------------------------------------------
    def resposta(self):
        p = self.c_t.get()
        r = self.robo.responder(p)
        self.re.configure(text = f"{r}")
#------------------------------------------------------------------------------------------------------------------------------
    def run(self):
        self.janela.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    janela_c = Janela_chat()
    janela_c.run() #janela_c.janela.mainloop()

