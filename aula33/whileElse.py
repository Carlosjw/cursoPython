'''
    While / Else
    contadores: Conta quantas vezes o laco se repete
    acumuladores: Soma todos os valores inseridos no laco
'''

contador = 1  # Impede que o laco entre em loop infinito
acumulador = 1
while contador <= 10:
    print(f'{contador} | {acumulador}')

    if contador > 9:
        break  # interrompe a execućão do laco

    acumulador += contador
    contador += 1
else:  # Sera executado somente se a condicao no while for falsa
    print('Cheguei no Else.') # Não sera executado por causa do Break

print('Saí do laco while')  # Nao sera afetado pelo break
