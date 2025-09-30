import tkinter as tk
from tkinter import ttk, messagebox
from calculadora_pesos import peso_linear

class Aplicativo:

    def __init__(self, parent: tk.Tk):
        parent.geometry('340x250')
        self.lbl_titulo = ttk.Label(parent, text='Calculadora de pesos')
        self.lbl_escolha1 = ttk.Label(parent, text='Escolha o perfil')
        self.lbl_escolha2 = ttk.Label(parent, text='Escolha o material')
        self.str_perfil = tk.StringVar()
        self.rdb_redondo = ttk.Radiobutton(parent, text='Redondo',
                                           variable=self.str_perfil,
                                           value='R',
                                           command=self.update_lbl)
        self.rdb_quadrado = ttk.Radiobutton(parent, text='Quadrado',
                                           variable=self.str_perfil,
                                           value='Q',
                                           command=self.update_lbl)
        self.rdb_triangular = ttk.Radiobutton(parent, text='Triangular',
                                           variable=self.str_perfil,
                                           value='T',
                                           command=self.update_lbl)
        self.int_material = tk.IntVar()
        self.rdb_aco = ttk.Radiobutton(parent, text='Aço',
                                       variable=self.int_material,
                                       value=1)
        self.rdb_latao = ttk.Radiobutton(parent, text='Latao',
                                       variable=self.int_material,
                                       value=2)
        self.rdb_aluminio = ttk.Radiobutton(parent, text='Alumínio',
                                       variable=self.int_material,
                                       value=3)
        self.lbl_tamanho = ttk.Label(parent, text='Digite o valor (cm):')
        self.txb_tamanho = ttk.Entry(parent)
        self.bot_calcular = ttk.Button(parent, text='Calcular', command=self.calcular)
        self.lbl_resultado = ttk.Label(parent, text='teste')

        self.show_grid()
        
    def show_grid(self):
        self.lbl_titulo.grid(row=0, column=0,
                             sticky='n', pady=5,
                             columnspan=3)
        self.lbl_escolha1.grid(row=1, column=0, sticky='w')
        self.rdb_redondo.grid(row=2, column=0,sticky='w')
        self.rdb_quadrado.grid(row=2, column=1,sticky='w')
        self.rdb_triangular.grid(row=2, column=2,sticky='w')
        self.lbl_escolha2.grid(row=3, column=0, sticky='w', pady=2)
        self.rdb_aco.grid(row=4, column=0,sticky='w')
        self.rdb_latao.grid(row=4, column=1,sticky='w')
        self.rdb_aluminio.grid(row=4, column=2,sticky='w')
        self.lbl_tamanho.grid(row=5, column=1, pady=5)
        self.txb_tamanho.grid(row=5, column=2, pady=5)
        self.bot_calcular.grid(row=6, column=1)
        self.lbl_resultado.grid(row=7,column=0, columnspan=3, pady=5)

    def update_lbl(self):
        perfil = self.str_perfil.get()
        if perfil=='R':
            self.lbl_tamanho.config(text='Digite o raio   (cm):')
        elif perfil=='Q':
            self.lbl_tamanho.config(text='Digite o lado  (cm):')
        elif perfil=='T':
            self.lbl_tamanho.config(text='Digite a base  (cm):')

    def calcular(self):
        perfil = self.str_perfil.get()
        material = self.int_material.get()
        tamanho = self.txb_tamanho.get()
        funfa = False

        try:
            tamanho = float(tamanho)
            funfa = True
        except:
            messagebox.showerror('Erro de leitura!', 'Digite números para realizar o cálculo\nUtilize . no lugar de ,')

        if funfa == True:
            if perfil == 'R' and material in [1,2,3]:
                resultado = peso_linear.perfil_redondo(tamanho, material)
            elif perfil == 'Q' and material in [1,2,3]:
                resultado = peso_linear.perfil_quadrado(tamanho, material)
            elif perfil == 'T' and material in [1,2,3]:
                resultado = peso_linear.perfil_triang(tamanho, material)
            else:
                messagebox.showwarning('Seleção!', 'Selecione uma das opções para o perfil e uma para o material')
                resultado = 'erro'

            if resultado!='erro':
                self.lbl_resultado.config(text=f'Resultado: {resultado:.3f}')
            
if __name__=="__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()