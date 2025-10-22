import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from pymongo import MongoClient

class Conexao_bd:
    def __init__(self):
        self.conexao_mongo = MongoClient('localhost', 27017)
        self.conector_setores = self.conexao_mongo['MeuBancodeDados']['setores']
        self.conector_funcionarios = self.conexao_mongo['MeuBancodeDados']['funcionarios']

    def inserir_setor(self, setor_id, nome):
        self.conector_setores.insert_one({'_id':setor_id,
                                          'setor_nome':nome})
        
    def listar_setores(self):
        resposta = list()
        for documento in self.conector_setores.find():
            resposta.append(documento)
        return resposta
    
    def cadastrar_funcionario(self, id_funcionario, func_nome, gerente_id, setor_id, func_salario, func_dataNasc):
        '''Cadastra novos funcionários
        id_funcionario
        func_nome
        gerente_id
        setor_id
        func_salario
        func_dataNasc
        '''
        self.conector_funcionarios.insert_one({'_id': id_funcionario,
                                               'func_nome': func_nome,
                                               'gerente_id': gerente_id,
                                               'setor_id': setor_id,
                                               'func_salario': func_salario,
                                               'func_dataNasc': func_dataNasc})
        
    def listar_funcionarios(self):
        lista = list()
        for dado in self.conector_funcionarios.find():
            lista.append(dado)
        return lista


class Aplicativo:
    def __init__(self, parent):
        # SETORES
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
        ttk.Button(self.frm_setores, text='Atualizar lista setores', command=self.listar_setores).grid(row=3,column=0)

        # FUNCIONÁRIOS
        self.frm_funcionarios = ttk.Labelframe(parent, text="Gerenciamento de funcionários")
        self.txb_func_id = ttk.Entry(self.frm_funcionarios)
        self.txb_func_nome = ttk.Entry(self.frm_funcionarios)
        self.txb_func_ger_id = ttk.Entry(self.frm_funcionarios)
        self.txb_func_set_id = ttk.Entry(self.frm_funcionarios)
        self.txb_func_salario = ttk.Entry(self.frm_funcionarios)
        self.txb_func_dataNasc = ttk.Entry(self.frm_funcionarios)
        self.scr_lista_funcionarios = ScrolledText(self.frm_funcionarios)
        self.scr_lista_funcionarios.configure(width=10, height=10)

        self.frm_funcionarios.pack(fill='both', expand=True)
        ttk.Label(self.frm_funcionarios, text='Código do funcionário').grid(row=0,column=0)
        self.txb_func_id.grid(row=0, column=1)
        ttk.Label(self.frm_funcionarios, text='Nome do funcionário').grid(row=1, column=0)
        self.txb_func_nome.grid(row=1, column=1)
        ttk.Label(self.frm_funcionarios, text='ID Gerente').grid(row=2, column=0)
        self.txb_func_ger_id.grid(row=2, column=1)
        ttk.Label(self.frm_funcionarios, text='ID Setor').grid(row=3, column=0)
        self.txb_func_set_id.grid(row=3, column=1)
        ttk.Label(self.frm_funcionarios, text='Salário').grid(row=4, column=0)
        self.txb_func_salario.grid(row=4, column=1)
        ttk.Label(self.frm_funcionarios, text='Aniversário').grid(row=5, column=0)
        self.txb_func_dataNasc.grid(row=5, column=1)
        ttk.Button(self.frm_funcionarios, text='Inserir', command=self.inserir_funcionario).grid(row=0,column=2,rowspan=6,sticky='ns')
        self.scr_lista_funcionarios.grid(row=6, column=0, columnspan=3, sticky='news')
        ttk.Button(self.frm_funcionarios, text='Atualizar lista funcionários', command=self.listar_funcionarios).grid(row=7, column=0)

        

    # Inserir um novo setor no Banco de Dados
    def inserir_setor(self):
        # Atribui um novo objeto da classe de conexão com o banco de dados
        conexao = Conexao_bd()
        try:
            setor = int(self.txb_setor_id.get())
            # Método para inserção de um novo documento a partir da classe de conexão de banco de dados
            conexao.inserir_setor(setor_id= setor,
                              nome= self.txb_setor_nome.get())
            messagebox.showinfo('Sucesso!', 'Registro adicionado ao banco de dados.\n\nVerifique para ter certeza.')
        except:
            messagebox.showerror('Erro', 'O registro nao pôde ser inserido.\n\nDigite um número que ainda não esteja na coleção.')
        
    # Atualizar a caixa de texto com a lista de documentos da coleção setores
    def listar_setores(self):
        conexao = Conexao_bd()
        # Limpar conteúdo de texto
        self.scr_lista_setores.delete(0.0, 'end')
        # Inserir o texto
        for registro in conexao.listar_setores():
            self.scr_lista_setores.insert('end', f"{registro['_id']}\t{registro['setor_nome']}\n")

    def inserir_funcionario(self):
        conexao = Conexao_bd()
        try:
            id = int(self.txb_func_id.get())
            conexao.cadastrar_funcionario(id_funcionario=id,
                                          func_nome=self.txb_func_nome.get(),
                                          gerente_id=self.txb_func_ger_id.get(),
                                          setor_id=self.txb_func_set_id.get(),
                                          func_salario=self.txb_func_salario.get(),
                                          func_dataNasc=self.txb_func_dataNasc.get())
            messagebox.showinfo('Sucesso!', 'Cadastro de funcionário realizado com sucesso.\n\nVerifique para ter certeza.')
        except:
            messagebox.showerror('Erro!', 'O funcionário não pôde ser cadastrado.\n\nDigite um id que ainda não foi utilizado.')

    def listar_funcionarios(self):
        conexao = Conexao_bd()
        self.scr_lista_funcionarios.delete(0.0, 'end')
        for funcionario in conexao.listar_funcionarios():
            self.scr_lista_funcionarios.insert('end', f"{funcionario['_id']}\t{funcionario['func_nome']} \t{funcionario['func_salario']}\n")


if __name__=="__main__":
    window = tk.Tk()
    Aplicativo(window)
    window.mainloop()