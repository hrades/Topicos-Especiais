import tkinter as tk
from tkinter import ttk, messagebox
from leis_de_ohm import LeiDeOhm

class Aplicativo():
    def  __init__(self, parent: tk.Tk):
        parent.geometry('300x300')
        parent.columnconfigure((0,1), weight=1)
        parent.rowconfigure((0,1,2,3), weight=1)
        self.features(parent)    
        self.show_pack()
        self.show_grid()

    def features(self, parent):
        self.lbl_lei = ttk.Label(parent, text='Calculadora 1ª Lei de Ohm', font=('Calibri Light',14))
        self.fr_quadro1 = ttk.LabelFrame(parent, text='Escolha para calcular',relief='groove')
        self.str_opt = tk.StringVar()
        self.rdb_tensao = ttk.Radiobutton(self.fr_quadro1, text='Tensão',
                                           variable=self.str_opt,
                                           value='V',
                                           command=self.update_label)
        self.rdb_corrente = ttk.Radiobutton(self.fr_quadro1, text='Corrente',
                                           variable=self.str_opt,
                                           value='A',
                                           command=self.update_label)
        self.rdb_resistencia = ttk.Radiobutton(self.fr_quadro1, text='Resistência',
                                           variable=self.str_opt,
                                           value='R',
                                           command=self.update_label)
        self.fr_quadro2 = ttk.Frame(parent,relief='groove')
        self.lbl_valor1 = ttk.Label(self.fr_quadro2, text='Valor 1: ')
        self.txb_valor1 = ttk.Entry(self.fr_quadro2)
        self.lbl_valor2 = ttk.Label(self.fr_quadro2, text='Valor 2: ')
        self.txb_valor2 = ttk.Entry(self.fr_quadro2)
        self.fr_quadro3 = ttk.Frame(parent,relief='groove')
        self.bot_calcular = ttk.Button(self.fr_quadro3, text='Calcular', command=self.calcular)
        self.lbl_resultado = ttk.Label(self.fr_quadro3, text='Resultado: ')
        self.bot_fechar = ttk.Button(self.fr_quadro3, text='Fechar aplicação',command=self.close_app)

    def show_pack(self):
        self.lbl_lei.pack(anchor='w')
        self.fr_quadro1.pack(anchor='w', pady=5)
        self.fr_quadro2.pack(anchor='w', pady=5)
        self.fr_quadro3.pack(anchor='w',pady=5)
        
    def show_grid(self):
        self.rdb_tensao.grid(row=0, column=0)
        self.rdb_corrente.grid(row=0, column=1)
        self.rdb_resistencia.grid(row=0, column=2)
        self.lbl_valor1.grid(row=0,column=0)
        self.txb_valor1.grid(row=0,column=1)
        self.lbl_valor2.grid(row=1,column=0)
        self.txb_valor2.grid(row=1,column=1)
        self.bot_calcular.grid(row=0,column=0,columnspan=2, pady=5)
        self.lbl_resultado.grid(row=1,column=0, pady=5)
        self.bot_fechar.grid(row=2,column=1,pady=5)

    def calcular(self):
        calculo = self.str_opt.get()
        valor1 = self.txb_valor1.get()
        valor2 = self.txb_valor2.get()
        if calculo == 'V':
            resultado = LeiDeOhm.primeira_lei(corrente=valor1, resistencia=valor2)
        elif calculo == 'A':
            resultado = LeiDeOhm.primeira_lei(tensao=valor1, resistencia=valor2)
        elif calculo == 'R':
            resultado = LeiDeOhm.primeira_lei(tensao=valor1, corrente=valor2)
        else:
            resultado = 'select'

        self.lbl_resultado.config(text=f'Resultado: {str(resultado)}')


    def close_app(self):
        pass

    def update_label(self):
        # Obtém o valor do Radiobutton selecionado (V, A ou R)
        escolha = self.str_opt.get()

        if escolha == 'V':
            self.lbl_valor1.config(text='Corrente (A):')
            self.lbl_valor2.config(text='Resistência (Ω):')
        elif escolha == 'A':
            self.lbl_valor1.config(text='Tensão (V):')
            self.lbl_valor2.config(text='Resistência (Ω):')
        elif escolha == 'R':
            self.lbl_valor1.config(text='Tensão (V):')
            self.lbl_valor2.config(text='Corrente (A):')

if __name__ == "__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()