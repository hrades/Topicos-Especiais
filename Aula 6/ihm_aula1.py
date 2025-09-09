import tkinter

# Classe responsável por criar e montar as ferramentas da GUI
class Aplicativo:
    def __init__(self, parent): #parent é o objeto do tipo canvas
        self.back_color = "#EBEBEB"
        self.font_color = '#87CEFA'
        self.cor_botao = False
        parent.config(background=self.back_color)
        # Ferramentas
        self.lbl_texto =  tkinter.Label(parent, text= 'Teste',  #objeto tipo texto
                                   font=('Arial', 14, 'italic', 'underline'),
                                   foreground=self.font_color,
                                   background=self.back_color)
        self.bot_teste = tkinter.Button(parent, text='Clique aqui',
                                        command=self.trocar_cor_texto)
        #Montagem
        self.lbl_texto.pack() #mostrar na janela
        self.bot_teste.pack()

    def trocar_cor_texto(self):
        if self.cor_botao == False:
            self.lbl_texto.config(foreground='red')
            self.cor_botao = True
        else:
            self.lbl_texto.config(foreground=self.font_color)
            self.cor_botao = False

if __name__ == "__main__":
    window = tkinter.Tk() #Declara um objeto tipo canvas (janela)
    window.geometry('500x500') # X e Y
    window.title('GUI teste') #Nome da tela
    Aplicativo(window) #executa a classe Aplicativo com argumento como o canvas
    
    window.mainloop() #Laço de repetição que mantém a tela ativa e funcional
