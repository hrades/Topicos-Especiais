from math import pi

# LISTAS
empty_list = list()  #Define lista vazia
list_example = ['banana', pi, True, [1,2,3,4], 8]
# Maneiras de acessar os itens de uma lista em ordem
for item in list_example:
  print(item) #printa em ordem
i = 1
for i in range(i, (len(list_example)+1)):
    print(list_example[-i]) #printa ao contrário
# Sublistas
# Retorna um subset de elementos da lista
print(list_example[1:4]) #printa os elementos 1,2 e 3
# Strings também são listas
string_example = "mystring"
print(string_example[2:8])
sorted_list = list()
sorted_list = sorted(string_example)
print(sorted_list)

# TUPLAS
months = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
#months.count()  months.index()

# SET
set_example = {1, 2.2, 'test'}
print(set_example)
set_example.add('Grande teste')
print(set_example)

# DICIONÁRIO
# Coleção chave:valor
student1 = {'nome':'Heloísa', 'ra':'061210035', 'semestre':10, 'curso':'ECA'}
student2 = {'nome':'Guilherme', 'ra':'061210033', 'semestre':8, 'curso':'EC'}
student1['new_key'] = 'new value' # Adicionar nova chave ao dicionário
lista_dicio = [student1, student2]
for dicio in lista_dicio:
    for info in dicio:    
        print(dicio[info])

