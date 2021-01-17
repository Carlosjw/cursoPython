hora = input('QUe horas são? ')

if hora.isnumeric():
    if int(hora) <= 11:
        print('Bom dia!')
    elif (int(hora) > 11) and (int(hora) <= 17):
        print('Boa tarde!')
    else:
        print('Boa noite!')
else:
    print('Você forneceu uma hora inválida!')
