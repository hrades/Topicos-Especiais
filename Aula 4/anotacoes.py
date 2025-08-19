#import calculadora_areas
import math
import modulos as mod
from datetime import datetime as dt
#calculadora_areas.retangulo()

# Uma classe e a estrutura que vai definir um objeto

class Carro: #Declara uma nova classe chamada carro
    # Método construtor
    def __init__(self, marca, modelo, ano, cor='Default'): # Executado automaticamente ao criar um novo objeto
        # O argumento self é uma palavra reservada do sistema e não pode ser trocada para sua funcionalidade
        # self indica que o objeto está associado à classe (parâmetro > valores associados ao objeto)
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
    def mostra_dados(self):
        return f'Marca: {self._marca}; Modelo: {self._modelo}; Ano: {self._ano}; Cor: {self._cor}'
    
    def idade_carro(self):
        return dt.now().year - self._ano

if __name__ == '__main__':
    #print(math.__name__)
    #print(__name__)
    #var = mod.retangulo(2,5)
    #print(var)
    novo_carro = Carro('Ford','KA',2013,'Preto') # Declara novo objeto com a classe Carro
    outro_carro = Carro('Chevrolet', 'Onix', 2022)
    print(novo_carro.mostra_dados())
    print(f'A idade desse carro é {novo_carro.idade_carro()} anos')
    print(outro_carro.mostra_dados())
    print(f'A idade desse carro é {outro_carro.idade_carro()} anos')
