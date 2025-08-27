# Manipular arquivos com python

class Anotacoes:
    def __init__(self):
        pass

    def __doc__(self):
        return 'Esta é uma classe que trabalha a manipulação de arquivos de texto'
    
    def ler_arquivo(self):
        # arquivo = open()
        # arquivo.close()
        
        # Maneira mais fácil de utilizar o open()
        with open(r"C:\Users\061210035\Downloads\teste.txt") as arquivo: # Método builtin para acessar um arquivo do sistema
            arquivo.write('Teste de escrita em arquivo')

if __name__=='__main__':
    meu_teste = Anotacoes()