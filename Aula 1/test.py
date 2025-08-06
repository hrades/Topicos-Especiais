print('Hello World')

# Toda "variável" é um objeto em python

a = 'i'*20
print(dir(a)) # Retorna os métodos e parâmetros do objeto
a = a.upper()
print(a.lower())

a = 1.0 * 2
print(type(a))