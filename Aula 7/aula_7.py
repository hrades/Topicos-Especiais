import tkinter as tk
from tkinter import ttk

class Aplicativo:
    def __init__(self, parent: tk.Tk):
        parent.geometry('300x300')
        self.lbl_title = ttk.Label(parent, text='Escolha uma cor', font=('Arial', 16))
        self.cmbbox_escolha = ttk.Combobox(parent, 
                                           values=('red', 'green', 'blue'))
        self.lbl_cor = ttk.Label(parent, text='Cor', font=('Arial', 14))
        self.bot_cor = ttk.Button(parent, text='Mudar cor')
        
        self.show_app()

    def show_app(self):
        self.lbl_title.pack()
        self.cmbbox_escolha.pack()
        self.bot_cor.pack(anchor='e')
        self.lbl_cor.pack(pady=15)

    def change_color(self):
        pass

if __name__=="__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()