'''
    For / Else em Python
'''

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

# # Checando dados em listas
comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        # Verificando se determinada letra (maiúscula ou minúscula,
        # está em uma lista de nomes.
        comeca_com_j = True

    if comeca_com_j:
        print('Existe uma palavra que comeca com J.')
    else:
        print('Nào existe uma palavra que comeca com J')



