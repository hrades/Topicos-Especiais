import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

class Conexao_bd:
    def __init__(self):
        pass

class Aplicativo:
    def __init__(self, parent):
        self.frm_setores = ttk.LabelFrame(parent, text= "Gerenciamento de setores")
        self.txb_setor_id = ttk.Entry(self.frm_setores)
        self.txb_setor_nome = ttk.Entry(self.frm_setores)
        
        self.frm_setores.pack(fill='both', expand=True)
        ttk.Label(self.frm_setores, text='Código do setor').grid(row=0,column=0)
        ttk.Label(self.frm_setores, text='Nome do setor').grid(row=1, column=0)
        self.txb_setor_id.grid(row=0, column=1)
        self.txb_setor_nome.grid(row=1, column=1)
        ttk.Button(self.frm_setores, text='Inserir', command=self.inserir_setor).grid(row=0,column=2,rowspan=2,sticky='ns')

    def inserir_setor(self):
        pass


if __name__=="__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()