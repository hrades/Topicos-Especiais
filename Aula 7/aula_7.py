import tkinter as tk
from tkinter import ttk

class Aplicativo:
    
    def __init__(self, parent: tk.Tk):
        parent.geometry('300x300')
        self.cores = ['red', 'green', 'blue']

        self.lbl_title = ttk.Label(parent, text='Escolha uma cor', font=('Arial', 16))
        self.cmbbox_escolha = ttk.Combobox(parent, 
                                           values=self.cores)
        self.lbl_cor = ttk.Label(parent, text='Cor', font=('Arial', 14))
        self.bot_cor = ttk.Button(parent, text='Mudar cor', command=self.change_color)
        self.str_opt = tk.StringVar()
        self.rdb_option1 = ttk.Radiobutton(parent, text='Opção 1',
                                           variable=self.str_opt,
                                           value='OP1')
        self.rdb_option2 = ttk.Radiobutton(parent, text='Opção 2',
                                           variable=self.str_opt,
                                           value='OP2')
        self.rdb_option3 = ttk.Radiobutton(parent, text='Opção 3',
                                           variable=self.str_opt,
                                           value='OP3')
        
        self.show_app()

    def show_app(self):
        self.lbl_title.pack()
        self.cmbbox_escolha.pack()
        self.bot_cor.pack(anchor='e')
        self.lbl_cor.pack(pady=15)
        self.rdb_option1.pack(anchor='w')
        self.rdb_option2.pack(anchor='w')
        self.rdb_option3.pack(anchor='w')

    def change_color(self):
        cor = self.cmbbox_escolha.get()
        index_select = self.cmbbox_escolha.current() # Retorna o index do elemento selecionado no combo box. Retorna -1 se não está na lista
        if index_select != -1:
            self.lbl_cor.config(background=cor,foreground='white',text=cor)
        else:
            try: # Se a cor for válida, ela é adicionada à lista de cores
                if cor not in self.cores and cor != '':
                    self.cores.append(cor)
                if cor == '':
                    self.lbl_cor.config(background=cor,foreground='black', text='Escolha uma cor')
                else:
                    self.lbl_cor.config(background=cor,foreground='white', text=cor)
                    self.cmbbox_escolha.config(values=self.cores)
            except:
                self.lbl_cor.config(background=cor,foreground='black', text='Escolha uma cor')

if __name__=="__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()