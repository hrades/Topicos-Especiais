import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from pymongo import MongoClient

class Conexao_bd:
    def __init__(self):
        self.conexao_mongo = MongoClient('localhost', 27017)
        self.conector_setores = self.conexao_mongo['MeuBancodeDados']['setores']

    def inserir_setor(self, setor_id, nome):
        self.conector_setores.insert_one({'_id':setor_id,
                                          'setor_nome':nome})

class Aplicativo:
    def __init__(self, parent):
        self.frm_setores = ttk.LabelFrame(parent, text= "Gerenciamento de setores")
        self.txb_setor_id = ttk.Entry(self.frm_setores)
        self.txb_setor_nome = ttk.Entry(self.frm_setores)
        self.scr_lista_setores = ScrolledText(self.frm_setores)
        #Configurar tamanho da caixa de texto
        self.scr_lista_setores.configure(width=10, height=10)
        
        self.frm_setores.pack(fill='both', expand=True)
        ttk.Label(self.frm_setores, text='Código do setor').grid(row=0,column=0)
        ttk.Label(self.frm_setores, text='Nome do setor').grid(row=1, column=0)
        self.txb_setor_id.grid(row=0, column=1)
        self.txb_setor_nome.grid(row=1, column=1)
        ttk.Button(self.frm_setores, text='Inserir', command=self.inserir_setor).grid(row=0,column=2,rowspan=2,sticky='ns')
        self.scr_lista_setores.grid(row=2, column=0, columnspan=3, sticky='news')

    # Inserir um novo setor no Banco de Dados
    def inserir_setor(self):
        # Atribui um novo objeto da classe de conexão com o banco de dados
        conexao = Conexao_bd()
        try:
            setor = int(self.txb_setor_id.get())
            # Método para inserção de um novo documento a partir da classe de conexão de banco de dados
            conexao.inserir_setor(setor_id= setor,
                              nome= self.txb_setor_nome.get())
            messagebox.showinfo('Sucesso!', 'Registro adicionado ao banco de dados.\nVerifique para ter certeza.')
        except:
            messagebox.showerror('Erro', 'O registro nao pôde ser inserido.\nDigite um número que ainda não esteja na coleção')
        
    # Atualizar a caixa de texto com a lista de documentos da coleção setores
    def listar_setores(self):
        pass


if __name__=="__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()