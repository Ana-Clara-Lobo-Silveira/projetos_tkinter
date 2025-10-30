import ttkbootstrap as ttk

j = ttk.Window(themename="vapor")

treeview = ttk.Treeview(j)
treeview.pack()

treeview["columns"] = ("nome", "idade", "cidade")


treeview["show"] = "headings"
treeview.heading("nome", text="Nome Completo")
treeview.heading("idade", text="Idade")
treeview.heading("cidade", text="Cidade")

treeview.insert("", "end",values = ["Ana", "17", "R$1000,00"])

j.mainloop()