import tkinter as tk
from tkinter import ttk
from leis_de_ohm import LeiDeOhm

class Aplicativo():
    def  __init__(self, parent: tk.Tk):
        parent.geometry('300x300')
        self.lbl_lei = ttk.Label(parent, text='Calculadora de Lei de Ohm', font=('Calibri Light',14))
        self.fr_quadro1 = ttk.Frame(parent, relief='groove')
        self.str_opt = tk.StringVar()
        self.rdb_option1 = ttk.Radiobutton(self.fr_quadro1, text='1ª Lei de Ohm',
                                           variable=self.str_opt,
                                           value='1 Lei')
        self.rdb_option2 = ttk.Radiobutton(self.fr_quadro1, text='2ª Lei de Ohm',
                                           variable=self.str_opt,
                                           value='2 Lei')
        
        self.show_features()

    def show_features(self):
        self.lbl_lei.pack()
        self.fr_quadro1.pack(anchor='w')
        self.rdb_option1.pack()

if __name__ == "__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()