'''
    Operadores relacionais(retornam valores booleanos:
        == : igual e do mesmo tipo que ... (compara igualdade)
        > : maior que ...
        >= : maior ou igual à...
        < : menor que...
        <= : menor ou igual à...
        !=
'''

# num_1 = 2  # int
# num_2 = 3  # int
#
# print(num_1 == num_2)
# print(num_1 > num_2)
# print(num_1 < num_2)
#
# expressao = num_1 == num_2
#
# print(expressao)

nome = input('Qual o seu nome? ')
idade = int(input(f'Qual a sua idade, {nome}? '))

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} PODE pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
