import tkinter as tk
from tkinter import ttk, messagebox
from leis_de_ohm import LeiDeOhm

class Aplicativo():
    def  __init__(self, parent: tk.Tk):
        self.parent = parent # Define a variável self.parent como parent para utilizar fora do __init__
        parent.geometry('215x240') # Fixa a janela com um tamanho
        parent.resizable(False, False) # Desabilita redimensionamento da janela
        parent.protocol("WM_DELETE_WINDOW", self.disable_close) # Atribui a função disable_close para o botão de fechar
        self.features(parent) # Cria os elementos da janela
        self.show_pack() # Coloca elementos na janela
        self.show_grid() # Coloca elementos dentro de outros elementos na janela

    def features(self, parent):
        self.lbl_lei = ttk.Label(parent, text='Calculadora 1ª Lei de Ohm', font=('Calibri Light',14))
        self.fr_quadro1 = ttk.LabelFrame(parent, text='Escolha para calcular',relief='groove')
        self.str_opt = tk.StringVar()
        self.rdb_tensao = ttk.Radiobutton(self.fr_quadro1, text='Tensão',
                                           variable=self.str_opt,
                                           value='V',
                                           command=self.update_label) # command adicionado para chamar função ao clicar no radiobutton
        self.rdb_corrente = ttk.Radiobutton(self.fr_quadro1, text='Corrente',
                                           variable=self.str_opt,
                                           value='A',
                                           command=self.update_label)
        self.rdb_resistencia = ttk.Radiobutton(self.fr_quadro1, text='Resistência',
                                           variable=self.str_opt,
                                           value='R',
                                           command=self.update_label)
        self.fr_quadro2 = ttk.Frame(parent,relief='flat')
        self.lbl_valor1 = ttk.Label(self.fr_quadro2, text='            Valor 1: ')
        self.txb_valor1 = ttk.Entry(self.fr_quadro2)
        self.lbl_valor2 = ttk.Label(self.fr_quadro2, text='            Valor 2: ')
        self.txb_valor2 = ttk.Entry(self.fr_quadro2)
        self.fr_quadro3 = ttk.Frame(parent,relief='flat')
        self.bot_calcular = ttk.Button(parent, text='Calcular', command=self.calcular)
        self.lbl_resultado = ttk.Label(self.fr_quadro3, text='Resultado: ')
        self.bot_fechar = ttk.Button(parent, text='Fechar aplicação',command=self.close_app)

    def show_pack(self): # Posicionamento dos elementos relacionados à janela
        self.lbl_lei.pack(anchor='w')
        self.fr_quadro1.pack(anchor='w', pady=5)
        self.fr_quadro2.pack(anchor='w', pady=5)
        self.bot_calcular.pack(pady=5)
        self.fr_quadro3.pack(anchor='w',pady=5)
        self.bot_fechar.pack(anchor='e', pady=5)
        
    def show_grid(self): # Posicionamento de elementos relacionados a outros elementos
        self.rdb_tensao.grid(row=0, column=0)
        self.rdb_corrente.grid(row=0, column=1)
        self.rdb_resistencia.grid(row=0, column=2)
        self.lbl_valor1.grid(row=0,column=0)
        self.txb_valor1.grid(row=0,column=1)
        self.lbl_valor2.grid(row=1,column=0)
        self.txb_valor2.grid(row=1,column=1)
        self.lbl_resultado.grid(row=1,column=0, pady=5)

    def calcular(self):
        calculo = self.str_opt.get() # Pega o valor retornado pelo radiobutton selecionado
        valor1 = self.txb_valor1.get() # Pega o valor no 1º textbox
        valor2 = self.txb_valor2.get() # Pega o valor no 2º textbox
        try: # Testa conversão de valores para o cálculo
            valor1 = float(valor1)
            valor2 = float(valor2)
        except: # Se um dos valores der erro, mostra messagebox de erro de leitura
            if calculo != '': # O radiobutton deve ter sido selecionado
                messagebox.showerror('Erro de leitura!', 'Digite números para realizar o cálculo') #exemplo

        # Calcula de acordo com o valor selecionado
        if calculo == 'V':
            resultado = LeiDeOhm.primeira_lei(corrente=valor1, resistencia=valor2)
        elif calculo == 'A':
            resultado = LeiDeOhm.primeira_lei(tensao=valor1, resistencia=valor2)
        elif calculo == 'R':
            resultado = LeiDeOhm.primeira_lei(tensao=valor1, corrente=valor2)
            calculo = 'Ω' # muda o valor para formatar o resultado
        else:
            resultado = 'select'

        if resultado == 'select': # Mostra erro de seleção se nada for selecionado para calcular
            messagebox.showwarning('Seleção!', 'Selecione uma das opções para calcular')
            self.lbl_resultado.config(text=f'Resultado: ')
        elif resultado == 'Erro': # Utilizado para quando há erro de leitura
            self.lbl_resultado.config(text=f'Resultado: ')
        else: # Mostra o resultado quando não houver erros anteriores
            self.lbl_resultado.config(text=f'Resultado: {str(resultado)} {calculo}')

    def close_app(self): # Ação do botão Fechar aplicação
        if messagebox.askyesno('Encerrar', 'Deseja encerrar a aplicação?') == tk.YES: # Mostra messagebox de seleção
            self.parent.destroy()

    def disable_close(self): # Ação do botão de fechar integrado
        messagebox.showinfo('Encerrar', 'Utilize o botão "Fechar aplicação" para encerrar') # Mostra messagebox indicando a maneira correta de fechar o programa

    def update_label(self): # Função para atualizar label ao selecionar radiobutton
        # Obtém o valor do Radiobutton selecionado (V, A ou R)
        escolha = self.str_opt.get()
        # Muda os valores dos labels de acordo com o que foi selecionado
        if escolha == 'V':
            self.lbl_valor1.config(text='    Corrente (A):')
            self.lbl_valor2.config(text='Resistência (Ω):')
        elif escolha == 'A':
            self.lbl_valor1.config(text='      Tensão (V):')
            self.lbl_valor2.config(text='Resistência (Ω):')
        elif escolha == 'R':
            self.lbl_valor1.config(text='      Tensão (V):')
            self.lbl_valor2.config(text='    Corrente (A):')

if __name__ == "__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()