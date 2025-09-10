import tkinter as tk

class Aplicativo:
    def __init__(self, parent):
        parent.geometry('200x200') #Edita tamanho da janela

        # Ferramentas
        self.tbox_entrada = tk.Entry()
        self.lbl_resultado = tk.Label(parent, text='Resultado')
        self.bot_calcular = tk.Button(parent, text='Calcular', command=self.calcular_dobro)

        # Mostrar
        self.tbox_entrada.pack()
        self.lbl_resultado.pack()
        self.bot_calcular.pack()

    def calcular_dobro(self): # Associado ao bot_calcular
        try:
            numero = self.tbox_entrada.get() # Pega o valor do textbox, retornando o texto
            numero = float(numero)
        except:
            numero = 0

        self.lbl_resultado.config(text=f'{numero*2}')


if __name__ == "__main__":
    tela = tk.Tk()
    Aplicativo(tela)
    tela.mainloop()