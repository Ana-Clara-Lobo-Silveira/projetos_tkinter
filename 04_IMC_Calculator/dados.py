import ttkbootstrap as ttk

class Janela_dados:
        def __init__(self):
                self.janela = ttk.Window(title="Calculadora de IMC", themename= "vapor")
                self.janela.geometry("800x600")
                self.janela.iconbitmap("04_IMC_Calculator/bmi.ico")
#----------------------------------------------------------------------------------------------------------------------
                t = ttk.Label(text="Bem-vindo ao IMC Calculator!",
                                font=("Calisto MT", 40),
                                foreground="#7700FF"                    )
                t.pack(pady=(60,0))
#----------------------------------------------------------------------------------------------------------------------
                peso = ttk.Label(text="Indique abaixo o seu peso (kg), exemplo: 70;",
                                font=("Calisto MT", 20),
                                foreground="#7700FF")
                peso.pack(pady=(20,0))
#----------------------------------------------------------------------------------------------------------------------
                self.r_p = ttk.Entry(self.janela,
                                justify="center",
                                font=("Times New Roman",15))
                self.r_p.pack(pady=(20,0))
#----------------------------------------------------------------------------------------------------------------------
                altura = ttk.Label(text = "Indique abaixo a sua altura (m), exemplo: 1.60;",
                                font=("Calisto MT", 20),
                                foreground="#7700FF")
                altura.pack(pady=(20,0))
#----------------------------------------------------------------------------------------------------------------------
                self.r_a = ttk.Entry(self.janela,
                                justify="center",
                                font=("Times New Roman",15))
                self.r_a.pack(pady=(20,0))
#----------------------------------------------------------------------------------------------------------------------
                b = ttk.Button(self.janela,
                        text="Enviar",
                        padding=9,
                        width= 30,
                        command=self.coleta)
                b.pack(pady=(30,0))
#----------------------------------------------------------------------------------------------------------------------
                self.rc = ttk.Label(self.janela,
                        text = " ",
                        font=("Calisto MT",30),

                        foreground= "#9D00FF")
                self.rc.pack(pady=(20,0))

#----------------------------------------------------------------------------------------------------------------------

                self.result = ttk.Label(self.janela,
                                        text = (""))
#----------------------------------------------------------------------------------------------------------------------
        def coleta(self):
                caixa_peso_str = self.r_p.get()
                caixa_altura_str = self.r_a.get()
                c_peso = float(caixa_peso_str)
                c_altura = float(caixa_altura_str)
                self.conta = c_peso/c_altura**2


                
                if self.conta <= 18.5:
                        self.result = ttk.Label(text = "abaixo peso").pack()
                else:
                        self.result = ttk.Label(text = "okkoo").pack()

                self.result.pack()

                self.rc.configure(text = f"O seu IMC é: {self.conta:.1f}")
                self.result.configure(text = self.result)
#---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
        def run(self):
                self.janela.mainloop()  
#------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    janela_c = Janela_dados()
    janela_c.run() #janela_c.janela.mainloop()

