import tkinter

class Aplicativo:
    def __init__(self):
        pass

if __name__ == "__main__":
    window = tkinter.Tk() #Declara um objeto tipo canvas (janela)
    window.geometry('500x500') # X e Y
    window.title('GUI teste') #Nome da tela
    window.mainloop() #Laço de repetição que mantém a tela ativa e funcional
