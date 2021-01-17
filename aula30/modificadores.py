# FORMATANDO VALORES COM MODIFICADORES

# :s - Texto(strings)
# :d - Inteiros (int)
# :f - Números de ponto flutuante (float)
# :.(NÚMERO)f - Qunatidade de casas decimais (float)

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{}'.format(divisao))
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

# :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, f)

# > - Esquerda
num_3 = 1
print(f'{num_3:0>10}')  # 9 zeros à esquerda do número (0000000001)
num_4 = 1150
print(f'{num_4:0>10}')  # 6 zeros à esquerda do número (0000001150)

# < - Direita
print(f'{num_4:0<10}')  # 6 zeros à direita do número (1150000000)

# ^ - Centro
print(f'{num_4:0^10}')  # 6 zeros no centro do número (0001150000)

nome = 'Carlos'
# print((50 - len(nome)) / 2)
# print(f'{nome:#^50}') ###################Carlos Lima####################
sobrenome = 'Lima'
nome_formatado = '{n}'.format(n=nome)
print(nome_formatado)

nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

nome_formatado = '{0} {1:#^50}'.format(nome, sobrenome)  # Pelo índice
print(nome_formatado)

print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiúscula
print(nome.title())  # primeiras letras maiúsculas






