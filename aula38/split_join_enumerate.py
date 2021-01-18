'''
    Split, Join, Enumarate em Python
    * Split - Dividir uma strint (str)
    * Join - Juntar umas lista (str)
    * Enumerate - Enumerar elementos da lista (list)
'''

# FUNĆAO ESPLIT:

string = 'O Brasil é o país o futebol, o Brasil é penta.'
lista_1 = string.split(' ')  # Separa todas as palavras em índices diferentes
lista_2 = string.split(',')  # Separa a string em dois índices: um para cada lado da vírgula

# print(lista_1)
# print(lista_2)
#
# for valor in lista_1:  # Iterando sobre os valores da lista_1
#     print(valor)

# Contando quantas vezes uma palavra aparece:
# for valor in lista_1:
#     # INCREMENTO PESSOAL
#     if len(valor) > 1:
#         print(f'A palavra "{valor}" apareceu {lista_1.count(valor)} vez(es) na frase.')
#     else:
#         print(f'A letra "{valor}" apareceu {lista_1.count(valor)} vez(es) na frase.')

palavra = ''  # String vazia para receber valores
contagem = 0  # Varável contador para incrementacao ou soma
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        # contagem = qtd_vezes
        if len(valor) > 1:
            contagem = qtd_vezes
            palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for word in lista_2:
    print(word.strip())  # strip remove os espaćos em branco no início das frases
