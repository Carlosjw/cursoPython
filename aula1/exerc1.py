# TESTANDO CALULCADORA EM PYTHON

def tabuada(painel(escolha)):
    if escolha == '1':
        escolha = '1: ADIÇÃO'
        print(f'Você escolheu a opção {escolha}:')
        for i in range(1, 11):
            for j in range(1, 11):
                print('|--------------------|')
                print(f'{j} + {i} = {j + i}')
                print('|--------------------|')
        return painel()
    elif escolha == '2':
        escolha = '2: SUBTRAÇÃO'
        print(f'Você escolheu a opção {escolha}:')
        for i in range(1, 11):
            for j in range(1, 11):
                print('|--------------------|')
                print(f'{j} - {i} = {j - i}')
                print('|--------------------|')
        return painel()
    elif escolha == '3':
        escolha = '3: MULTIPLICAÇÃO'
        print(f'Você escolheu a opção {escolha}:')
        for i in range(1, 11):
            for j in range(1, 11):
                print('|--------------------|')
                print(f'{j} x {i} = {j * i}')
                print('|--------------------|')
        return painel()
    elif escolha == '4':
        escolha = '4: DIVISÃO'
        print(f'Você escolheu a opção {escolha}:')
        for i in range(1, 11):
            for j in range(1, 11):
                print('|--------------------|')
                print(f'{j} / {i} = {j / i}')
                print('|--------------------|')
        return painel()
    elif escolha == '5':
        escolha = '5: EXPONENCIAÇÃO'
        print(f'Você escolheu a opção {escolha}:')
        for i in range(1, 11):
            for j in range(1, 11):
                print('|--------------------|')
                print(f'{j} ** {i} = {j ** i}')
                print('|--------------------|')
        return painel()


def painel(escolha):
    print('|-------------------------|')
    print('Escolha uma opção: ')
    print('1: ADIÇÃO \n'
          '2: SUBTRAÇÃO \n'
          '3: MULTIPLICAÇÃO \n'
          '4: DIVISÃO \n'
          '5: EXPONENCIAÇÃO \n'
          '0: SAIR')
    print('|-------------------------|')

escolha = input(f'OPÇÃO ESCOLHIDA: ')
painel(escolha)


tabuada()










