#import calculadora_areas
import math
import modulos as mod
#calculadora_areas.retangulo()

# Uma classe e a estrutura que vai definir um objeto

class Carro: #Declara uma nova classe chamada carro
    # Método construtor
    def __init__(self): # Executado automaticamente ao criar um novo objeto
        # self indica que o objeto está associado à classe (parâmetro)
        self.marca = 'Ford'
        self.modelo = 'Maverick'
        self.ano = 1979
        self.cor = 'Preto'

if __name__ == '__main__':
    #print(math.__name__)
    #print(__name__)
    #var = mod.retangulo(2,5)
    #print(var)
    novo_carro = Carro() # Declara novo objeto com a classe Carro
    print(novo_carro.marca)


