import tkinter as tk
from tkinter import ttk, messagebox

class Aplicativo:
    def __init__(self, parent: tk.Tk):
        parent.geometry('200x200')
        self.btn_acao = ttk.Button(parent, text='Clique aqui', command=self.acao)
        self.btn_exemplo = ttk.Button(parent, text='Exemplo', command=self.exemplo)

        self.btn_acao.pack()
        self.btn_exemplo.pack()

    def acao(self):
        messagebox.showinfo('Informação!', 'Ontem choveu muito')
        messagebox.showwarning('Aviso!', 'Pode ser que hoje chova novamente')
        messagebox.showerror('Problemas!', 'Queda de árvores e enchentes')
        

    def exemplo(self):
        messagebox.showinfo(title='Questão',
                            message='Responda rápido',
                            icon='question')
        resposta = messagebox.askyesno('Para hoje', 'Você trouxe seu guarda-chuva?')
        if resposta == tk.YES:
            messagebox.showinfo('Boa', 'Você está preparado para a chuva')
        else:
            messagebox.showwarning('Cuidado', 'Pegue um guarda-chuva. Vai chover')

if __name__ == "__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()