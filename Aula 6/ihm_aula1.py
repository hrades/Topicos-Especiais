import tkinter

# Classe responsável por criar e montar as ferramentas da GUI
class Aplicativo:
    def __init__(self, parent): #parent é o objeto do tipo canvas
        back_color = "#EBEBEB"
        font_color = '#87CEFA'
        parent.config(background=back_color)
        lbl_texto =  tkinter.Label(parent, text= 'Teste',  #objeto tipo texto
                                   font=('Arial', 14, 'italic', 'underline'),
                                   foreground=font_color,
                                   background=back_color)
        lbl_texto.pack() #mostrar na janela

if __name__ == "__main__":
    window = tkinter.Tk() #Declara um objeto tipo canvas (janela)
    window.geometry('500x500') # X e Y
    window.title('GUI teste') #Nome da tela
    Aplicativo(window) #executa a classe Aplicativo com argumento como o canvas
    
    window.mainloop() #Laço de repetição que mantém a tela ativa e funcional
