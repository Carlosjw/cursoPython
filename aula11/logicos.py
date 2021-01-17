'''
    Operadores lógicos:
        and, or, not
        in e not in
'''

a = 1
b = 2
c = 3

# a == b and b < c
#
# a == b or b < c

if not b > a:  # Inverte o valor
    print('B é maior que A.')
else:
    print('A é maior que B.')

#  IN : Veririfica se determinado valor está contido em...

if 's' in 'Carlos':
    print('Existe.')
else:
    print('Não existe.')

#  NOT IN: Verifica se algo não está contido em...

if 's' not in 'Carlos':
    print('Existe.')
else:
    print('Não existe.')