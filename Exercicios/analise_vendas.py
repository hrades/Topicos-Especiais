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
        cont_aux = 0
        for dado in self.lista_dados:
            if cont_aux>0:
                total += float(dado[7])
            cont_aux+=1
            
        cont_aux = 0
        return total
    
    def marcas(self):
        lista_marcas = []
        carro = []
        marca_por_carro = {}
        cont_aux1 = 0
        for dado in self.lista_dados:
            if cont_aux1>0:
                carro.append(dado[2])
            cont_aux1+=1
        cont_aux2 = 0
        for dado in self.lista_dados:
            if cont_aux2>0:
                if dado[2] not in lista_marcas:
                    lista_marcas.append(dado[2])
            cont_aux2+=1
        
        for marca in lista_marcas:
            marca_por_carro[marca] = carro.count(marca)

        return marca_por_carro

    def vendedores(self):
        lista_vendedores = []
        vendas = []
        vendas_por_vendedor = {}
        cont_aux1 = 0
        for dado in self.lista_dados:
            if cont_aux1>0:
                vendas.append(dado[8])
            cont_aux1+=1
        cont_aux2 = 0
        for dado in self.lista_dados:
            if cont_aux2>0:
                if dado[8] not in lista_vendedores:
                    lista_vendedores.append(dado[8])
            cont_aux2+=1
        
        for vendedor in lista_vendedores:
            vendas_por_vendedor[vendedor] = vendas.count(vendedor)

        return vendas_por_vendedor
    
    def media_valor_vendido(self):
        total_valor = self.valor_total()
        total_carros = self.contar_vendas()
        return total_valor/total_carros

if __name__=='__main__':
    #vendas = AnaliseVendas(r"Z:\Topicos-Especiais\Dados\dados.csv")
    vendas = AnaliseVendas(r"D:\Topicos Especiais\Meus Códigos\Topicos-Especiais\Dados")
    vendas.ler_arquivo()
    print(vendas.contar_vendas())
    print(vendas.valor_total())
    print(vendas.marcas())
    print(vendas.vendedores())
    print(vendas.media_valor_vendido())