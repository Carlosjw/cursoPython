'''
    Split, Join, Enumarate em Python
    * Split - Dividir uma strint (str)
    * Join - Juntar umas lista (str)
    * Enumerate - Enumerar elementos da lista (list)
'''

# FUNĆAO ESPLIT:

string = 'O Brasil é o país o futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

# print(lista_1)
# print(lista_2)
#
# for valor in lista_1:  # Iterando sobre os valores da lista_1
#     print(valor)

# Contando quantas vezes uma palavra aparece:
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}')
