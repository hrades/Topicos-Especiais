moedas = dict()
while True:
    valor_reais = input('Digite o valor a ser convertido (use . na vírgula): R$ ')
    try:
        valor_reais = float(valor_reais)
    except:
        print('O valor informado não é válido')
        continue
    
    # Moedas de 1
    if valor_reais>0:
        moedas_1 = valor_reais//1
        moedas['1 real'] = moedas_1
        valor_reais -= moedas_1
        print(valor_reais)

    print(moedas)
    print(valor_reais)
    break
        