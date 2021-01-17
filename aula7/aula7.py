nome = 'Carlos'
idade = 33
altura = 1.80
e_maior = idade > 18
peso = 69.00
IMC = peso / (altura ** altura)


print(nome, 'tem', idade, 'anos de idade e seu IMC é', IMC, '.')
print(f'{nome} tem {idade} anos de idade e seu IMC é {IMC:.2f}.')  # Usando fstring (mais fácil e elegante)
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, IMC))  # Usando a função .format()
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=IMC))  # Utilizando parâmetros para nomear
print('{im:.2f} tem {n} anos de idade e seu IMC é {i}'.format(n=nome, i=idade, im=IMC))  # Invertendo posições
