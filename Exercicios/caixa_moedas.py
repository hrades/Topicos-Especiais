troco = dict()
notas = (100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01)
valor_reais = ' '
def calcular_troco(valor, reais):
    dinheiro = reais//valor
    if valor>1:
        troco[f'{valor} reais'] = dinheiro
    elif valor<1:
        #centavos = 1/valor
        troco[f'{valor*100} cents'] = dinheiro
    elif valor==1:
        troco['1 real'] = dinheiro
    return reais%valor

while True:
    valor_reais = input('Digite o valor a ser convertido (use . na vírgula): R$ ')
    try:
        valor_reais = float(valor_reais)
    except:
        print('O valor informado não é válido')
        continue
    
    # Moedas de 1
    for real in notas:
        if valor_reais>=real:
            valor_reais = round(calcular_troco(real, valor_reais), 2)
    
        
    print(valor_reais)
    print(troco)
    break
        