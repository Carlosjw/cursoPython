# DESEMPACOTAMENTO DE LISTAS EM PYTHON:

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

# n1, n2, n3, *outra_lista, ultimo_da_lista = lista  # Desempacotando os valores da lista2 em varáveis independentes
# *outra_lista (detalhe no asterisco) recebe todos os outros valores não atribuídos as variáveis
# ultimo_da_lista recebe o ultimo valor da lista

# print(n1, n2, n3, outra_lista, ultimo_da_lista)

*another_list, n1, n2, n3 = lista

print(*another_list, n1, n2, n3)  # Também pode ser usado *_ que significa a mesma coisa
