"""
While em Python - Aula 32
utilizado para realizar acoes enquanto
uma condicao for verdeira

Requisitos: entender condicoes e operadores
"""

#  LOOP INFINITO!
# while True:
#     nome = input('Qual o seu nome? ')
#     print(f'Olá, {nome}')

# x = 0
# while x <= 10:
#     if x == 3:  # elimina o 3 da contagem
#         x = x + 1
#         continue
#
#
#     print(x)
#     x = x + 1  # incrementa o contador e impede o loop infinito
#
# print('Acabou!')

# x = 0  # coluna
#
# while x < 10:
#     y = 0  # linha
#
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#
#     # print(x)
#     x += 1  # igual a x = x + 1
#
# print('Acabou!')

#  CALCULADORE BÁSICA:

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():  # Verifica se os valores digitados NÃO são númericos
        print('Você precisa digitar um número!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    #  + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido!')



