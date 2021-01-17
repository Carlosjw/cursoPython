secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:  # Mensagem de chances esgotadas
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:  # Verifica se foi digitada somente uma letra
        print('Ahh isso não vale. Digite apenas uma letra.')
        continue

    digitadas.append(letra)  # Adiciona letra a lista de digitadas

    if letra in secreto:  #  Verifica se letra digitada está na palavra secreta
        print(f'Muito bem! A letra "{letra}" EXISTE na palavra secreta!')
    else:
        print(f'Uma pena! A letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()  # Remove letra errada da lista

    secreto_temporario = ''  # Variável comparativa com a secreta
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta  #  Adiconando letra certa a variável secreto_temporario
        else:
            secreto_temporario += '*'  # Substituindo letra errada por asterisco

    if secreto_temporario == secreto:  # Verificando se variável gerada é igual a matrix
        print(f'Que legal! VOCÊ GANHOU! A palavra secreta era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:  # Dedućão das quantidades de tentativas
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
