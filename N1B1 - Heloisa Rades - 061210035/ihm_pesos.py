import tkinter as tk
from tkinter import ttk, messagebox
from calculadora_pesos import peso_linear

class Aplicativo:

    def __init__(self, parent: tk.Tk):
        parent.geometry('250x250')
        self.lbl_titulo = ttk.Label(parent, text='Calculadora de pesos')
        self.lbl_escolha1 = ttk.Label(parent, text='Escolha o perfil')
        self.str_perfil = tk.StringVar()
        self.rdb_redondo = ttk.Radiobutton(parent, text='Redondo',
                                           variable=self.str_perfil,
                                           value='R')
        self.rdb_quadrado = ttk.Radiobutton(parent, text='Quadrado',
                                           variable=self.str_perfil,
                                           value='Q')
        self.rdb_triangular = ttk.Radiobutton(parent, text='Triangular',
                                           variable=self.str_perfil,
                                           value='T')
        
        self.show_grid()
        
    def show_grid(self):
        self.lbl_titulo.grid(row=0, column=0,
                             sticky='n', pady=5,
                             columnspan=3)
        self.lbl_escolha1.grid(row=1, column=0, sticky='w')
        self.rdb_redondo.grid(row=2, column=0)
        self.rdb_quadrado.grid(row=2, column=1)
        self.rdb_triangular.grid(row=2, column=2)

if __name__=="__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()