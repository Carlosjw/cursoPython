'''
    OPERADOR TERNÁRIO
'''

logged_user = False

# if logged_user:
#     msg = 'Usuario logado'
# else:
#     msg = 'Usuário precisa logar.'
#
# print(msg)

# SIMPLICANDO COM OPERADOR TERNÁRIO
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
# varável, valor variável se a condićão for True (if logged_user) e se for False (else)
print(msg)

# PADRÃO
idade = input('Qual a sua idade? ')

if int(idade) >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')

# SIMPLIFICANDO (OPERADOR TERNARIO):
if not idade.isdigit():
    print('Você precisa digitar apenas números!')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg2 = 'Pode acessar.' if e_de_maior else 'Nào pode acessar.'

    print(msg2)
