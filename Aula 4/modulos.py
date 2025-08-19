from math import pi

def retangulo(lado_a, lado_b):
    return float(lado_a)*float(lado_b)

def triangulo(base,altura):
    return (float(base)*float(altura))/2

def circulo(raio):
    return pi*pow(float(raio),2)

if __name__ == '__main__':
    print('Execução do modulo')
    print(__name__)