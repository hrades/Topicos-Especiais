import tkinter as tk
from tkinter import ttk

class Aplicativo:
    def __init__(self, parent):
        self.fr_quadro1 = ttk.LabelFrame(parent, text='Quadro 1') # Texto + linha da moldura
        self.lbl_texto1 = ttk.Label(self.fr_quadro1, text='Texto 1')
        self.fr_quadro2 = ttk.Frame(parent, relief='groove') # Apenas a moldura - n necessariamente aparente
        self.lbl_texto2 = ttk.Label(self.fr_quadro2, text='Texto 2')

        self.fr_quadro1.pack()
        self.lbl_texto1.pack()
        self.fr_quadro2.pack(ipadx=3, ipady=3) # Adicionando margens
        self.lbl_texto2.pack()

if __name__ == "__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()