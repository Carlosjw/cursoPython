usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

# print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Digite pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')