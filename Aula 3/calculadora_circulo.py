from math import pi
from os import system

while True:
    raio = input('Digite o valor do raio: ')
    is_num = raio.isnumeric()
    while is_num!=True:
        system('cls')
        print('VALOR INVÁLIDO! O valor deve ser um número')
        raio = input('Digite o valor do raio: ')
        is_num = raio.isnumeric()
    raio = float(raio)
    perimetro = 2*pi*raio
    area = pi*pow(raio,2)

    print(f'O perímetro do circulo é {perimetro:.2f} e área do circulo é {area:.2f}')
    repetir = input('Deseja realizar outro cálculo? (s/n): ').lower()
    while repetir not in 'sn':
        repetir = input('Digite uma resposta válida!\nDeseja realizar outro cálculo? (s/n): ').lower()
    if repetir=='n':
        break
    else:
        system('cls')
