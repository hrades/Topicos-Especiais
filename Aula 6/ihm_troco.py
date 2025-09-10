from calculadora_troco import NotasMoedas
import tkinter as tk

class AplicativoTroco():
    def __init__(self, parent):
        self.back_color = "#EBEBEB"
        self.font_color = '#87CEFA'

        self.txtbox_valor = tk.Entry()
        self.bot_computar = tk.Button(parent, text='Calcular troco',
                                        command=self.resultado)
        self.bot_apagar = tk.Button(parent, text='Apagar mensagem',
                                        command=self.apagar_msg)
        self.lbl_msg = tk.Label(parent, text="",
                                font=('Arial', 12),
                                foreground='black',
                                background=self.back_color)

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

    def resultado(self):
        valor = self.converter_texto()
        moedas = NotasMoedas(valor)
        self.lbl_msg.config(text=f'{moedas.mostrar_troco()}', foreground='black')

if __name__=="__main__":
    window = tk.Tk() #Declara um objeto tipo canvas (janela)
    window.geometry('200x200') # X e Y
    window.title('Calculadora de troco') #Nome da tela
    AplicativoTroco(window) #executa a classe Aplicativo com argumento como o canvas
    
    window.mainloop()