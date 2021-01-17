# nome = input('Qual o seu nome? ')
# idade = int(input(f'Qual a sua idade, {nome}? '))
# nascimento = 2021 - idade
# peso = float(input(f'Qual o seu peso, {nome}? '))
# altura = float(input(f'Qual a sua altura? '))

# imc = peso / (altura * altura)

# print(f'Você tem {idade} anos, {nome}, tem {altura}m, pesa {peso}kg e nasceu em {nascimento}.')
# print(f'Seu IMC é {imc:.2f}.')

# nome = input('Qual o seu nome? ')
# resposta = input(f'Você sabe qual a velocidade da luz, {nome}? ')

# if resposta == 'Sim':
#     print(f'Então me diga, {nome}')
# else:
#     print('A velocidade da luz é 300000 km/s')

raiz81 = input('Qual a raiz quadrada de 81? ')

cont = 0
soma = 0
while raiz81 != 9:
    raiz81 = int(input('Tente outro valor: '))
    cont = cont + 1
    soma = soma + raiz81
    # if raiz81 == '9':
    #     break


if cont >= 5:
    print('Você excedeu 5 tentativas.')
    print(f'Você errou {cont} vezes.')
    print(f'A soma de todos os valores digitados é: {soma}.')
else:
    print(f'Parabéns! Você acertou na primeira!')



