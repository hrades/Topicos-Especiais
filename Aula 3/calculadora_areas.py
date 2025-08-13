from math import pi
from os import system

is_menu = True

def menu():
    print('Escolha a figura')
    for c in range(0,3):
        print(f'{c} - {figuras[c]}')

def confere_var(var=str()):
    while var.isnumeric()!=True and var.find('.') == (-1):
        system('cls')
        print('Erro de leitura! Digite um número')
        if is_menu == True:
            menu()
        var_leitura = input('Número: ')
        var = var_leitura
    return var

def circulo(raio):
    return pi*pow(float(raio),2)

def retangulo(lado_a, lado_b):
    return float(lado_a)*float(lado_b)

def triangulo(base,altura):
    return (float(base)*float(altura))/2

def ler_numero(frase):
    dado = input(f'{frase} ')
    dado = confere_var(dado)
    return dado

figuras = ('circulo', 'retângulo', 'triângulo')

while True:
    print('- Calculadora de áreas -')
    print('Escolha a figura')
    for c in range(0,3):
        print(f'{c} - {figuras[c]}')
    escolha = input('Figura: ')
    escolha = confere_var(escolha)
    while escolha not in range(0, len(figuras)):
        escolha = input('Digite um dos valores possíveis: ')
        escolha = confere_var(escolha)
        if escolha.find('.') == (-1):
            escolha = int(escolha)

    if escolha==0:
        dado1 = ler_numero('Digite o raio: ')
        dado2 = 0
        is_menu = False
    elif escolha==1:
        dado1 = ler_numero('Digite um lado: ')
        dado2 = ler_numero('Digite o outro: ')
        is_menu = False
    elif escolha==2:
        dado1 = ler_numero('Digite a base: ')
        dado2 = ler_numero('Digite a altura: ')
        is_menu = False

    metodos = (circulo(dado1), retangulo(dado1,dado2), triangulo(dado1,dado2))
    area = metodos[escolha]
    print(f'A área da figura {figuras[escolha]} é {area:.2f}')
    is_menu = True
    repetir = input('Deseja calcular novamente? (s/n): ')
    if repetir == 'n':
        break
    else:
        system('cls')
