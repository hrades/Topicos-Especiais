from pymongo import MongoClient
import json

class Conexao_bd:
    def __init__(self):
        #Cria um objeto de conexão com o banco de dados
        self.conexao = MongoClient('localhost', 27017)
        #Cria um objeto para manipulação da coleção setores
        self.cursor_setores = self.conexao['MeuBancodeDados']['setores']
        self.cursor_funcionarios = self.conexao['MeuBancodeDados']['funcionarios']

    def listar_setores(self):
        resposta = list()
        for documento in self.cursor_setores.find():
            resposta.append(documento)
        return resposta

    def inserir_colecoes(self):
        #Acessa o arquivo do tipo JSON para obter os documentos a serem inseridos
        with open(r"C:\Users\061210035\Downloads\colecao_setores.json", encoding= 'utf-8') as arquivo:
            colecao = json.load(arquivo)#Converte o arquivo de texto para uma lista de dicionários
        self.cursor_setores.delete_many({}) #Remove os documentos pré-existentes
        self.cursor_setores.insert_many(colecao) #Insere os novos documentos na coleção
        with open(r"C:\Users\061210035\Downloads\colecao_funcionarios.json", encoding= 'utf-8') as arquivo:
            colecao = json.load(arquivo)
        self.cursor_funcionarios.delete_many({})
        self.cursor_funcionarios.insert_many(colecao)

if __name__ == "__main__":
    obj_bd = Conexao_bd()
    lista_setores = obj_bd.listar_setores()
    print(lista_setores)
    #obj_bd.inserir_colecoes()