'''
    * Criar variáveis para nome (str), idade (int),
    * altura (float) e peso (float) de uma pessoa.
    * Criar variável com o ano atual (int).
    * Obter o ano de nascimento da pessoa (baseado na idade e no ano atual).
    * Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa).
    * Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
    RESULTADO PRETENDIDO:
        Carlos tem 33 anos, 1.80 de altura e pesa 69kg.
        O IMC de Carlos é 23.95.
        Carlos nasceu em 1987.

'''

nome = 'Carlos'
idade = 33
altura = 1.80
e_maior = idade > 18
peso = 69
ano_atual = 2020
nascimento = ano_atual - idade
IMC = peso / (altura ** altura)

print(f'{nome} tem {idade} anos, e {altura}m de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {IMC:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
