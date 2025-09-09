class NotasMoedas():
    def __init__(self, reais):
        self.troco = dict()
        self.notas = (100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01)
        self.reais = reais

    def calcular_troco(self, valor):
        dinheiro = self.reais//valor
        if valor>1:
            self.troco[f'{valor} reais'] = dinheiro
        elif valor<1:
            self.troco[f'{valor*100} cents'] = dinheiro
        elif valor==1:
            self.troco['1 real'] = dinheiro
        return self.reais%valor
    
    def mostrar_troco(self):
        for real in self.notas:
            if self.reais>=real:
                self.reais = round(self.calcular_troco(real, self.reais), 2)
        return self.troco