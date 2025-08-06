valor_a = int(input('Digite o primeiro número: '))
valor_b = int(input('Digite o segundo número: '))
# Diferentes maneiras de mostrar a mensagem
print('O resultado da multiplicação desses números é: {0}'.format(valor_a*valor_b))
print('O resultado da multiplicação desses números é: '+ str(valor_a*valor_b))
print(f'O resultado da multiplicação desses números é: {valor_a*valor_b}')
# Modificações com texto
valor = (1/3.0)*2
print(f'{valor:.2}')

''' Anotações de placeholders
{:2} - Determina no mínimo dois caracteres do marcador
{:^12} - Mínimo de 12 caracteres com o posicionamento centralizado
{:*>12} - Mínimo de 12 caracteres alinhado à direita com os catacteres de preenchimento como '*'
{:.2f} - Casas decimais de floats arredondadas para 2
{:X} - Representação em hexadecimal
{:o} - Representação em octal
'''
