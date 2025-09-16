import tkinter as tk
from tkinter import ttk

class Aplicativo:
    def __init__(self, parent: tk.Tk):
        parent.geometry('300x300')
        self.cmbbox_escolha = ttk.Combobox(parent, 
                                           values=('red', 'green', 'blue'))
        self.bot_cor = tk
        
        self.show_app()

    def show_app(self):
        self.cmbbox_escolha.pack()

if __name__=="__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()