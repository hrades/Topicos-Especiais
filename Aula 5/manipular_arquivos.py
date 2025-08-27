# Manipular arquivos com python

class Anotacoes:
    def __init__(self, endereco):
        self._endereco = endereco

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
        with open(self._endereco, mode='r', encoding='UTF-8') as dados:
            for linha in dados:
                print(linha.strip().split(','))

    def adicionar_dados(self, texto):
        with open(self._endereco, mode='a', encoding='UTF-8') as dados:
            dados.write(f'\n{texto}')


if __name__=='__main__':
    meu_teste = Anotacoes(r"C:\Users\061210035\Downloads\dados.csv")
    meu_teste.adicionar_dados('11,2025-08-25,Mariana Costa,Câmera Canon EOS Rebel T7,1,3200.00')
    meu_teste.ler_arquivo()