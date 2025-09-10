from calculadora_troco import NotasMoedas
from math import trunc
import tkinter as tk

class AplicativoTroco():
    def __init__(self, parent):
        self.back_color = "#EBEBEB"
        self.font_color = '#87CEFA'

        self.lbl_title = tk.Label(parent, text="Troque seu dinheiro aqui! \nDigite o valor",
                                font=('Arial', 12),
                                foreground='black',
                                background=self.back_color)
        self.txtbox_valor = tk.Entry()
        self.bot_computar = tk.Button(parent, text='Calcular troco',
                                        command=self.resultado)
        self.bot_apagar = tk.Button(parent, text='Apagar mensagem',
                                        command=self.apagar_msg)
        self.lbl_msg = tk.Label(parent, text="",
                                font=('Arial', 12),
                                foreground='black',
                                background=self.back_color)

        self.lbl_title.pack()
        self.txtbox_valor.pack()
        self.bot_computar.pack()
        self.bot_apagar.pack()
        self.lbl_msg.pack()

    def converter_texto(self):
        entrada = self.txtbox_valor.get()
        entrada = entrada.replace(',','.')
        try: 
            num = float(entrada) # Verificar se é possível fazer isso
            return num
        except:
            self.lbl_msg.config(text='Erro! Digite um número', foreground='red')
            return None
        
    def apagar_msg(self):
        self.lbl_msg.config(text=f"")

    def formatar_troco(self, troco_dict):
        
        mensagem = "Troco:\n"
        for nota, quantidade in troco_dict.items():
            if quantidade > 0:
                mensagem += f"{trunc(float(quantidade))} x {nota}\n"
        return mensagem.strip()

    def resultado(self):
        valor = self.converter_texto()
        if valor is not None:
            moedas = NotasMoedas(valor)
            troco_formatado = self.formatar_troco(moedas.mostrar_troco())
            self.lbl_msg.config(text=troco_formatado, foreground='black')

if __name__=="__main__":
    window = tk.Tk() #Declara um objeto tipo canvas (janela)
    window.geometry('200x500') # X e Y
    window.title('Calculadora de troco') #Nome da tela
    AplicativoTroco(window) #executa a classe Aplicativo com argumento como o canvas
    
    window.mainloop()