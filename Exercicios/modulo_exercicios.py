from math import pi, cos, sin

class Exercicios:
    def __init__(self):
        pass

    @staticmethod
    def area_circulo(raio):
        return pow(raio,2)*pi
    
    @staticmethod
    def area_retangulo(base, altura):
        return base*altura
    
    @staticmethod
    def conversor_CF(temp):
        return (temp*9/5)+32
    
    @staticmethod
    def conversor_comprimento(metros):
        return metros*1000
    
    @staticmethod
    def primeira_lei_ohm(tensao=None, corrente=None, resistencia=None):
        try:
            if tensao==None:
                return corrente*resistencia
            elif corrente==None:
                return tensao/resistencia
            elif resistencia==None:
                return tensao/corrente
        except Exception as e:
            return e
    
    @staticmethod
    def potencia_eletrica(tensao, corrente, fator):
        pot = tensao*corrente
        return f'potencia aparente: {pot}, potencia ativa: {pot*cos(fator)}, potencia reativa: {pot*sin(fator)}'
        
    @staticmethod    
    def volume_esfera(raio):
        return (4/3)*pi*pow(raio, 3)
    
    @staticmethod
    def area_cilindro(raio, altura):
        return 2*pi*raio*(raio+altura)
    
    @staticmethod
    def conversor_velocidade(vel, unidade=str()):
        if unidade.lower()=='km/h':
            return vel*0.27778
        if unidade.lower()=='m/s':
            return vel/0.27778

    @staticmethod    
    def conversor_pressao(pres, unidade=str()):
        if unidade.lower()=='pa':
            return pres/101325
        if unidade.lower()=='atm':
            return pres*101325
        

if __name__=='__main__':
    exercicios = Exercicios()
    # Ex a
    raio = input('Digite o raio do círculo: ')
    try:
        raio = float(raio)
        print(exercicios.area_circulo(raio))
    except Exception as e:
        print(f'Valor fornecido inválido\nErro {e}')
    
    # Ex e
    print(exercicios.primeira_lei_ohm(5,10)) # Padrão: calcular a resistência
    print(exercicios.primeira_lei_ohm(resistencia=5,tensao=10)) # Calcular a corrente
    print(exercicios.primeira_lei_ohm(corrente=5,resistencia=10)) # Calcular a tensão
    print(exercicios.primeira_lei_ohm(10.0)) # Erro por falta de argumentos