'''
    For in em Python
    Iterando strings com for
    Funcao range(start=0, stop, step=1):
    Ex: inicia do zero, vai até 10 (9), saltando de 1 em 1 (padrão),
    mas pode ser de qualquer outro valor
'''

# Iterando Strings:
# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# Funcao range:
for numero in range(0, 10, 2):
    print(numero)

for n in range(20, 1, -1):
    print(n)

for m in range(0, 100, 8):  # Exibirá os múltiplos de 8
    print(m)

for p in range(100):
    if p % 8 == 0:  # Exibirá os múltiplos de 8 também
        print(p)

texto = 'Python'
print(texto)
nova_string = ''  # string vazia
# user = input('Que letra queres que fique maiúscula? ')

# continue -> pula para o pŕoximo laćo
# break -> para de executar o laco

for letra in texto:
    if letra == 't':
        # continue  # elimina a letra 't'
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        # break  # finaliza o laco
    else:
        nova_string += letra

print(nova_string)



