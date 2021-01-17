'''
    ENTRADA DE DADOS:
'''
'''
nome = input('Qual o seu nome? ')
idade = input(f'Qual a sua idade, {nome}? ')
# print(f'O usuário digitou "{nome}" e o tipo da variável '
      # f'é {type(nome)}')

ano_nascimento = 2020 - int(idade)
print(f'{nome} tem {idade} anos. Logo, ele'
      f' nasceu em {ano_nascimento}.')
'''

n1 = int(input('Digite um número: '))  # Uma opção de casting
n2 = input('Digite outro número: ')
n2 = int(n2)  # Outra opção de casting
soma = n1 + n2

print(f'{n1} + {n2} = {soma}')
