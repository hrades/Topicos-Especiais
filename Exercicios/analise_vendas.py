class AnaliseVendas:
    def __init__(self, endereco):
        self._endereco = endereco
        self.lista_dados = []

    def ler_arquivo(self):
        with open(self._endereco, mode='r', encoding='UTF-8') as dados:
            for linha in dados:
                listinha = linha.strip().split(',')
                if linha: 
                    self.lista_dados.append(listinha)

    def contar_vendas(self):
        return len(self.lista_dados)-1
    
    def valor_total(self):
        total = 0.0
        lista_manipulada = self.lista_dados
        lista_manipulada.pop(0)
        for dado in lista_manipulada:
           total += float(dado[7])
        return total

if __name__=='__main__':
    vendas = AnaliseVendas(r"Z:\Topicos-Especiais\Dados\dados.csv")
    vendas.ler_arquivo()
    qtd_linhas = vendas.contar_vendas()
    print(qtd_linhas)
    vendas.valor_total()
    total_vendido = vendas.valor_total()
    print(total_vendido)