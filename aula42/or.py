# USO DE OR
nome = input('Qual o seu nome? ')

if nome:  # Tem algo digitado em nome?
    print(nome)  # ... então imprima nome
else:
    print('Você não digitou nada!')  # Se não, escreva isso.

# SIMPLICANDO COM OR
print(nome or 'Você não digitou nada!')

a = 0  # False
b = None  # False
c = False  # False
d = []  # False
e = {}  # False
f = 22  # True
g = 'Luiz'  # True

variavel = a or b or c or d or e or f or g

print(variavel)  # 22 - Primeiro valor verdadeiro


