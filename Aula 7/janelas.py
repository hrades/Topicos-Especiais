import tkinter as tk
from tkinter import ttk

class Aplicativo:
    def __init__(self, parent):
        self.fr_quadro1 = ttk.LabelFrame(parent, text='Quadro 1')
        self.lbl_texto1 = ttk.Label(self.fr_quadro1, text='Texto 1')

        self.fr_quadro1.pack()
        self.lbl_texto1.pack()

if __name__ == "__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()