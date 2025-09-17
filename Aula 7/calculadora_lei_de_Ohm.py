import tkinter as tk
from tkinter import ttk
from Exercicios import modulo_exercicios as mde

class Aplicativo():
    def  __init__(self, parent: tk.Tk):
        parent.geometry('300x300')
        self.lbl_lei = ttk.Label(parent, text='Calculadora de Lei de Ohm', font=('Calibri Light',14))
        

        self.show_features()

    def show_features(self):
        self.lbl_lei.pack()

if __name__ == "__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()

    mde.Exercicios.primeira_lei_ohm()