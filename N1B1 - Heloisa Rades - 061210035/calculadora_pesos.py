# Programa para calcular pesos de barras

from math import pi # Importar constante pi da biblioteca math

class peso_linear():
    def __init__(self):
        pass

    @staticmethod
    def nome():
        return 'Heloísa Rades de Souza, RA: 061210035'
       
    @staticmethod
    def peso_especifico(material): # Retorna o peso específico baseado no material selecionado
        if material == 1: # Aço
            return 0.787
        elif material == 2: # Latão
            return 0.87
        elif material == 3: # Alumínio
            return 0.27
       
    # Cálculos de peso da barra de acordo com a seção transversal
    def perfil_redondo(self, raio, material):
        peso_esp_material = self.peso_especifico(material)
        return ((pow(raio,2)*pi)*1000)*(peso_esp_material/1000)
      
    def perfil_quadrado(self, lado, material):
        peso_esp_material = self.peso_especifico(material)
        return (pow(lado,2)*1000)*(peso_esp_material/1000)
       
    def perfil_triang(self, lado, material):
        peso_esp_material = self.peso_especifico(material)
        return (((pow(3,(1/2))/4)*pow(lado,2))*1000)*(peso_esp_material/1000)
        
    @staticmethod
    def ler_numero(frase=str()):  # Função para ler valores 
        num = input(frase)
        while True:
            try:
                num = float(num)
                return num
            except:
                print('Erro! O valor deve ser um número')
                num = input(frase)

    # Função para selecionar
    def selecionar(self):
        # Valores utilizados pelo algoritmo
        secao = 'j' # Inicializar sem estar vazio para entrar na condição
        dimensao = 0.0
        material = 0

        print('-'*36)
        print('Calculadora de peso linear de barras')
        print('-'*36)
        print('Qual o perfil da barra?\nR - Redondo\nQ - Quadrado\nT - Triângulo equilátero')
        
        while secao not in ['R','Q','T']: # Condição para aceitar somente essas respostas do usuário
            secao = input('Digite uma das letras apresentadas: ').upper()
            if secao not in 'RQT':
                print('Seleção inválida!')
        
        print('-'*36)
        print('Qual o material da barra?\n1 - Aço\n2 - Latão\n3 - Alumínio')

        while material not in [1,2,3]: # Só aceita os valores inteiros 1, 2 ou 3
            material = input('Digite um dos números apresentados: ')
            try: # Tenta converter para inteiro
                material = int(material)
            except:
                print('Erro! Selecione uma das opções válidas')

        if secao == 'R': # Barra redonda selecionada
            dimensao = self.ler_numero('Digite o valor do raio em cm: ')
            return self.perfil_redondo(dimensao, material)

        if secao == 'Q': # Barra quadrada selecionada
            dimensao = self.ler_numero('Digite o valor do lado em cm: ')
            return self.perfil_quadrado(dimensao, material)
        
        if secao == 'T': # Barra triangular selecionada
            dimensao = self.ler_numero('Digite o valor do lado em cm: ')
            return self.perfil_triang(dimensao, material)


# Utilizando a main para caso outros módulos sejam implementados
if __name__=='__main__':
    while True: # loop para possibilitar repetição
        peso = peso_linear()
        valor = peso.selecionar()
        print('-'*36) # Separar o resultado no terminal
        print(f'O peso da barra é de {valor:.2f} Kg.m') # Formatado para 2 casas depois da ,
        print('-'*36) # Separar o resultado no terminal

        # Verificar se o usuário quer repetir o processo
        print('Deseja realizar outra operação?')
        reset = input('Digite (s) para sim e (n) para não: ').lower()
        # Fazer com que as únicas respostas aceitas sejam s e n
        while reset not in ['s','n']:
            print('Resposta inválida!!')
            reset = input('Digite (s) para sim e (n) para não: ').lower()
        if reset == 'n': # Se o usuário digitar n, o programa encerra
            break
        