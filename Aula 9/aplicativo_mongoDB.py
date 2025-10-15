from inicio_MongoDB import Conexao_bd
import tkinter as tk
from tkinter import ttk

class Aplicativo:
    def __init__(self, parent):
        parent.geometry("500x200")
        self.conexao_banco = Conexao_bd()
        self.lbl_setores = ttk.Label(parent, text="Aguardando...", font=('Arial', 14, 'bold'))
                
        self.lbl_setores.pack()
        ttk.Button(parent, text="Consultar", command=self.acao_consultar).pack()

    def acao_consultar(self):
        print(self.conexao_banco.listar_setores())

if __name__ == "__main__":
    window =  tk.Tk()
    Aplicativo(window)
    window.mainloop()