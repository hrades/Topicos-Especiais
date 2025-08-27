# Manipular arquivos com python

class Anotacoes:
    def __init__(self):
        pass

    def __doc__(self):
        return 'Esta é uma classe que trabalha a manipulação de arquivos de texto (txt, csv...)'
    
    def escrever_teste(self):
        # arquivo = open()
        # arquivo.close()
        
        # Maneira mais fácil de utilizar o open()
        with open(r"C:\Users\061210035\Downloads\teste.txt", mode='w') as arquivo: # Método builtin para acessar um arquivo do sistema com um modo
            # 'w' : write
            # 'r' : read
            # 'a' : append
            arquivo.write('Teste de escrita em arquivo')

    def ler_arquivo(self):
        with open(r"C:\Users\061210035\Downloads\dados.csv", mode='r', encoding='UTF-8') as dados:
            for linha in dados:
                print(linha)


if __name__=='__main__':
    meu_teste = Anotacoes()
    meu_teste.ler_arquivo()