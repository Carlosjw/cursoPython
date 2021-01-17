'''
    Listas em Python
    fatiamento
    append, insert, pop, dell, clear, extend, +
    min, max
    range
'''

'''
#         0    1    2    3    4     5
lista = ['A', 'B', 'C', 'D', 'E', 10.5, True]  # A lista pode conter valores de diferentes tipos
# lista[5] = 'Qualquer outra coisa'  # Alterando o valor em uma lista a partir do índice

print(lista)

# FATIAMENTO DA LISTA

print(lista[0:3])  # O valor do último índice não é incluído
print(lista[0:4])
print(lista[:3])  # Mesmo que 0:3
print(lista[2:])  # Índice 2 até o final
print(lista[0])  # Imprime o primeiro índice da lsita
print(lista[-1])  # Imprime o último índice/elemento da lista
print(lista[::2])  # Imprime de 2 em 2
print(lista[::-1])  # Imprime a lista de trás para frente
'''

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l2)
l3 = l1 + l2  # Concatenando as listas
l1.extend(l2)  #  Adiciona os valores de l2 a l1
l1.extend('a')  # Adiciona valor 'a' a lista l1
l2.append('b')  #  Adiciona o valor 'b' a l2

l2.insert(0, 'banana')  # Adiciona elemento em índice da lista SEM substituir o atual
print(l2)
l2.pop()  # Deleta o último elemento da lista
print(l2)

# print(l1)
# print(l2)
# print(l3)


