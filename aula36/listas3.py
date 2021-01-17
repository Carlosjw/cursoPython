# Gerando uma lista automaticamente:
l5 = list(range(1, 10))
print(l5)

#  Somando valores da lista gerada
soma = 0
for number in l5:
    soma += number

print(f'A soma da lista é {soma}')

#  Listas com mútliplos de números:
l6 = list(range(0, 100, 5))  # Múltplos de 5
print(l6)
l7 = list(range(0, 100, 7))  # Múltiplos de 7
print(l7)

#  Verificando o tipo de valores em uma lista:
l8 = ['String', True, 10, -20.5]

for elem in l8:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')