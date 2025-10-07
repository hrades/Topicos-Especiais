# Desenvolvedora: Heloísa Rades de Souza - 061210035

import tkinter as tk
from tkinter import ttk, messagebox
from amp_op import Calculos # importar o módulo de cálculos

class Aplicativo:
    def __init__(self, parent = tk.Tk):
        parent.geometry('350x300')
        parent.resizable(False, False)
        self.parent = parent # Criando uma variável para trabalhar o parent fora do init

        # Criando os componentes do processo
        self.lbl_title = ttk.Label(parent, text='AmpOp não inversor', font=('Arial',14))
        self.lbf_operacao = ttk.Labelframe(parent, text='Escolha uma operação')
        self.str_op = tk.StringVar()
        self.rdb_Vin = ttk.Radiobutton(self.lbf_operacao, text='Tensão de entrada (Vin)',
                                       variable=self.str_op,
                                       value='Vin', command=self.change_label)
        self.rdb_Vout = ttk.Radiobutton(self.lbf_operacao, text='Tensão de saída (Vout)',
                                       variable=self.str_op,
                                       value='Vout', command=self.change_label)
        self.rdb_Rin = ttk.Radiobutton(self.lbf_operacao, text='Resistor de entrada (Rin)',
                                       variable=self.str_op,
                                       value='Rin', command=self.change_label)
        self.rdb_Rf = ttk.Radiobutton(self.lbf_operacao, text='Resistor de realimentação (Rf)',
                                       variable=self.str_op,
                                       value='Rf', command=self.change_label)
        self.lbf_valores = ttk.Labelframe(parent, text='Digite os valores')
        self.lbl_valor1 = ttk.Label(self.lbf_valores, text='Escolha uma opção')
        self.lbl_valor2 = ttk.Label(self.lbf_valores, text='Escolha uma opção')
        self.lbl_valor3 = ttk.Label(self.lbf_valores, text='Escolha uma opção')
        self.txb_val1 = ttk.Entry(self.lbf_valores)
        self.txb_val2 = ttk.Entry(self.lbf_valores)
        self.txb_val3 = ttk.Entry(self.lbf_valores)
        self.bot_calcular = ttk.Button(parent, text='                      Calcular                    ', command=self.amp_calcular)
        self.lbl_resultado = ttk.Label(parent, text='Resultado: ', font=('Arial', 14))
        self.bot_close = ttk.Button(parent, text='Fechar programa', command=self.close_window)

        self.show() # Chamando a função que contém os componentes organizados

    def show(self): # Função para localizar os componentes na tela
        # Pack está sendo utilizado para a tela toda
        # Grid está sendo utilizado para os LabelFrames
        self.lbl_title.pack()
        self.lbf_operacao.pack(pady=5)
        self.rdb_Vin.grid(row=0,column=0)
        self.rdb_Vout.grid(row=0, column=1)
        self.rdb_Rin.grid(row=1,column=0)
        self.rdb_Rf.grid(row=1,column=1)
        self.lbf_valores.pack(pady=5)
        self.lbl_valor1.grid(row=0,column=0)
        self.lbl_valor2.grid(row=1,column=0)
        self.lbl_valor3.grid(row=2,column=0)
        self.txb_val1.grid(row=0,column=1)
        self.txb_val2.grid(row=1,column=1)
        self.txb_val3.grid(row=2,column=1)
        self.bot_calcular.pack()
        self.lbl_resultado.pack(pady=2, anchor='w')
        self.bot_close.pack(anchor='se')

    def close_window(self): # Função para fechar por botão programável
        if messagebox.askyesno('Encerrar', 'Deseja fechar o programa?') == tk.YES: #Abre caixa de texto e fecha se for 'Sim'
            self.parent.destroy()

    def change_label(self): # Mudar textos dos labels
        escolha = self.str_op.get()

        if escolha == 'Vin': # Seleção de Tensão de entrada
            self.lbl_valor1.config(text='Tensão de saída: ')
            self.lbl_valor2.config(text='Resistor de entrada: ')
            self.lbl_valor3.config(text='Resistor de realimentação: ')
        elif escolha == 'Vout': # Seleção de Tensão de saída
            self.lbl_valor1.config(text='Tensão de entrada: ')
            self.lbl_valor2.config(text='Resistor de entrada: ')
            self.lbl_valor3.config(text='Resistor de realimentação: ')
        elif escolha == 'Rin': # Seleção de Resistor de entrada
            self.lbl_valor1.config(text='Tensão de entrada: ')
            self.lbl_valor2.config(text='Tensão de saída: ')
            self.lbl_valor3.config(text='Resistor de realimentação: ')
        elif escolha == 'Rf': # Seleção de Resistor de realimentação
            self.lbl_valor1.config(text='Tensão de entrada: ')
            self.lbl_valor2.config(text='Tensão de saída: ')
            self.lbl_valor3.config(text='Resistor de entrada: ')

    def amp_calcular(self): # Função que realiza os cálculos
        # Lê os valores dos textbox e do radiobutton
        valor1 = self.txb_val1.get()
        valor2 = self.txb_val2.get()
        valor3 = self.txb_val3.get()
        escolha = self.str_op.get()
        calculo = Calculos() # Cria uma instância da classe para os cálculos
        
        if escolha!='Rin' or escolha!='Rf': # Checa o que está sendo calculado
            try:
                valor1 = float(valor1)
                valor2 = float(valor2)
                valor3 = float(valor3)
            except:
                messagebox.showerror('Erro de leitura!', 'Digite valores numéricos para calcular.\nUse . no lugar de ,') # Erro de leitura
        else: # O calculo aceita que o valor do resistor não seja informado
            try:
                valor1 = float(valor1)
                valor2 = float(valor2)
                if valor3.isnumeric():
                    valor3 = float(valor3)
                else:
                    valor3 = None # Se não for informado, o valor do resistor fica None
            except:
                messagebox.showerror('Erro de leitura!', 'Digite valores numéricos para calcular.') # Erro de leitura

        # Verifica o que foi escolhido nos RadioButtons para realizar o calculo
        if escolha == 'Vin':
            resultado = calculo.calcular_vin(valor1, valor3, valor2)
        elif escolha == 'Vout':
            resultado = calculo.calcular_vout(valor1, valor3, valor2)
        elif escolha == 'Rin':
            resultado = calculo.calcular_res(valor1, valor2, rf=valor3)
        elif escolha == 'Rf':
            resultado = calculo.calcular_res(valor1, valor2, rin=valor3)
        else:
            messagebox.showinfo('Seleção!', 'Escolha uma operação clicando nas opções disponíveis') # Mostra uma informação se a escolha não for feita
        
        if resultado != None: # Testa se o resultado não é None (uma possibilidade)
            self.lbl_resultado.config(text=f'Resultado: {resultado}', font=('Arial',14)) # Mostra apenas resultados numéricos
        else:
            messagebox.showwarning('Cuidado!', 'Revise os valores para realizar os cálculos') # Mostra se tiver None no resultado
        

if __name__=="__main__": # Ativação da janela
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()