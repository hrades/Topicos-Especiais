if __name__ == '__main__':
    lista = ('2', 2, 'banana', True)
    try:  # Inica um bloco de instruções que, em caso de erro, será tratado
        print(lista[9])
    except Exception as e: # Incia um bloco de instruções executadas no caso de erro no try
        print(f'Ocorreu um erro!\n{e}')
    finally:
        print('Bloco executado no caso de sucesso ou não do bloco try')

    try:
        lado = float(input('Digite o lado do quadrado: '))
        print(f'A área é de {pow(lado, 2)}')
    except ValueError:
        print('Não foi possível converter o valor para número')
    except:
        print('Ocorreu qualquer outro erro que não é de ValueError')