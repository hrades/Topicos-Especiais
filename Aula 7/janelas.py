import tkinter as tk
from tkinter import ttk

class Aplicativo:
    def __init__(self, parent: tk.Tk):
        parent.geometry('200x200')

        parent.columnconfigure((0,1), weight=1)  # Divisão igual da janela para redimensionamento das colunas
        parent.rowconfigure((1,2), weight=1)  # Divisão igual da janela para redimensionamento das colunas

        self.fr_quadro1 = ttk.LabelFrame(parent, text='Quadro 1') # Texto + linha da moldura
        self.lbl_texto1 = ttk.Label(self.fr_quadro1, text='Texto 1')
        self.fr_quadro2 = ttk.Frame(parent, relief='groove') # Apenas a moldura - n necessariamente aparente
        self.lbl_texto2 = ttk.Label(self.fr_quadro2, text='Texto 2')
        self.fr_quadro3 = ttk.Frame(parent, relief='groove') 
        self.lbl_texto3 = ttk.Label(self.fr_quadro3, text='Texto 3', width=15)
        

        self.show_grid()
        self.show_pack() # Utilizando o pack para mostrar na tela

    # Utilizar somente um dos tipos para organizar a janela principal (parent)
    # Podemos utilizar pack ou grid dentro dos contentores (frames)
    def show_pack(self):
        self.lbl_texto1.pack()
        #self.fr_quadro2.pack(ipadx=3, ipady=3) # Adicionando margens
        self.lbl_texto2.pack(pady=5)
        self.lbl_texto3.pack(padx=3,pady=3)

    def show_grid(self):
        self.fr_quadro1.grid(row=0, column=0, 
                             sticky='ew',
                             columnspan=2) # Mescla duas colunas
        self.fr_quadro2.grid(row=1, column=0, ipadx=5, ipady=5)
        self.fr_quadro3.grid(row=1, column=1, sticky='news')

if __name__ == "__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()