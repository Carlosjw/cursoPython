# string = 'O Brasil é penta'
# lista = string.split(' ')

# for indice, valor in enumerate(lista):
#     print(indice, valor)

lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

# for v in lista:
#     # print(v)
#     print(v[0], v[1])

for indice, valor in enumerate(lista):  # Desempacotamento de lista
    print(indice, valor)

lista2 = ['Luiz', 'Maria', 'João']

n1, n2, n3 = lista2  # Desempacotando os valores da lista2 em varáveis independentes

print(n2)
