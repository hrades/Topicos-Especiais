import pymongo

class banco_dados:
    def __init__(self, endereco="mongodb://localhost:27017/"):
        self.conexao = pymongo.MongoClient(endereco)
        self.banco_de_dados = self.conexao["monitoramento_agricola"]
        self.colecao_sensores = self.banco_de_dados["sensores_umidade"]

    def inserir_registro(self, documento):
        return self.colecao_sensores.insert_one(documento)
