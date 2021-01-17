# positivos [012345678]

texto = 'Python s2'

print(texto[2])  # imprime o t
print(texto[8])  # imprime o 2

nova_string = texto[2:6]  # índice 2 até o 5 (fatiamento)
                          # o último não é incluído
print(nova_string)

nova_string2 = texto[:6]  # do índice 0 até o 5
print(nova_string2 )

print(texto[:-1])  # exclui o último caractere

print(texto[0:6:2])  # de zero à 6 de 2 em 2
print(texto[0::3])  # de zero ao final de 3 em 3
print(texto[:])  # de zero até o final

